
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
        'B': (2,45)
    }

    # iterate through input string and count number of each unique sku
    counts = {}
    for x in set(skus):
        counts[x] = skus.count(x)
    print(counts)
    
checkout("ABCABB")

