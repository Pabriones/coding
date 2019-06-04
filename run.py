from menu import Menu
from menuitem import MenuItem
from ordertotal import OrderTotal
from payment import Payment
from inventory import Inventory

def main():

    item1=Menu(1,'soap', 2.25)
    item2=Menu(2,'cookies', 4.43)
    item3 =Menu(3,'milk', 2.45)

    inventory = Inventory()
    inventory.addItem(item1)
    inventory.addItem(item2)
    inventory.addItem(item3)
    
    
    orderitem1=MenuItem(inventory.getItemByNumber(1),1)
    orderitem2=MenuItem(inventory.getItemByNumber(2),2)
    orderitem3=MenuItem(inventory.getItemByNumber(3),1)

    order = OrderTotal()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)
    order.addOrderItems(orderitem3)

    payment =order.calcTotal()
    print(payment)

main()
