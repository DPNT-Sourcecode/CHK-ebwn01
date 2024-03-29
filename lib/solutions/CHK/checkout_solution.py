
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # need to establish a dict for the prices:
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    offers = {
        'A': (3,130),
        'B': (2,45),
        'C': None,
        'D': None
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
            quantity_needed, reduced_price = offer
            discounted_amount = (count // quantity_needed) * reduced_price
            reminder_items = count % quantity_needed
            regular_price = reminder_items * price
            total += discounted_amount + regular_price
        # if we dont have offer
        else:
            total += count * price
    return total

print(checkout("ABCDABCD"))





