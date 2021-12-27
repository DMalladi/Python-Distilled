# pcost.py

# Reads input lines of the form 'Name, Shares, Price"
# e.g. SYM, 123, 456.78

# sys module is used to obtain command-line-arguments
# which is found in sys.argv
import sys


if len(sys.argv) != 2:
    # sys.arv[0] is a running program file name => pcost.py
    raise SystemExit(f"Usage: {sys.argv[0]} filename.")

rows = []
filename = sys.argv[1]
with open(filename, 'rt') as file:
    for line in file:
        rows.append(line.split(','))

share_value = [ int(row[1]) * float(row[2]) for row in rows ]
total = sum(share_value)
print(f"Total cost: {total:0.2f}")