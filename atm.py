class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    def login(self):
        entered_pin = int(input("Enter PIN: "))
        if entered_pin == self.__pin:
            print("Login successful")
            return True
        else:
            print("Wrong PIN")
            return False

    def check_balance(self):
        print("Balance:", self.__balance)

    def deposit(self):
        amount = int(input("Enter amount: "))
        self.__balance += amount
        print("Deposited")

    def withdraw(self):
        amount = int(input("Enter amount: "))
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn")
        else:
            print("No balance")

obj = BankAccount("Jenish", 1000, 1234)

if obj.login():
    obj.check_balance()
    obj.deposit()
    obj.withdraw()
    obj.check_balance()
