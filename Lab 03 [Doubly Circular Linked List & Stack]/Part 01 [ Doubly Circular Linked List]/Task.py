
"""

**Assignment Part 1: Doubly Linked List**

For Assignment Part 1, you should write your full code in the following cells along with your driver codes on your own.
"""

#Assignment Part 1

class Patient:
  #write a constructor
  def __init__(self, id, name, age, bloodgroup, next, prev):
    self.id = id
    self.name = name
    self.age = age
    self.bloodgroup = bloodgroup
    self.next = next
    self.prev = prev

class WRM:

  def __init__(self):
    #Creating the dummy head
    self.dh = Patient(None,None,None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh

  def registerPatient(self,id, name, age, bloodgroup):

    new_patient = Patient(id, name, age, bloodgroup, None, None)
    first = self.dh
    current = self.dh
    while current.next != self.dh:
      current = current.next

    new_patient.prev= current
    new_patient.next= first
    first.prev= new_patient
    current.next= new_patient

    print("Mr./Mrs. " ,new_patient.name, ", your registration is confirmed. Thank you for choosing us.")


  def servePatient(self):
    if self.dh.next==self.dh:
      print("There is no patient to serve")

    else:
      first_patient= self.dh.next
      self.dh.next= first_patient.next
      first_patient.next.prev= self.dh
      first_patient.prev= None
      first_patient.next=None
      print(first_patient.name, "is served. Thank you. ")

  def showAllPatient(self):
    if self.dh.next== self.dh:
      print("No patient!")

    else:
      patient= self.dh.next
      print("Showing all the patient's id:  ")
      counter= 1
      while patient!= self.dh:
        print("Patient no " ,counter, " : ", patient.id)
        counter+=1
        patient= patient.next


  def canDoctorGoHome(self):
    if self.dh.next== self.dh:
      print("Doctor can go home. ")
    else:
      print("Doctor cannot go home. ")

  def cancelAll(self):
    self.dh.next= self.dh
    self.dh.prev= self.dh
    print("Cancalation successfull. All appointments has been canceled ")

  def ReverseTheLine(self):
        if self.dh.next == self.dh:
            print("No patients to reverse")
        else:

          current = self.dh.next
          while current != self.dh:

            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.dh.next, self.dh.prev = self.dh.prev, self.dh.next
        print("Line reversed successfully")

#Write a Tester Code in this cell
print("**Welcome to Waiting Room Management System**")

def tester():
    wrm = WRM()

    while True:
        print("1. Add Patient")
        print("2. Serve Patient")
        print("3. Show All Patients")
        print("4. Can Doctor Go Home?")
        print("5. Cancel All Appointments")
        print("6. Reverse The Line")
        print("7. Exit")


        choice = input("Please enter your choice (1-7): ")

        if choice == '1':
            id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            bloodgroup = input("Enter patient blood group: ")
            wrm.registerPatient(id, name, age, bloodgroup)

        elif choice == '2':
            wrm.servePatient()

        elif choice == '3':

            wrm.showAllPatient()

        elif choice == '4':
            wrm.canDoctorGoHome()

        elif choice == '5':
            wrm.cancelAll()

        elif choice == '6':
            wrm.ReverseTheLine()

        elif choice == '7':
            print("Execution completed. ")
            break

        else:
            print("Invalid choice! Please select a valid option.")

tester()