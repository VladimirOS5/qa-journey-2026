# 🗺 ROADMAP: 16 недель до Junior QA Automation

> Полный план обучения. Каждая неделя = конкретные темы, материалы и артефакты.

---

## 📐 Принципы обучения

1. **70/30** — 70% практики, 30% теории.
2. **Один артефакт в неделю** — если нет файла в репозитории, неделя не засчитана.
3. **Помодоро** — 50 минут учёбы, 10 минут отдыха. После 3 циклов — перерыв 30 минут.
4. **1 выходной в неделю** — полностью без QA.
5. **Если застрял >2 часа** — спрашивай, не сиди в тупике.

---

## 🟦 Этап 1: Manual QA + Инструменты (Недели 1–2)

### Неделя 1: Основы QA + Тест-дизайн + DevTools

**Цель:** Уметь находить баги, писать тест-кейсы, использовать DevTools.

**Темы:**
- Виды тестирования: функциональное, нефункциональное, регрессионное, смоук
- Уровни тестирования: модульное, интеграционное, системное, приёмочное
- Тест-дизайн: эквивалентное разбиение, граничные значения, pairwise
- Chrome DevTools: Elements, Console, Network, Application
- Баг-репорт: summary, steps, expected, actual, severity, priority, environment

**Материалы:**
- [Хекслет — Основы тестирования](https://ru.hexlet.io/courses/testing) (модули 1–3, бесплатно)
- [Тест-дизайн — просто о сложном](https://habr.com/ru/articles/567826/) (Habr)
- [Chrome DevTools для QA](https://testgrow.ru/) (раздел DevTools)

**Практика:**
- Сайт для тестирования: [SauceDemo](https://www.saucedemo.com/)
- Логин: `standard_user`, Пароль: `secret_sauce`
- Составить чек-лист на авторизацию, каталог, корзину, оформление заказа
- Найти и задокументировать 3+ бага

**Артефакты:**
- `phase-1-manual/test-cases/saucedemo-checklist.md`
- `phase-1-manual/bug-reports/bug-001.md`, `bug-002.md`, `bug-003.md`

---

### Неделя 2: API + SQL + Jira

**Цель:** Работать с REST API в Postman, писать SQL-запросы, оформлять баги в Jira.

**Темы:**
- HTTP: методы (GET, POST, PUT, DELETE, PATCH), заголовки, тело запроса
- Статус-коды: 1xx, 2xx, 3xx, 4xx, 5xx
- JSON: структура, типы данных, массивы vs объекты
- Postman: коллекции, переменные, тесты (Tests tab)
- SQL: SELECT, WHERE, ORDER BY, JOIN (INNER, LEFT), GROUP BY, агрегаты (COUNT, SUM)
- Jira: создание issue, workflow (Open → In Progress → Resolved → Closed), приоритеты

**Материалы:**
- [Postman Learning Center — APIs 101](https://learning.postman.com/) (бесплатно)
- [SQLBolt](https://sqlbolt.com/) (уроки 1–12, бесплатно)
- [Jira Getting Started](https://www.atlassian.com/software/jira/guides)

**Практика:**
- API для тестирования: [Reqres](https://reqres.in/) или [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- Создать Postman-коллекцию: 5+ запросов (GET users, POST user, PUT user, DELETE user)
- SQL: решить 12 уроков на SQLBolt, сохранить запросы и результаты
- Jira: создать 5 баг-репортов на SauceDemo (можно в бесплатном облачном Jira)

**Артефакты:**
- `phase-1-manual/postman-collection.json`
- `phase-1-manual/sql-exercises.md`
- `phase-1-manual/bug-reports/jira-bugs.md`

---

## 🟩 Этап 2: Python для QA (Недели 3–5)

### Неделя 3: Python Basics

**Цель:** Уверенно писать скрипты на Python.

**Темы:**
- Переменные, типы: int, float, str, bool, None
- Операторы: арифметические, сравнения, логические (and, or, not)
- Условия: if / elif / else
- Циклы: for, while, break, continue
- Функции: def, return, аргументы (positional, keyword, default)
- Коллекции: list (списки), dict (словари), tuple, set
- Методы строк: split, join, replace, upper, lower, strip
- Методы списков: append, extend, pop, sort, len
- Методы словарей: keys, values, items, get

**Материалы:**
- [Automate the Boring Stuff — глава 1–6](https://automatetheboringstuff.com/) (бесплатно)
- [HackerRank Python](https://www.hackerrank.com/domains/python) (30 задач)

**Практика:**
- 30 задач на HackerRank (Easy уровень)
- Сохранить решения в `phase-2-python/exercises/`

**Артефакты:**
- `phase-2-python/exercises/hackerrank-w3.md` — список решённых задач со ссылками

---

### Неделя 4: Файлы, JSON, Модули

**Цель:** Работать с файлами и JSON — основа для API-тестов.

**Темы:**
- Работа с файлами: open, read, write, with (context manager)
- JSON: json.load, json.loads, json.dump, json.dumps
- Модули: import, from ... import, __name__ == '__main__'
- pip: установка пакетов, requirements.txt
- Виртуальное окружение: venv

**Материалы:**
- [Automate the Boring Stuff — глава 8, 14, 16](https://automatetheboringstuff.com/)

**Практика (мини-проект):**
- Скрипт `json-parser.py`:
  - Читает JSON-файл (ответ от API)
  - Выводит список имён пользователей
  - Считает количество записей
  - Фильтрует по условию (например, id > 5)
- Сохранить в `phase-2-python/mini-projects/json-parser/`

**Артефакты:**
- `phase-2-python/mini-projects/json-parser/json_parser.py`
- `phase-2-python/mini-projects/json-parser/sample_data.json`
- `phase-2-python/mini-projects/json-parser/README.md`

---

### Неделя 5: ООП для QA

**Цель:** Понимать классы и объекты — основа для Page Object Model.

**Темы:**
- Классы: class, __init__, self
- Атрибуты и методы экземпляра
- Наследование: class Child(Parent), super()
- Инкапсуляция: _protected, __private (понимание на уровне конвенций)
- Исключения: try/except/else/finally, raise, стандартные исключения
- Магические методы: __str__, __repr__ (базово)

**Материалы:**
- [Automate the Boring Stuff — глава 15, 16](https://automatetheboringstuff.com/)
- [Real Python — Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)

**Практика (мини-проект):**
- Класс `TestCase`:
  - Поля: title, description, steps (list), expected_result, actual_result, status (passed/failed/skipped)
  - Методы: run(), set_status(), to_dict()
- Класс `BugReport`:
  - Поля: title, severity, priority, steps, actual_result, expected_result, environment
  - Методы: to_markdown() — возвращает оформленный баг-репорт
- Класс `TestSuite`:
  - Поле: test_cases (list)
  - Методы: add_test(), run_all(), get_summary()

**Артефакты:**
- `phase-2-python/mini-projects/oop-models/test_case.py`
- `phase-2-python/mini-projects/oop-models/bug_report.py`
- `phase-2-python/mini-projects/oop-models/test_suite.py`
- `phase-2-python/mini-projects/oop-models/demo.py` — демо использования

---

## 🟨 Этап 3: UI-автоматизация (Недели 6–9)

### Неделя 6: Selenium WebDriver

**Цель:** Писать первые автотесты на Selenium.

**Темы:**
- Установка: selenium, webdriver-manager
- WebDriver: Chrome(), Firefox()
- Локаторы: By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR, By.XPATH
- XPath: абсолютный vs относительный, оси, предикаты, contains(), starts-with()
- CSS Selector: #id, .class, [attribute], >, +, ~, :nth-child()
- Ожидания: implicit_wait, explicit_wait (WebDriverWait + expected_conditions)
- Действия: click, send_keys, clear, submit, get_text, get_attribute
- Навигация: get, back, forward, refresh, current_url, title

**Материалы:**
- [Selenium with Python — официальная документация](https://selenium-python.readthedocs.io/)
- [WebDriverManager](https://github.com/SergeyPirogov/webdriver_manager)

**Практика:**
- 5+ тестов на SauceDemo:
  1. Успешная авторизация
  2. Авторизация с неверным паролем (проверка ошибки)
  3. Добавление товара в корзину
  4. Переход в корзину и проверка товара
  5. Оформление заказа (checkout)

**Артефакты:**
- `phase-3-ui-automation/tests/test_login.py`
- `phase-3-ui-automation/tests/test_cart.py`
- `phase-3-ui-automation/requirements.txt`

---

### Неделя 7: Pytest

**Цель:** Рефакторить тесты под Pytest, использовать фикстуры.

**Темы:**
- Установка pytest
- Запуск: pytest, pytest -v, pytest -s, pytest -k "keyword"
- Фикстуры: @pytest.fixture, scope (function, class, module, session)
- conftest.py — общие фикстуры
- Параметризация: @pytest.mark.parametrize
- Маркеры: @pytest.mark.smoke, @pytest.mark.regression, @pytest.mark.skip, @pytest.mark.xfail
- Assert: стандартный assert, проверка исключений (pytest.raises)

**Материалы:**
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)

**Практика:**
- Рефакторинг тестов недели 6 под Pytest
- Фикстура `driver` — создаёт и закрывает браузер
- Параметризованный тест авторизации (3 набора данных)
- Маркеры: smoke для критичных тестов

**Артефакты:**
- `phase-3-ui-automation/conftest.py`
- `phase-3-ui-automation/tests/test_login.py` (обновлённый)
- `phase-3-ui-automation/tests/test_cart.py` (обновлённый)

---

### Неделя 8: Page Object Model (POM)

**Цель:** Структурировать код по паттерну POM.

**Темы:**
- Зачем POM: разделение логики страницы и тестов
- Структура: pages/ (логика), tests/ (сценарии), conftest.py (фикстуры)
- BasePage: общие методы (find_element, click, send_keys, wait_for_element)
- Конкретные страницы: LoginPage, InventoryPage, CartPage
- Методы страниц возвращают другие страницы (навигация)

**Материалы:**
- [Page Object Model — Selenium Docs](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

**Практика:**
- Создать структуру:
  ```
  phase-3-ui-automation/
  ├── pages/
  │   ├── __init__.py
  │   ├── base_page.py
  │   ├── login_page.py
  │   ├── inventory_page.py
  │   └── cart_page.py
  ├── tests/
  │   ├── __init__.py
  │   ├── test_login.py
  │   ├── test_inventory.py
  │   └── test_cart.py
  ├── conftest.py
  └── requirements.txt
  ```

**Артефакты:**
- Полная POM-структура с 10+ тестами

---

### Неделя 9: Allure Report

**Цель:** Красивые отчёты о тестировании.

**Темы:**
- Установка allure-pytest
- Аннотации: @allure.feature, @allure.story, @allure.step, @allure.severity
- Вложения: allure.attach (скриншоты, логи, текст)
- Скриншот при падении (в фикстуре с yield)
- Генерация отчёта: allure serve, allure generate

**Материалы:**
- [Allure Report Docs](https://docs.qameta.io/allure/)

**Практика:**
- Добавить Allure-аннотации ко всем тестам
- Скриншот при падении
- Сгенерировать отчёт, сделать скриншот, добавить в README

**Артефакты:**
- Обновлённые тесты с Allure
- Скриншот отчёта в README

---

## 🟪 Этап 4: API-автоматизация (Недели 10–11)

### Неделя 10: Requests + Pytest для API

**Цель:** Автоматизировать API-тесты.

**Темы:**
- Библиотека requests: get, post, put, delete, patch
- Параметры: params (query string), json (тело), headers, auth
- Response: status_code, json(), text, headers
- Pytest для API: фикстуры для base_url, session
- Проверки: assert response.status_code == 200, assert data["name"] == "John"

**Материалы:**
- [Requests: HTTP for Humans](https://docs.python-requests.org/)

**Практика:**
- API: [Reqres](https://reqres.in/)
- Тесты:
  1. GET /users — проверка статуса 200, проверка структуры ответа
  2. GET /users/2 — проверка конкретного пользователя
  3. POST /users — создание, проверка 201, проверка полей
  4. PUT /users/2 — обновление, проверка 200
  5. DELETE /users/2 — проверка 204
  6. GET /users/23 — несуществующий, проверка 404
  7. POST /register — успешная регистрация
  8. POST /register — неуспешная (без пароля), проверка 400

**Артефакты:**
- `phase-4-api-automation/tests/test_reqres.py`
- `phase-4-api-automation/conftest.py`
- `phase-4-api-automation/requirements.txt`

---

### Неделя 11: JSON Schema + Негативные сценарии

**Цель:** Валидировать структуру ответов и тестировать ошибки.

**Темы:**
- JSON Schema: типы, required, properties, items
- Библиотека jsonschema: validate, ValidationError
- Негативные тесты: невалидный JSON, неверный Content-Type, превышение лимитов
- Фикстуры для схем

**Материалы:**
- [JSON Schema Docs](https://json-schema.org/)
- [python-jsonschema](https://python-jsonschema.readthedocs.io/)

**Практика:**
- Создать схемы для:
  - GET /users (список)
  - GET /users/2 (один пользователь)
  - POST /users (создание)
- Негативные тесты:
  - Несуществующий endpoint
  - Невалидный JSON в POST
  - Пустое тело

**Артефакты:**
- `phase-4-api-automation/schemas/user_schema.json`
- `phase-4-api-automation/schemas/users_list_schema.json`
- `phase-4-api-automation/tests/test_reqres.py` (обновлённый)

---

## 🟫 Этап 5: Git + CI/CD (Недели 12–13)

### Неделя 12: Git

**Цель:** Профессиональная работа с Git.

**Темы:**
- git init, git add, git commit, git push, git pull
- git branch, git checkout, git merge
- git log, git status, git diff
- .gitignore
- Pull Request: создание, review, merge
- Конвенции коммитов: type: description

**Материалы:**
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Conventional Commits](https://www.conventionalcommits.org/)

**Практика:**
- Переписать историю коммитов: сделать их чистыми и понятными
- Создать ветку `feature/week-12`, сделать PR, смержить

---

### Неделя 13: GitHub Actions

**Цель:** Автоматический запуск тестов в облаке.

**Темы:**
- GitHub Actions: workflow, job, step, action
- Триггеры: on: push, pull_request
- Runners: ubuntu-latest
- Установка зависимостей: pip install -r requirements.txt
- Запуск тестов: pytest
- Сохранение артефактов: actions/upload-artifact
- Badge в README

**Материалы:**
- [GitHub Actions Docs](https://docs.github.com/en/actions)

**Практика:**
- Создать `.github/workflows/ci.yml`
- Настроить запуск UI и API тестов
- Добавить badge в README

**Артефакты:**
- `.github/workflows/ci.yml`
- Зелёный badge в README.md

---

## 🟥 Этап 6: Портфолио + Собеседования (Недели 14–16)

### Неделя 14: Проект 1 — UI-фреймворк

**Требования:**
- Отдельная папка `phase-5-portfolio/ui-project/`
- 20+ UI-тестов
- POM-структура
- Allure-отчёты
- GitHub Actions CI
- README с инструкцией по запуску
- requirements.txt

**Сайт для тестирования:** SauceDemo или [Automation Practice](http://automationpractice.com/)

---

### Неделя 15: Проект 2 — API-фреймворк

**Требования:**
- Отдельная папка `phase-5-portfolio/api-project/`
- 15+ API-тестов
- JSON Schema валидация
- GitHub Actions CI
- README с инструкцией по запуску
- requirements.txt

**API для тестирования:** Reqres или [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

---

### Неделя 16: Резюме + Собеседования

**Задачи:**
- Составить резюме (русское + английское)
- Подготовить ответы на вопросы:
  - Расскажи о себе
  - Что такое тестирование и зачем оно нужно
  - Жизненный цикл бага
  - Разница между severity и priority
  - Что такое регрессия и смоук
  - POM: зачем и как работает
  - Разница implicit vs explicit wait
  - Статус-коды HTTP
  - Что такое CI/CD и зачем нужен
- Пройти тестовое собеседование
- Разместить ссылку на GitHub в резюме

---

## 📚 Сводка материалов

| Ресурс | Тип | Цена | Этап |
|--------|-----|------|------|
| Хекслет — Основы тестирования | Тренажёр | Бесплатно | 1 |
| SQLBolt | Интерактив | Бесплатно | 1 |
| Postman Learning Center | Курс | Бесплатно | 1 |
| Automate the Boring Stuff | Книга | Бесплатно | 2 |
| HackerRank Python | Задачи | Бесплатно | 2 |
| Selenium Python Docs | Документация | Бесплатно | 3 |
| Pytest Docs | Документация | Бесплатно | 3 |
| Allure Report Docs | Документация | Бесплатно | 3 |
| Requests Docs | Документация | Бесплатно | 4 |
| GitHub Actions Docs | Документация | Бесплатно | 5 |
