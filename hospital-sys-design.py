# Hospital system design project from Mastering 4 critical skills using python on udemy by prof mostafa saad


class Patient():
    def __init__(self,name,status):
        self.name = name 
        self.status = status 

class HospitalManger():
    def __init__(self, specilizations_count):
        self.specializations = [[] for i in range(specilizations_count)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2 

    def add_patient(self, name, specialization, status):
        spec_list = self.specializations[specialization]   
        added_patients = 0 
        patient = Patient(name, status) 
        if len(spec_list) == 0:
            spec_list.append(patient) 
        elif len(spec_list) < self.MAX_QUEUE:
            for i in range(len(spec_list)):
                curr_patient = spec_list[i]
                if patient.status > curr_patient.status:
                    spec_list.insert(i, patient)
                    added_patients += 1 
                    break
            if added_patients == 0:
                spec_list.append(patient)    

    
class FrontendManager():
    def __init__(self, specilization_count = 20):
        self.specialization_count = specilization_count 
        self.hospital_manager = HospitalManger(self.specialization_count)
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

    def run_programme(self):
        choice = self.print_menu()
        if choice == 1:
            spec = input("enter specilization: ")
            name = input("enter name")
            status = input("enter status ")
            self.hospital_manager.add_patient(name,spec, status)
             
        elif choice == 2:
            pass 
        elif choice == 3:
            pass 
        elif choice == 4: 
            pass 
        elif choice == 5:
            pass 


