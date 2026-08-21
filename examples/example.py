import csv

csv.register_dialect('pipes', delimiter='|', quoting=csv.QUOTE_MINIMAL)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='pipes')
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])