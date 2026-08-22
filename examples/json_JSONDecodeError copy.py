## Example

import json

bad_json = '{"name": "Aice", "age": }' #invalid JSON (missing value)
try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e.msg} at line {e.lineno}, column {e.colno}")
