from custom_error import Environment_Variable_Exception  
from decouple import config
import hashlib
import hmac


def get_env_value( var_name: str) -> str | None:
    """Function to get the value of an environment variable."""
    value = config(var_name)
    if value is None:
        raise Environment_Variable_Exception(f"Environment variable '{var_name}' not found.")
    return value

def public_key(path = None, pub_key=None, merchant_id=None) -> dict[str, str] | None:
    """Function to return public key and merchant ID as a dictionary."""
    if pub_key is None:
        pub_key = get_env_value( "PUBLIC_KEY")
    if merchant_id is None:
        merchant_id = get_env_value("MERCHANT_ID")

    if pub_key and merchant_id:
        data = {"pub_key": pub_key, "merchant_id": merchant_id} 
        return data
    else:
        print("Key not found")

def private_key(prv_key=None, merchant_id=None) -> dict[str, str] | None:
    """Function to return private_key and merchant ID as a dictionary."""
    if prv_key is None:
        prv_key = get_env_value( "PRIVATE_KEY")
    if merchant_id is None:
        merchant_id = get_env_value("MERCHANT_ID")
    
    if prv_key and merchant_id:
        json_data = {"prv_key": prv_key, "merchant_id": merchant_id}
        print("Keys found:", json_data)
        return json_data
    else:
        print("Key not found")
        return None


def private_key_signature(payload, secret_key=None):
    if secret_key is None:
        auth_details = private_key()
        secret_key = auth_details.get("private_key", "key not found")
        merchant_id = auth_details.get("merchant_id", "merchant_id not found")

    signature = hmac.new(secret_key.encode(), payload.encode(), hashlib.sha512).hexdigest()
    headers = {
            'Authorization': f'Bearer {signature}',
        'MerchantId': merchant_id,
        'Content-Type': 'application/json'
        }
    return headers

def public_key_signature( pub_key=None):
    if pub_key is None:
        auth_details = public_key()
       # print(auth_details)
        pub_key = auth_details.get("pub_key", "key not found")
        merchant_id = auth_details.get("merchant_id", "merchant_id not found")

    headers = {
            'Authorization': f'Bearer {pub_key}',
        'MerchantId': merchant_id, 
        }
    return headers


