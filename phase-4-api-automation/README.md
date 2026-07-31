# Phase 4: API-автоматизация

> Недели 10–11

## Структура

```
phase-4-api-automation/
├── tests/           ← API-тесты
│   └── test_reqres.py
├── schemas/         ← JSON Schema
│   ├── user_schema.json
│   └── users_list_schema.json
├── conftest.py      ← Фикстуры
├── requirements.txt ← Зависимости
└── README.md
```

## Запуск

```bash
pip install -r requirements.txt
pytest -v
```

## Чек-лист

- [ ] 10+ API-тестов
- [ ] JSON Schema валидация
- [ ] Негативные сценарии
