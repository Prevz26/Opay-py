from .models import *
import json
import helpers
import requests
import constants
from typing import Optional

class Opay_Cashier():
    def __init__(self, environment="sandbox", headers: Optional[dict]=None):
        self.environment = environment
        self.headers = headers
        if self.headers is None:
            self.headers = helpers.public_key_signature()
        if not self.headers:
            raise ValueError("Missing API kry: set your keys in your environment variable or pass it as an args")

        self.base_url = constants.CASHIER_ENDPOINTS.get(self.environment)
        if not self.base_url:
            raise ValueError("Missing Environment: Environment args should be set to sandbox or production")
    def __repr__(self) -> str:
        return f"this class is instanisted correctly: headers:{self.headers}, environment: {self.environment}, base_url: {self.base_url}"
    
    def request(self, payload: dict) -> dict:
        self.payload: Params = Params(**payload) 
        self.data = self.payload.model_dump()


        self.response: requests.Response = requests.post(
                url=self.base_url, headers=self.headers, json=self.data
    )
        print(self.response.status_code)
        return self.response.json()
