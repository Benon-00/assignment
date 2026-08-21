## Example

import csv

with open('IBM Attrition.csv', newline='') as f:
    reader = csv.reader(f)
    for column in reader:
        print(column)

