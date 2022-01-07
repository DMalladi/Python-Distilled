# Version-1
nums = [1, 2, 3, 4, 5]
squares1 = []
for num in nums:
    squares1.append(num * num) # [1, 4, 9, 16, 25]

# Version-2 (compact version of version-1 operation)
# AKA list comprehension
squares2 = [num * num for num in nums] # [1, 4, 9, 16, 25]

# Apply a filter on comprehension
squares3 = [num * num for num in nums if num > 1] # [4, 9, 16, 25]

# All variables that are used inside a comprehension are private only

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "MSFT", "shares": 50, "price": 45.67},
    {"name": "HPE", "shares": 75, "price": 34.51},
    {"name": "CAT", "shares": 60, "price": 67.89},
    {"name": "IBM", "shares": 200, "price": 95.25}
]

# collect all names ["IBM", "MSFT", "HPE", "CAT", "IBM"]
names = [port["name"] for port in portfolio]

# collect all names which have shares > 99
names_with_shares_over_99 = [port["name"] 
            for port in portfolio 
                if port["shares"] > 99] # ['IBM', 'IBM]

# collect name & share in a tuple
#[('IBM', 100), ('MSFT', 50), ('HPE', 75), ('CAT', 60), ('IBM', 200)]
name_share = [(port["name"], port["shares"]) 
                for port in portfolio]

# set comprehension
# {"IBM", "MSFT", "HPE", "CAT"} If you notice, you only see one IBM name
names_set = { port["name"] for port in portfolio }

# dictionary comprehension
# {'IBM': 95.25, 'MSFT': 45.67, 'HPE': 34.51, 'CAT': 67.89}
share_prices = {port["name"]: port["price"] for port in portfolio}

# When creating sets and dictionaries, be aware that later entries might 
# overwrite earlier entries

# Within a comprehension, it's not possible to include any sort of exception
# handling. If this is a concern, consider wrapping exceptions with a function
def toint(x):
    try:
        return int(x)
    except ValueError:
        return None

values = ['1', '2', 'n/a', '-3']
values_data = [toint(v) for v in values] # [1, 2, None, -3]
data_without_none_values = [toint(v) 
                                for v in values
                                    if toint(v) is not None] #[1, 2, -3]

# double evaluation of toint(x) in the previous example can be avoided by using
# evaluation assignment operator (:=)
data_without_none_values_2 = [v for x in values if (v:=toint(x)) is not None]