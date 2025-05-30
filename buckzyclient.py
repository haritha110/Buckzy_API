import requests
import json
import base64
import os

class BuckzyAPIClient:
    """
    A Python client for interacting with the Buckzy API.

    *** IMPORTANT: ***
    This implementation assumes common REST API patterns for endpoints,
    request/response bodies, and API key authentication via an 'X-API-Key' header.
    YOU MUST CONSULT THE OFFICIAL BUCKZY API DOCUMENTATION (https://docs-api.buckzy.net/)
    TO VERIFY AND ADJUST THE FOLLOWING:
    - Base URL (e.g., whether it includes /v1 or not)
    - Exact Authentication Method (e.g., API Key, Bearer Token via OAuth2)
    - Precise Endpoint Paths (e.g., /customers/individual vs. /api/v1/customers/individual)
    - Required fields and their data types in ALL request bodies (JSON payloads)
    - Exact keys to extract IDs (customerId, accountId, transactionId, documentId) from responses
    - Specifics of file uploads (multipart/form-data vs. base64 encoding in JSON)
    """

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-Key": self.api_key  # Common API Key authentication header
        }
        self.timeout = 30 # seconds for API requests

    def _make_request(self, method, endpoint, data=None, params=None):
        """Helper method to make HTTP requests."""
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            elif method == "POST":
                response = requests.post(url, headers=self.headers, data=json.dumps(data), timeout=self.timeout)
            elif method == "PUT":
                response = requests.put(url, headers=self.headers, data=json.dumps(data), timeout=self.timeout)
            elif method == "DELETE":
                response = requests.delete(url, headers=self.headers, params=params, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status() # Raises HTTPError for 4xx/5xx responses
            
            try:
                return response.json()
            except json.JSONDecodeError:
                # Handle cases where API returns 200 OK but no JSON (e.g., 204 No Content)
                print(f"INFO: No JSON response from {url}. Status: {response.status_code}")
                return {"message": "Success, but no JSON content.", "status_code": response.status_code, "raw_response": response.text}

        except requests.exceptions.HTTPError as e:
            print(f"ERROR HTTP {e.response.status_code} for {url}: {e}")
            return {"error": str(e), "status_code": e.response.status_code, "details": e.response.json() if e.response.text else None}
        except requests.exceptions.ConnectionError as e:
            print(f"ERROR Connection to {url}: {e}")
            return {"error": f"Network connection error: {e}"}
        except requests.exceptions.Timeout as e:
            print(f"ERROR Timeout for {url}: {e}")
            return {"error": f"Request timed out after {self.timeout}s: {e}"}
        except requests.exceptions.RequestException as e:
            print(f"ERROR Unexpected request error for {url}: {e}")
            return {"error": f"An unexpected requests error occurred: {e}"}
        except Exception as e:
            print(f"ERROR An unhandled exception occurred: {e}")
            return {"error": f"An unhandled error occurred: {e}"}

    # 1. Entity Documents Management (Assumes base64 encoded file in JSON payload)
    def upload_entity_document(self, entity_id, document_data_base64, document_type, filename):
        endpoint = f"documents/entity/{entity_id}" # Placeholder path
        payload = {"documentType": document_type, "filename": filename, "fileContentBase64": document_data_base64}
        return self._make_request("POST", endpoint, data=payload)

    def get_entity_document(self, entity_id, document_id):
        endpoint = f"documents/entity/{entity_id}/{document_id}" # Placeholder path
        return self._make_request("GET", endpoint)

    def list_entity_documents(self, entity_id):
        endpoint = f"documents/entity/{entity_id}" # Placeholder path
        return self._make_request("GET", endpoint)

    # 2. Customer Management (Individual, Corporate)
    def create_individual_customer(self, customer_data):
        endpoint = "customers/individual" # Placeholder path
        return self._make_request("POST", endpoint, data=customer_data)

    def create_corporate_customer(self, customer_data):
        endpoint = "customers/corporate" # Placeholder path
        return self._make_request("POST", endpoint, data=customer_data)

    def get_customer(self, customer_id):
        endpoint = f"customers/{customer_id}" # Placeholder path
        return self._make_request("GET", endpoint)

    def update_customer(self, customer_id, update_data):
        endpoint = f"customers/{customer_id}" # Placeholder path
        return self._make_request("PUT", endpoint, data=update_data)

    # 3. SPOT Rates
    def get_spot_rates(self, from_currency, to_currency):
        endpoint = "rates/spot" # Placeholder path
        params = {"fromCurrency": from_currency, "toCurrency": to_currency}
        return self._make_request("GET", endpoint, params=params)

    # 4. Buckzy Account Management
    def create_buckzy_account(self, account_data):
        endpoint = "accounts" # Placeholder path
        return self._make_request("POST", endpoint, data=account_data)

    def get_buckzy_account_details(self, account_id):
        endpoint = f"accounts/{account_id}" # Placeholder path
        return self._make_request("GET", endpoint)

    def get_buckzy_account_balance(self, account_id):
        endpoint = f"accounts/{account_id}/balance" # Placeholder path
        return self._make_request("GET", endpoint)

    # 5. Payout Transaction Endpoint
    def initiate_payout_transaction(self, transaction_data):
        endpoint = "payouts" # Placeholder path
        return self._make_request("POST", endpoint, data=transaction_data)

    def get_payout_transaction_status(self, transaction_id):
        endpoint = f"payouts/{transaction_id}/status" # Placeholder path
        return self._make_request("GET", endpoint)

# --- Example Usage ---
if __name__ == "__main__":
    # --- Configuration (UPDATE THESE) ---
    BUCKZY_BASE_URL = "https://api.buckzy.net/v1"  # *** VERIFY THIS from Buckzy API Docs ***
    BUCKZY_API_KEY = "YOUR_BUCKZY_API_KEY"        # *** REPLACE WITH YOUR ACTUAL API KEY ***

    if BUCKZY_API_KEY == "YOUR_BUCKZY_API_KEY":
        print("WARNING: Please update BUCKZY_API_KEY and BUCKZY_BASE_URL with your actual credentials.")
        print("Exiting example usage.")
        exit()

    client = BuckzyAPIClient(BUCKZY_BASE_URL, BUCKZY_API_KEY)

    print("--- Buckzy API Client Demo ---")

    # To chain operations, we need to store IDs from successful creations
    customer_id = None
    buckzy_account_id = None
    document_id = None
    payout_transaction_id = None

    # 1. Customer Management (Individual) - First as it provides a customer_id
    print("\n--- Testing Customer Management ---")
    customer_data = {
        "firstName": "Test", "lastName": "User", "email": "test.user@example.com",
        "phone": "+1234567890", "address": {"street": "123 Main St", "city": "Anytown", "country": "USA"}
        # *** ADD ALL REQUIRED FIELDS PER BUCKZY DOCS ***
    }
    create_resp = client.create_individual_customer(customer_data)
    print(f"Create Customer: {json.dumps(create_resp, indent=2)}")
    if not create_resp.get("error"):
        customer_id = create_resp.get("id") or create_resp.get("customerId") # Common keys for ID
        print(f"Obtained Customer ID: {customer_id}")
        if customer_id:
            get_resp = client.get_customer(customer_id)
            print(f"Get Customer ({customer_id}): {json.dumps(get_resp, indent=2)}")
            update_data = {"phone": "+1987654321"} # Example update
            update_resp = client.update_customer(customer_id, update_data)
            print(f"Update Customer ({customer_id}): {json.dumps(update_resp, indent=2)}")
    else:
        print("Skipping further customer operations due to creation failure.")

    # 2. Buckzy Account Management (requires customer_id)
    print("\n--- Testing Buckzy Account Management ---")
    if customer_id:
        account_data = {
            "customerId": customer_id, "currency": "USD", "accountType": "PRIMARY"
            # *** ADD ALL REQUIRED FIELDS PER BUCKZY DOCS ***
        }
        create_acc_resp = client.create_buckzy_account(account_data)
        print(f"Create Account: {json.dumps(create_acc_resp, indent=2)}")
        if not create_acc_resp.get("error"):
            buckzy_account_id = create_acc_resp.get("id") or create_acc_resp.get("accountId")
            print(f"Obtained Buckzy Account ID: {buckzy_account_id}")
            if buckzy_account_id:
                get_acc_details_resp = client.get_buckzy_account_details(buckzy_account_id)
                print(f"Get Account Details ({buckzy_account_id}): {json.dumps(get_acc_details_resp, indent=2)}")
                get_acc_balance_resp = client.get_buckzy_account_balance(buckzy_account_id)
                print(f"Get Account Balance ({buckzy_account_id}): {json.dumps(get_acc_balance_resp, indent=2)}")
        else:
            print("Skipping further account operations due to creation failure.")
    else:
        print("Skipping Buckzy Account Management: No customer ID available.")

    # 3. SPOT Rates
    print("\n--- Testing SPOT Rates ---")
    spot_rates_resp = client.get_spot_rates("USD", "EUR")
    print(f"Get SPOT Rates (USD/EUR): {json.dumps(spot_rates_resp, indent=2)}")

    # 4. Payout Transaction (requires customer_id and buckzy_account_id)
    print("\n--- Testing Payout Transaction Endpoint ---")
    if customer_id and buckzy_account_id:
        payout_data = {
            "sourceAccountId": buckzy_account_id, "sourceCurrency": "USD", "sourceAmount": 50.00,
            "destinationCurrency": "EUR", "receiverDetails": {"name": "Jane Recipient", "country": "DE"}
            # *** ADD ALL REQUIRED FIELDS PER BUCKZY DOCS ***
        }
        initiate_payout_resp = client.initiate_payout_transaction(payout_data)
        print(f"Initiate Payout: {json.dumps(initiate_payout_resp, indent=2)}")
        if not initiate_payout_resp.get("error"):
            payout_transaction_id = initiate_payout_resp.get("id") or initiate_payout_resp.get("transactionId")
            print(f"Obtained Payout Transaction ID: {payout_transaction_id}")
            if payout_transaction_id:
                get_payout_status_resp = client.get_payout_transaction_status(payout_transaction_id)
                print(f"Get Payout Status ({payout_transaction_id}): {json.dumps(get_payout_status_resp, indent=2)}")
        else:
            print("Skipping further payout operations due to initiation failure.")
    else:
        print("Skipping Payout Transaction: Missing customer ID or Buckzy account ID.")

    # 5. Entity Documents Management (requires entity_id, which can be customer_id)
    print("\n--- Testing Entity Documents Management ---")
    if customer_id:
        # Simulate a base64 encoded document
        dummy_doc_content = "This is a sample document for Buckzy API."
        encoded_doc = base64.b64encode(dummy_doc_content.encode('utf-8')).decode('utf-8')
        
        upload_doc_resp = client.upload_entity_document(
            customer_id, encoded_doc, "PROOF_OF_IDENTITY", "my_id.pdf"
        )
        print(f"Upload Document: {json.dumps(upload_doc_resp, indent=2)}")
        if not upload_doc_resp.get("error"):
            document_id = upload_doc_resp.get("id") or upload_doc_resp.get("documentId")
            print(f"Obtained Document ID: {document_id}")
            if document_id:
                get_doc_resp = client.get_entity_document(customer_id, document_id)
                print(f"Get Document ({document_id}): {json.dumps(get_doc_resp, indent=2)}")
                list_docs_resp = client.list_entity_documents(customer_id)
                print(f"List Documents for Customer ({customer_id}): {json.dumps(list_docs_resp, indent=2)}")
        else:
            print("Skipping further document operations due to upload failure.")
    else:
        print("Skipping Entity Documents Management: No customer ID available.")

    print("\n--- Demo Complete ---")
    
