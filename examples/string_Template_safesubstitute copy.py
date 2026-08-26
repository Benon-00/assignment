## Example

import string as str

t = str.Template('Hello, $name! Your balance is $${amount}.')
result = t.safe_substitute(name='Bob')
print(result)

