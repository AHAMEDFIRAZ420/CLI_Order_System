from modules.handler import menu_management_flow, cart_management_flow

def main():
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