# PyOpay Documentation
PyOpay is a Python client library designed to facilitate interaction with the Opay API. It offers methods and attributes that enhance the developer experience when working with the Opay API. This documentation covers installation, and provides guides on using and interacting with the Opay API through this library.

# Getting Started
### 1. Installation

- **Create an Opay account**: Go to [Opay official docs](https://documentation.opaycheckout.com/), follow instructions and obtain your public and private keys, merchant ID from your account settings, which is necessary for using this package.
- **Store your Opay secret key securely**: Store your Opay secret key in your environment variable as `PUBLIC_KEY`, `PRIVATE_KEY`, `MERCHANT_ID`, or provide it to the PyOpay API wrapper during initialization. Ensure that you keep your secret key secure and do not push it to a remote version control system. It is recommended to begin with your test private key.
- **Install the PyOpay package**: Run the following command to install the PyOpay package:

```bash
pip install pyopay
```

### 2. Usage
Opay has two major important features that can be used to interact with the API:
The express checkout feature and the server side feature. Both of them can be used to interact with the API.

### 3. express 
```python
from pyopay import PyOpay
