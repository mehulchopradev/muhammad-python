from .min_bal_error import MinBalNotMaintainedError

class Account:
    def __init__(self, name, acc_type, balance):
        self.acc_name = name
        self.acc_type = acc_type
        self.acc_balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amt to withdraw must be more than 0')
        if self.acc_balance - amount < 1000:
            # exception condition that has happened here in the withdraw method

            # raise error to the caller
            raise MinBalNotMaintainedError('Min balance not getting maintained')
        self.acc_balance -= amount
        return self.acc_balance
