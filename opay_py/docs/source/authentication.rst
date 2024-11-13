Authentication
==============

This section describes the authentication process required to use the API.

Overview
--------

The API uses token-based authentication. Each request must include a valid token in the headers.

Obtaining a Token
-----------------

1. Register for an API key through our developer portal.
2. Use the API key to obtain an access token.

Example
-------

To retrieve an access token, make a POST request to:

.. code-block:: http

   POST /api/auth/token
   Host: api.example.com
   Content-Type: application/json

   {
       "apiKey": "your_api_key"
   }

Best Practices
--------------

- **Keep tokens secure**: Avoid exposing tokens in public code repositories.
- **Renew tokens periodically**: Tokens are valid for 24 hours.
