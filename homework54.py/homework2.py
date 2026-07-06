employees = [
    {"name": "Alice", "salary": 75000, "department": "IT"},
    {"name": "Bob", "salary": 55000, "department": "HR"},
    {"name": "Charlie", "salary": 90000, "department": "IT"},
    {"name": "David", "salary": 45000, "department": "Finance"},
    {"name": "Esha", "salary": 62000, "department": "IT"}
]
def check(tech):
    return tech["salary"] > 60000 and tech["department"] == "IT"
result = list(filter(check,employees))
print(result)