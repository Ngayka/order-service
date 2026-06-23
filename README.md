# Order Service API (FastAPI)

REST API для керування клієнтами, продуктами та замовленнями. 
Реалізовано на FastAPI + SQLAlchemy + SQLite + Alembic.

### Features

* Створення та перегляд клієнтів
* Управління продуктами
* Створення замовлень з позиціями (order items)
* Автоматичний розрахунок total_price
* Зв’язки між сутностями:
*     Client → Orders (one-to-many)
*     Order → OrderItems (one-to-many)
*     Product → OrderItems (one-to-many)
* Міграції через Alembic

### Tech Stack

* Python 3.12
* FastAPI
* SQLAlchemy (ORM)
* Pydantic
* SQLite
* Alembic

### Project Structure
```text
order_service/
│
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── service/         # Business logic layer
├── views/           # FastAPI routes
├── db/              # Database session & base
└── main.py          # Entry point
```

### Run project
1. Install dependencies

`pip install -r requirements.txt`

2. Run migrations

`alembic upgrade head`

3. Start server

`uvicorn order_service.main:app --reload`

### API Endpoints
**Clients**
* POST /clients – create client
* GET /clients – list clients
**Products**
* POST /products – create product
* GET /products – list products
* GET /products/{id} – get product
**Orders**
* POST /orders – create order (with items)
* GET /orders?client_id={id} – list orders by client

### Business Logic
При створенні замовлення:

* Перевіряється існування клієнта
* Перевіряються товари
* Розраховується total_price
* Створюються OrderItems
* Все зберігається в одній транзакції