import json
import os
from typing import Dict, Any

class CartManager:
    """
    Handles customer transaction state. 
    Integrates with MenuItemManager's data structure for validation.
    """
    def __init__(self, filepath: str = 'data/menu.json'):
        self.filepath = filepath
        self.cart: Dict[str, int] = {}  # Format: { item_id: quantity }

    def _get_latest_menu(self) -> Dict[str, Any]:
        """Reads the menu file to ensure we have the most recent items/prices."""
        if not os.path.exists(self.filepath):
            return {}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def update_cart(self, item_id: str, quantity: int) -> dict:
        """
        - Quantity > 0: Adds/Updates item.
        - Quantity = 0: Removes specific item.
        """
        menu = self._get_latest_menu()

        # 1. Validation: Item Existence
        if item_id not in menu:
            return {"status": "error", "message": f"ID {item_id} NOT FOUND"}

        item_name = menu[item_id]['name']

        # 2. Logic: Removal (The '0' Rule)
        if quantity == 0:
            if item_id in self.cart:
                del self.cart[item_id]
                return {"status": "success", "message": f"REMOVED: {item_name}"}
            return {"status": "info", "message": f"NOT_IN_CART: {item_name}"}

        # 3. Logic: Update/Add
        if quantity > 0:
            self.cart[item_id] = quantity
            return {"status": "success", "message": f"UPDATED: {item_name} x{quantity}"}

        return {"status": "error", "message": "INVALID_QUANTITY"}

    def calculate_total(self) -> float:
        """Computes the total based on current menu prices."""
        menu = self._get_latest_menu()
        return sum(menu[id]['price'] * qty for id, qty in self.cart.items() if id in menu)