class Fraction():

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return "{}/{}".format(self.num, self.denom)

    def reduce(self):
        div = 2
        smaller = min(self.num, self.denom)
        for each in range(0, smaller):
            if self.num % div == 0 and self.denom % div == 0:
                self.num //= div
                self.denom //= div
            else:
                div += 1
        if self.denom == 1:
            return self.num
        else:
            return self

    def __add__(self, other):
        x = Fraction(0, 0)
        if self.denom == other.denom:
            x.num = self.num + other.num
            x.denom = self.denom
        else:
            self.num *= other.denom
            other.num *= self.denom
            x.num = self.num + other.num
            x.denom = self.denom * other.denom
        return x.reduce()

    def __sub__(self, other):
        x = Fraction(0, 0)
        if self.denom == other.denom:
            x.num = self.num - other.num
            x.denom = self.denom
        else:
            self.num *= other.denom
            other.num *= self.denom
            x.num = self.num - other.num
            x.denom = self.denom * other.denom
        return x.reduce()

    def __eq__(self, other):
        x = Fraction(0, 0)
        y = Fraction(0, 0)
        x.num = self.num
        x.denom = self.denom
        y.num = other.num
        y.denom = other.denom
        x = x.reduce()
        y = y.reduce()
        print (x)
        print (y)
        if x.num == y.num and x.denom == y.denom:
            return True
        return False

    def __bigger__(self, other):
        x = Fraction(0, 0)
        y = Fraction(0, 0)
        y.num = other.num
        x.num = self.num
        if self.denom == other.denom:
            x.denom = self.denom
            y.denom = other.denom
        else:
            x.num = self.num * other.denom
            y.num = other.num * self.denom
        x = x.reduce()
        y = y.reduce()
        if x.num > y.num and x.denom == y.denom:
            return True
        return False

    def __smaller__(self, other):
        x = Fraction(0, 0)
        y = Fraction(0, 0)
        y.num = other.num
        x.num = self.num
        if self.denom == other.denom:
            x.denom = self.denom
            y.denom = other.denom
        else:
            x.num = self.num * other.denom
            y.num = other.num * self.denom
        x = x.reduce()
        y = y.reduce()
        if x.num < y.num and x.denom == y.denom:
            return True
        return False

a = Fraction(7, 8)
b = Fraction(9, 12)
print (a.__smaller__(b))
