# Barcode API

## Overview
This project is a barcode scanning API built with FastAPI. It allows users to scan barcodes, store product information in a database, and interact with the data through various API endpoints.

## Project Structure
```
barcode-api/
├── app/
│   ├── main.py          # Entry point of the API application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas for data validation
│   ├── crud.py          # CRUD operations for database interaction
│   └── database.py      # Database connection and session management
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd barcode-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database (if necessary) and configure the connection settings in `app/database.py`.

## Usage
To run the API, execute the following command:
```
uvicorn app.main:app --reload
```
This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

## API Endpoints
- **POST /products**: Add a new product.
- **GET /products/{id}**: Retrieve a product by ID.
- **DELETE /products/{id}**: Delete a product by ID.

## License
This project is licensed under the MIT License.