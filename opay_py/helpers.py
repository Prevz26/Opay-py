
# secret_key = 'your_secret_key'
# merchant_id = '256612345678901'

# # Payload (data you want to send in the request)
# payload = '{"orderId": "12345", "amount": "1000"}'

# # Generate the signature using HMAC-SHA512
# signature = hmac.new(secret_key.encode(), payload.encode(), hashlib.sha512).hexdigest()

# # Set headers
# headers = {
#     'Authorization': f'Bearer {signature}',
#     'MerchantId': merchant_id,
#     'Content-Type': 'application/json'
# }

# # Send the request
# response = requests.post('https://api.opay.com/cashier/payment-status', headers=headers, data=payload)

# # Print response
# print(response.json())
