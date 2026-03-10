# This module handles the CRUD operations for the menu.json file. 
# It ensures that if a user enters a non-numeric price or an invalid ID, the program guides them back rather than crashing

import json
import os

class MenuItemManager:
    def __init__(self, filepath='data/menu.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        self.menu_data = self._load_menu()

    def _load_menu(self):
        # Loads menu from JSON
        if not os.path.exists(self.filepath):
            print(f"\n[!] Warning: Menu file '{self.filepath}' not found.")
            choice = input("Would you like to create a new menu list? (yes/no): ").strip().lower()
            if choice in ['yes','y']:
                return {}
            else:
                print("No menu loaded. System may have limited functionality.")
                return {}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("\n[!] Error: Menu file is corrupted. Starting with an empty list.")
            return {}

    def save_menu(self):
        # Persists the current menu_data to the JSON file.
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.menu_data, f, indent=4)
                print("\nMenu saved successfully!")
        except IOError as e:
            print(f"\nFailed to save menu: {e}")

    def add_item(self, name, price):
        """Prevents duplicates and handles price updates."""
        existing_id = None
        # Check for item name duplicates (Case-insensitive)
        for uid, details in self.menu_data.items():
            if details['name'].lower() == name.lower():
                existing_id = uid
                break

        if existing_id:
            print(f"\n[!] Item '{name}' is already present at ID {existing_id}.")
            update_choice = input(f"Update price to ${price:.2f}? (y/n): ").lower()
            if update_choice == 'y':
                self.menu_data[existing_id]['price'] = float(price)
                self.save_menu() # Auto-save on update
                print("Item updated.")
            return
        
        # Adds a new item and auto-saves
        new_id = str(len(self.menu_data) + 1)
        self.menu_data[new_id] = {"name": name.capitalize(), "price": float(price)}
        self.save_menu() 
        print(f"\nAdded: {name.capitalize()} (${price:.2f})")
        
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
            for i, details in enumerate(self.menu_data.values(), start=1):
                new_menu[str(i)] = details
                
            self.menu_data = new_menu
            self.save_menu()
            print(f"\nSuccessfully removed '{removed_name}'. Menu IDs re-sequenced.")
        else:
            print(f"\nError: ID {item_id} not found.")

    def list_items(self):
        # Displays the menu for the user[cite: 1, 6].
        if not self.menu_data:
            print("\n[ Menu is currently empty ]")
            return
            
        print("\n--- Current Coffee Menu ---")
        for idx, details in self.menu_data.items():
            print(f"{idx}. {details['name']:<15} - ${details['price']:.2f}")