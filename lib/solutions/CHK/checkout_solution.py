

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': {'price': 50, 'offers': [(3, 130), (5, 200)]},
        'B': {'price': 30, 'offers': [(2, 45)]},
        'C': {'price': 20, 'offers': []},
        'D': {'price': 15, 'offers': []},
        'E': {'price': 40, 'offers': [(2, 'B')]}
    }

    # Initialize counts for each product
    product_counts = {}
    for item in skus:
        product_counts[item] = product_counts.get(item, 0) + 1

    total_price = 0

    # Iterate over each product and apply discounts
    for product, count in product_counts.items():
        if product not in price_table:
            return -1  # Illegal input

        price = price_table[product]['price']
        offers = price_table[product]['offers']

        # Check if there are any special offers for this product
        for offer in offers:
            offer_quantity, offer_item = offer
            if offer_quantity <= count:
                if offer_item in product_counts:
                    offer_count = min(product_counts[offer_item], count // offer_quantity)
                    total_price += offer_count * price
                    count -= offer_count * offer_quantity

        total_price += count * price

    return total_price

# Example usage:
basket = "AAAAAAAAABBEE"
print("Total price:", checkout(basket))  # Output: 210


# Test cases
print(checkout("A"))  # Output: 50
print(checkout("BB"))  # Output: 45
print(checkout("CCC"))  # Output: 60
print(checkout("ABCD"))  # Output: 115
print(checkout("AAABB"))  # Output: 175
print(checkout("E"))  # Output: -1 (Illegal input)




