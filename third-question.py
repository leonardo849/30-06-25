products = []

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"price {self.price} quantity {self.quantity} name {self.name}" 


while True:
    reply = input("do you want to buy a product? Y or N").upper()
    if reply == "Y":
        productReply = input("you will type like this: name quantity price you have to space between each one")
        arrayReply = productReply.split(" ")
        newP = Product(arrayReply[0], int(arrayReply[1]), float(arrayReply[2]))
        print("new product:", newP)
        products.append(newP)
    elif reply == "N":
        valueBeforeTax = 0
        for product in products:
            valueBeforeTax += (product.price * product.quantity)
        finalValue = valueBeforeTax * 1.15
        print("value before tax:", valueBeforeTax)
        print("final value:", finalValue)
        break
    