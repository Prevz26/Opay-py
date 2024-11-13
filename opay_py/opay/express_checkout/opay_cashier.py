from .models import *
import json
import helpers
import requests
import constants
from typing import Optional, Any


class Opay_Cashier:
    def __init__(self, environment: str = "sandbox", headers: Optional[dict[str, Any]] = None) -> None:
        self.environment = environment
        self.headers = headers if headers else {}
        # print(type(self.environment))
        # print(self.environment)
       
       # Accessing CASHIER_ENDPOINTS dictionary
        self.base_url = constants.CASHIER_ENDPOINTS.get(self.environment)

        if not self.base_url:
            raise ValueError("Missing Environment: Environment should be set to 'sandbox' or 'production'")

    def auth(self, **kwargs):
        if self.headers == {}:
            self.headers = helpers.public_key_signature()
            return self.headers
        if not self.headers:
            self.auth_data = kwargs
            return self.auth_data
        raise ValueError("Missing API kry: set your keys in your environment variable or pass it as an args")

    def __repr__(self) -> str:
        return f"this class is instanisted correctly: headers:{self.headers}, environment: {self.environment}, base_url: {self.base_url}"
    
    def request(self, payload: dict) -> dict:
        self.payload: Params = Params(**payload) 
        self.data = self.payload.model_dump()
        self.headers = self.auth()
        self.response: requests.Response = requests.post(
                url=self.base_url, headers=self.headers, json=self.data
    )
        print(self.response.status_code)
        return self.response.json()
