# Hospital system design project from Mastering 4 critical skills using python on udemy by prof mostafa saad


class Patient:
    def __init__(self,name,status):
        self.name = name 
        self.status = status 
    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'
    def __repr__(self):
        return f'Patient(name="{self.name}", status={self.status})'


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


    def print_all_patients(self):
        patients = []
        for idx, specialization in enumerate(self.specializations):
            if not specialization:
                continue
            print(f"specialization {idx + 1}")
            for patient in specialization:
                print("repr will be printed")
                print(repr(patient))
                print("str will be printed")
                print(str(patient))
                print(patient.name)
                patients.append(str(patient))

    def get_next_patient(self, specialization):
        specializaion_arr = self.specializations[specialization]
        if len(specializaion_arr) == 0:
            print("no patients in the queue")
        else :
            next_patient = specializaion_arr[0]
            print(f"next patient name {next_patient.name}")
            self.specializations[specialization].pop(0)  

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization] 
        for idx, patient in enumerate(spec):
            if patient.name == name :
                del spec[idx] 
                return True 
        #no patient with this name      
        return False

    
class FrontendManager():
    def __init__(self, specilization_count = 20):
        self.specialization_count = specilization_count 
        self.hospital_manager = HospitalManger(self.specialization_count)
    # printing menu and returning a option
    def print_menu(self):
        print("program options")
        options = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        options = [f'{idx + 1}: {option}' for idx, option in enumerate(options)] 
        print("\n".join(options)) 
        user_choice = input("enter your option: ") 

        return int(user_choice )

    def run_programme(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                spec = int(input("enter specilization: "))
                name = input("enter name: ")
                status = int(input("enter status "))
                self.hospital_manager.add_patient(name,spec, status)
                
            elif choice == 2:
                self.hospital_manager.print_all_patients()
            elif choice == 3:
                spec = int(input("enter specialzation: "))
                self.hospital_manager.get_next_patient(specialization= spec)
            elif choice == 4: 
                spec = int(input("enter specialzation: "))
                name = input("enter leaving patient name")
                self.hospital_manager.remove_patient(
                    specialization=spec,name=name
                )
            elif choice == 5:
                pass 


app = FrontendManager()
app.run_programme()