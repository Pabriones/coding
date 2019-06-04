from menu import Menu
from menuitem import MenuItem
from payment import Payment

class OrderTotal():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, menuitem):
        self.orderitems.append(menuitem)

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total += o.getItem().itemprice * o.quantity
        payment=Payment(total)
        return payment

    