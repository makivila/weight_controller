from utils import is_numeric, is_positive_number


class Service():
    def __init__(self, repository):
        self.repository = repository

    def add_weight(self, id_user, message):
        if not is_numeric(message): 
            raise Exception("Invalid value entered")
        if not is_positive_number(message):
            raise Exception("Weight must be more than zero")
        self.repository.add_weight(message, id_user)

    def compare(self, id_user, period):
        return self.repository.compare(id_user, period)
    
            
        
        
 