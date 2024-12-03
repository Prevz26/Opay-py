from .models import *
import json

from ..auth import private_key_signature, public_key_signature
import constants
from typing import Optional, Any, Dict
import requests


class Opay_Cashier:
    def __init__(self, environment: str = "sandbox", auth_keys: Optional[Dict[str, Any]] = None) -> None:
        self.environment = environment
        self.auth_keys = auth_keys if auth_keys else {}
        
        # Accessing CASHIER_ENDPOINTS dictionary
        self.base_url = constants.CASHIER_ENDPOINTS.get(self.environment)
        
        if not self.base_url:
            raise ValueError("Invalid Environment: Environment should be 'sandbox' or 'production'")

    def auth(self, **kwargs) -> dict:
        """Generate authentication headers if not provided, requiring 'public_key' and 'merchant_id'."""
        
        # Check if auth_keys are already set, otherwise validate **kwargs
        if not self.auth_keys:
            # Ensure both 'public_key' and 'merchant_id' are provided in kwargs
            if 'public_key' in kwargs and 'merchantId' in kwargs:
                self.auth_keys = {
                    "Authorization": kwargs['public_key'],
                    "MerchantId": kwargs['merchantId']
                }
            else:
                # Generate keys using public_key_signature if no kwargs are given
                self.auth_keys = public_key_signature()
                
                # Verify that the generated headers contain the required fields
                if 'Authorization' not in self.auth_keys or 'MerchantId' not in self.auth_keys:
                    raise ValueError("Authentication failed: Required 'public_key' and 'merchant_id' are missing.")
        return self.auth_keys

    def __repr__(self) -> str:
        return (f"Opay_Cashier(environment: {self.environment}, auth_keys: {self.auth_keys}, "
                f"base_url: {self.base_url})")

    def request(self, payload: dict) -> dict:
        # Validate and prepare the payload
        self.payload: Params = Params(**payload)  
        self.data = self.payload.model_dump()
        
        # Authenticate and set headers
        self.auth_keys = self.auth()  # This ensures headers are set or generated correctly
        self.response = requests.post(
    url= self.base_url, json=self.data, headers=self.auth_keys)
        data = self.response.json()
        return Response(**data)
