class Category:
    
    # category constructor method
    def __init__(self, name):
        self.name = name

    # overload __str__ method to return the name of a category
    def __str__(self):
        return self.name
