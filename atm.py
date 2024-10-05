class MyAtm:
    
    # create constructor for the class (magic / dunder method)
    def __init__(self,pin = '',balance = 0):
        self.pin = pin
        self.balance = balance
        self.menu()
    
    def menu(self):
        """
        dsiplay menu for doing functions through the atm
        """
        user_input = input("""
        Hi! Please chose from the following options:
        1. create account pin
        2. change account pin
        3. check your account balance
        4. withdraw from your account
        5. Anything else to exit
        """)
        
        if user_input == '1':
            self.create_pin()
            
        if user_input == '2':
            self.change_pin()
            
        if user_input == '3':
            self.check_balance()
            
        if user_input == '4':
            self.withdraw()
            
        else:
            exit()
            pass
        
    def create_pin(self):
        " method to create initial pin and balance of our account"
        user_pin = input("Enter your new pin: ")
        self.pin = user_pin
        
        user_balance = int(input("Enter your account balance: "))
        self.balance = user_balance
        
        print("PIN created successfully")
        self.menu()
        
    def change_pin(self):
        "method to change pin of our account"
        
        old_pin = input("Enter your old pin ")        
                
        if old_pin == self.pin:
            new_pin = input("enter your new pin: ")
            self.pin = new_pin
            print("PIN changed successfully")
        else:
            print("incorrect pin, please try again")
        
        self.menu()
     
    def check_balance(self):
        "method to check account balance"
        
        user_pin = input("Enter your PIN: ")
        
        if user_pin == self.pin:
            print(f"Your current balance is $ {self.balance}")
        else:
            print("incorrect pin, please try again")
            
        self.menu()    
        
    def withdraw(self):
        "method to withdraw money from account"
        
        user_pin = input("Enter your PIN: ")
        
        if user_pin == self.pin:
            
            amt_withdrawn = int(input("Enter amount you want to withdraw: "))
            
            if amt_withdrawn <= self.balance:
                self.balance-= amt_withdrawn
                print(f"$ {amt_withdrawn} withdrawn successfully, remaining balance ${self.balance}")
            else:
                print("Not enough balance")
            
        else:
            print("incorrect pin, please try again")
            
        self.menu()   
            