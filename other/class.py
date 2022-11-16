class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        self.v = v
        if self.capacity - self.v >= 0:
            return True

    def add(self, v):
        if MoneyBox.can_add(self, v):
            print(self.capacity - self.v)


a = MoneyBox(100)
a.add(a.can_add(50))
