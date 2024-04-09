

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    special_offers = {'A': (3, 130), 'B': (2, 45)}

    # Initialize total price
    total_price = 0

    # Count the occurrences of each product
    product_counts = {}
    for product in skus:
        if product not in prices:
            return -1
        product_counts[product] = product_counts.get(product, 0) + 1
    print(product_counts)

    # Calculate the total price considering special offers
    for product, count in product_counts.items():
        price = prices[product]
        if product in special_offers:
            required_count, special_price = special_offers[product]
            special_total = (count // required_count) * special_price
            remaining_count = count % required_count
            total_price += special_total + remaining_count * price
        else:
            total_price += count * price

    return total_price

# Test cases
print(checkout("A"))  # Output: 50
print(checkout("BB"))  # Output: 45
print(checkout("CCC"))  # Output: 60
print(checkout("ABCD"))  # Output: 115
print(checkout("AAABB"))  # Output: 175
print(checkout("E"))  # Output: -1 (Illegal input)



