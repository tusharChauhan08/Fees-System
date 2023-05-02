import decimal
import connection
import student

class Fees:
    def __init__(self):
        self.database = connection.database
        self.Cursor = connection.cursorObj

    def slipCreate(self):
        self.Query = "Create Table if not exists feeslip(ROLL_NO INT NOT NULL, PAID_FEES INT NOT NULL, BALANCE_FEES INT NOT NULL)"
        self.Cursor.execute(self.Query)
        self.roll_no = int(input("Enter roll no of the student:"))
        self.studentValue = [self.roll_no]
        # For fetching the total fees of the student
        self.studentQuery = "Select TOTAL_FEES From student Where ROLL_NO=%s"
        self.Cursor.execute(self.studentQuery,self.studentValue)
        self.studentResult = self.Cursor.fetchall()
        if not self.studentResult:
            print("{} student is not found in the database. Please check the roll no.".format(self.roll_no))
        else:
            print("Total Fees of the student is {}.".format(self.studentResult[0][0]))
            self.feesQuery = "Select SUM(PAID_FEES),MIN(BALANCE_FEES) From feeslip Where ROLL_NO=%s"
            self.Cursor.execute(self.feesQuery,[self.roll_no])
            self.resultFees = self.Cursor.fetchall()
            # For update the balance in the database on the first paid amount
            if self.resultFees[0][0] is None:
                self.paid_fees = int(input("Enter paid amount of fees by student:"))
                self.balance_fees = self.studentResult[0][0] - self.paid_fees
                print("Balance Fees of the student is {}.".format(self.balance_fees))
                self.query = "Insert into feeslip(ROLL_NO, PAID_FEES, BALANCE_FEES) Value(%s,%s,%s)"
                self.value = (self.roll_no, self.paid_fees, self.balance_fees)
                self.Cursor.execute(self.query, self.value)
                self.database.commit()
                self.database.close()
            else:
                # For update the balance amount after first paid amount
                self.paid_fees = int(input("Enter paid amount of fees by student:"))
                if self.resultFees[0][1] <= 0:
                    print("{} roll no student is already paid his all fees.".format(self.roll_no))

                elif self.resultFees[0][1] < self.paid_fees:
                    print("Paid amount can't be greater than the Balance fees and Balance fees is {}.".format(self.resultFees[0][1]))
                    self.paid_fees = self.resultFees[0][1]
                    self.totalPaidFees = decimal.Decimal(self.resultFees[0][0]) + decimal.Decimal(self.paid_fees)
                    self.balance_fees = decimal.Decimal(self.studentResult[0][0]) - decimal.Decimal(self.totalPaidFees)
                    print("Balance Fees of the student is {}.".format(self.balance_fees))
                    self.query = "Insert into feeslip(ROLL_NO, PAID_FEES, BALANCE_FEES) Value(%s,%s,%s)"
                    self.value = (self.roll_no, self.paid_fees, self.balance_fees)
                    self.Cursor.execute(self.query, self.value)
                    self.database.commit()

                elif self.paid_fees <= self.resultFees[0][1]:
                    print("Balance Fees of the student is {}.".format(self.resultFees[0][1]))
                    self.totalPaidFees = decimal.Decimal(self.resultFees[0][0]) + decimal.Decimal(self.paid_fees)
                    self.balance_fees = decimal.Decimal(self.studentResult[0][0]) - self.totalPaidFees
                    self.query = "Insert into feeslip(ROLL_NO, PAID_FEES, BALANCE_FEES) Value(%s,%s,%s)"
                    self.value = (self.roll_no, self.paid_fees, self.balance_fees)
                    self.Cursor.execute(self.query, self.value)
                    self.database.commit()

    def printSlip(self):
        self.roll_no = int(input("Enter student roll no for print the slip:"))
        self.joinQuery = "Select Student.NAME, feeslip.ROLL_NO, Student.MOBILE_NUMBER, Student.TOTAL_FEES, feeslip.PAID_FEES, feeslip.BALANCE_FEES From feeslip INNER JOIN STUDENT ON Student.ROLL_NO=feeslip.ROLL_NO"
        self.Cursor.execute(self.joinQuery)
        self.result = self.Cursor.fetchall()
        if not self.result:
            print("You enter the wrong ")
        else:
            self.name = "Name"
            self.roll = "Roll-no"
            self.number = "Mobile-no"
            self.total = "Total-Fees"
            self.paid = "Paid-Fees"
            self.balance = "Balance-Fees"
            print(self.name.center(10),self.roll.center(40),self.number.center(20),self.total.center(35),self.paid.center(30),self.balance.center(30))
            for self.iterative in self.result:
                if self.iterative[1] == self.roll_no:
                    print(self.iterative[0].center(10), str(self.iterative[1]).center(30), self.iterative[2].center(30), str(self.iterative[3]).center(30), str(self.iterative[4]).center(30),str(self.iterative[5]).center(30))





