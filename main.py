class Value:

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, obj, val):
        self.val = int(val * (1 - obj.commission))


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
