class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def __str__(self):
        return f"{self.name} (Electronics, Warranty: {self.warranty_years} years) - ₹{self.price}"


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{self.name} (Clothing, Size: {self.size}) - ₹{self.price}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product}")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"Removed {product.name}")
                return
        print(f"{product_name} not found in cart.")

    def show_cart(self):
        if not self.products:
            print("Cart is empty.")
        else:
            print("Shopping Cart:")
            for index, product in enumerate(self.products, start=1):
                print(f"{index}. {product}")

    @staticmethod
    def calculate_total(products):
        total = sum(product.price for product in products)
        if total > 5000:
            discount = total * 0.10  
            print(f"Discount applied: ₹{discount}")
            total -= discount
        return total


cart = ShoppingCart()
laptop = Electronics("Asus laptop", 80000, 2)
tshirt = Clothing("US-Polo T-Shirt", 800, "L")
phone = Electronics("I-Phone 16promax", 125000, 1)

cart.add_product(laptop)
cart.add_product(tshirt)
cart.add_product(phone)

cart.show_cart()

cart.remove_product("T-Shirt")
cart.show_cart()

final_total = ShoppingCart.calculate_total(cart.products)
print(f"Final Total: ₹{final_total}")
