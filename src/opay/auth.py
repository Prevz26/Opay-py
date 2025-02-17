from utils.custom_error import Environment_Variable_Exception
from decouple import config
import hashlib
import hmac

class Auth:
    def __init__(self, pub_key=None, merchant_id=None, prv_key=None):
        self.pub_key = pub_key
        self.merchant_id = merchant_id
        self.prv_key = prv_key

    def get_env_value(self, var_name: str) -> str:
        value = config(var_name)
        if value is None:
            raise Environment_Variable_Exception(f"Environment variable '{var_name}' not found.")
        return value

    def get_public_key(self) -> dict[str, str]:
        if self.pub_key is None:
            self.pub_key = self.get_env_value("PUBLIC_KEY")
        if self.merchant_id is None:
            self.merchant_id = self.get_env_value("MERCHANT_ID")

        if self.pub_key and self.merchant_id:
            return {"pub_key": self.pub_key, "merchant_id": self.merchant_id}
        raise ValueError("Public key or merchant ID not found")

    def get_private_key(self) -> dict[str, str]:
        if self.prv_key is None:
            self.prv_key = self.get_env_value("PRIVATE_KEY")
        if self.merchant_id is None:
            self.merchant_id = self.get_env_value("MERCHANT_ID")

        if self.prv_key and self.merchant_id:
            return {"prv_key": self.prv_key, "merchant_id": self.merchant_id}
        raise ValueError("Private key or merchant ID not found")

    def private_key_signature(self, payload: str) -> dict[str, str]:
        if self.prv_key is None:
            auth_details = self.get_private_key()
            self.prv_key = auth_details["prv_key"]
            self.merchant_id = auth_details["merchant_id"]

        signature = hmac.new(self.prv_key.encode(), payload.encode(), hashlib.sha512).hexdigest()
        return {
            'Authorization': f'Bearer {signature}',
            'MerchantId': self.merchant_id,
            'Content-Type': 'application/json'
        }

    def public_key_signature(self) -> dict[str, str]:
        if self.pub_key is None:
            auth_details = self.get_public_key()
            self.pub_key = auth_details["pub_key"]
            self.merchant_id = auth_details["merchant_id"]

        return {
            'Authorization': f'Bearer {self.pub_key}',
            'MerchantId': self.merchant_id,
        }

