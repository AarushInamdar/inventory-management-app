class Order:
    # constructor method
    # initialized with an empty dictionary for products (i.e., self.products),
    # where each product, dictionary entry, will be organized as sku: {'product': product, 'quantity': quantity},
    # which can be acccessed with self.products[sku], and name is assigned to self.name
    def __init__(self,name):
        self.products = {}
        self.name = name

    # overloads the __str__ method by using the format: "{self.name} ({size} products total)"
    def __str__(self):
        size = 0
        for value in self.products.values():
            size += value['quantity']
        return f"{self.name} ({size} products total)"

    # add a setter method, set_name(self, name) for modifying the name of an order
    def set_name(self, name):
        self.name = name

    # function used for adding a product to an order
    def add_product(self, product, quantity):
        sku = product.get_sku() 
        
        if sku in self.products:
            self.products[sku]['quantity'] += quantity
        else:
            self.products[sku] = {'product': product, 'quantity': quantity}
        self.products[sku]['product'].set_quantity(self.products[sku]['product'].get_quantity() - quantity)

    # function used for removing a product from an order by quantity
    def remove_product(self, product, quantity):
        sku = product.get_sku() 
        if sku in self.products:
            if quantity > self.products[sku]['quantity']:
                print("Cannot remove product, not enough in order.")
            else:
                self.products[sku]['quantity'] -= quantity
                self.products[sku]['product'].set_quantity(self.products[sku]['product'].get_quantity() + quantity)
        else:
            print("Cannot remove product, doesn't exist in this order.")

    # function used for getting the price for all items currently in order
    def get_total_price(self):
        total_price = 0
        for value in self.products.values():
            total_price += (value['quantity'] * value['product'].price)
        return total_price
