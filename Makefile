test:
	@poetry run pytest -vv -n auto --disable-socket --cov=. --cov-report html --cov-fail-under 100 tests

qa: test
	@echo
	@echo "=========================="
	@echo "=== Checking main code ==="
	@echo "=========================="
	@echo
	@echo "=== pylint ==="
	-@poetry run pylint pynsted
	@echo "=== ruff ==="
	-@poetry run ruff check pynsted
	@echo "=== pyright ==="
	-@poetry run pyright pynsted
	@echo "=== checking types with mypy ==="
	-@poetry run mypy --strict pynsted
	@echo "=== checking formatting with black ==="
	-@poetry run black -l 79 --check pynsted
	@echo
	@echo "======================"
	@echo "=== Checking tests ==="
	@echo "======================"
	@echo
	@echo "=== pylint ==="
	-@poetry run pylint tests
	@echo "=== ruff ==="
	-@poetry run ruff check tests
	@echo "=== pyright ==="
	-@poetry run pyright tests
	@echo "=== checking types with mypy ==="
	-@poetry run mypy --strict tests
	@echo "=== checking formatting with black ==="
	-@poetry run black -l 79 --check tests
	@echo "========================================"
	@echo "=== Checking import order with isort ==="
	@echo "========================================"
	@PATCH="$$(poetry run isort pynsted tests --diff)" && echo $$PATCH && test -z "$$PATCH"

format:
	@poetry run black -l 79 pynsted
	@poetry run black -l 79 tests
	@poetry run isort pynsted tests

.PHONY: build clean format help install qa test
