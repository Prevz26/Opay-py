import json
#from opay.auth import public_key_signature
from opay.express_checkout.opay_cashier import Opay_Cashier
from opay.express_checkout.models import Params
from pathlib import Path

# Get the path to the .env file located 3 directories up from the current file
path = Path(__file__).resolve().parent.parent / '.env'

print(path)

data = "data.json"
with open(data, mode="r") as file:
    loaded_data = json.load(file)


<<<<<<< HEAD
# app = Opay_Cashier()
# app.auth()
# (app.request(loaded_data))



=======
#auth_key= {'Authorization': 'Bearer OPAYPUB17307038061480.45658992285396927', 'MerchantId': '281824110469808'}
app = Opay_Cashier()
# print (app.auth())
print(app.request(payload=loaded_data))
>>>>>>> bfc9cb397bc0b399494c3b0152c715d2d0b01351
#d = Params(**loaded_data)
# da = d.model_dump()
# print(json.dumps(da, indent=4))
##print(app)
