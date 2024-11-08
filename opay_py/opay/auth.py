import os
import json
from dotenv import load_dotenv
from pathlib import Path
from custom_error import Environment_Variable_Exception  

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env file
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

def get_env_value(var_name: str) -> str | None:
    """Function to get the value of an environment variable."""
    value = os.getenv(var_name)
    if value is None:
        raise Environment_Variable_Exception(f"Environment variable '{var_name}' not found.")
    return value

def public_key(pub_key=None, merchant_id=None) -> dict[str, str] | None:
    """Function to return public key and merchant ID as a dictionary."""
    if pub_key is None:
        pub_key = get_env_value("PUBLIC_KEY")
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
        prv_key = get_env_value("PRIVATE_KEY")
    if merchant_id is None:
        merchant_id = get_env_value("MERCHANT_ID")
    
    if prv_key and merchant_id:
        json_data = {"prv_key": prv_key, "merchant_id": merchant_id}
        print("Keys found:", json_data)
        return json_data
    else:
        print("Key not found")
        return None
