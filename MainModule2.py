# Main Module 2
# Ctrl+Space : Listing all offers
# import something from sales.py
# Way 2 : import as a "Class"


from ecommerce.shopping import sales
from ecommerce.customer import contact

print(dir(sales))
print(dir(contact))

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
