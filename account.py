import connection
import base64

class Admin:
    def __init__(self):
        self.DataBase = connection.database
        self.Cursor = connection.cursorObj

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
            else:
                print("You entered wrong password. Login Failed!")
                self.again = input("For try again please enter Y and For exit please enter N:")
                if self.again.upper() == "Y":
                    self.loginAccount()
                else:
                    print("Successfully Exit. Thank you for your time.")


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
        self.DataBase.close()


