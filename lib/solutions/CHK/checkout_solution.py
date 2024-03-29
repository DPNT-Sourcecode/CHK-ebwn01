def checkout(skus):
    skus = ''.join(sorted(skus))
    skus = skus[::-1]
    # Prices of individual items
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10, 
    }

    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'C': None,
        'D': None,
        'E': [(2, 'B')],
        'F': [(2, 'F')],
    }

    # Count occurrences of each item
    counts = {}
    for item in skus:
        counts[item] = counts.get(item, 0) + 1
    
    total = 0
    # Input validation:
    for item, count in counts.items():
        if item not in prices:
            return -1
        
        price = prices[item]
        offer = offers[item]

        if offer:
            for offer_info in offer:
                if isinstance(offer_info[1], int):  # Normal offer
                    quantity_needed, reduced_price = offer_info
                    discounted_sets = count // quantity_needed 
                    reminder_items = count % quantity_needed
                    total += discounted_sets * reduced_price
                    count = reminder_items
                elif offer_info[1] == 'B' and item == 'E':
                    required_quantity, free_item = offer_info
                    if free_item in counts and counts[free_item] > 0:
                        free_items_to_deduct = min(counts.get('E', 0) // required_quantity, counts[free_item])
                        counts[free_item] -= free_items_to_deduct
                        # Update the count of purchased Es accordingly
                        counts['E'] -= free_items_to_deduct * required_quantity
                elif offer_info[1] == 'F' and item == 'F':
                    print("ssss")
                    required_quantity, free_item = offer_info
                    if free_item in counts and counts[free_item] > 0:
                        free_items_to_deduct = min(counts.get('F', 0) // required_quantity, counts[free_item])
                        counts[free_item] -= free_items_to_deduct
                        counts['F'] -= free_items_to_deduct * required_quantity
            print(counts)
            total += count * price  # Add remaining items at regular price
        else:
            total += count * price

    return total

print(checkout("EEBFF"))  # Output should be 80