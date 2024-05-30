# It is an implementation of an e-commerce system where products can be added, customers can be created and then products can
# be added to the cart. Find the cases where the logic to handle adding or removing
# products from cart fails. Handle these cases after debugging.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")

class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            print("Invalid quantity. Cannot add non-positive quantity to cart.")
            return
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        if product not in self.products:
            print("Product not found in the cart.")
            return
        if quantity <= 0:
            print("Invalid quantity. Cannot remove non-positive quantity from cart.")
            return
        if self.products[product] <= quantity:
            del self.products[product]
        else:
            self.products[product] -= quantity

    def get_total_cart_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_total_price() * quantity
        return total_price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_product(product, quantity)

    def checkout(self):
        total_price = self.shopping_cart.get_total_cart_price()
        if total_price > 0:
            print(f"Checking out... Your total is ${total_price}.")
            self.shopping_cart.products = {}
        else:
            print("Your cart is empty. Nothing to checkout.")

# Test the e-commerce system
product1 = Product("Keyboard", 50, 2)
product2 = Product("Mouse", 30, 3)

customer = Customer("John Doe", "john.doe@example.com")

# Adding products to the cart
customer.add_to_cart(product1, 1)  # Valid addition
customer.add_to_cart(product2, 2)  # Valid addition
customer.checkout()

# Debugging invalid operations
customer.add_to_cart(product1, -1)  # Invalid addition
customer.remove_from_cart(product2, 3)  # Valid removal
customer.remove_from_cart(product2, 1)  # Invalid removal (product already removed)

# It is an implementation of a food ordering system.
# Negative quantity should not be allowed and non present food item should not be allowed to remove

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, food_item, quantity):
        if quantity < 0:
            print("Invalid quantity. Cannot add non-positive quantity to menu.")
            return
        if food_item in self.menu:
            self.menu[food_item] += quantity
        else:
            self.menu[food_item] = quantity

    def remove_from_menu(self, food_item, quantity):
        if food_item not in self.menu:
            print(f"{food_item.name} not found in the menu.")
            return
        if quantity <= 0:
            print("Invalid quantity. Cannot remove non-positive quantity from menu.")
            return
        if self.menu[food_item] <= quantity:
            del self.menu[food_item]
        else:
            self.menu[food_item] -= quantity

    def get_total_revenue(self):
        total_revenue = 0
        for food_item, quantity in self.menu.items():
            total_revenue += food_item.price * quantity
        return total_revenue

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = {}

    def add_to_cart(self, food_item, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        if food_item in self.cart:
            self.cart[food_item] += quantity
        else:
            self.cart[food_item] = quantity

    def remove_from_cart(self, food_item, quantity):
        if food_item not in self.cart:
            print(f"{food_item.name} not found in the cart.")
            return
        if quantity <= 0:
            print("Invalid quantity. Cannot remove non-positive quantity from cart.")
            return
        if self.cart[food_item] <= quantity:
            del self.cart[food_item]
        else:
            self.cart[food_item] -= quantity

class DeliveryService:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def find_restaurant_by_name(self, name):
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None

# Test the food delivery system
restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Spice Delight")

food_item1 = FoodItem("Burger", 8)
food_item2 = FoodItem("Pizza", 12)
food_item3 = FoodItem("Pasta", 10)

restaurant1.add_to_menu(food_item1, 10)
restaurant1.add_to_menu(food_item2, 5)

restaurant2.add_to_menu(food_item2, 8)
restaurant2.add_to_menu(food_item3, 12)

customer = Customer("Alice", "123 Main St.")
customer.add_to_cart(food_item1, 2)
customer.add_to_cart(food_item2, 3)
customer.add_to_cart(food_item3, -2)  # This should print an error message

delivery_service = DeliveryService()
delivery_service.add_restaurant(restaurant1)
delivery_service.add_restaurant(restaurant2)

restaurant1.remove_from_menu(food_item2, 6)  # This should print an error message

restaurant2.remove_from_menu(food_item1, 1)  # This should print an error message

print("Total revenue for Tasty Bites:", restaurant1.get_total_revenue())
print("Total revenue for Spice Delight:", restaurant2.get_total_revenue())
