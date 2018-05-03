class Product(object):
     
    def __init__(self, itemName, brand, price, weight, status="for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = status
        self.sellPrice = 0
    
    def sell(self, localTax):
        self.status = "sold"
        self.sellPrice = self.tax(localTax)
        self.displayInfo() 
        print("\nITEM SOLD for ", self.sellPrice)
        return self

    def tax(self, tax):
        return (self.price + (tax * self.price))
    
    def returnItem(self, status):
        if status == "in box":
            self.status = "for sale"
            print("<<===CUSTOMER RETURNED===>>")
            self.displayInfo()
            print("Customer refunded ", self.sellPrice)
        elif status == "defective":
            self.status = "defective"
            print("<<===CUSTOMER RETURNED===>>")
            self.displayInfo()
            self.price = 0
            print("Customer refunded ", self.sellPrice)
        elif status == "open box":
            self.status = "used"
            self.decreasePrice()
            print("<<===CUSTOMER RETURNED===>>")
            self.displayInfo()
            print("Customer refunded ", self.sellPrice)
        return self

    def decreasePrice(self):
        self.price = self.price - (self.price * 0.2) 
        return self

    def displayInfo(self):
        print("=================================================")
        print("Item name: ",self.itemName)
        print("Brand name: ", self.brand)
        print("Price: ", self.price)
        print("Weight: ", self.weight)
        print("Status: ", self.status)
        return self

# IL_TAX = 0.08
# potatoe = Product("Potatoes", "Kirkland", 2, 5)
# grapes = Product("Grapes", "Chicago", 10, 3)

# grapes.sell(IL_TAX)
# print()
# potatoe.sell(IL_TAX)
# print()
# potatoe.returnItem("defective")
# print()
# potatoe.displayInfo()
# print()
# grapes.returnItem("open box")