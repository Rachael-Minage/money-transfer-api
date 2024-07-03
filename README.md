# money-transfer-api

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Create Account
- **URL**: `/accounts`
- **Method**: POST
- **Payload**:
    ```json
    {
        "account_number": 1234567890,
        "account_name": "John Doe",
        "account_type": "Checking",
        "balance": "1000.00",
        "currency": "USD"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "account_number": 1234567890,
        "account_name": "John Doe",
        "account_type": "Checking",
        "balance": "1000.00",
        "currency": "USD",
        "is_active": true,
        "date_created": "2024-07-03T00:00:00Z"
    }
    ```

### Get Account
- **URL**: `/accounts/{id}`
- **Method**: GET
- **Response**:
    ```json
    {
        "id": 1,
        "account_number": 1234567890,
        "account_name": "John Doe",
        "account_type": "Checking",
        "balance": "1000.00",
        "currency": "USD",
        "is_active": true,
        "date_created": "2024-07-03T00:00:00Z"
    }
    ```

### Create Transfer
- **URL**: `/transfers`
- **Method**: POST
- **Payload**:
    ```json
    {
        "origin_account": 1,
        "destination_account": 2,
        "transfer_amount": "100.00",
        "transfer_type": "Online",
        "transfer_code": "TRN12345",
        "transfer_charge": "5.00",
        "status": "Completed"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Transfer successful",
        "transfer_id": 1
    }
    ```

## Running Tests
To run tests, execute:
```bash
python manage.py test
