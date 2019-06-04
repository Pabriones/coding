from menu import Menu

class MenuItem():
    def __init__(self, item, quantity):
        self.item=item
        self.quantity=quantity

    def getItem(self):
        return self.item
    
    def getQuantity(self):
        return self.quantity