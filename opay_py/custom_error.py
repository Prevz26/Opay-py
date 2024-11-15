class Environment_Variable_Exception(Exception):
    def __init__ (self, variable_name):
        self.variable_name = variable_name
        super().__init__(f"Environment_Variable_Error: Variable missing {self.variable_name}")

class Environment_Exception(Exception):
    def __init__(self, environment) -> None:
        self.environment = environment
        super().__init__(f"Wrong Enviroment given: {self.environment}. Environment must either be production or development")



class Opay_Exception(Exception):
    def __init__(self, error_code):
        self.error_code = error_code

    def error(self):
        if self.error_code == "02000":
            return super().__init__("Authentication Error, check your headers")

        elif self.error_code == "02001":
            return super().__init__("Invalid Request Parameters")

        elif self.error_code == "02003":
            return super().__init__("Pay Method is not supported")
        
        elif self.error_code == "02004":
            return super().__init__("the payment reference(merchant order number) already")

        elif self.error_code == "02002":
            return super().__init__("merchant not configured with this function.")

        elif self.error_code == "02007":
            return super().__init__("Merchant not available")

        elif self.error_code == "50003":
            return super().__init__("service not available, please try again")





        


