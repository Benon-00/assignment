## Example

import string as str

t = str.Template("Dear $name, your order #$order_id has shipped to $name's address.")
result = t.get_identifiers()
print(result)


