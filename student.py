import connection


class AddStudent:
    def __init__(self):
        self.database = connection.database
        self.Cursor = connection.cursorObj

    def studentInfo(self):
        self.query = "Create table if not exists Student(NAME VARCHAR(50) NOT NULL,ROLL_NO INT AUTO_INCREMENT PRIMARY KEY, MOBILE_NUMBER VARCHAR(50) NOT NULL UNIQUE, COURSE VARCHAR(50) NOT NULL, YEAR INT NOT NULL, STATUS VARCHAR(5) NOT NULL, TOTAL_FEES DOUBLE NOT NULL)"
        self.Cursor.execute(self.query)
        self.name = input("Enter name of the student:")
        self.roll_no = int(input("Enter roll no of the student:"))
        self.mobile = input("Enter mobile no of the student:")
        self.course = input("Enter course of the student:")
        self.year = int(input("Enter admission year of the student:"))
        self.status = input("Enter status of student is active or not so please enter yes or no:")
        self.fees = int(input("Enter total fees of the student:"))
        self.Query = "Insert into Student(NAME, ROLL_NO, MOBILE_NUMBER, COURSE, YEAR, STATUS, TOTAL_FEES) value(%s, %s, %s, %s, %s, %s, %s)"
        self.value = (self.name, self.roll_no, self.mobile, self.course, self.year, self.status, self.fees)
        self.Cursor.execute(self.Query, self.value)
        self.database.commit()
        self.database.close()

    def studentInfoUpdate(self):
        self.roll_no = int(input("Enter roll no of the student to update details:"))
        self.name = input("Enter updated name of student:")
        self.mobile = int(input("Enter updated mobile number of the student:"))
        self.course = input("Enter updated course name of the student:")
        self.year = int(input("Enter updated admission year of the student:"))
        self.status = input("Enter updated status of the student that student is active or not so please enter yes or no:")
        self.Query = "Update Student SET NAME=%s, MOBILE_NUMBER=%s, COURSE=%s, YEAR=%s, STATUS=%s Where ROLL_NO=%s"
        self.value = (self.name, self.mobile, self.course, self.year, self.status, self.roll_no)
        self.Cursor.execute(self.Query, self.value)
        self.database.commit()
        self.database.close()

    def studentInfoDelete(self):
        self.roll_no = int(input("Enter roll no of the student you want to delete:"))
        self.query = "Delete From student where ROLL_NO=%s"
        self.value = [self.roll_no]
        self.Cursor.execute(self.query,self.value)
        self.database.commit()
        self.database.close()
        print("{} roll_no students details are successfully deleted.".format(self.roll_no))
