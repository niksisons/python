class frac:
    def __init__(self, a=4, b=16):
        self.chislitel = a
        self.znamenatel = b

    def sokr(self):
        if self.znamenatel % self.chislitel == 0:
            self.znamenatel //= self.chislitel
            self.chislitel = 1
        while self.chislitel % 2 == 0 and self.znamenatel % 2 == 0:
            self.chislitel //= 2
            self.znamenatel //= 2
        while self.chislitel % 3 == 0 and self.znamenatel % 3 == 0:
            self.chislitel //= 3
            self.znamenatel //= 3
        while self.chislitel % 5 == 0 and self.znamenatel % 5 == 0:
            self.chislitel //= 5
            self.znamenatel //= 5
        return f'{self.chislitel} / {self.znamenatel}'

    def add(self, a):
        # self.a = a
        return self.sokr() + a


a = frac(3, 7)
print(a.sokr())
