# 🧪 Web Automation Suite (Selenium, Python & Pytest)

Automated web UI testing project designed using the **Page Object Model (POM)** pattern, built with **Python**, **Selenium WebDriver**, and **Pytest**. The main goal is to validate search workflows on the **DuckDuckGo** search engine, ensuring test execution scalability, maintainability, and robustness.

---

## 🛠️ Tech Stack & Tools
* 🐍 **Python 3.x** - Core programming language.
* 🌐 **Selenium WebDriver** - Web browser interaction and automation.
* 🧪 **Pytest** - Test runner framework and fixture management.
* 🏛️ **Page Object Model (POM)** - Design pattern separating business logic from web element locators.
* 📄 **JSON** - Centralized environment configuration file (`config.json`).

---

## 📁 Project Structure

```text
tau_selenium/
├── config.json          # Global configuration (browser type, wait timeouts, headless settings)
├── pages/               # Page Object Model (POM) Layer
│   ├── search.py        # Locators and actions for the main search page
│   └── result.py        # Locators and actions for the search results page
├── tests/               # Test Suite Layer
│   ├── conftest.py      # Pytest fixtures and WebDriver lifecycle management
│   └── test_search.py   # Parameterized test cases
└── README.md            # Project documentation