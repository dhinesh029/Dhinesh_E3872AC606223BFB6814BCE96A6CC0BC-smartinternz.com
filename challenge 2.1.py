class BankAccount:
  def __init__(self account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number 
    self.__account_holder_name=account_holder_name
    self.__balance=initial_balance
  def deposit(self amount):
    if amount>0:
      self._balance += amount
      print(f"deposited ${amount}.new balance:${self.balance}")
    else:
      print("invalid deposit amount.please enter a positive value.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__balance:
      self.balance -= amount
      print(f"withdraw ${amount}. new balance:${self.__balance}")
    elif amount <= 0:
      print("invalid withdrawl amount.please enter a positive value.")
    else:
      print("insufficient funds for withdrawl.")
  def display_balance(self):
    print(f"account balance for {self.__account_holder_name: ${self.__balance}")

#create an instance of the BankAccount class
account = BankAccount("1234566789","john doe",1000.0)

#test deposit annd withdrwal functionally
account.display_balance()
account.deposit(500..0)
account.withdraw(200.0)
account.withdraw(1500.0)
account.display_balance()
    
      
    
 