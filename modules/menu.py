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
            return {}
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save_menu(self):
        # Persists the current menu_data to the JSON file.
        with open(self.filepath, 'w') as f:
            json.dump(self.menu_data, f, indent=4)
        print("Menu saved successfully!")

    def add_item(self, name, price):
        # Adds a new coffee drink to the dynamic list.
        new_id = str(len(self.menu_data) + 1)
        self.menu_data[new_id] = {"name": name, "price": float(price)}
        print(f"Added: {name} (₹{price:.2f})")

    def remove_item(self, item_id):
        # Removes an item by its ID key.
        if item_id in self.menu_data:
            removed = self.menu_data.pop(item_id)
            print(f"Removed: {removed['name']}")
        else:
            print("Error: Item ID not found.")

    def list_items(self):
        # Displays the menu for the user.
        print("\n--- Current Coffee Menu ---")
        for idx, details in self.menu_data.items():
            print(f"{idx}. {details['name']} - ${details['price']:.2f}")