import datetime

products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

shopping_cart = []

def display_items():
    print("\n========== AVAILABLE PRODUCTS ==========")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]}       ${prices[i]:.2f}")

def add_item(cart, prods):
    valid_input = False
    
    while valid_input == False:
        product_num = int(input("\nEnter product number: "))
        
        if product_num >= 1 and product_num <= len(prods):
            cart.append(prods[product_num - 1])
            print(f"{prods[product_num - 1]} was added to your cart!")
            valid_input = True
        else:
            print("Invalid product!\nPlease choose a number between 1 and 6.")

def display_cart(cart, prods, prcs):
    print("\n========== YOUR SHOPPING CART ==========")
    
    if len(cart) == 0:
        print("Your shopping cart is empty!")
    else:
        for i in range(len(cart)):
            item_name = cart[i]
            index_num = prods.index(item_name)
            item_price = prcs[index_num]
            print(f"{i + 1}. {item_name}       ${item_price:.2f}")
            
        print(f"\nTotal Items: {len(cart)}")

def remove_item(cart):
    if len(cart) == 0:
        print("Your shopping cart is empty!\nThere is nothing to remove.")
    else:
        display_cart(cart, products, prices)
        print("\nWhich item would you like to remove?")
        
        is_valid = False
        
        while is_valid == False:
            remove_num = int(input("Enter item number: "))
            
            if remove_num >= 1 and remove_num <= len(cart):
                deleted_item = cart[remove_num - 1]
                cart.pop(remove_num - 1)
                print(f"{deleted_item} was removed from your cart!")
                is_valid = True
            else:
                print("That item does not exist in your cart!")

def get_subtotal(cart, prods, prcs):
    total = 0.0
    for item in cart:
        idx = prods.index(item)
        total = total + prcs[idx]
    return total

def get_discount(subtotal_amount):
    if subtotal_amount < 10:
        return 0.0
    elif subtotal_amount >= 10 and subtotal_amount < 20:
        return 0.05
    elif subtotal_amount >= 20 and subtotal_amount < 40:
        return 0.10
    else:
        return 0.15

user_choice = 0

while user_choice != 6:
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
   
    user_choice = int(input("\nEnter your choice: "))

    if user_choice == 1:
        display_items()
        
    elif user_choice == 2:
        display_items()
        add_item(shopping_cart, products)
        
    elif user_choice == 3:
        remove_item(shopping_cart)
        
    elif user_choice == 4:
        display_cart(shopping_cart, products, prices)
        
    elif user_choice == 5:
        print("\n========== CURRENT TOTAL ==========")
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
        else:
            for item in shopping_cart:
                idx = products.index(item)
                print(f"{item}       ${prices[idx]:.2f}")
                
            current_subtotal = get_subtotal(shopping_cart, products, prices)
            print(f"\nSubtotal:   ${current_subtotal:.2f}")
            
    elif user_choice == 6:
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty! You cannot checkout yet.")
            user_choice = 0
        else:
            print("\n========== RECEIPT ==========")
            
            today_date = datetime.date.today()
            print(f"Date: {today_date.strftime('%m/%d/%Y')}\n")
            
            for item in shopping_cart:
                idx = products.index(item)
                print(f"{item}           ${prices[idx]:.2f}")
                
            final_subtotal = get_subtotal(shopping_cart, products, prices)
            discount_rate = get_discount(final_subtotal)
            amount_saved = final_subtotal * discount_rate
            final_total = final_subtotal - amount_saved
            
            print(f"\nSubtotal:       ${final_subtotal:.2f}")
            print(f"Discount:       {int(discount_rate * 100)}%")
            print(f"Amount Saved:   ${amount_saved:.2f}")
            print(f"\nFinal Total:    ${final_total:.2f}")
            print("\nThank you for shopping!")
            
    else:
        print("Invalid option! Please choose a number between 1 and 6.")