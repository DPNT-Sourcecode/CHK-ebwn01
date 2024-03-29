
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
        'E': [(2,"B")]
    }

    # iterate through input string and count number of each unique sku
    counts = {}
    for x in set(skus):
        counts[x] = skus.count(x)
    
    total = 0
    # input validation:
    for item, count in counts.items():
        if item not in prices:
            return -1
        
        price = prices[item]
        offer = offers[item]

        if offer:
            for offer_info in offer:
                if isinstance(offer_info[1], str):
                    quantity_needed, free_item = offer_info
                    if free_item in counts and counts[free_item] > 0:
                        amount_to_remove = min(counts[free_item], count // quantity_needed)
                        counts[free_item] -= amount_to_remove
                else:
                    quantity_needed, reduced_price = offer_info
                    discounted_sets = (count // quantity_needed) 
                    reminder_items = count % quantity_needed
                    total += discounted_sets * reduced_price
                    count = reminder_items
            total += count * price
        # if we dont have offer
        else:
            total += count * price
    return total

print(checkout("EEB"))






