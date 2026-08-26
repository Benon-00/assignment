## Example

import string as str

t = str.Template('Hello, $name! Yo have $count new messages.')
result = t.substitute(name='Alice', count=3)
print(result)

