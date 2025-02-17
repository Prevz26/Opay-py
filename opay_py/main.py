import json
#from opay.auth import public_key
#from helpers import public_key_signature
from opay.express_checkout.opay_cashier import Opay_Cashier
from opay.express_checkout.models import Params
from pathlib import Path

# Get the path to the .env file located 3 directories up from the current file
path = Path(__file__).resolve().parent.parent / '.env'

print(path)

data = "data.json"
#print(public_key_signature())

with open(data, mode="r") as file:
    loaded_data = json.load(file)

# headers = {'pub_key': 'OPAYPUB17307038061480.45658992285396927', 'merchant_id': '281824110469808'}


# app = Opay_Cashier()
# app.auth()
# (app.request(loaded_data))



#d = Params(**loaded_data)
# da = d.model_dump()
# print(json.dumps(da, indent=4))
##print(app)
