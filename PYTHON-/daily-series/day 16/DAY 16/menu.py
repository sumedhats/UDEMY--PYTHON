class Menuitem:
    def init(name,self ,water ,milk ,cofee,cost):
        self.name = name
        self.cost = float(cost)
        self.ingredients ={
            "water": int(water) ,
            "milk":int(milk),
            "cofee": int(cofee) 
        }
class menu:
    def __init__(self):
     self.menu = [
        MenuItem(name="latte", water=100, milk=20, coffee=20, cost=1),
        MenuItem(name="espresso", water=200, milk=25, coffee=20, cost=1.5),
        MenuItem(name="cappuccino", water=300, milk=20, coffee=60, cost=3)
     ]
    def get_item(self):
       options= ""
       for item in self.menu:
          options += f"{item.name}/"
          return options.rstrip("/")
    def find_drink(self,order_name,):
       for item in self.menu:
          if item.name == order_name:
             return item
          print("sorry not available")


          

