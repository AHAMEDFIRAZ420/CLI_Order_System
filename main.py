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

"""Write your main logic execution within this function cart_management_flow()"""

def cart_management_flow():
    cart=CartManager
    while:
    

def main():
    while True:
        print("\n===== Coffee Shop System =====")
        print("1. Open Menu (CRUD)")
        print("2. New Bill (Order)")
        print("3. Exit")
        
        choice = input("Select operation: ")
        
        if choice == '1':
            menu_management_flow()
        elif choice == '2':
            print("Billing logic coming soon in cart.py...")
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input, please use numbers 1-3.")
 

if __name__ == "__main__":
    main()