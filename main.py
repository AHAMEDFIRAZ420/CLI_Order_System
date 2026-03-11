import os
from modules.handler import *

def user_manual():
    clear_screen()
    print("====================================================")
    print("     WELCOME TO THE COFFEE SHOP SYSTEM (v1.0)      ")
    print("====================================================")
    print("\nThis system is designed to manage your shop efficiently.")
    print("\nCORE FUNCTIONS:")
    print("1. MENU MANAGEMENT: Add, Update, or Remove drinks.")
    print("   - All data is saved automatically to 'menu.json'.")
    print("   - IDs are re-sequenced automatically when items are removed.")
    
    print("\n2. BILLING TERMINAL: Take customer orders quickly.")
    print("   - Usage: Enter 'ID Quantity' (e.g., 1 2) to add to cart.")
    print("   - Use 'IDr' (e.g., 1r) to remove an item from the cart.")
    print("   - Press 'D' to generate a clean Final Invoice.")
    
    print("\n3. DATA INTEGRITY:")
    print("   - The system handles corrupted files and prevents empty checkouts.")
    print("====================================================")
    
    while True:
        choice = input("\nReady to start the system for your shop? (y/n): ").lower().strip()
        if choice == 'y':
            # Create a flag file so they don't see this every single time
            with open("data/.initialized", "w") as f:
                f.write("System initialized.")
            break
        else:
            print("Please type 'y' to confirm and enter the system.")

def main():
    if not os.path.exists("data/.initialized"):
        user_manual()

    while True:
        print("\n===== Coffee Shop System =====")
        print("1. Open Menu (CRUD)")
        print("2. New Bill (Order)")
        print("3. Exit")
        
        choice = input("\nSelect operation: ")
        
        if choice == '1':
            menu_management_flow()
        elif choice == '2':
            cart_management_flow()
        elif choice == '3':
            print("\nExiting...")
            break
        else:
            print("\nInvalid input, please use numbers 1-3.")
 
if __name__ == "__main__":
    main()