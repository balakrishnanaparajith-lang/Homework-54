from functools import reduce

products = [
    {"price": 1200, "quantity": 2, "discount": 10},
    {"price": 500, "quantity": 5, "discount": 20},
    {"price": 3000, "quantity": 1, "discount": 5}
]

def calc(p):
    price_after = p["price"] * (1 - p["discount"] / 100)
    return price_after * p["quantity"]

mapped = list(map(calc, products))

total = reduce(lambda a, b: a + b, mapped)

print(total)
