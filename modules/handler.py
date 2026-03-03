from modules.menu import MenuItemManager
from modules.cart import CartManager

def menu_management_flow():
    manager = MenuItemManager()
    while True:
        print("\n--- Menu Settings ---")
        print("1. Add New Item")
        print("2. Remove Item")
        print("3. View Menu")
        print("4. Save and Exit to Main")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter price: "))
                manager.add_item(name, price)
            except ValueError:
                print("Invalid input. Price must be a number.") # 
        elif choice == '2':
            manager.list_items()
            item_id = input("Enter ID to remove: ")
            manager.remove_item(item_id)
        elif choice == '3':
            manager.list_items()
        elif choice == '4':
            manager.save_menu()
            break
        else:
            print("Invalid selection. Please try again.")

def cart_management_flow():
    menu_mgr = MenuItemManager()
    cart = CartManager()
    menu = menu_mgr.menu_data

    while True:
        print("\n" + "="*40)
        print(f"{'BILLING TERMINAL':^40}")
        print("="*40)

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
            print("\n" + "="*40)
            print(f"{'FINAL INVOICE':^40}")
            print("="*40)
            cart.display_cart()
            print(f"TOTAL PAID: ${cart.get_total():.2f}")
            print("="*40)
            input("\nPress Enter to return to main menu...")
            break

        elif action.endswith('r'):
            cart.remove_item(action[:-1])
        
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
