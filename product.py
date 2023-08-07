class Product:

    # constructor method
    # assign all components to their respective attribute 
    # (e.g., self.sku, self.name)
    def __init__(self, sku, name, price, category, quantity):
        self.sku = sku
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
    

    # write and fill-in all getter and setter methods
    # (e.g., get_sku(self) & set_sku(self, sku)
    # FILL-IN HERE - 8 methods total
    def get_sku(self):
        return self.sku
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_category(self):
        return self.category
    
    def get_quantity(self):
        return self.quantity

    def set_sku(self, var):
        if type(var) == str:
            self.sku = var
        else:
            print("That is not the correct type of variable that can be set for price. Please try again with a string.")
    
    def set_name(self, var):
        if type(var) == str:
            self.name = var
        else:
            print("That is not the correct type of variable that can be set for price. Please try again with a string.")
    
    def set_price(self, var):
        list = [float, int]
        if (type(var) not in list) or var <= 0:
            print("That is not the correct type of variable that can be set for price. Please try again with an integer.")
        else:
            self.price = int(var)
    
    def set_category(self, var):
        self.category = var
        
    def set_quantity(self, var):
        if type(var) != int or var < 0:
            print("That is not the correct type of variable that can be set for quantity. Please try again with an integer.")
        else:    
            self.quantity = var
        


    # write all overload methods for __str__ (i.e., str), >, <, and ==
    # __str__ should return the format "{self.name} (${self.price}): {self.quantity} left"
    # all other overloaded comparison operators should compare based on price
    # FILL-IN HERE - 4 methods total

    def __str__(self):
        return f'{self.name} (${self.price}): {self.quantity} left'
    
    def __eq__(self, other: object) -> bool:
        if self.price == other.price:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False

