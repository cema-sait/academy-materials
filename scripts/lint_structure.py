#!/usr/bin/env python3
"""
Academy Materials — Structure Linter

Validates the three-level course hierarchy (theme → module → lesson) for every
course registered in the root index.md.

Checks performed:
  Root index.md
    • 'themes' field exists and is a YAML list
    • Each theme name has a matching folder on disk

  Theme index.md  (<theme>/index.md)
    • Required fields: id, name, courses, summary
    • 'id' matches the folder name exactly
    • 'courses' is a YAML list
    • Each course name has a matching subfolder

  Module index.md  (<theme>/<module>/index.md)
    • Required fields: name, id, dependsOn, files, summary
    • 'id' matches the folder name exactly
    • 'files' is a YAML list
    • 'dependsOn' is a YAML list
    • 'learningOutcomes' (if present) is a YAML list, not a pipe string
    • No learningOutcomes item is parsed as a YAML mapping (colon-space bug)
    • Every filename in 'files' exists on disk
    • A figs/ or fig/ directory exists inside the module folder

  Lesson files  (<theme>/<module>/<lesson>.md)
    • Required fields: name, dependsOn
    • 'dependsOn' is a YAML list
    • 'learningOutcomes' (if present) is a YAML list
    • No learningOutcomes item is parsed as a YAML mapping (colon-space bug)
    • No KaTeX-incompatible unicode characters inside math spans:
        ′  U+2032  →  use \\prime or '
        ∅  U+2205  →  use \\emptyset

Usage:
    python3 scripts/lint_structure.py [--root /path/to/repo]

Exit codes:
    0  all checks passed
    1  one or more errors found
"""

import sys
import re
import argparse
from pathlib import Path

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML is required. Install it with:\n"
        "    pip install pyyaml\n"
        "or add it to your environment before running this linter."
    )

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------
ERRORS: list[str] = []
WARNINGS: list[str] = []

# Unicode characters that KaTeX cannot render and that cause build crashes.
# Maps the character to its recommended LaTeX replacement.
KATEX_INCOMPATIBLE: dict[str, str] = {
    "\u2032": r"' or \prime",   # ′ prime
    "\u2205": r"\emptyset",     # ∅ empty set
}

# Regex to strip fenced code blocks before scanning for math unicode
_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
# Inline math: $...$
_MATH_INLINE_RE = re.compile(r"\$(?!\$).+?\$")
# Block math: \[...\]
_MATH_BLOCK_RE = re.compile(r"\\\[.*?\\\]", re.DOTALL)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
RED    = "\033[31m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def _err(path: Path, root: Path, msg: str) -> None:
    rel = path.relative_to(root)
    full = f"{rel}: {msg}"
    ERRORS.append(full)
    print(f"  {RED}✗{RESET} {full}")


def _warn(path: Path, root: Path, msg: str) -> None:
    rel = path.relative_to(root)
    full = f"{rel}: {msg}"
    WARNINGS.append(full)
    print(f"  {YELLOW}⚠{RESET} {full}")


def _ok(label: str) -> None:
    print(f"  {GREEN}✓{RESET} {label}")


def _parse_frontmatter(path: Path, root: Path) -> tuple[dict | None, str]:
    """
    Read *path*, split out the YAML frontmatter, and return (parsed_dict, body).
    Returns (None, full_text) if the file has no frontmatter or the YAML is invalid.
    """
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        _err(path, root, "no YAML frontmatter block found")
        return None, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        return fm, text[m.end():]
    except yaml.YAMLError as exc:
        _err(path, root, f"invalid YAML frontmatter: {exc}")
        return None, text


def _require_fields(fm: dict, fields: list[str], path: Path, root: Path) -> None:
    for field in fields:
        if field not in fm:
            _err(path, root, f"missing required field '{field}'")


def _require_list(fm: dict, field: str, path: Path, root: Path) -> bool:
    """Check that *field* is a Python list (YAML sequence).  Returns True if OK."""
    if field not in fm:
        return False
    if not isinstance(fm[field], list):
        _err(
            path, root,
            f"'{field}' must be a YAML list (use '- item' syntax), "
            f"got {type(fm[field]).__name__}",
        )
        return False
    return True


def _check_outcomes_not_objects(
    outcomes: list, path: Path, root: Path
) -> None:
    """
    Detect learningOutcomes items that were parsed as YAML mappings (dicts)
    instead of strings.  This happens when an item contains ': ' (colon-space),
    causing js-yaml (and PyYAML) to interpret it as a key: value pair.

    Fix: wrap the item in double quotes.
    """
    for i, item in enumerate(outcomes):
        if isinstance(item, dict):
            key = next(iter(item))
            _err(
                path, root,
                f"learningOutcomes[{i}] was parsed as a YAML mapping, not a string. "
                f'It contains ": " — wrap the item in double quotes. '
                f"Detected key: '{key}'",
            )


def _check_math_unicode(body: str, path: Path, root: Path) -> None:
    """
    Find KaTeX-incompatible unicode characters inside math spans
    ($...$  and  \\[...\\]) after stripping fenced code blocks.
    """
    stripped = _CODE_FENCE_RE.sub("", body)
    math_spans = _MATH_INLINE_RE.findall(stripped) + _MATH_BLOCK_RE.findall(stripped)
    for span in math_spans:
        for char, replacement in KATEX_INCOMPATIBLE.items():
            if char in span:
                _err(
                    path, root,
                    f"unicode character U+{ord(char):04X} ({char!r}) inside a math "
                    f"expression — KaTeX cannot render it. "
                    f"Replace it with: {replacement}",
                )


