
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # need to establish a dict for the prices:
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    offers = {
        'A': [(5,200), (3,130)],
        'B': [(2,45)],
        'C': None,
        'D': None,
        'E': [(2,"E")]
    }

    # iterate through input string and count number of each unique sku
    counts = {}
    for x in set(skus):
        counts[x] = skus.count(x)
    
    total = 0
    # input validation:
    for x, count in counts.items():
        if x not in prices:
            return -1
        
        # get price
        price = prices[x]
        # get special offer if any
        offer = offers[x]

        if offer:
            for offer_info in offer:
                if isinstance(offer_info[1], int):
                    quantity_needed, reduced_price = offer_info
                    discounted_sets = (count // quantity_needed)
                    reminder_items = count % quantity_needed
                    total += discounted_sets * reduced_price
                    count = reminder_items
                else:
                    required_quantity, free_item = offer_info
                    if free_item in counts and counts[free_item] >= count //required_quantity:
                        free_items_to_deduct = count // required_quantity
                        counts[free_item] -= free_items_to_deduct
                        count -= free_items_to_deduct * required_quantity
            total += count * prices[x]
        # if we dont have offer
        else:
            total += count * price
    return total

print(checkout("EEB"))



