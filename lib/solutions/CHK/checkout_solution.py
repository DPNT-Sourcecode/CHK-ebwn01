

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table = {
    'A': {'price': 50, 'offers': [(5, 200), (3, 130)]},
    'B': {'price': 30, 'offers': [(2, 45)]},
    'C': {'price': 20, 'offers': []},
    'D': {'price': 15, 'offers': []},
    'E': {'price': 40, 'offers': [(2, 'B')]},
    'F': {'price': 10, 'offers': [(2, 'F')]},
    'G': {'price': 20, 'offers': []},
    'H': {'price': 10, 'offers': [(10, 80), (5, 45)]},
    'I': {'price': 35, 'offers': []},
    'J': {'price': 60, 'offers': []},
    'K': {'price': 70, 'offers': [(2, 120)]},
    'L': {'price': 90, 'offers': []},
    'M': {'price': 15, 'offers': []},
    'N': {'price': 40, 'offers': [(3, 'M')]},
    'O': {'price': 10, 'offers': []},
    'P': {'price': 50, 'offers': [(5, 200)]},
    'Q': {'price': 30, 'offers': [(3, 80)]},
    'R': {'price': 50, 'offers': [(3, 'Q')]},
    'S': {'price': 20, 'offers': [(3, 45, ['S', 'T', 'X', 'Y', 'Z'])]},
    'T': {'price': 20, 'offers': [(3, 45, ['S', 'T', 'X', 'Y', 'Z'])]},
    'U': {'price': 40, 'offers': [(3, 'U')]},
    'V': {'price': 50, 'offers': [(3, 130), (2, 90)]},
    'W': {'price': 20, 'offers': []},
    'X': {'price': 17, 'offers': [(3, 45, ['S', 'T', 'X', 'Y', 'Z'])]},
    'Y': {'price': 20, 'offers': [(3, 45, ['S', 'T', 'X', 'Y', 'Z'])]},
    'Z': {'price': 21, 'offers': [(3, 45, ['S', 'T', 'X', 'Y', 'Z'])]}
}



    # reverse skus:
    sorted_reversed_skus = ''.join(sorted(skus, reverse=True))

    # Print the sorted and reversed string
    # print(sorted_reversed_skus)
     
    # Initialize counts for each product
    product_counts = {}
    for item in sorted_reversed_skus:
        product_counts[item] = product_counts.get(item, 0) + 1
    print(product_counts)
    total_price = 0
    # print(product_counts)
    # Iterate over each product and apply discounts
    for product, count in product_counts.items():
        if product not in price_table:
            return -1  # Illegal input

        price = price_table[product]['price']
        offers = price_table[product]['offers']

        # Check if there are any special offers for this product
        for offer in offers:
            if len(offer) == 3:
                offer_quantity, offer_price, offered_items = offer
                num_of_eligible_items = 0
                for prod in offered_items:
                    if prod in product_counts:
                         num_of_eligible_items += product_counts[prod]
                offer_count = num_of_eligible_items // offer_quantity
                print("offer can be applied: ", offer_count)
                total_price += offer_count * offer_price
                print("total price to add ", total_price)
                # # set current product to 0
                # count -= offer_count * offer_quantity
                for prod in offered_items:
                    if prod in product_counts:
                        product_counts[prod] -= offer_count * offer_quantity
                print(product_counts)
                count = product_counts[product]
                # print(product_counts)
                # break
            else:
                offer_quantity, offer_item = offer
                if offer_quantity <= count:
                    if isinstance(offer_item, int):
                        offer_count =  count // offer_quantity
                        total_price += offer_count * offer_item
                        count -= offer_count * offer_quantity
                    else:
                        if offer_item == product and count >= offer_quantity + 1:
                            increased = 0
                            toRemove = 0
                            for i in range(count):
                                increased +=1
                                if increased == offer_quantity:
                                    toRemove +=1
                                    increased = -1
                            # print(toRemove)
                            # print("the offer item is F")
                            # offer_count =  count // offer_quantity
                            # print("this offer can be applied: ", offer_count)
                            # print(f"the count of {product} was {count}")
                            count -= toRemove
                            # print(f"the count of {product} now is {count}")
                        else :
                            if offer_item in product_counts: # if the offer item exists in our SKU 
                                offer_count =  count // offer_quantity
                                product_counts[offer_item] -= offer_count
        print("Adding : ", count * price)                        
        total_price += count * price

    return total_price

# # Example usage:
# basket = "AAAAAAAAABBEEEFFF"
# print("Total price:", checkout(basket))  # Output: 530


# Test cases
print(checkout("SSSX"))  # Output: 50
# print(checkout("FFF"))  # Output: 45
# print(checkout("FFFF"))  # Output: 60
# print(checkout("ABCD"))  # Output: 115
# print(checkout("AAABB"))  # Output: 175
# print(checkout("E"))  # Output: -1 (Illegal input)