# ---------------------------------------------------------------------------
# Per-level validators
# ---------------------------------------------------------------------------
def lint_lesson(path: Path, root: Path) -> None:
    fm, body = _parse_frontmatter(path, root)
    if fm is None:
        return

    _require_fields(fm, ["name", "dependsOn"], path, root)
    _require_list(fm, "dependsOn", path, root)

    if "learningOutcomes" in fm:
        if _require_list(fm, "learningOutcomes", path, root):
            _check_outcomes_not_objects(fm["learningOutcomes"], path, root)

    _check_math_unicode(body, path, root)


def lint_module(module_dir: Path, root: Path) -> None:
    index = module_dir / "index.md"
    print(f"\n  Module: {module_dir.name}")

    if not index.exists():
        _err(module_dir, root, "index.md missing")
        return

    fm, _ = _parse_frontmatter(index, root)
    if fm is None:
        return

    _require_fields(fm, ["name", "id", "dependsOn", "files", "summary"], index, root)

    # id must match folder name
    if fm.get("id") != module_dir.name:
        _err(
            index, root,
            f"'id' is '{fm.get('id')}' but folder name is '{module_dir.name}' "
            f"— they must be identical",
        )

    _require_list(fm, "files", index, root)
    _require_list(fm, "dependsOn", index, root)

    if "learningOutcomes" in fm:
        if _require_list(fm, "learningOutcomes", index, root):
            _check_outcomes_not_objects(fm["learningOutcomes"], index, root)

    # Every file listed in 'files' must exist
    for fname in fm.get("files") or []:
        fpath = module_dir / fname
        if not fpath.exists():
            _err(
                index, root,
                f"files entry '{fname}' does not exist at "
                f"{fpath.relative_to(root)}",
            )
        else:
            lint_lesson(fpath, root)

    # figs/ or fig/ directory should exist (warning, not a hard error, since
    # text-only modules are valid — but a missing dir can cause app build crashes
    # if the renderer enumerates module assets without a null-guard)
    has_figs = (module_dir / "figs").is_dir() or (module_dir / "fig").is_dir()
    if not has_figs:
        _warn(
            module_dir, root,
            "no figs/ directory found — add figs/.gitkeep if the module has no "
            "images, so asset enumeration in the app always returns [] not null",
        )
    else:
        _ok(f"{module_dir.name}/figs/ present")


def lint_theme(theme_dir: Path, root: Path) -> None:
    index = theme_dir / "index.md"

    if not index.exists():
        _err(theme_dir, root, "index.md missing")
        return

    fm, _ = _parse_frontmatter(index, root)
    if fm is None:
        return

    _require_fields(fm, ["id", "name", "courses", "summary"], index, root)

    # id must match folder name
    if fm.get("id") != theme_dir.name:
        _err(
            index, root,
            f"'id' is '{fm.get('id')}' but folder name is '{theme_dir.name}' "
            f"— they must be identical",
        )

    if not _require_list(fm, "courses", index, root):
        return

    for course_id in fm["courses"]:
        course_dir = theme_dir / course_id
        if not course_dir.is_dir():
            _err(
                index, root,
                f"courses entry '{course_id}' has no matching folder at "
                f"{course_dir.relative_to(root)}/",
            )
        else:
            lint_module(course_dir, root)


def lint_root(root: Path) -> None:
    index = root / "index.md"
    if not index.exists():
        _err(root, root, "root index.md is missing")
        return

    fm, _ = _parse_frontmatter(index, root)
    if fm is None:
        return

    if not _require_list(fm, "themes", index, root):
        return

    for theme_id in fm["themes"]:
        theme_dir = root / theme_id
        print(f"\n{BOLD}Theme: {theme_id}{RESET}")
        if not theme_dir.is_dir():
            _err(
                index, root,
                f"themes entry '{theme_id}' has no matching folder",
            )
        else:
            lint_theme(theme_dir, root)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Academy Materials structure linter")
    parser.add_argument(
        "--root",
        default=None,
        help="Path to the repository root (default: parent of this script's directory)",
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root).resolve()
    else:
        root = Path(__file__).resolve().parent.parent

    print(f"{'=' * 62}")
    print(f"  Academy Materials — Structure Linter")
    print(f"  Root: {root}")
    print(f"{'=' * 62}")

    lint_root(root)

    print(f"\n{'=' * 62}")
    if WARNINGS:
        print(f"{YELLOW}{BOLD}{len(WARNINGS)} warning(s):{RESET}")
        for w in WARNINGS:
            print(f"  ⚠ {w}")
    if ERRORS:
        print(f"{RED}{BOLD}{len(ERRORS)} error(s) found:{RESET}")
        for e in ERRORS:
            print(f"  • {e}")
        sys.exit(1)
    else:
        status = "All checks passed" + (f" ({len(WARNINGS)} warning(s))" if WARNINGS else "")
        print(f"{GREEN}{BOLD}{status}.{RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
