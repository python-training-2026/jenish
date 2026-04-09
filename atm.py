class BankAccount:
      def __init__(self):
        self.balance = 0

      def check_balance(self):
        print("balance:",self.balance)

      def deposit(self):
        amount = int(input("Enter amount: "))
        self.balance += amount
        print("Deposited")

      def withdraw(self):
        amount = int(input("Enter amount: "))
        self.balance -= amount
        print("withdraw")

class ATM(BankAccount):
  def menu(self):
   while True:
    print("check_balance ,deposit ,withdraw")

    choice = input("Enter choice:")

    if choice =='1':
      self.check_balance()

    elif choice =='2':
      self.deposit()

    elif choice =='3':
       self.withdraw()

    elif choice =='4':
      break


    else:
      print("Invalid choice")

obj=ATM()
obj.menu()