class Bank:
    acbal=10000
    def deposite(self):
        amount=int(input("Enter deposit amount"))
        if amount%100==0:
            if amount<=50000:
                self.acbal=self.acbal+amount
            else:
                print("Deposit limit is 50K only")
        else:
            print("Please enter multiples of 100 only")
        print("Available bal is: ",self.acbal)

    def validate(self):
        pin = 1234
        print("Welcome to RKCE bank")
        upin=int(input("Enter your pin : "))

        if upin==pin:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Bal Enquiry")
            print("0. Exit")
            option=int(input("choose your option"))
            if option==1:
                obj.deposite()
        else:
            print("Invalid pin")
obj=Bank()
obj.validate()