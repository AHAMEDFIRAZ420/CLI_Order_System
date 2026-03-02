
import json
import os
from typing import Dict, Any, Union

class CartManager:
    """
    Manages the customer shopping cart logic, including item validation,
    quantity updates, and specific item removal based on ID codes.
    """

    def __init__(self, filepath: str = 'data/menu.json'):
        self.filepath = filepath
        self.menu = self._load_menu_data()
        self.cart: Dict[str, int] = {}  # Store as {item_id: quantity}

    def _load_menu_data(self) -> Dict[str, Any]:
        """Loads and returns the menu configuration from a JSON source."""
        if not os.path.exists(self.filepath):
            # In an enterprise app, you might log this error to a file
            return {}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def update_item_quantity(self, item_id: str, quantity: int) -> Dict[str, Union[bool, str]]:
        """
        Updates the quantity of a specific item in the cart.
        If quantity is set to 0, the item is removed from the record.
        """
        # 1. Validation: Does the item exist in the master menu?
        if item_id not in self.menu:
            return {"success": False, "message": f"INVALID_CODE: {item_id} not found in system."}

        item_name = self.menu[item_id]['name']

        # 2. Logic: Handle specific item removal
        if quantity == 0:
            if item_id in self.cart:
                del self.cart[item_id]
                return {"success": True, "message": f"REMOVED: {item_name} cleared from session."}
            return {"success": True, "message": f"NO_ACTION: {item_name} was not in cart."}

        # 3. Logic: Handle addition/modification
        if quantity > 0:
            self.cart[item_id] = quantity
            return {"success": True, "message": f"UPDATED: {item_name} quantity set to {quantity}."}

        return {"success": False, "message": "ERROR: Quantity must be a non-negative integer."}

    def get_cart_summary(self) -> Dict[str, Any]:
        """
        Calculates and returns a detailed summary of the current cart state.
        """
        items_list = []
        grand_total = 0.0

        for item_id, qty in self.cart.items():
            unit_price = self.menu[item_id]['price']
            subtotal = unit_price * qty
            items_list.append({
                "id": item_id,
                "name": self.menu[item_id]['name'],
                "quantity": qty,
                "subtotal": subtotal
            })
            grand_total += subtotal

        return {
            "items": items_list,
            "grand_total": round(grand_total, 2),
            "item_count": len(items_list)
        }