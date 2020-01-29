from com.abc.bank.account import Account
from com.abc.bank.min_bal_error import MinBalNotMaintainedError
from traceback import print_exc

a1 = Account('mehul', 'savings', 10000)

try:
    ub = a1.withdraw(95600)
except ValueError:
    print_exc()
except MinBalNotMaintainedError:
    print_exc()
else:
    print(ub)


# Internally
# ub = Account.withdraw(a1, 5000)