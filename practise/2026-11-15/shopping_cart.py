"""Task 1 — Shopping cart (Lists).

Do these steps, printing the cart after EACH step:
1. append
2. insert at index 1
3. pop
4. remove

Run it with:
    python3 shopping_cart.py
"""

# Start with a small cart
cart = ["milk", "bread"]
print("Start:", cart)

# 1. append — adds an item at the END of the list
cart.append("eggs")
print("After append('eggs'):", cart)

# 2. insert at index 1 — puts an item at position 1,
#    everything from there moves one place to the right
cart.insert(1, "cheese")
print("After insert(1, 'cheese'):", cart)

# 3. pop — removes the LAST item and returns it
removed_item = cart.pop()
print("Popped item:", removed_item)
print("After pop():", cart)

# 4. remove — removes the FIRST item with this value
cart.remove("bread")
print("After remove('bread'):", cart)

print("Final cart:", cart)
