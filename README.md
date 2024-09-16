Here's a concise version of the `README.md` file:

```markdown
# Product Catalog API

This is a Django-based RESTful API for managing a product catalog, with features like real-time inventory updates, product search, and asynchronous tasks using Celery.

## Features
- **CRUD Operations**: Create, Read, Update, Delete products
- **Product Search**: Search by name, description, category
- **Popularity Calculation**: Asynchronous popularity score based on sales
- **Real-Time Inventory Updates**: Handled using Celery

## Tech Stack
- **Backend**: Django, Django Rest Framework
- **Asynchronous Tasks**: Celery with Redis
- **Database**: PostgreSQL
- **Containerization**: Docker and Docker Compose

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/khand420/product-catalog-api.git
cd product-catalog-api
```

### 2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up the database:
Configure `.env` file with your DB credentials and run migrations:
```bash
python manage.py migrate
```

### 5. Create superuser:
```bash
python manage.py createsuperuser
```

### 6. Run the project:
```bash
python manage.py runserver
```

## Running Celery
Start Redis locally:
```bash
redis-server
```
Then, run Celery worker:
```bash
celery -A product_catalog worker --loglevel=info
or
celery -A product_catalog worker --pool=solo --loglevel=info
```

## Docker Setup
Build and run the app, Celery, and Redis using Docker:
```bash
docker-compose up --build
```

## API Endpoints

- **GET /api/products/**: List all products
- **POST /api/products/**: Create a product
- **GET /api/products/{id}/**: Get product by ID
- **PUT /api/products/{id}/**: Update product by ID
- **DELETE /api/products/{id}/**: Delete product by ID
- **GET /api/products/?search=product**: Search Query 

 

## License
This project is licensed under the MIT License.
```

This short version includes all the essential information needed to get the project up and running without overloading the reader with too many details.
