class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):                        #Protected Method
        print(f"Balance: ₹{self.balance}")

    def __updated_balance(self, amount):            #Private Method
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__updated_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()
account.deposit(4000)