import json
from opay.auth import public_key
from helpers import public_key_signature
from opay.opay_cashier.opay_cashier import Opay_Cashier
from opay.opay_cashier.models import Params

data = "data.json"
#print(public_key_signature())

with open(data, mode="r") as file:
    loaded_data = json.load(file)

# print(public_key_signature())
app = Opay_Cashier()
print (app.headers)
print (app.request(loaded_data))
# d = Params(**loaded_data)
# da = d.model_dump()
# print(json.dumps(da, indent=4))
##print(app)
