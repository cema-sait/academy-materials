# CEMA Academy — Course Materials

This repository holds all course content consumed by the CEMA Academy application. The app reads the markdown files and their YAML frontmatter at build time to generate course pages. Getting the structure and frontmatter right is what makes content appear correctly in the app.

---

## Repository Layout

```
index.md                          ← root registry: lists every theme
<theme_folder>/
  index.md                        ← theme metadata and module list
  <module_folder>/
    index.md                      ← module metadata, learning outcomes, file list
    00_first_lesson.md            ← lesson file
    01_second_lesson.md
    ...
    figs/                         ← images referenced by lessons in this module
```

The three levels are **theme → module → lesson**. In the app's URL structure this maps to `/material/<repoId>/<themeId>/<moduleId>`.

---

## File Roles and Frontmatter

### 1. Root registry (`index.md`)

Registers every theme in the repository. The app reads this file to know which top-level directories to load.

```yaml
---
id: cema_academy
name: CEMA Academy
themes: [
  docker_containerization,
  introduction_to_R,
  introduction_to_statistics,
]
---
```

| Field    | Type            | Description |
|----------|-----------------|-------------|
| `id`     | string          | Unique identifier for this repository instance. Not used in URLs. |
| `name`   | string          | Display name shown in the app header. |
| `themes` | list of strings | Folder names of every theme in the repo. Each entry must exactly match the folder name and the `id` declared inside that folder's `index.md`. |

---

### 2. Theme `index.md`

Lives at `<theme_folder>/index.md`. Describes the theme and lists its modules.

```yaml
---
id: introduction_to_R
name: "Introduction to R"
courses: [
  introduction_to_r,
]
summary: |
  One paragraph. What the theme covers, what skills learners leave with.
---

One paragraph. What the theme covers, what skills learners leave with.
```

| Field     | Type            | Description |
|-----------|-----------------|-------------|
| `id`      | string          | Must exactly match the folder name and the entry in the root `themes` list. Must be lowercase `snake_case` — e.g. `introduction_to_statistics`. |
| `name`    | string          | Display name. Wrap in quotes if it contains special characters. |
| `courses` | list of strings | Folder names of every module inside this theme, in the order they should appear in the app. Each entry must match the `id` in that module's `index.md`. |
| `summary` | pipe string     | Plain prose description of the theme. |

The body text (after the closing `---`) must be the same text as `summary`. The app uses both.

---

### 3. Module `index.md`

Lives at `<theme_folder>/<module_folder>/index.md`. Describes a single module and enumerates its lesson files.

```yaml
---
name: Introduction to R and Data Wrangling
id: introduction_to_r
dependsOn: []
files: [
  00_getting_started_with_r.md,
  01_reading_data_into_r.md,
  02_dataset_overview.md,
]
learningOutcomes:
  - Set up and navigate R and RStudio for reproducible analysis.
  - Use core R structures including vectors, matrices, lists, and data frames.
  - Import CSV and Excel data and inspect structure, types, and data quality.
summary: |
  One paragraph. What this module covers and what learners practise.
---

One paragraph. What this module covers and what learners practise.
```

