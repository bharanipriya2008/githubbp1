class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 5  # 5% tax

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.get_total()

        return subtotal

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                    FINAL BILL")
        print("=" * 60)

        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Amount':>12}")
        print("-" * 60)

        for product in self.products:
            amount = product.get_total()
            print(f"{product.name:<20}{product.price:>10.2f}"
                  f"{product.quantity:>8}{amount:>12.2f}")

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print("-" * 60)
        print(f"{'Subtotal':>48}{subtotal:>12.2f}")
        print(f"{'Tax (5%)':>48}{tax:>12.2f}")
        print(f"{'Grand Total':>48}{total:>12.2f}")
        print("=" * 60)


# Main program
bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i + 1}")

    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()
