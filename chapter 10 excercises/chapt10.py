

# Now in your main script or another module
from account import Account
from decimal import Decimal

value = Decimal('12.34')

account1 = Account('John Green', Decimal('50.00'))

print(account1.name)  # This should print 'John Green'
