import datetime

class Menu:

    def printMenu():
        print('1. Create new patient')
        print('2. Search patient record')
        print('3. View patient information')
        print('4. Create new doctor')
        print('5. Search doctor record')
        print('6. View list of doctors')
        print('7. Create new bill')
        print('8. Search bill records')
        print('9. View bills')
        print('99. Exit\n')


    def Switch(num):

        option = int(num)

        while option != 99:
            
            if option == 1:
                patient = patientType(input("\nPatient first name: "), input("Patient last name: "), input("Patient Id: "), input("Age: "), input("Date of Birth (DD/MM/YYYY): "), input ("Doctor's first name: " ), input ("Doctor's last name: " ), input ("Doctor's specialize: " ), input("Admit Date (DD/MM/YYYY): "), input("Discharge date (DD/MM/YYYY): "), input("Pharmacy charge: "), input("Doctor fee: "), input("Room charge: "))
                patientType.appendPatient(patient)


                print("\nSuccessfully added new patient")

            elif option == 2:
                
                patientType.searchByPatientName(patient)


            elif option == 3:
                patientType.printPatient(patient)
            
            elif option == 4:
                doctor = doctorType(input("\nDoctor first name: "), input("Doctor last name: "), input("Specialize: "))
                doctorType.appendDoctors(doctor)
                print("\nSuccessfully added new doctor")

            elif option == 5:

                doctorType.searchDoctorByName(doctor)
            
            elif option == 6:
                doctorType.printDoctors(doctor)
                

            elif option == 7: 
                bill = billType(input("\nPatient ID: "), input("Pharmacy charge: "), input("Doctor fee: "), input("Room charge: "))
                billType.appendBills(bill)
                print("\nSuccessfully added new bill")
                
            elif option == 8:

                billType.searchBillByPatientId(bill)


            elif option == 9:
                billType.pritnPatientBills(bill)

            else: 
                print("The input is invalid. Please input a number from 1 to 9 or 99 to exit the menu")
                option = input("\nOption: ")
        
            print("\nWhat do you want to do next?")
            Menu.printMenu()
            
            option = int(input("\nOption: "))
        



class personType:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getName(self):
        name = [self.firstName, self.lastName]
        return name


class doctorType (personType):
    listOfDoctors = []
    
    def __init__(self,firstName, lastName,specialize):
        super().__init__(firstName, lastName)
        self.specialize = specialize
        self.doctorData = [self.firstName, self.lastName, self.specialize]
        
    
    def setDoctor(self,firstName, lastName, specialize):
        super().setName (firstName, lastName)
        self.specialize = specialize
        self.doctorData = [self.firstName, self.lastName, self.specialize]

    def appendDoctors(self):    
       self.listOfDoctors.append(self.doctorData)
        
        
    def getDoctor(self):
        return self.doctorData

    def searchDoctorByName(self):

        doctorFirstName = input("Enter the first name of the doctor: ")
        doctorLastName = input("Enter the last name of the doctor: ")

               
        doctorData = []

        i = 0

        while i < len(self.listOfDoctors):

            doctorInfo = self.listOfDoctors[i]
        
            if doctorInfo[0] == doctorFirstName and doctorInfo[1] == doctorLastName:
                doctorData.append(doctorInfo)
            
            else:
                pass

            i += 1

        print("\n=============== List of found doctor ===============")


        if len(doctorData) > 0:
        
            i = 0

            while i < len(doctorData):

                doctorInfo = doctorData[i]

                name = str(doctorInfo[0]) +' ' + str(doctorInfo[1])

                doctorSpecialize = str(doctorInfo[2])

                print('\nDoctors name: ', name)
                print('Specialize:  ', doctorSpecialize)
                print('\n')

                i = i + 1
            print("===================================================")

        else: 
            print("Doctor is not found\n")


    def printDoctors(self):

        print("\n================== List of doctors =================")
        
        i = 0

        while i < len(self.listOfDoctors):

            doctorInfo = self.listOfDoctors[i]

            name = str(doctorInfo[0]) +' ' + str(doctorInfo[1])

            doctorSpecialize = str(doctorInfo[2])

            print('\nDoctors name: ', name)
            print('Specialize:  ', doctorSpecialize)
            print('\n')

            i = i + 1
        
        print("===================================================")


