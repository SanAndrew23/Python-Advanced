class Money():
    def __init__(self, currency='', balance=0, owner='', *, f=None):
        if f:
            self.currency = f['currency']
            self.__balance = f['balance']
        else:
            self.owner = owner
            self.__balance = balance
            self.currency = currency
    def convert(self, currency):
        sp = {
            'USD': {'balance' : 0.0},
            'RUB': {'balance': 0.0},
            'EUR': {'balance': 0.0},
        }
        c = 0
        for i in sp:
            if i == self.currency:
                sp[i]['balance'] = self.__balance
                flag = c
            c += 1
        if self.currency == 'USD':
            sp['EUR']['balance'] = round(0.86 * self.__balance, 2)
            sp['RUB']['balance'] = round(84.54 * self.__balance, 2)
        elif self.currency == 'EUR':
            sp['RUB']['balance'] = round(1.157 * self.__balance, 2)
            sp['USD']['balance'] = round(97.51 * self.__balance, 2)
        else:
            sp['USD']['balance'] = round(0.01187 * self.__balance, 2)
            sp['EUR']['balance'] = round(0.01026 * self.__balance, 2)

        self.sp = sp
        return sp[currency]['balance']

    def __add__(self, currency, balance):
        slovar = {'balance': balance, 'currency': currency}
        result = self.__balance + Money(f=slovar).convert(self.currency)
        return result

    def __str__(self):
        return self

money = Money('RUB',1500, 'Andrew')
print(money.convert('USD'))
print(money + Money(f={'currency': 'RUB', 'balance': 1500}))