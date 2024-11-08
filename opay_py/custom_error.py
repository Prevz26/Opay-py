class Environment_Variable_Exception(Exception):
    def __init__ (self, variable_name):
        self.variable_name = variable_name
        super().__init__(f"Environment_Variable_Error: Variable missing {self.variable_name}")

class Environment_Exception(Exception):
    def __init__(self, environment) -> None:
        self.environment = environment
        super().__init__(f"Wrong Enviroment given: {self.environment}. Environment must either be production or development")
