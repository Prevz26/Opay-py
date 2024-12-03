from typing import Optional
import constants

class Environment_Variable_Exception(Exception):
    def __init__ (self, variable_name):
        self.variable_name = variable_name
        super().__init__(f"Environment_Variable_Error: Variable missing {self.variable_name}")

class Environment_Exception(Exception):
    def __init__(self, environment) -> None:
        self.environment = environment
        super().__init__(f"Wrong Enviroment given: {self.environment}. Environment must either be production or development")


class Custom_Response():
    """custom response class"""
    def success_response(self, data:dict, status_code: int = 200, code:str = "00000"):
        '''Returns a success response'''
        final_data = {'status': 'success', 'data': data, "code":code, "status_code":status_code}
        return final_data

    def base_error_response(self, message: str, status_code: int, error_code: str):
        '''Return a custom error response'''

        return ({'status': 'error', 'error': message}, status_code, error_code)

    def failed_auth(self, message= constants.AUTHENTICATION_FAILED):
        return self.base_error_response(message, status_code=401, error_code="02000")

    def Invalid_params(self, message= constants.INVALID_PARAMAS):
        return self.base_error_response(message, status_code=400, error_code="02000")

    def pay_method_error(self, message= constants.PAY_METHOD_ERROR):
        return self.base_error_response(message, status_code=400, error_code="02004")
    
    def already_exist(self, message= constants.ALREADY_EXISTS):
        return self.base_error_response(message, status_code=409, error_code= "02004")

    def merchant_not_config(self, message= constants.ALREADY_EXISTS):
        return self.base_error_response(message, status_code=409, error_code= "02004")

    def merchant_not_found(self, message=constants.MERCHANT_NOT_AVAILABLE):
        return self.base_error_response(message, status_code=400, error_code="02007")

    def service_unavailable(self, message= constants.SERVICE_NOT_AVAILABLE):
        return self.base_error_response(message, status_code=500, error_code= "50003")



       
class Opay_Exception(Custom_Response):
    def __init__(self, error_code):
        self.error_code = error_code
        if self.error_code == "02000":
            return super().failed_auth()

        elif self.error_code == "02001":
            return super().Invalid_params()

        elif self.error_code == "02003":
            return super().pay_method_error()
        
        elif self.error_code == "02004":
            return super().already_exist()
    
        elif self.error_code == "02002":
            return super().merchant_not_config()
        elif self.error_code == "02007":
            return super().merchant_not_found()
        elif self.error_code == "50003":
            return super().service_unavailable()



        


