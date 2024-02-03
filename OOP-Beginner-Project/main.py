from bank_accounts import *

Teodor = BankAccount(1000, "Teodor")
Maria = BankAccount(2000, "Maria")

Teodor.getBalance()
Maria.getBalance()

Maria.deposit(500)

Teodor.withdraw(10000)
Teodor.withdraw(10)

Teodor.transfer(10000, Maria)
Teodor.transfer(100, Maria)

Ivan = InterestRewardsAccount(1000, "Ivan")

Ivan.getBalance()

Ivan.deposit(100)

Ivan.transfer(100, Teodor)

Bojidar = SavingsAccount(1000, "Bojidar")

Bojidar.getBalance()

Bojidar.deposit(100)

Bojidar.transfer(10000, Maria)
Bojidar.transfer(1000, Maria)
