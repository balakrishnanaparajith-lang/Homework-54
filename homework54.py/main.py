numbers = [2,4,7,13,15]
def transform(n):
    if n % 2 == 0:
        return n**2
    else:
        return n**3
result = list(map(transform, numbers))
print(result)
