
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
        'A': [(5,200), (1,130)],
        'B': [(2,45)],
        'C': None,
        'D': None,
        'E': [(2,'B')]
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
            for various_offer in offer:
                if isinstance(various_offer[1], int):  # noqa: E721
                    quantity_needed, reduced_price = various_offer
                    discounted_amount = (count // quantity_needed) * reduced_price
                    reminder_items = count % quantity_needed
                    regular_price = reminder_items * price
                    count = reminder_items
                    total += discounted_amount + regular_price
                else: 
                    required_amount, free_item = various_offer
                    if free_item in counts and counts[free_item] >= count // required_amount:
                        to_deduct = count // required_amount
                        counts[free_item] -= to_deduct
                        count -= to_deduct * required_amount
            total += count * prices[x]
        else:
            total += count * price
    return total

print(checkout("ABCDABCD"))
