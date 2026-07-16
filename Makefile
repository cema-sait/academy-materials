.PHONY: install-hooks lint

## install-hooks: point git's hook path at .githooks/ and make the hook executable
install-hooks:
	git config core.hooksPath .githooks
	chmod +x .githooks/pre-commit
	@echo "✓ Git hooks installed. The structure linter will run before every commit that touches a .md file."

## lint: run the structure linter manually against the whole repository
lint:
	@python3 -c "import yaml" 2>/dev/null || (echo "PyYAML required: pip install pyyaml" && exit 1)
	python3 scripts/lint_structure.py

## help: list available targets
help:
	@grep -E '^## ' Makefile | sed 's/## /  /'
