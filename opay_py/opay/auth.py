import os
import json
from dotenv import load_dotenv
from pathlib import Path
from custom_error import Environment_Variable_Exception  



def load_and_get_env(var_name: str, path=None) -> str:
    """
7    Loads the .env file from the given path (if not already loaded) and
    returns the value of the specified environment variable.
    If path is None, it loads from the default location.
    """
    # Check if the environment file has already been loaded
    if "DOTENV_LOADED" not in os.environ:
        if path:
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Env file not found at: {path}")
            load_dotenv(dotenv_path=path)
        else:
            load_dotenv()  # Load from default .env file in current directory
        
        # Mark that the .env file has been loaded
        os.environ["DOTENV_LOADED"] = "1"
    
    # Retrieve the environment variable
    value = os.getenv(var_name)
    if value is None:
        raise Environment_Variable_Exception(f"Environment variable '{var_name}' not found.")
    
    return value

def public_key(path=None) -> dict[str, str] | None:
    """Function to return public key and merchant ID as a dictionary."""
    try:
        pub_key = load_and_get_env("PUBLIC_KEY", path)
        merchant_id = load_and_get_env("MERCHANT_ID", path)
        return {"pub_key": pub_key, "merchant_id": merchant_id}
    except Environment_Variable_Exception:
        print("Key not found")
        return None

def private_key(path=None) -> dict[str, str] | None:
    """Function to return private key and merchant ID as a dictionary."""
    try:
        prv_key = load_and_get_env("PRIVATE_KEY", path)
        merchant_id = load_and_get_env("MERCHANT_ID", path)
        return {"prv_key": prv_key, "merchant_id": merchant_id}
    except Environment_Variable_Exception:
        print("Key not found")
        return None
