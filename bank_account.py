#1-Créez une classe appelée « Account » qui possède
#les attributs: account_number(str),solde_du_compte(flot),account_holder(str)

class Account :
    # définir les attributs de la classe
    def __init__(self,account_number:str,account_holder:str,account_balance :float):
        self.account_number = account_number    # Numéro de compte
        self.account_holder = account_holder    # Titulaire du compte
        self.account_balance = account_balance  # Solde du compte

#2-Définir la méthode deposit() pour déposer de l'argent

    def deposit(self,amount : float):
      if amount >0:                         # montant à déposer doit etre sup à zéro
        self.account_balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.account_balance}")
      else :
        print("Invalid deposit amount.")

#3-Définir la méthode withdraw() pour retirer de l'argent
    def withdraw(self,amount : float):
      if self.account_balance >= amount:           # verifier si le solde est suffisant pour le retrait
        self.account_balance -= amount             # Soustrait le montant du solde du compte
        print(f"Withdrawal of ${amount} successful. New balance: ${self.account_balance}")
      else :
        print("Insufficient funds.")
      pass

#4-Définir la méthode check_balance() pour vérifier le solde du compte
    def check_balance(self):
      print(f"Current balance for account {self.account_number}: ${self.account_balance}")
      pass
#5- Créer une instance de la classe Account
my_account = Account("123456789", "Ali", 500000.0)

#7- Utiliser les méthodes de la classe
my_account.deposit(50000.0)                                # Déposer de l'argent
my_account.withdraw(2500.0)                                # Retirer de l'argent
my_account.check_balance()                                 # Vérifier le solde du compte


#6-Testez le programme en créant plusieurs instances
   #- Créer une instance de la classe Account
my_account = Account(input("Numéro de compte: "), input("Titulaire du compte: "), float(input("Solde du compte: ")))

   #- Utiliser les méthodes de la classe
my_account.deposit(float(input("Amount to deposit: ")))                                # Déposer de l'argent
my_account.withdraw(float(input("Amount to be withdrawn: ")))                                # Retirer de l'argent
my_account.check_balance()                                                              # Vérifier le solde du compte