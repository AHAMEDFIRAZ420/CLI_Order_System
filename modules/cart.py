
class CartManager:
    def __init__(self):
        self.items = {}

    def update_or_add(self, item_id, name, price, qty):
        if qty <= 0:
            self.remove_item(item_id)
        else:
            self.items[item_id] = {
                'name': name, 'price': price, 'qty': qty, 'subtotal': price * qty
            }
    
    def remove_item(self, item_id):
        """Removes an item from the cart[cite: 1]."""
        if item_id in self.items:
            del self.items[item_id]

    def clear_cart(self):
        """Empties the cart for a cancelled order."""
        self.items = {}

    def get_total(self):
        """Calculates total strictly on item prices[cite: 1]."""
        return sum(item['subtotal'] for item in self.items.values())

    def display_cart(self):
        """Prints the current cart state in the requested format[cite: 6]."""
        if not self.items:
            print("=" * 40)
            print("\n[ Cart is currently empty ]")
            return

        print("\n| ID | Product          | Qty | Subtotal |")
        print("-" * 42)
        for uid, info in self.items.items():
            print(f"| {uid:<2} | {info['name']:<16} | {info['qty']:<3} | ${info['subtotal']:>8.2f} |")
        print("-" * 42)
        print(f"Running Total: ${self.get_total():.2f}")



# import json
# import os
# from typing import Dict, Any

# class CartManager:
#     """
#     Handles customer transaction state. 
#     Integrates with MenuItemManager's data structure for validation.
#     """
#     def __init__(self, filepath: str = 'data/menu.json'):
#         self.filepath = filepath
#         self.cart: Dict[str, int] = {}  # Format: { item_id: quantity }

#     def _get_latest_menu(self) -> Dict[str, Any]:
#         """Reads the menu file to ensure we have the most recent items/prices."""
#         if not os.path.exists(self.filepath):
#             return {}
#         try:
#             with open(self.filepath, 'r') as f:
#                 return json.load(f)
#         except (json.JSONDecodeError, IOError):
#             return {}

#     def update_cart(self, item_id: str, quantity: int) -> dict:
#         """
#         - Quantity > 0: Adds/Updates item.
#         - Quantity = 0: Removes specific item.
#         """
#         menu = self._get_latest_menu()

#         # 1. Validation: Item Existence
#         if item_id not in menu:
#             return {"status": "error", "message": f"ID {item_id} NOT FOUND"}

#         item_name = menu[item_id]['name']

#         # 2. Logic: Removal (The '0' Rule)
#         if quantity == 0:
#             if item_id in self.cart:
#                 del self.cart[item_id]
#                 return {"status": "success", "message": f"REMOVED: {item_name}"}
#             return {"status": "info", "message": f"NOT_IN_CART: {item_name}"}

#         # 3. Logic: Update/Add
#         if quantity > 0:
#             self.cart[item_id] = quantity
#             return {"status": "success", "message": f"UPDATED: {item_name} x{quantity}"}

#         return {"status": "error", "message": "INVALID_QUANTITY"}

#     def calculate_total(self) -> float:
#         """Computes the total based on current menu prices."""
#         menu = self._get_latest_menu()
#         return sum(menu[id]['price'] * qty for id, qty in self.cart.items() if id in menu)