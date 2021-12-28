portfolio = [
    ("ACME", 50, 92.34),
    ("IBM", 75, 102.25),
    ("PHP", 40, 74.50),
    ("IBM", 50, 124.75)
]

total_shares = { share[0]: 0 for share in portfolio }
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(total_shares["IBM"])