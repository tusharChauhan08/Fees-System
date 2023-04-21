import connection
import student
import account
import feeSystem

class Main:
    def __init__(self):
        self.Add = account.Admin()
        self.Student = student.AddStudent()
        self.Fee = feeSystem.Fees()
    def mainFunction(self):
        print("Welcome! to the dashboard of the feeSystem.")
        self.choice = input("Choose what you have to do Choices is::\n If you want to add an admin Account enter A. \n If you want to add student details then enter S. \n If you want to update student details enter U.\n If you want to delete student details enter D. \n If you want to submit fees of the student enter F. \n If you want to create the fees slip enter V \n::")
        if self.choice.upper() == "A":
            self.Add.addAdminAccount()
        elif self.choice.upper() == "S":
            self.Add.loginAccount()
            self.Student.studentInfo()
        elif self.choice.upper() == "U":
            self.Add.loginAccount()
            self.Student.studentInfoUpdate()
        elif self.choice.upper() == "D":
            self.Add.loginAccount()
            self.Student.studentInfoDelete()
        elif self.choice.upper() == "F":
            self.Add.loginAccount()
            self.Fee.slipCreate()
        elif self.choice.upper() == "V":
            self.Add.loginAccount()
            self.Fee.printSlip()
        else:
            print("You have entered wrong key. Please entered valid key.")

def main():
    mainModule = Main()
    mainModule.mainFunction()

if __name__ == "__main__":
    main()