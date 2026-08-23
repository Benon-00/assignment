## Example

import itertools

x = itertools.chain(['a', 'b',], [1,2,3], (True, False))

for item in x:
    print(item)


