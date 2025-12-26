# my-new-qa

QA automation project covering UI, API, and database tests with pytest.

## Description

This repository includes:
- UI tests built with Selenium and the Page Object Model (GitHub login, Rozetka cart/track flow)
- API tests against GitHub public endpoints
- SQLite database tests for customers, orders, and products

## Tech Stack

- Python 3.x
- pytest
- Selenium
- requests
- pytest-html
- sqlite3 (built-in)

## Project Structure

```
my-new-qa/
├── config/
│   └── config.py                 # URLs, users, browser settings
├── modules/
│   ├── api/
│   │   └── clients/              # API client wrappers
│   ├── common/
│   │   └── database.py           # SQLite helpers
│   └── ui/
│       └── page_objects/         # UI page objects
├── tests/
│   ├── api/                      # API tests
│   ├── database/                 # Database tests
│   └── ui/                       # UI tests
├── become_qa_auto.db             # SQLite database
├── conftest.py                   # pytest fixtures
├── pytest.ini                    # pytest configuration
└── requirements.txt              # Python dependencies
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- Google Chrome (or compatible) and matching ChromeDriver

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Update `config/config.py` with:
- Test URLs
- Valid/invalid user credentials
- Browser settings (headless, window size, timeouts)

Note: `modules/common/database.py` uses an absolute path to `become_qa_auto.db`. If you move the repo, update that path.

## Running Tests

Run all tests:
```bash
pytest -v
```

Run by area:
```bash
pytest tests/ui/ -v
pytest tests/api/ -v
pytest tests/database/ -v
```

Run by marker:
```bash
pytest -m api -v
pytest -m http -v
pytest -m database -v
pytest -m check -v
pytest -m change -v
```

Run a single test:
```bash
pytest tests/ui/test_ui_page_object.py::test_check_incorrect_username_page_object -v
```

Generate an HTML report:
```bash
pytest -v --html=report.html
```

## Test Coverage Overview

- UI: GitHub login validation, Rozetka cart/track flows
- API: GitHub user/repo/emoji/commit endpoints
- Database: customer, order, and product queries/updates

## Author

Oksana Matviyiv
