import connection
import base64
import feeSystem
import student

class Admin:
    def __init__(self):
        self.DataBase = connection.database
        self.Cursor = connection.cursorObj
        self.Student = student.AddStudent()
        self.Fee = feeSystem.Fees()

    def loginAccount(self):
        self.user = input("Enter your email id for authentication:")
        self.password = input("Enter your password for authentication:")
        self.Query = [self.user]
        self.Cursor.execute("Select * from adminAccount Where EMAIL_ID=%s", self.Query)
        self.result = self.Cursor.fetchall()
        if not self.result:
            print("You are not registered we are not found you.")
        else:
            self.decodePassword = base64.b64decode(self.result[0][4]).decode("utf-8")
            if self.password == self.decodePassword:
                print("Welcome! You are successfully login into your account.")
                print("Welcome! to the dashboard of the feeSystem.")
                self.choice = input("Choose what you want to do::\n If you want to add student details then enter S. \n If you want to update student details enter U.\n If you want to delete student details enter D. \n If you want to submit fees of the student enter F. \n If you want to create the fees slip enter V ::")
                if self.choice.upper() == "S":
                    self.Student.studentInfo()
                elif self.choice.upper() == "U":
                    self.Student.studentInfoUpdate()
                elif self.choice.upper() == "D":
                    self.Student.studentInfoDelete()
                elif self.choice.upper() == "F":
                    self.Fee.slipCreate()
                elif self.choice.upper() == "V":
                    self.Fee.printSlip()
                else:
                    print("You have entered wrong key. Please entered valid key.")
            else:
                print("You entered wrong password. Login Failed!")

    def addAdminAccount(self):
        self.query = "Create Table if not exists adminAccount(NAME VARCHAR(50) NOT NULL, AGE INT, NUMBER VARCHAR(50) NOT NULL UNIQUE, EMAIL_ID VARCHAR(100) NOT NULL UNIQUE, PASSWORD VARCHAR(50) NOT NULL)"
        self.Cursor.execute(self.query)
        self.name = input("Enter your name for account:")
        self.age = int(input("Enter your age for account:"))
        self.number = input("Enter you phone number for account:")
        self.email_id = input("Enter your email id for account:")
        self.password = input("Set your password for account:")
        self.encodePassword = base64.b64encode(self.password.encode("utf-8"))
        self.dataQuery = "Insert into adminAccount(NAME,AGE,NUMBER,EMAIL_ID,PASSWORD) value(%s,%s,%s,%s,%s)"
        self.value = (self.name, self.age, self.number, self.email_id, self.encodePassword)
        self.Cursor.execute(self.dataQuery, self.value)
        self.DataBase.commit()
        print("Account is successfully created. Please login yourself into your account.")
        self.loginAccount()
        self.DataBase.close()

def main():
    accountAdd = Admin()
    choice = input("If you want to add Admin Account please enter A. \n If you want login into Admin Account please enter L ::")
    if choice.upper() == "A":
        accountAdd.addAdminAccount()
    elif choice.upper() == "L":
        accountAdd.loginAccount()
    else:
        print("Please enter the valid option. Try again later!")

if __name__ == "__main__":
    main()