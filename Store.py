from Product import Product


class Store(object):
    prodID = 0
    products = []
    # location = "123 Purrr srt., Catlandia"
    # owner = 

    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
    
    def addProduct(self):
        itmName = input("Item name: ")
        brandName = input("Brand name: ")
        price = input("Price: ")
        weight = input("Weight: ")
        prod = Product(itmName, brandName, price, weight)
        # self.products.append({str(prodID) : prod})
        self.products.append(prod)
        # self.prodID += 1
        return self

    def removeProd(self, prod):
        del self.products[prod]

    def printProducts(self):
        
        for i in self.products:
            i.displayInfo()
            

storeLocation = input("Store Location: ")
storeOwner = input("Store Owner: ")
store1 = Store(storeLocation, storeOwner)

#add some dummy Products  3 of them
for i in range(3):
    store1.addProduct()
store1.removeProd(0)
#print all products 
store1.printProducts()