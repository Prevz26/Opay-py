CASHIER_ENDPOINTS = {
    'sandbox': "https://sandboxapi.opaycheckout.com/api/v1/international/cashier/create",

    'production': "https://api.opaycheckout.com/api/v1/international/cashier/create"
}

print(CASHIER_ENDPOINTS.get("sandbox"))