class Date:
    
    def __init__(self, dateOfBirth,admitDate,dischargeDate):
        self.dateOfBirth = dateOfBirth
        self.admitDate = admitDate
        self.dischargeDate = dischargeDate

        day, month, year = map(int, dateOfBirth.split('/'))
        self.dateOfBirth = datetime.date(year, month, day)

        day, month, year = map(int, admitDate.split('/'))
        self.admitDate = datetime.date(year, month, day)

        day, month, year = map(int, dischargeDate.split('/'))
        self.dischargeDate = datetime.date(year, month, day)

        self.listOfDate = [self.dateOfBirth, self.admitDate, self.dischargeDate]
         
         
    
    def setDate(self,dateOfBirth,admitDate,dischargeDate):
        
        self.dateOfBirth = dateOfBirth
        self.admitDate = admitDate
        self.dischargeDate = dischargeDate

        day, month, year = map(int, dateOfBirth.split('/'))
        self.dateOfBirth = datetime.date(year, month, day)

        day, month, year = map(int, admitDate.split('/'))
        self.admitDate = datetime.date(year, month, day)

        day, month, year = map(int, dischargeDate.split('/'))
        self.dischargeDate = datetime.date(year, month, day)

        self.listOfDate = [self.dateOfBirth, self.admitDate, self.dischargeDate]
         
         

    def getDate(self):
        return self.listOfDate


class patientType(personType):
    listOfPatients = []
    
    def __init__(self, patientFirstName, patientLastName, patientId, age, dateOfBirth, doctorFirstName, doctorLastName, specialize, admitDate, dischargeDate, pharmacyCharge, doctorFee, roomCharge):
        personType.__init__(self, patientFirstName, patientLastName)
        self.patientId = patientId
        self.age = age
        self.dateData = Date(dateOfBirth,admitDate,dischargeDate)
        self.doctorData = doctorType(doctorFirstName,doctorLastName,specialize)
        self.billData = billType(patientId, pharmacyCharge, doctorFee, roomCharge)
        self.patientData = [patientFirstName, patientLastName, self.patientId, self.age, list(self.dateData.getDate()) , list(self.doctorData.getDoctor()), list(self.billData.getBills())]
       
    
    def setPatient(self, patientFirstName, patientLastName, patientId, age, dateOfBirth, doctorFirstName, doctorLastName, specialize, admitDate, dischargeDate, pharmacyCharge, doctorFee, roomCharge):
        personType.setName(self,patientFirstName, patientLastName)
        self.patientId = patientId
        self.age = age
        self.dateData = Date.setDate(self,dateOfBirth,admitDate,dischargeDate)
        self.doctorData = doctorType.setDoctor(self,doctorFirstName,doctorLastName,specialize)
        
        self.patientData = [patientFirstName, patientLastName, self.patientId, self.age, list(Date.getDate()) , list(doctorType.getDoctor()),  list(self.billData.getBills())]


    def appendPatient(self):
        self.listOfPatients.append(self.patientData)

    def getPatient(self):
        return self.patientData

    def searchByPatientName(self):

        patientFirstName = input("Enter the first name of the patient: ")
        patientLastName = input("Enput the last name of the patient: ")

               
        patientData = []

        i = 0

        while i < len(self.listOfPatients):

            patientInfo = self.listOfPatients[i]
        
            if patientInfo[0] == patientFirstName and patientInfo[1] == patientLastName:
                patientData.append(patientInfo)
            
            else:
                pass

            i += 1
        
        print("\n=============== List of found patient ===============")

        if len(patientData) > 0:

            i = 0
            
            while i < len(patientData):
                patientInfo = patientData[i]

                name = str(patientInfo[0]) +' ' + str(patientInfo[1])

                patientId = int(patientInfo[2])

                patientAge = int(patientInfo[3])
                
                patientDateOfBirth = patientInfo[4][0]         

                patientAdmitDate = patientInfo[4][1] 

                patientDischargeDate = patientInfo[4][2] 

                patientAtendingDoctor = str(patientInfo[5][0]) + ' ' + str(patientInfo[5][1])

                print('\nPatient name: ', name)
                print('Patient ID:  ', patientId)
                print('Patient age:  ', patientAge)
                print('Date of Birth (YYYY-MM-DD):  ', patientDateOfBirth)
                print('Attending phycisian:  ', patientAtendingDoctor)
                print('Admit date (YYYY-MM-DD):  ', patientAdmitDate)
                print('Discharge date (YYYY-MM-DD):  ', patientDischargeDate)
                print('\n')

                i = i + 1

            print("===================================================")
            

        else:
            print("Patient not found")



    
    def printPatient(self):

        print("\n================== List of patients =================")
        
        i = 0

        while i < len(self.listOfPatients):
            patientInfo = self.listOfPatients[i]

            name = str(patientInfo[0]) +' ' + str(patientInfo[1])

            patientId = str(patientInfo[2])

            patientAge = str(patientInfo[3])
            
            patientDateOfBirth = patientInfo[4][0]         

            patientAdmitDate = patientInfo[4][1] 

            patientDischargeDate = patientInfo[4][2] 

            patientAteendingDoctor = str(patientInfo[5][0]) + ' ' + str(patientInfo[5][1])

            print('\nPatient name: ', name)
            print('Patient ID:  ', patientId)
            print('Patient age:  ', patientAge)
            print('Date of Birth (YYYY-MM-DD):  ', patientDateOfBirth)
            print('Attending phycisian:  ', patientAteendingDoctor)
            print('Admit date (YYYY-MM-DD):  ', patientAdmitDate)
            print('Discharge date (YYYY-MM-DD):  ', patientDischargeDate)
            print('\n')

            i = i + 1

        print("===================================================")

