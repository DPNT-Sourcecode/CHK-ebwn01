

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
        'A': {'price': 50, 'offers': [(5, 200), (3, 130)]},
        'B': {'price': 30, 'offers': [(2, 45)]},
        'C': {'price': 20, 'offers': []},
        'D': {'price': 15, 'offers': []},
        'E': {'price': 40, 'offers': [(2, 'B')]}
    }

    # reverse skus:
    sorted_reversed_skus = ''.join(sorted(skus, reverse=True))

    # Print the sorted and reversed string
    print(sorted_reversed_skus)
     
    # Initialize counts for each product
    product_counts = {}
    for item in sorted_reversed_skus:
        product_counts[item] = product_counts.get(item, 0) + 1

    total_price = 0
    print(product_counts)
    # Iterate over each product and apply discounts
    for product, count in product_counts.items():
        if product not in price_table:
            return -1  # Illegal input

        price = price_table[product]['price']
        offers = price_table[product]['offers']

        # Check if there are any special offers for this product
        for offer in offers:
            offer_quantity, offer_item = offer
            print("offer item is: ", offer_item)
            if offer_quantity <= count:
                if isinstance(offer_item, int):
                    offer_count =  count // offer_quantity
                    total_price += offer_count * offer_item
                    count -= offer_count * offer_quantity
                    print("its a number")
                else:
                    print("the offer is an item!")
                    if offer_item in product_counts: # if the offer item exists in our SKU 
                        offer_count =  count // offer_quantity
                        product_counts[offer_item] -= offer_count
                        print("its a product")
        total_price += count * price

    return total_price

# Example usage:
basket = "AAAAAAAAABBEEE"
print("Total price:", checkout(basket))  # Output: 530


# # Test cases
# print(checkout("A"))  # Output: 50
# print(checkout("BB"))  # Output: 45
# print(checkout("CCC"))  # Output: 60
# print(checkout("ABCD"))  # Output: 115
# print(checkout("AAABB"))  # Output: 175
# print(checkout("E"))  # Output: -1 (Illegal input)

