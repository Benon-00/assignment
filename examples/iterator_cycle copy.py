## Example

import itertools

x = itertools.cycle(['A', 'B', 'C'])
counter = 0

for i in x:
    if counter >= 7:
        break
    print(i)
    counter += 1