class billType():
    listOfBills = []

    def __init__(self, patientId, pharmacyCharge, doctorFee, roomCharge):

        self.patientId = int(patientId)
        self.pharmacyCharge = float(pharmacyCharge)
        self.doctorFee = float(doctorFee)
        self.roomCharge = float(roomCharge)
        self.totalFee = float(self.pharmacyCharge) + float(self.doctorFee) + float(self.roomCharge)
        self.bills = [self.patientId, self.pharmacyCharge, self.doctorFee, self.roomCharge, self.totalFee]

    def setBills(self, patientId, pharmacyCharge, doctorFee, roomCharge):
        self.patientId = int(patientId)
        self.pharmacyCharge = float(pharmacyCharge)
        self.doctorFee = float(doctorFee)
        self.roomCharge = float(roomCharge)
        self.totalFee = float(self.pharmacyCharge) + float(self.doctorFee) + float(self.roomCharge)
        self.bills = [self.patientId, self.pharmacyCharge, self.doctorFee, self.roomCharge, self.totalFee]

    def appendBills (self):
        self.listOfBills.append(self.bills)

    def getBills (self):
        return self.bills
    
    def searchBillByPatientId(self):

        patientId = input("\nPlease input the patient ID: ")

               
        billData = []

        i = 0

        while i < len(self.listOfBills):

            bill = self.listOfBills[i]
        
            if bill[0] == patientId:
                billData.append(bill)
            
            else:
                pass

            i += 1

        print("\n================ List of found bills ================")
        
        if len(billData) > 0:
            i = 0

            while i < len(billData):

                billInfo = billData[i]

                patientId = str(billInfo[0])

                pharmacyCharge = float(billInfo[1])

                doctorFee= float(billInfo[2])

                roomCharge = float(billInfo[3])

                totalBill = float(billInfo[4])

                print('Patient ID:  ', patientId)
                print('Pharmacy charge: ${:.2f} '.format(pharmacyCharge))
                print('Doctor Fee: ${:.2f} '.format(doctorFee))
                print('Room charge: ${:.2f} '.format(roomCharge))
                print('Total bill: ${:.2f} '.format (totalBill))
                print('\n')

                i = i + 1

            print("===================================================")

        else:
            print("Bills are not found")


    def pritnPatientBills(self):

        print("\n================ List of bills ================")
        
        i = 0

        while i < len(self.listOfBills):

            billInfo = self.listOfBills[i]

            patientId = str(billInfo[0])

            pharmacyCharge = float(billInfo[1])

            doctorFee = float(billInfo[2])

            roomCharge = float(billInfo[3])

            totalBill = float(billInfo[4])

            print('Patient ID:  ', patientId)
            print('Pharmacy charge: ${:.2f} '.format(pharmacyCharge))
            print('Doctor Fee: ${:.2f} '.format(doctorFee))
            print('Room charge: ${:.2f} '.format(roomCharge))
            print('Total bill: ${:.2f} '.format (totalBill))
            print('\n')

            i = i + 1

            print("===================================================")

def main():
  print("Welcome to the Hospital management system. What do you wish to do today?\n")
  Menu.printMenu()

  Menu.Switch(input("Option: "))

  print("Thank you for using the hospital management system")

  

if __name__ == "__main__": 
  main()
