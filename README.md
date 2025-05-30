# Buckzy API Integration (Python)

This repository contains a Python implementation for interacting with the Buckzy API, covering key endpoints for managing entities, customers, rates, accounts, and payout transactions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Examples](#running-the-examples)
  - [Key API Methods](#key-api-methods)
- [Error Handling](#error-handling)
- [Assumptions](#assumptions)
- [License](#license)

## Project Overview

This project serves as a practical assessment demonstrating the ability to integrate with the Buckzy API using Python. It utilizes the `requests` library for making HTTP requests and is designed to be configurable via environment variables for sensitive information like API keys.

## Features

The following Buckzy API endpoints have been implemented:

1.  **Entity Documents Management:**
    * Upload entity documents.
    * Retrieve entity documents.
2.  **Customer Management (Individual, Corporate):**
    * Create individual customers.
    * Retrieve individual customer details.
    * Create corporate customers.
    * Retrieve corporate customer details.
3.  **SPOT Rates:**
    * Fetch real-time SPOT exchange rates.
4.  **Buckzy Account Management:**
    * Create Buckzy accounts.
    * Retrieve Buckzy account details.
5.  **Payout Transaction Endpoint:**
    * Initiate payout transactions.
    * Check payout transaction status.

## Prerequisites

Before you begin, ensure you have the following:

* **Python 3.7+** installed.
* **Buckzy API Key** and **Base URL**: Obtain these credentials from your Buckzy developer account.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/haritha110/buckzy-api-integration.git](https://github.com/YOUR_USERNAME/buckzy-api-integration.git)
    cd buckzy-api-integration
    ```
    (Replace `YOUR_USERNAME` with your GitHub username)

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

Sensitive information like your API key and the base URL should be managed securely, ideally using environment variables.

1.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env` and add your Buckzy API credentials:

    ```ini
    BUCKZY_API_KEY="YOUR_BUCKZY_API_KEY"
    BUCKZY_BASE_URL="[https://api.buckzy.net/v1](https://api.buckzy.net/v1)" # Or your specific base URL
    ```
    **Replace `YOUR_BUCKZY_API_KEY` and `https://api.buckzy.net/v1` with your actual credentials.**

2.  **Load environment variables in your Python code:**
    The provided `buckzy_assessment.py` (and presumably `buckzy_client.py`) will use the `python-dotenv` library to load these variables automatically.

## Usage

The core API interaction logic resides in a Python class (e.g., `BuckzyAPIClient` in `buckzy_client.py`). An example script, `buckzy_assessment.py`, demonstrates how to use this client to perform all required assessment tasks.

### Running the Examples

1.  **Ensure you have the `buckzy_client.py` file:** This file should contain the `BuckzyAPIClient` class with methods for each endpoint.
2.  **Ensure you have the `buckzy_assessment.py` file:** This script orchestrates the calls to `BuckzyAPIClient` methods.
3.  **Execute the assessment script:**
    ```bash
    python buckzy_assessment.py
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

## Error Handling

The `BuckzyAPIClient` methods are designed to raise exceptions for API errors (e.g., HTTP status codes 4xx or 5xx). It's crucial to implement `try-except` blocks in your application code (as demonstrated in `buckzy_assessment.py`) to gracefully handle these scenarios, log errors, and provide appropriate feedback.

## Assumptions

* The Buckzy API uses an API key for authentication, passed in the `Authorization` header as a `Bearer` token.
* Request bodies for `POST` and `PUT` methods are typically JSON.
* Response bodies from the API are typically JSON.
* Specific endpoint paths and required payload structures (e.g., fields for customer creation, document formats, payout details) are derived from Buckzy's official API documentation (`https://docs-api.buckzy.net/`). You must consult their latest documentation for exact specifications.
* For document upload, the `fileContent` is assumed to be Base64 encoded.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.
  
  
