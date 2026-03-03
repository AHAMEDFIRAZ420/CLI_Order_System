
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
        # Removes an item from the cart[cite: 1].
        if item_id in self.items:
            del self.items[item_id]

    def clear_cart(self):
        # Empties the cart for a cancelled order.
        self.items = {}

    def get_total(self):
        # Calculates total strictly on item prices[cite: 1].
        return sum(item['subtotal'] for item in self.items.values())

    def display_cart(self):
        # Prints the current cart state in the requested format[cite: 6].
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