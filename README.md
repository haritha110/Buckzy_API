# Buckzy API Python Client

This repository contains a Python client implementation for interacting with the Buckzy API, focusing on key endpoints for financial operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Initializing the Client](#initializing-the-client)
  - [Entity Documents Management](#entity-documents-management)
  - [Customer Management (Individual, Corporate)](#customer-management-individual-corporate)
  - [SPOT Rates](#spot-rates)
  - [Buckzy Account Management](#buckzy-account-management)
  - [Payout Transaction Endpoint](#payout-transaction-endpoint)
- [Important Notes & Assumptions](#important-notes--assumptions)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a Python wrapper for selected endpoints of the Buckzy API, simplifying interaction with its services for tasks such as customer management, account operations, document handling, and transaction processing. The client is built using the `requests` library for robust HTTP communication.

## Features

- **Entity Documents Management:** Upload, retrieve, and list documents associated with entities.
- **Customer Management:** Create, retrieve, and update individual and corporate customer profiles.
- **SPOT Rates:** Fetch real-time foreign exchange spot rates.
- **Buckzy Account Management:** Create, retrieve details, and get balances of Buckzy internal accounts.
- **Payout Transaction Endpoint:** Initiate and check the status of money payout transactions.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** (Recommended)
- **`requests` library**: This HTTP library is used for making API calls.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/haritha110/Buckzy_API.git](https://github.com/your-username/buckzy-api-python-client.git)
    cd buckzy-api-python-client
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

## Configuration

The client requires your Buckzy API Key and the correct Base URL.

**Security Warning:** **NEVER hardcode your API key directly in your scripts for production environments.** It's strongly recommended to use environment variables.

1.  **Obtain your Buckzy API Key:** Log in to your Buckzy developer portal or contact Buckzy support to get your API key.
2.  **Determine the Buckzy Base URL:** Refer to the official Buckzy API documentation (`https://docs-api.buckzy.net/`) to confirm the exact base URL for the API endpoints (e.g., `https://api.buckzy.net/v1`).

**Using Environment Variables (Recommended):**

Create a `.env` file in the root of your project:
  
  
