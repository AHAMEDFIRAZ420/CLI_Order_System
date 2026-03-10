from modules.menu import MenuItemManager
from modules.cart import CartManager
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_management_flow():
    manager = MenuItemManager()
    while True:
        print("\n--- Menu Settings ---")
        print("1. Add New Item")
        print("2. Remove Item")
        print("3. View Menu")
        print("4. Save and Exit to Main")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            name = input("\nEnter item name: ")
            try:
                price = float(input("Enter price: "))
                manager.add_item(name, price)
            except ValueError:
                print("Invalid input. Price must be a number.") # 
        elif choice == '2':
            manager.list_items()
            item_id = input("\nEnter ID to remove: ")
            manager.remove_item(item_id)
        elif choice == '3':
            manager.list_items()
        elif choice == '4':
            manager.save_menu()
            break
        else:
            print("\nInvalid selection. Please try again.")

def cart_management_flow():
    menu_mgr = MenuItemManager()
    cart = CartManager()
    menu = menu_mgr.menu_data

    while True:
        clear_screen()
        print("\n" + "="*44 + f"\n{'BILLING TERMINAL':^44}" + "\n" + "="*44)

        menu_mgr.list_items() # Shows dynamic menu 
        cart.display_cart()

        print("\nOptions: [ID Qty] to Add/Update | [ID]r to Remove | 'D' for Done | 'C' to Cancel")
        action = input("Order >> ").strip().lower()

        if action == 'c':
            cart.clear_cart()
            print("Order cancelled.")
            break
        
        elif action == 'd':
            if not cart.items:
                print("\n[!] Cannot checkout an empty cart.")
                continue
            
            # Final Invoice display before exiting loop
            clear_screen()
            print("\n" + "="*44 + f"\n{'FINAL INVOICE':^44}\n" + "="*44)

            cart.display_cart(show_total=False)

            print(f"{'GRAND TOTAL:':<30} ${cart.get_total():>8.2f}\n" + "="*44)
            input("\nOrder Confirmed. Press Enter to return to main menu...\n")
            break

        elif action.endswith('r'):
            item_id = action[:-1]
            if item_id in cart.items:
                cart.remove_item(item_id)
            else:
                input(f"\n[!] Item ID {item_id} is not in your cart. Press Enter...")
        
        else:
            try:
                parts = action.split()
                if len(parts) == 2:
                    item_id, qty = parts[0], int(parts[1])
                    if item_id in menu:
                        # Logic to add/update item in cart [cite: 2]
                        cart.update_or_add(item_id, menu[item_id]['name'], menu[item_id]['price'], qty)
                    else:
                        print(f"Error: Item ID {item_id} not found.")
                else:
                    print("Usage: Enter [ID] [Quantity] (e.g., 1 2)")
            except ValueError:
                print("Error: Quantity must be a number.")
