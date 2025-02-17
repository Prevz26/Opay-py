from .models import * 
from ..auth import public_key_signature
import utils.constants as constants
from utils.custom_error import Opay_ResponseHandler, Custom_Response
from typing import Optional, Any, Dict
import requests
from requests.exceptions import ConnectionError
import time



class Opay_Cashier:
    def __init__(self, environment: str = "sandbox", auth_keys: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize the Opay_Cashier instance with the specified environment and optional authentication keys.

        Args:
            environment (str): The operating environment for the Opay_Cashier instance, either "sandbox" or "production".
            auth_keys (Optional[Dict[str, Any]]): Optional dictionary containing authentication credentials.

        Raises:
            ValueError: If the environment is not "sandbox" or "production".
        """

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

        #To-do: error handling for failed connection
        self.response = requests.post(
    url= self.base_url, json=self.data, headers=self.auth_keys)
        data = self.response.json()
        if data["code"] != "00000":
            error = Error(**data).model_dump()
            error_code = error["code"]
            #print(error)
            opay_handler = Opay_ResponseHandler(error_code=error_code)
            print (opay_handler.response)

        else:
            #print(data)
            res = Response(**data).model_dump()
            success =Custom_Response()
            response = success.success_response(res)
            print(response)
            
       
