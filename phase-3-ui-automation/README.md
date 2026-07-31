# Phase 3: UI-автоматизация

> Недели 6–9

## Структура

```
phase-3-ui-automation/
├── pages/           ← Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/           ← Тестовые сценарии
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── conftest.py      ← Фикстуры Pytest
├── requirements.txt ← Зависимости
└── README.md
```

## Запуск

```bash
pip install -r requirements.txt
pytest -v
pytest -m smoke
pytest --alluredir=allure-results
allure serve allure-results
```

## Чек-лист

- [ ] 5+ тестов на Selenium
- [ ] Рефакторинг под Pytest
- [ ] POM-структура
- [ ] Allure-отчёты
