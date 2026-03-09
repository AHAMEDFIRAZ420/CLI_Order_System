# This module handles the CRUD operations for the menu.json file. 
# It ensures that if a user enters a non-numeric price or an invalid ID, the program guides them back rather than crashing

import json
import os

class MenuItemManager:
    def __init__(self, filepath='data/menu.json'):
        self.filepath = filepath
        self.menu_data = self._load_menu()

    def _load_menu(self):
        # Loads menu from JSON
        if not os.path.exists(self.filepath):
            print(f"\n[!] Warning: Menu file '{self.filepath}' not found.")
            choice = input("Would you like to create a new menu list? (yes/no): ").strip().lower()
            if choice == 'yes' or 'y':
                return {}
            else:
                print("No menu loaded. System may have limited functionality.")
                return {}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_menu(self):
        # Persists the current menu_data to the JSON file.
        with open(self.filepath, 'w') as f:
            json.dump(self.menu_data, f, indent=4)
        print("\nMenu saved successfully!")

    def add_item(self, name, price):
        existing_id = None
        for uid, details in self.menu_data.items():
            if details['name'].lower() == name.lower():
                existing_id = uid
                break

        if existing_id:
            print(f"\n[!] Item '{name}' is already present at ID {existing_id}.")
            update_choice = input(f"Would you like to update its price to ${price:.2f}? (y/n): ").lower()
            if update_choice == 'y':
                self.menu_data[existing_id]['price'] = float(price)
                print("Item updated.")
            return
        
        # Adds a new coffee drink to the dynamic list.
        new_id = str(len(self.menu_data) + 1)
        self.menu_data[new_id] = {"name": name, "price": float(price)}
        print(f"\nAdded: {name} (₹{price:.2f})")

    def remove_item(self, item_id):
        if item_id in self.menu_data:
            removed_name = self.menu_data[item_id]['name']
            del self.menu_data[item_id]
            
            # Re-index the remaining items
            new_menu = {}
            for i, (old_id, details) in enumerate(self.menu_data.items(), start=1):
                new_menu[str(i)] = details
                
            self.menu_data = new_menu
            print(f"\nSuccessfully removed '{removed_name}'. Menu IDs re-sequenced.")
        else:
            print(f"\nError: ID {item_id} not found.")

    def list_items(self):
        # Displays the menu for the user.
        print("\n--- Current Coffee Menu ---")
        for idx, details in self.menu_data.items():
            print(f"{idx}. {details['name']} - ${details['price']:.2f}")