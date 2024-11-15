from .models import *
import json
import helpers
import requests
import constants
from typing import Optional, Any, Dict



class Opay_Cashier:
    def __init__(self, environment: str = "sandbox", headers: Optional[Dict[str, Any]] = None) -> None:
        self.environment = environment
        self.headers = headers if headers else {}
        
        # Accessing CASHIER_ENDPOINTS dictionary
        self.base_url = constants.CASHIER_ENDPOINTS.get(self.environment)
        
        if not self.base_url:
            raise ValueError("Invalid Environment: Environment should be 'sandbox' or 'production'")

    def auth(self, **kwargs) -> dict:
        """Generate authentication headers if not provided, requiring 'public_key' and 'merchant_id'."""
        
        # Check if headers are already set, otherwise validate **kwargs
        if not self.headers:
            # Ensure both 'public_key' and 'merchant_id' are provided in kwargs
            if 'public_key' in kwargs and 'merchant_id' in kwargs:
                self.headers = {
                    "Authorization": kwargs['public_key'],
                    "Merchant-Id": kwargs['merchant_id']
                }
            else:
                # Generate headers using public_key_signature if no kwargs are given
                self.headers = helpers.public_key_signature()
                
                # Verify that the generated headers contain the required fields
                if 'Authorization' not in self.headers or 'Merchant-Id' not in self.headers:
                    raise ValueError("Authentication failed: Required 'public_key' and 'merchant_id' are missing.")
        return self.headers

    def __repr__(self) -> str:
        return (f"Opay_Cashier(environment: {self.environment}, headers: {self.headers}, "
                f"base_url: {self.base_url})")

    def request(self, payload: dict) -> dict:
        # Validate and prepare the payload
        self.payload: Params = Params(**payload)  
        self.data = self.payload.model_dump()
        
        # Authenticate and set headers
        self.headers = self.auth()  # This ensures headers are set or generated correctly

        # Send the HTTP POST request
        try:
            self.response: requests.Response = requests.post(
                url=self.base_url, headers=self.headers, json=self.data
            )
            self.response.raise_for_status()  # Raise error for bad HTTP responses
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {"error": str(e), "status_code": self.response.status_code if self.response else None}
        
        # Return the response in JSON format
        return self.response.json()
