# ag-tigo-legalizer-bot
This is the documentation of ag-tigo-legalizer-bot project.
The project automate to fill the forms to legalize Sim Cards from Tigo telecomunications using Selenium

## Project Structure
Below is an overview of the main directories and files in the application, along with their purposes:

```bash
── ag-tigo-legalizer-bot
│ ├── app/
│ │ ├── init.py
│ │ ├── form_automation.py
│ ├── statics/
│ │ ├── chromedriver.exe
│ │ ├── LICENSE.chromedriver
│ │ ├── THIRD_PARTY_NOTICES.chromedriver
│ ├── init.py
│ ├── .flake8
│ ├── .gitignore
│ ├── .pre-commit-config.yaml
│ ├── CHANGELOG.md
│ ├── Dockerfile
│ ├── License
│ ├── main.py
│ ├── Makefile
│ ├── PULL_REQUEST_TEMPLATE.md
│ ├── pyproject.toml
│ ├── README.md
```
### Main Directory: app
This directory contains the core business logic and services of the application. It is modularly structured to ensure
scalability.

- app/form_automation/: This folder contains the main business logic of the application, organized into subdirectories
and files by service.

### Configuration and Utilities
These files handle configurations, tools, and code quality standards:

- .flake8: Configuration file for Flake8, defining exceptions and linting rules.
- .gitignore: Specifies files and directories to exclude from the Git repository.
- .pre-commit-config.yaml: Configuration for running linters and formatters automatically before committing changes.
- CHANGELOG.md: Records all significant changes made to the project over time.
- Dockerfile: Contains instructions for building the Docker image for the application.
- License: Contains License MIT contract about the project.
- main.py: File with config to run the project.
- Makefile: Provides common commands to simplify recurring tasks, such as testing, building Docker images, etc.
- PULL_REQUEST_TEMPLATE.md: Provides a standard structure to follow when submitting changes to the repository.
- pyproject.toml: Configuration file for Python tools like Poetry, managing dependencies settings and code formatting.
- README.md: Provides an overview of the project, its structure, purpose, and instructions for usage.

### Testing
tests/: Contains unit and integration tests for each service and utility function in the application.

## Installation Guide:
### 1. Clone the Repository:
Clone the repository using Git:
```bash
git clone https://github.com/Faanagor/AG-legalization-form-automation.git
cd project-name
```

### 2. Create and Activate Virtual Environment
- Create the virtual environment:
```bash
python -m venv venv
```
- Activate the virtual environment:
#### Windows:
```bash
venv\Scripts\activate
```
#### Linux:
```bash
source venv/bin/activate
```
- (Optional) Upgrade pip:
```bash
python -m pip install --upgrade pip
```
### 3. Install and Configure ChromeDriver for Selenium
- Install ChromeDriver:
Download the appropriate version of ChromeDriver for your Chrome browser from the official website.
Place the chromedriver executable in your system's PATH or in the project directory.
- Verify Installation:
Run the following command to ensure ChromeDriver is correctly installed:
```bash
chromedriver --version
```

### 4. From Install Dependencies to Run project:
#### - Using Makefile:
Install Dependencies:
```bash
make install
```
Configure Pre-Commit Hooks:
```bash
make pre-commit
```
Test Project:
```bash
make test
make test-coverage
```
Format and lint project:
```bash
make lint
```
Run Project:
```bash
make run
```

#### - Using Poetry:
Install Dependencies:
```bash
poetry install
```
Configure Pre-Commit Hooks:
```bash
pre-commit run --all-files
```
Test Project:
```bash
poetry run pytest
poetry run pytest --cov=app --cov-report=term-missing --cov-fail-under=85 tests/ 
```
Format and lint project:
```bash
poetry run black api
poetry run flake8
poetry run isort
```
Run Project:
```bash
python main.py
```
