
class Item (object):
    def __init__ (self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def total_price (self):
        return self.cost * self.quantity

class Invoice (object):
    def __init__ (self):
        self.item_list = []

    def add_item (self, item):
        self.item_list.append(item)

    

