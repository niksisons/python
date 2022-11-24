class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        self.v = v
        if self.capacity - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v
            return self.capacity


a = MoneyBox(110)
print(a.can_add(120))
print(a.add(30))
print(a.add(50))

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def can_add(self, v):
#         self.v = v
#         if self.capacity - self.v >= 0:
#             return MoneyBox.add(self, v)
#
#     def add(self, v):
#         self.v = v
#         self.capacity = self.capacity - self.v
#         return self.capacity
