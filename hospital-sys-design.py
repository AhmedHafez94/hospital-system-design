# Hospital system design project from Mastering 4 critical skills using python 

class Patient():
    def __init__(self,name,status,specilization):
        self.name = name 
        self.status = status 
        self.specializatation = specializatation 
        

class Specialization():
    queue = [] # list of patients in the speciliazation 
    def __init__(self, specialtion_name):
        self.specialization_name = specialtion_name