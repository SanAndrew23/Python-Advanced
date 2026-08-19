class Money:
    def __init__(self, owner="", *, f=None):
        self.cash = {0.01 : 0,  0.05 : 0,
                     0.10 : 0,  0.50 : 0,
                     1 : 0,     2 : 0,
                     5 : 0,     10 : 0,
                     50 : 0,    100 : 0,
                     200 : 0,   500 : 0,
                     1000 : 0,  2000 : 0,
                     5000 : 0}
        if f:
            pass

    @property
    def balance(self):
       pass

    def __add__(self, other):
        '''
        Метод складывает другой "кошелёк" и возвращает новый объект с новой суммой
        '''
        pass

    def __str__(self):
        return f'{f"{self.balance:,.2f}".replace(',', ' ')} ₽'


money = Money("Andrew")
