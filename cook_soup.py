# Project Cook Soup

import webbrowser

class Ingredient:

    """Models a food item used as an ingredient."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def use(self, use_amount):
        self.amount -= use_amount

    def __add__(myself, other):
        """Combines two ingredients."""
        new_name = (myself.name, other.name)
        return Ingredient(new_name, other.amount)

class Spice(Ingredient):
    
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

class Soup:
    
    def __init__(self, *args):
        names = []
        amounts = []
        for arg in args:
            names.append(arg.name)
            amounts.append(arg.amount)
        self.names = names
        self.amounts = amounts

    def cook(self):
        my_sum = "https://www.google.com/search?q="
        for i in range(0, len(self.names)):
            my_sum += f"(x{self.amounts[i]}) {self.names[i]}+"
        my_sum += "soup"
        webbrowser.open(my_sum)

class SoupFeeds(Soup):
    
    def __init__(self, feeds, *args):
        self.feeds = feeds
        super().__init__(*args)
    
    def cook(self):
        my_sum = "https://www.google.com/search?q="
        for i in range(0, len(self.names)):
            my_sum += f"(x{self.amounts[i]}) {self.names[i]}+"
        my_sum += f"soup which feeds {self.feeds}"
        webbrowser.open(my_sum)


a = Ingredient('carrot', 1)
b = Spice('pepper', 2, 'hot')

c = Soup(a, b)
# c.cook() # Opens google search as expected.

d = SoupFeeds(5, a, b)
d.cook()
