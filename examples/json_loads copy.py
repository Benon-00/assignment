## Example

import json

json_str = '{"name": "Bob", "age": 25, "hobbies": ["chess", "reading"]}'
data = json.loads(json_str)
print(data['hobbies'])
