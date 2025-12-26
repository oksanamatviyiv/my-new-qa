# my-new-qa

Automated UI testing framework for web applications using Selenium and pytest.

## 📋 Description

This project is a QA automation framework designed to test web applications through UI page object model pattern. It includes tests for GitHub login and Rozetka e-commerce platform.

## 🛠 Technologies

- **Python** 3.x
- **Selenium** 4.15.2 - Web browser automation
- **pytest** 7.4.3 - Testing framework
- **pytest-html** 4.1.1 - HTML test reports
- **requests** 2.31.0 - HTTP library

## 📁 Project Structure

```
my-new-qa/
├── config/
│   └── config.py           # Configuration (URLs, users, settings)
├── modules/
│   └── ui/
│       └── page_objects/
│           ├── base_page.py        # Base page class
│           ├── sign_in_page.py     # GitHub login page
│           ├── header.py           # Header component
│           ├── cart_page.py        # Shopping cart page
│           └── track_page.py       # Tracking page
├── tests/
│   └── ui/
│       └── test_ui_page_object.py  # UI tests
├── requirements.txt        # Python dependencies
├── pytest.ini             # pytest configuration
├── conftest.py            # pytest fixtures
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd my-new-qa
```

2. Create virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

Run all UI tests:
```bash
pytest tests/ui/ -v
```

Run specific test:
```bash
pytest tests/ui/test_ui_page_object.py::test_check_incorrect_username_page_object -v
```

Generate HTML report:
```bash
pytest tests/ui/ -v --html=report.html
```

## 📝 Test Coverage

- GitHub login with invalid credentials
- Rozetka cart modal operations
- Product page cart functionality
- Parcel tracking input validation

## 🔧 Configuration

Update `config/config.py` with:
- Test URLs
- Valid/invalid user credentials
- Browser settings (headless mode, window size, timeout)

## 📚 Page Object Model

Tests use the Page Object Model pattern for maintainability:

- Each page has a dedicated class inheriting from `BasePage`
- Methods represent user interactions (login, click, fill, etc.)
- Selectors are centralized in page classes

## 👨‍💻 Author

Oksana Matviyiv
