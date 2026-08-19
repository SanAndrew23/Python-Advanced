class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # публичный
        self._transaction_log = []  # защищённый (соглашение)
        self.__balance = balance    # приватный (name mangling)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount
        self._transaction_log.append(f"+{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        self._transaction_log.append(f"-{amount}")

    def get_balance(self):
        return self.__balance

    def __repr__(self):
        return f"BankAccount({self.owner!r}, balance={self.__balance})"


acc = BankAccount("Алиса", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.owner = 'Андрей Руденко' # !!!!!!!!!!!!!!!!!!!!!!!!!


print(acc.get_balance())        # 1300
print(acc._transaction_log)     # ['+500', '-200']

# acc.__balance                 # AttributeError!
print(acc._BankAccount__balance)  # 1300 — можно обойти, но не нужно