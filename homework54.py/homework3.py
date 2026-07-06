from functools import reduce
bob = ["Timmy","Jeremy"]
def long(x,y):
    if len(x) > len(y):
        print(f"{x} is the longest word")
    else:
        print(f"{y} is the longest word")
result = reduce(long,bob)
print(result)