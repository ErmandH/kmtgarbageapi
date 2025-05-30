# Sample FastAPI Project

A sample REST API project built with FastAPI, demonstrating CRUD operations on items.

## Features

- FastAPI framework with automatic OpenAPI documentation
- CRUD operations for managing items
- Proper project organization with routes, models, and schemas
- In-memory database for demonstration purposes
- Pydantic models for data validation and serialization

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── items.py
│   └── schemas/
│       ├── __init__.py
│       └── item.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-sample.git
cd fastapi-sample
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server with:

```bash
python main.py
```

Alternatively, you can use Uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

## API Documentation

FastAPI provides automatic API documentation:

- OpenAPI documentation: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Root endpoint with API information
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item by ID
- `POST /items` - Create a new item
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item

## Example API Usage

### Creating a New Item

```bash
curl -X 'POST' \
  'http://localhost:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Example Item",
    "description": "This is an example item",
    "price": 19.99,
    "is_available": true
  }'
```

### Getting All Items

```bash
curl -X 'GET' 'http://localhost:8000/items/'
```

### Getting a Specific Item

```bash
curl -X 'GET' 'http://localhost:8000/items/1'
```

### Updating an Item

```bash
curl -X 'PUT' \
  'http://localhost:8000/items/1' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Updated Item",
    "price": 29.99
  }'
```

### Deleting an Item

```bash
curl -X 'DELETE' 'http://localhost:8000/items/1'
```
