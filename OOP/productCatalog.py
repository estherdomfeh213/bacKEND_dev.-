# Exercise 2: Creating a Product Catalog

# Instruction:

# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.

class Product():
  def __init__(self, name , price, quantity):
    self.name = name 
    self.price = price
    self.quantity = quantity
    
  def total_value(self): 
    return f"Total value of {self.name} is ${self.quantity * self.price}"
  
  
product1 = Product('coffee', 20, 2)
product2 = Product('sugar', 3, 90)


print(product1.total_value())
print(product2.total_value())