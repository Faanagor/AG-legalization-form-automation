POETRY = poetry
PYTHON = $(POETRY) run python
TEST = $(POETRY) run pytest
TEST_DIR = tests/
COV_REPORT_TERM = --cov-report=term-missing
COV_REPORT_HTML = --cov-report=html
APP = app
SCRIPT = $(APP)/form_automation.py
COV_PACKAGE = --cov=$(APP)
COV_FAILED_PERCENT = 85
COV_FAILED_UNDER = --cov-fail-under=$(COV_FAILED_PERCENT)
BLACK = $(POETRY) run black
ISORT = $(POETRY) run isort
FLAKE8 = $(POETRY) run flake8

.PHONY: install
install:
	pip install $(POETRY)
	$(POETRY) install
	pre-commit install

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files

.PHONY: test
test:
	$(TEST)

.PHONY: test-coverage
test-coverage:
	$(TEST) $(COV_PACKAGE) $(COV_REPORT_TERM) $(COV_FAILED_UNDER) $(TEST_DIR)

test-coverage-html:
	$(TEST) $(COV_PACKAGE) $(COV_REPORT_HTML) $(TEST_DIR) 

.PHONY: lint
lint:
	$(BLACK) . && $(ISORT) . && $(FLAKE8)

.PHONY: run
run:
	python $(SCRIPT)

.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -exec rm -rf {} +