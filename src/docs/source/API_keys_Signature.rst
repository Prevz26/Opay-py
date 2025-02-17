OPay API Key Usage
==================

OPay generates two types of API keys for secure communication with its payment APIs. These keys are used in different contexts to ensure secure and reliable transactions.

.. warning::

   **Do not commit your secret keys to Git, or use them in client-side code!**

   All API requests made without authentication will fail.
   All API requests must be made over a secure connection.


1. **Secret Key**
-----------------

   **Usage**: Used to sign critical payment APIs for secure transaction creation.

   **Headers**:
   
   - `Authorization`: Bearer {signature}
   - `MerchantId`: 256612345678901

   **Applicable API Calls**:

   - `Cashier Payment`
   - `Transaction Payment`

   For these calls, the `Authorization` header includes a **HMAC-SHA512** signature of the payload, signed with your secret key. This signature ensures the integrity of your transaction request payload, verifying that it has not been altered.

2. **Public Key**
-----------------

   **Usage**: Used as an authorization key in other payment-related API requests.

   **Headers**:
   
   - `Authorization`: Bearer {PublicKey}
   - `MerchantId`: 256612345678901

   **Applicable API Calls**:

   - `Cashier Create Payment`

   For these calls, the `Authorization` header should contain your **Public Key** and `MerchantId`.



