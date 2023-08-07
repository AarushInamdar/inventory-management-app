from product import Product
from category import Category
from order import Order

### TEST FLOW ###

points = 0

# Creating a category
electronics = Category("Electronics")

# Creating products
product1 = Product("p001", "iPhone 12", 1000, electronics, 5)
product2 = Product("p002", "Samsung TV", 1500, electronics, 3)

# Creating an order
order1 = Order("order1")
order1.add_product(product1, 3)
order1.remove_product(product1, 1)
total_cost = order1.get_total_price()
print("Points before TEST CASE 1: ", points)
# given test case in writeup
print(str(product1))
if ("3 left" in str(product1)):
    points += 0.25    
if ("2 products" in str(order1)):
    points += 0.25
if (int(order1.get_total_price()) == 2000):
    points += 0.25
if ((product1 < product2) == True): 
    points += 0.25
print("Points after TEST CASE 1: ", points)
# setters and getters 1
product1.set_sku("p1")
product1.set_name(500)
product1.set_quantity(10)
product1.set_price(1250)

if (product1.get_sku() == "p1"):
    points += 0.25
print(product1.get_name(), "NAME")
if (product1.get_name() == "iPhone 12"):
    points += 0.25
if (product1.get_quantity() == 10):
    points += 0.25
if (product1.get_price() == 1250):
    points += 0.25
print("Points after TEST CASE 2: ", points)

product1.set_sku(900)
product1.set_name("iPhone 13")
product1.set_quantity(-10)
product1.set_price(0)
if (product1.get_sku() == "p1"):
    points += 0.25
if (product1.get_name() == "iPhone 13"):
    points += 0.25
if (product1.get_quantity() == 10):
    points += 0.25
if (product1.get_price() == 1250):
    points += 0.25
print("Points after TEST CASE 3: ", points)

product3 = Product("p003", "Samsung Galaxy S9", 1250, electronics, 13)
if ((product1 == product3) == True):
    points += 0.25
if ((product1 > product2) == False):
    points += 0.25
if ((product2 == product3) == False):
    points += 0.25
if ((product2 < product3) == False):
    points += 0.25
print("Points after TEST 4:", points)

'''Ignore'''
product2.set_price(999.01)
order2 = Order("order2")
'''Ignore'''

print(product3) #13 left
order2.add_product(product3, 2) #13-2 = 11
print(product3) #11 left
order2.remove_product(product3, 3) #No operation done since too many in order
print(product3) #11 left

if (int(product2.get_price()) == 999):
    points += 0.25

if ("10 left" in str(product3)):
    points += 0.25
if ("2 products" in str(order2)):
    points += 0.25
if (int(order2.get_total_price()) == 2500):
    points += 0.25

# show total points
print("Total points: " + str(points))