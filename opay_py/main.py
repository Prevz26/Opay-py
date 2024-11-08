from opay.auth import public_key
from helpers import public_key_signature
from opay.opay_cashier.opay_cashier import Opay_Cashier

#print(public_key_signature())
app = Opay_Cashier(environment="production")
print(app)
