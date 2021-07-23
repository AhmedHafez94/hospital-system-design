# Hospital system design project from Mastering 4 critical skills using python on udemy by prof mostafa saad

from _typeshed import Self


class Patient():
    def __init__(self,name,status,specilization):
        self.name = name 
        self.status = status 
        self.specializatation = specilization 
        

class Specialization():
    queue = [] # list of patients in the speciliazation 
    def __init__(self, specialization_count):
        self.specialization_name = specialization_count


class Hospital_System():

    func add_new_patient():
        patient_name = input("enter patient name: ")
        specialization = input("enter specialiazation: ")
        status = input("enter patient statusL: ")
        patient = Patient(patient_name, status, specialization) 

class FrontendManager():
    def __init__(self, specilization_count):
        self.specialization_count = specilization_count 
        specialization = Specialization(self.specialization_count) 

    # printing menu and returning a option
    def print_menu():
        print("program options")
        options = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        options = [f'{idx + 1}: {option}' for idx, option in enumerate(options)] 
        print("/n".join(options)) 
        user_choice = input("enter your option") 

        return user_choice 

    def run_programme():
        choice = Self.print_menu() 
        if choice == 1:
            pass 
        elif choice == 2:
            pass 
        elif choice == 3:
            pass 
        elif choice == 4: 
            pass 
        elif choice == 5:
            pass 
         

