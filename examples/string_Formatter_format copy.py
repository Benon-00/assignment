## Example

import string as str

fmt = str.Formatter()
result = fmt.format('{0} scored {1} points', 'Alice', 42)
print(result)

