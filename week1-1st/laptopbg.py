class Product():

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = 0
        profit += self.final_price - self.stock_price
        return profit

    def __str__(self):
        return "{}".format(self.name)


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    products = {}
    profit = 0

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        self.products[product] = count
        #print (self.products)

    def list_products(self, product_class):
        for item in self.products:
            if isinstance(item, product_class):
                print(item, " - ", self.products[item])
                # print (item.name, " - ",
                           # self.products[item])
            else:
                print ("No such products exist in our store!")

    def sell_product(self, product):
        if product not in self.products:
            return False
        else:
            if self.products[product] > 0:
                self.profit += product.profit()
                self.products[product] -= 1
                return True
            else:
                return False

    def total_income(self):
        print (self.profit)

new_product = Product('HP HackBook', 1000, 1243)
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 2)
print (new_store.sell_product(new_smarthphone))
print (new_store.sell_product(new_smarthphone))
print (new_store.sell_product(new_smarthphone))
print (new_store.total_income())
