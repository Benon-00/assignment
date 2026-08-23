## Example

import itertools

x = itertools.count(10, 5)

for i in x:
    if i >30:
        break
    print(i)


