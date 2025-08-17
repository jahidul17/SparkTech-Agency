# Library Management System API

A RESTful API for managing a library, built with Django and Django REST Framework.

## Features

- **User Registration & Login:** Secure authentication using JWT.
- **Browse & Borrow Books:** Users can view available books and borrow up to 3 at a time.
- **Admin Management:** Admins can add, edit, and delete books, authors, and categories.
- **Inventory Control:** Books have multiple copies; only available copies can be borrowed.
- **Atomic Updates:** Inventory is updated atomically when books are borrowed or returned.
- **Borrowing Rules:** Each borrow has a due date (14 days from borrowing).
- **Early Returns:** Users can return books before the due date.

## Getting Started

### Prerequisites

- Python 3.8+
- Django
- Django REST Framework
- djangorestframework-simplejwt

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/jahidul17/library-management.git
    cd library-management
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```


4. **Create a superuser (As admin login -Optional)**
    ```bash
    python manage.py createsuperuser
    ```

5. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6. **Run the server**
    ```bash
    python manage.py runserver
    ```

7. **Access the project:**
    Open your browser and go to `http://127.0.0.1:8000/`<br>

### Usage

- Register and log in to obtain a JWT token.
- Use the token to access protected endpoints for borrowing and returning books.
- Admins can manage books, authors, and categories via the admin panel.

## API Endpoints

| Method | Endpoint                | Description                       |
|--------|------------------------|-----------------------------------|
| POST   | v/api/register/         | As general user |
| POST   | v/api/admin/register/         | As admin user |
| POST   | v/api/login/            | Obtain JWT token |
| POST   | v/api/logout/            | Logout |
| POST   | v/api/refreshtoken/            | Obtain Refreshtoken |
| GET    | api/books/            | List all books |
| GET    | api/books/{id}/ | Filter by id |
| POST    | api/books/ | Post admin only |
| PUT    | api/books/{id}/ | PUT admin only |
| DELETE     | api/books/{id}/ | DELETE admin only |
| GET     | api/authors/ | List all |
| POST     | api/authors/ | Add admin only |
| GET     | api/categories/ | List all |
| POST     | api/categories/ | Add admin only |
| POST   | b/api/borrow/           | User Borrow a book |
| POST   | b/api/return/           | Return a borrowed book |