| Field              | Type            | Description |
|--------------------|-----------------|-------------|
| `name`             | string          | Display name for the module. |
| `id`               | string          | Must exactly match the folder name and the entry in the theme's `courses` list. |
| `dependsOn`        | list            | List of `themeId.moduleId` strings this module requires before it can be studied. Use `[]` if there are no prerequisites. |
| `files`            | list of strings | Lesson filenames in the order they should appear, including the `.md` extension. Must exactly match files on disk. |
| `learningOutcomes` | YAML list       | Bullet list of outcomes. See the [YAML gotcha](#yaml-gotcha-colon-space-in-learning-outcomes) below before writing these. |
| `summary`          | pipe string     | Plain prose summary of the module. |

The body text must repeat the `summary` value.

---

### 4. Lesson file (`##_name.md`)

Each lesson file lives inside the module folder. The filename must match what is listed in the module's `files` array.

```yaml
---
name: Reading Data into R
dependsOn: [introduction_to_R.introduction_to_r]
learningOutcomes:
  - Load data from CSV and Excel files into tibbles.
  - Choose appropriate import functions for common file formats.
---

## Section heading

Lesson content starts here...
```

| Field              | Type            | Description |
|--------------------|-----------------|-------------|
| `name`             | string          | Display name for the lesson, shown as the page title. |
| `dependsOn`        | list            | For the first lesson in a module, use `[themeId.moduleId]`. For subsequent lessons, use `[themeId.moduleId.previous_lesson_filename_without_extension]` to enforce ordering. |
| `learningOutcomes` | YAML list       | What learners can do after this lesson. Same colon-space rule applies. |
| `tags`             | list (optional) | Topic tags, e.g. `[docker, containerization]`. |

There is no body summary for lesson files — content starts directly after the closing `---`.

---

## Naming Conventions

| What               | Convention | Example |
|--------------------|-----------|---------|
| Theme folder       | Match `id` exactly, lowercase `snake_case` | `introduction_to_r`, `introduction_to_statistics` |
| Module folder      | Match `id` exactly, `snake_case` | `introduction_to_r`, `module_one` |
| Lesson files       | Zero-padded two-digit prefix followed by a short descriptive slug | `00_getting_started_with_r.md`, `03_building_your_own_images.md` |
| `figs/` folder     | One per module, lowercase | `introduction_to_r/figs/` |
| `id` values        | Must be stable — the app derives URLs from them. Changing an `id` after publication will break links. | |

---

## YAML Gotcha — Colon-Space in Learning Outcomes

In YAML block sequences, any list item that contains `: ` (colon followed by a space) is parsed as a **mapping (object)** rather than a plain string. The app calls `.map()` on each outcome expecting a string; receiving an object instead throws `TypeError: a.map is not a function` and crashes the Next.js build.

**Wrong — `js-yaml` parses this as `{Define statistics and explain its key components: "data collection..."}`**

```yaml
learningOutcomes:
  - Define statistics and explain its key components: data collection, analysis, interpretation, and presentation.
```

**Correct — wrap in double quotes to force plain string parsing**

```yaml
learningOutcomes:
  - "Define statistics and explain its key components: data collection, analysis, interpretation, and presentation."
```

Use double quotes around any outcome that contains a colon followed by a space. Outcomes without colons do not need quoting.

---

## Step-by-Step Guide: Adding a New Theme and Module

### Step 1 — Create the folder structure

```
my_new_theme/
  index.md
  module_one/
    index.md
    00_first_lesson.md
    figs/
```

Create a `figs/` folder even if the module has no images yet — add a `.gitkeep` file inside to ensure it is tracked by git.

### Step 2 — Write the theme `index.md`

Set `id` to the exact folder name. Add the module folder names to `courses`. Write a one-paragraph `summary` and paste the same text as the body.

### Step 3 — Write the module `index.md`

Set `id` to the exact folder name. List every lesson filename in `files` in the order learners should read them. Write `learningOutcomes` as a YAML list, quoting any item that contains `: `. Populate `dependsOn` if this module requires a prior module from the same or a different theme.

### Step 4 — Write the lesson files

Name each file `##_slug.md` starting at `00`. Set `dependsOn` to `[themeId.moduleId]` on the first lesson. On each subsequent lesson, set `dependsOn` to `[themeId.moduleId.previous_lesson_filename_without_extension]`.

### Step 5 — Register the theme in the root `index.md`

Add the theme folder name to the `themes` list. The value must match the folder name and the theme's `id` exactly.

### Step 6 — Commit

```
feat(<theme_id>): add <theme name> theme with <n> module(s)
```

---

## Templates

### Theme `index.md`

```yaml
---
id: <folder_name>
name: "<Human Readable Name>"
courses: [
  <module_folder_name>,
]
summary: |
  <One paragraph describing what the theme covers and what learners leave with.>
---

<Same paragraph as summary above.>
```

### Module `index.md`

```yaml
---
name: <Module Display Name>
id: <folder_name>
dependsOn: []
files: [
  00_first_lesson.md,
  01_second_lesson.md,
]
learningOutcomes:
  - <Outcome that does not contain a colon.>
  - "<Outcome that contains a colon: must be quoted like this.>"
summary: |
  <One paragraph describing what this module covers and what learners practise.>
---

<Same paragraph as summary above.>
```

### Lesson file

```yaml
---
name: <Lesson Display Name>
dependsOn: [<themeId>.<moduleId>]
learningOutcomes:
  - <What learners can do after this lesson.>
---

## <First Section Heading>

Content begins here.
```

### Lesson file (with explicit lesson dependency)

```yaml
---
name: <Lesson Display Name>
dependsOn: [<themeId>.<moduleId>.<previous_lesson_filename_without_extension>]
learningOutcomes:
  - <What learners can do after this lesson.>
---
```

---

## Existing Themes

| Theme folder | `id` | Modules |
|---|---|---|
| `docker_containerization` | `docker_containerization` | `introduction_to_docker` |
| `introduction_to_R` | `introduction_to_R` | `introduction_to_r` |
| `introduction_to_statistics` | `introduction_to_statistics` | `statistics_and_probability`, `hypothesis_testing`, `statistical_modelling` |

---

## CI Checks

Every push and pull request targeting `main` that touches a `.md` file runs three automated checks defined in `.github/workflows/lint.yml`:

| Check | What it validates |
|---|---|
| `check-markdown-yaml` | YAML frontmatter in every `.md` file is syntactically valid (runs `alasdairwilson/front-matter-lint`). |
| `lint-python-codeblocks` | Python code blocks inside markdown files pass `flake8`-style linting (runs `OxfordRSE/lint-md-codeblocks`). R and shell code blocks are ignored. |
| `lint-markdown` | Markdown style rules via `markdownlint-cli`. A `.markdownlint.json` config at the repo root controls which rules are enforced. |

All three checks must pass before merging.
