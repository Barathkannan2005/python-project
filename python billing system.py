import os

FILENAME = "products.txt"


def load_products():
    products = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    product_id, name, price, quantity = line.split(',')
                    products[product_id] = {
                        'name': name,
                        'price': float(price),
                        'quantity': int(quantity)
                    }
    return products


def save_products(products):
    with open(FILENAME, 'w') as file:
        for product_id, details in products.items():
            line = f"{product_id},{details['name']},{details['price']},{details['quantity']}\n"
            file.write(line)


def view_products(products):
    if not products:
        print("No products available.")
    else:
        print("\nProduct List:")
        for product_id, details in products.items():
            print(
                f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']:.2f}, Quantity: {details['quantity']}"
            )


def add_product(products):
    product_id = input("Enter product ID: ")
    if product_id in products:
        print("Product already exists!")
    else:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        products[product_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        print("Product added successfully!")


def remove_product(products):
    view_products(products)
    product_id = input("Enter product ID to remove: ")
    if product_id in products:
        del products[product_id]
        print("Product removed successfully!")
    else:
        print("Product not found!")


def update_quantity(products):
    product_id = input("Enter product ID to update: ")
    if product_id in products:
        new_quantity = int(input("Enter new quantity: "))
        products[product_id]['quantity'] = new_quantity
        print("Quantity updated successfully!")
    else:
        print("Product not found!")


def billing(products):
    view_products(products)
    bill = 0.0
    while True:
        product_id = input("Enter product ID to bill (or 'done' to finish): ")
        if product_id == 'done':
            break
        if product_id in products:
            quantity = int(input("Enter quantity: "))
            if quantity <= products[product_id]['quantity']:
                products[product_id]['quantity'] -= quantity
                bill += products[product_id]['price'] * quantity
                print(f"Added to bill. Current total: Rs{bill:.2f}")
            else:
                print("Insufficient stock!")
        else:
            print("Product not found!")
    print(f"Total bill: Rs{bill:.2f}")


products = load_products()
while True:
    print("\nSupermarket Management System")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. Billing")
    print("5. View Products")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_product(products)
    elif choice == '2':
        remove_product(products)
    elif choice == '3':
        update_quantity(products)
    elif choice == '4':
        billing(products)
    elif choice == '5':
        view_products(products)
    elif choice == '6':
        save_products(products)
        print("Exiting the system.")
        break
    else:
        print("Invalid choice! Please try again.")
    save_products(products)
