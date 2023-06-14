# ThrillTogether

# Инициализация проекта

## Инициализация backend-а
1. Установка venv
/root
```bash
python3 -m venv venv
```
для windows
```bash
venv\Scripts\activate
```
для linux
```bash
source venv/bin/activate
```
2. Установка модулей
```bash
pip install flask flask_sqlalchemy flask_cors flask_jwt_extented flask_marshmallow marshmallow_sqlalchemy Werkzeug
```
3. Инициализация базы данных
```bash
flask db init
```
```bash
flask db migrate -m "add_tables"
```
```bash
flask db upgrade
```

## Запуск backend-а

```bash
python3 run.py
```

## Запуск frontend-a

```bash
cd /client
```
1. Установка (один раз)

```bash
npm install
```

2. Запуск
```bash
npm run dev
```


