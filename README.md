# Buckzy API Python Client

This repository hosts a Python client designed to facilitate interaction with the Buckzy API, implementing key endpoints for various financial operations. It provides a structured and extensible approach to integrating with Buckzy's services using the popular `requests` library.

## Table of Contents

- [Overview](#Overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Key API Methods](#key-api-methods)
- [API Endpoints Implementation](#api-endpoints-implementation)
  - [1. Entity Documents Management](#1-entity-documents-management)
  - [2. Customer Management (Individual, Corporate)](#2-customer-management-individual-corporate)
  - [3. SPOT Rates](#3-spot-rates)
  - [4. Buckzy Account Management](#4-buckzy-account-management)
  - [5. Payout Transaction Endpoint](#5-payout-transaction-endpoint)
- [Error Handling](#error-handling)
- [Assumptions](#assumptions)
- [Running the Example](running-the-example)

## Overview

This project serves as a foundational Python client for interacting with the Buckzy API. It abstracts the complexities of HTTP requests and JSON handling, allowing developers to focus on integrating Buckzy's financial services into their applications. The client covers essential functionalities such as managing customer profiles, handling financial accounts, processing payout transactions, and retrieving real-time exchange rates.

## Features

The current implementation of the Buckzy API Python Client includes support for the following core functionalities as specified:

  1. **Entity Documents Management**: Provides methods to upload, retrieve, and list documents associated with various entities (e.g., KYC documents for customers).
  2. **Customer Management (Individual, Corporate)**: Enables the creation, retrieval, and updating of both individual and corporate customer profiles within the Buckzy system.
  3. **SPOT Rates**: Offers functionality to fetch real-time foreign exchange spot rates for specified currency pairs.
  4. **Buckzy Account Management**: Supports the creation of new Buckzy internal accounts, retrieval of their detailed information, and querying of their current balances.
  5. **Payout Transaction Endpoint**: Facilitates the initiation of new money payout transactions and allows for checking the real-time status of these transactions.

## Prerequisites

Before you can use this client, ensure you have the following installed on your system:

* **Python 3.7+**: This client is developed and tested with Python 3.7 and newer versions.
* **`requests` library**: This is a powerful and user-friendly HTTP library for Python, essential for making API calls.
* **`python-dotenv` (Recommended)**: For securely managing environment variables, especially API keys.

You can install the necessary Python packages using `pip`:

```bash
pip install requests python-dotenv
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/haritha110/Buckzy_API.git](https://github.com/haritha110/Buckzy_API.git)
    cd Buckzy_API
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install required Python packages:**
    ```bash
    pip install requests python-dotenv
    ```

## Configuration

The client requires your Buckzy API Key and the correct Base URL to authenticate and communicate with the Buckzy API.

Security Best Practice: It is critically important to NEVER hardcode sensitive API keys directly in your source code, especially for production deployments. Environment variables are the recommended secure method.

  1. Obtain Your Buckzy API Key:
You will need to acquire your unique API key from the Buckzy developer portal or by contacting Buckzy support.

  2. Determine the Buckzy Base URL:
 This is typically in a format like `https://api.buckzy.net/v1`.

**Recommended Configuration Method (using .env file):**

Create a file named `.env` in the root directory of your project (the same directory as `buckzy_client.py`). Add your credentials to this file:

  ```bash
# .env file
BUCKZY_BASE_URL=[https://api.buckzy.net/v1](https://api.buckzy.net/v1)
BUCKZY_API_KEY=your_actual_buckzy_api_key_here
  ```

The `buckzy_client.py` script is set up to load these variables automatically if `python-dotenv` is installed:

   ```bash
import os
from dotenv import load_dotenv

load_dotenv() # This function loads variables from the .env file into os.environ

BUCKZY_BASE_URL = os.environ.get("BUCKZY_BASE_URL")
BUCKZY_API_KEY = os.environ.get("BUCKZY_API_KEY")

if BUCKZY_API_KEY == "YOUR_BUCKZY_API_KEY" or not BUCKZY_API_KEY or not BUCKZY_BASE_URL:
    print("WARNING: Please update BUCKZY_API_KEY and BUCKZY_BASE_URL with your actual credentials.")
    print("Exiting example usage.")
    exit()

# Initialize the client with loaded credentials
client = BuckzyAPIClient(BUCKZY_BASE_URL, BUCKZY_API_KEY)
  ```

### Key API Methods (as they might appear in `buckzy_client.py`)

Below is a representation of the key methods you would find in the `BuckzyAPIClient` class, which encapsulate the API calls:

* `__init__(self, api_key, base_url)`: Initializes the API client with credentials.
* `_make_request(self, method, endpoint, payload=None, params=None)`: A private helper method for making HTTP requests.
* `upload_entity_document(self, entity_id, document_data)`: Uploads a document for a given entity.
* `get_entity_documents(self, entity_id)`: Retrieves documents associated with an entity.
* `create_individual_customer(self, customer_data)`: Creates a new individual customer.
* `get_individual_customer(self, customer_id)`: Retrieves details of an individual customer.
* `create_corporate_customer(self, customer_data)`: Creates a new corporate customer.
* `get_corporate_customer(self, customer_id)`: Retrieves details of a corporate customer.
* `get_spot_rate(self, source_currency, target_currency, amount=None)`: Fetches the spot exchange rate between two currencies.
* `create_account(self, account_data)`: Creates a new Buckzy account.
* `get_account_details(self, account_id)`: Retrieves details of a Buckzy account.
* `initiate_payout(self, payout_data)`: Initiates a payout transaction.
* `get_payout_status(self, payout_id)`: Retrieves the status of a specific payout transaction.

## API Endpoints Implementation

The following sections detail the specific methods implemented within the `BuckzyAPIClient` for each of the required API endpoints.
  1. Entity Documents Management:
     
     Methods for uploading, retrieving, and listing documents associated with entities.
       - `upload_entity_document(self, entity_id, document_data_base64, document_type, filename)`:
         - Endpoint Placeholder: `documents/entity/{entity_id}`
         - Payload: Assumes `document_data_base64` is the Base64 encoded content of the file. `document_type` and `filename `are also part of the JSON payload.
         - Note: If Buckzy's API expects `multipart/form-data` for file uploads, this method and the `_make_request` helper would require significant modification (e.g., using files parameter in `requests.post`).
      - `get_entity_document(self, entity_id, document_id)`:
         - Endpoint Placeholder: `documents/entity/{entity_id}/{document_id}`
     - `list_entity_documents(self, entity_id`):
         - Endpoint Placeholder: `documents/entity/{entity_id}/{document_id}`

  **Example Usage**

  ```bash
import base64

# Assuming 'customer_id' is obtained from a successful customer creation
customer_id = "example_customer_id_123" # Replace with a real customer ID

# Simulate a base64 encoded document content (e.g., from reading a PDF file)
dummy_file_content = "This is a sample document for Buckzy API assessment. It represents a file."
encoded_content = base64.b64encode(dummy_file_content.encode('utf-8')).decode('utf-8')

print("\n--- Testing Entity Documents Management ---")
# Upload a document
upload_doc_resp = client.upload_entity_document(
    customer_id, encoded_content, "PROOF_OF_IDENTITY", "my_id_document.pdf" # Verify documentType
)
print(f"Upload Document: {json.dumps(upload_doc_resp, indent=2)}")

if not upload_doc_resp.get("error"):
    # Assuming 'id' or 'documentId' is the key for the document ID in the response
    document_id = upload_doc_resp.get("id") or upload_doc_resp.get("documentId")
    if document_id:
        print(f"Obtained Document ID: {document_id}")

        # Get a specific document
        get_doc_resp = client.get_entity_document(customer_id, document_id)
        print(f"Get Document ({document_id}): {json.dumps(get_doc_resp, indent=2)}")

        # List all documents for the entity
        list_docs_resp = client.list_entity_documents(customer_id)
        print(f"List Documents for Customer ({customer_id}): {json.dumps(list_docs_resp, indent=2)}")
    else:
        print("Document ID not found in upload response. Skipping get/list document operations.")
else:
    print("Skipping further document operations due to upload failure.")
```

  2. Customer Management (Individual, Corporate):
     
     Methods for creating, retrieving, and updating customer profiles.
     - `create_individual_customer(self, customer_data)`:
        - Endpoint Placeholder: `customers/individual`
     - `create_corporate_customer(self, customer_data)`:
       - Endpoint Placeholder: `customers/corporate`
     - `get_customer(self, customer_id)`:
         - Endpoint Placeholder:` customers/{customer_id}`
    - `update_customer(self, customer_id, update_data)`:
      - Endpoint Placeholder: `customers/{customer_id}`

  **Example Usage**

  ```bash
print("\n--- Testing Customer Management ---")
# Create an individual customer
customer_data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "email": "jane.doe.test@example.com",
    "phone": "+15551234567",
    "address": {
        "street": "789 Elm St", "city": "Springfield", "state": "IL",
        "zipCode": "62701", "country": "USA"
    },
    "dateOfBirth": "1990-05-15",
    "nationality": "US"
    # *** IMPORTANT: Add all other required fields as per Buckzy API docs ***
    # e.g., "uniqueId": "some_unique_identifier_for_jane"
}
create_customer_resp = client.create_individual_customer(customer_data)
print(f"Create Individual Customer: {json.dumps(create_customer_resp, indent=2)}")

customer_id = None # Initialize customer_id for chaining
if not create_customer_resp.get("error"):
    # Assuming 'id' or 'customerId' is the key for the customer ID in the response
    customer_id = create_customer_resp.get("id") or create_customer_resp.get("customerId")
    if customer_id:
        print(f"Obtained Customer ID: {customer_id}")

        # Get customer details
        get_customer_resp = client.get_customer(customer_id)
        print(f"Get Customer ({customer_id}): {json.dumps(get_customer_resp, indent=2)}")

        # Update customer details
        update_data = {"phone": "+15559876543", "address": {"street": "101 Maple Ave"}}
        update_customer_resp = client.update_customer(customer_id, update_data)
        print(f"Update Customer ({customer_id}): {json.dumps(update_customer_resp, indent=2)}")
    else:
        print("Customer ID not found in creation response. Skipping get/update operations.")
else:
    print("Failed to create individual customer. Skipping related operations.")

# Example for corporate customer (data structure would differ significantly)
# corporate_customer_data = {
#     "companyName": "Acme Corp",
#     "registrationNumber": "REG12345",
#     # ... other corporate specific fields
# }
# create_corporate_resp = client.create_corporate_customer(corporate_customer_data)
# print(f"Create Corporate Customer: {json.dumps(create_corporate_resp, indent=2)}")

```

  3. SPOT Rates:
     
     Method to fetch real-time foreign exchange spot rates.
     - `get_spot_rates(self, from_currency, to_currency):`
         - Endpoint Placeholder: `rates/spot`
      - Parameters: `fromCurrency, toCurrency`
        
  **Example Usage**

  ```bash
print("\n--- Testing SPOT Rates ---")
# Get SPOT rates for USD to JPY
spot_rates_resp = client.get_spot_rates("USD", "JPY")
print(f"Get SPOT Rates (USD/JPY): {json.dumps(spot_rates_resp, indent=2)}")
```

  4. Buckzy Account Management:
     
     Methods for creating, retrieving details, and querying balances of Buckzy internal accounts.
     - `create_buckzy_account(self, account_data`):
        - Endpoint Placeholder:` accounts`
      - `get_buckzy_account_details(self, account_id)`:
          - Endpoint Placeholder: `accounts/{account_id}`
      - `get_buckzy_account_balance(self, account_id):`
        - Endpoint Placeholder:` accounts/{account_id}/balance`
          
  **Example Usage**

  ```bash
print("\n--- Testing Buckzy Account Management ---")
buckzy_account_id = None # Initialize account_id for chaining
if customer_id: # Requires a customer to be created first
    account_data = {
        "customerId": customer_id, # Link to the customer created above
        "currency": "USD",
        "accountType": "PRIMARY_WALLET" # Verify valid account types with Buckzy docs
        # *** IMPORTANT: Add all other required fields as per Buckzy API docs ***
    }
    create_acc_resp = client.create_buckzy_account(account_data)
    print(f"Create Account: {json.dumps(create_acc_resp, indent=2)}")

    if not create_acc_resp.get("error"):
        # Assuming 'id' or 'accountId' is the key for the account ID in the response
        buckzy_account_id = create_acc_resp.get("id") or create_acc_resp.get("accountId")
        if buckzy_account_id:
            print(f"Obtained Buckzy Account ID: {buckzy_account_id}")

            # Get account details
            get_acc_details_resp = client.get_buckzy_account_details(buckzy_account_id)
            print(f"Get Account Details ({buckzy_account_id}): {json.dumps(get_acc_details_resp, indent=2)}")

            # Get account balance
            get_acc_balance_resp = client.get_buckzy_account_balance(buckzy_account_id)
            print(f"Get Account Balance ({buckzy_account_id}): {json.dumps(get_acc_balance_resp, indent=2)}")
        else:
            print("Buckzy Account ID not found in creation response. Skipping get details/balance.")
    else:
        print("Failed to create Buckzy account. Skipping related operations.")
else:
    print("Skipping Buckzy Account Management: No customer ID available from previous step.")
```


  5. Payout Transaction Endpoint:
     
     Methods for initiating new money payout transactions and checking their status.
     - ` initiate_payout_transaction(self, transaction_data`):
         - Endpoint Placeholder: `payouts`
      - ` get_payout_transaction_status(self, transaction_id):`
         - Endpoint Placeholder: `payouts/{transaction_id}/status`
    
  **Example Usage**

  ```bash
print("\n--- Testing Payout Transaction Endpoint ---")
payout_transaction_id = None # Initialize transaction_id for chaining
if customer_id and buckzy_account_id: # Requires customer and account
    payout_data = {
        "sourceAccountId": buckzy_account_id,
        "sourceCurrency": "USD",
        "sourceAmount": 50.00,
        "destinationCurrency": "EUR",
        "transactionType": "CROSS_BORDER_PAYOUT", # Verify valid transaction types
        "purposeOfTransaction": "Family Support",
        "receiverDetails": {
            "receiverName": "Recipient Name",
            "receiverEmail": "recipient@example.com",
            "bankDetails": {
                "bankName": "Deutsche Bank", "iban": "DE12345678901234567890", "bicSwift": "DEUTDEFF"
            },
            "address": {
                "street": "1 Bahnhofstr", "city": "Berlin", "zipCode": "10115", "country": "DEU"
            }
        }
        # *** IMPORTANT: Add all other required fields like idempotency key as per Buckzy API docs ***
    }
    initiate_payout_resp = client.initiate_payout_transaction(payout_data)
    print(f"Initiate Payout: {json.dumps(initiate_payout_resp, indent=2)}")

    if not initiate_payout_resp.get("error"):
        # Assuming 'id' or 'transactionId' is the key for the transaction ID in the response
        payout_transaction_id = initiate_payout_resp.get("id") or initiate_payout_resp.get("transactionId")
        if payout_transaction_id:
            print(f"Obtained Payout Transaction ID: {payout_transaction_id}")

            # Get payout transaction status
            get_payout_status_resp = client.get_payout_transaction_status(payout_transaction_id)
            print(f"Get Payout Status ({payout_transaction_id}): {json.dumps(get_payout_status_resp, indent=2)}")
        else:
            print("Transaction ID not found in payout initiation response. Skipping status check.")
    else:
        print("Failed to initiate payout transaction. Skipping status check.")
else:
    print("Skipping Payout Transaction: Missing customer ID or Buckzy account ID from previous steps.")
```

## Error Handling

The `BuckzyAPIClient` methods are designed to raise exceptions for API errors (e.g., HTTP status codes 4xx or 5xx). It's crucial to implement `try-except` blocks in your application code (as demonstrated in `buckzy_client.py`) to gracefully handle these scenarios, log errors, and provide appropriate feedback.

## Assumptions

* The Buckzy API uses an API key for authentication, passed in the `Authorization` header as a `Bearer` token.
* Request bodies for `POST` and `PUT` methods are typically JSON.
* Response bodies from the API are typically JSON.
* Specific endpoint paths and required payload structures (e.g., fields for customer creation, document formats, payout details) are derived from Buckzy's official API documentation (`https://docs-api.buckzy.net/`). You must consult their latest documentation for exact specifications.
* For document upload, the `fileContent` is assumed to be Base64 encoded.

## Running the Example

The `buckzy_client.py` file contains an `if __name__ == "__main__"`: block that demonstrates how to use each implemented endpoint. It attempts to chain operations where dependencies exist (e.g., creating a customer before creating an account for that customer).

  1. Ensure you have configured your API Key and Base URL as described in the Configuration section.
  2. Make sure all placeholder data in the example usage is updated to match the actual requirements of the Buckzy API.
  3. Run the script from your terminal:

 ```bash
python buckzy_client.py
```


  
  
