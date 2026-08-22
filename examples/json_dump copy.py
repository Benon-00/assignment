## Example

import json

data = {'name': 'Alice', 'age': 30, 'active': True}
result = json.dump(data, indent=2, sort_keys=False)
print(result)


