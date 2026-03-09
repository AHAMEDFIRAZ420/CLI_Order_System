
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
        # Removes an item from the cart.
        if item_id in self.items:
            del self.items[item_id]

    def clear_cart(self):
        # Empties the cart for a cancelled order.
        self.items = {}

    def get_total(self):
        # Calculates total strictly on item prices.
        return sum(item['subtotal'] for item in self.items.values())

    def display_cart(self, show_total=True, label = "Running Total"):
        # Prints the current cart state in the requested format.
        if not self.items:
            print("\n--- Current Order ---\n" + f"\n{'[EMPTY]':^44}\n" + "-"*44)
            return

        print("\n| ID | Product          | Qty | Subtotal  |")
        print("-" * 44)
        
        for uid, info in self.items.items():
            print(f"| {uid:<2} | {info['name']:<16} | {info['qty']:<3} | ${info['subtotal']:>8.2f} |")
        print("-" * 44)

        if show_total:
            print(f"{label}: ${self.get_total():.2f}")