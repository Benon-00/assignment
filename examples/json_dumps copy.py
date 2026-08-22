## Example

import json

data = {'name': 'Alice', 'age': 30, 'active': True}
result = json.dumps(data, indent=2, sort_keys=False)
print(result)

