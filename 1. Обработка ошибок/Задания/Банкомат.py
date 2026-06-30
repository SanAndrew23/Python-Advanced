class InvalidAmountError(Exception):
    def __init__(self, balance):
        self.balance = balance
        print(f'Некорректная сумма: {balance}. Сумма должна быть больше нуля.')


class InsufficientFundsError(Exception):
    def __init__(self, balance):
        self.balance = balance
        print(f'Недостаточно средств. Баланс: {balance}, требуется: {amount}.')


class DailyLimitExceededError(Exception):
    def __init__(self, balance):
        self.balance = balance
        print('Превышен дневной лимит снятия.')


class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.amount = 0

    def deposit(self, dep):
        if dep <= 0:
            raise InvalidAmountError
        self.balance += dep

    def withdraw(self, wdr):
        if wdr <= 0:
            raise InvalidAmountError
        elif wdr > self.balance:
            raise InsufficientFundsError
        elif self.amount > 10000:
            raise DailyLimitExceededError
        else:

