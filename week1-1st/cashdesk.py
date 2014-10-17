class CashDesk():

    money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    listmoney = []

    def take_money(self, notes):
        for each in notes:
            self.money[each] += notes[each]
        for each in self.money:
            for key in range(0, self.money[each]):
                if self.money[each] > 0:
                    self.listmoney.append(each)
        self.listmoney = sorted(self.listmoney)
        self.listmoney = self.listmoney[::-1]

    def total(self):
        sum = 0
        for each in self.money:
            sum += self.money[each]*each
        return sum

    def can_withdraw_money(self, cash):
        flag = False
        while flag is False:
            for each in self.listmoney:
                if (cash - each >= 0):
                    cash -= each
                elif cash == 0:
                    flag = True
                    return True
            return False
