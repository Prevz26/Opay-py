import json
#from opay.auth import public_key_signature
from opay.express_checkout.opay_cashier import Opay_Cashier
from opay.express_checkout.models import Params

data = "data.json"
with open(data, mode="r") as file:
    loaded_data = json.load(file)


#auth_key= {'Authorization': 'Bearer OPAYPUB17307038061480.45658992285396927', 'MerchantId': '281824110469808'}
app = Opay_Cashier()
# print (app.auth())
print(app.request(payload=loaded_data))
#d = Params(**loaded_data)
# da = d.model_dump()
# print(json.dumps(da, indent=4))
##print(app)
