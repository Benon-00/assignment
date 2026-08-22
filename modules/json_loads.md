# Function 3

## Function Name

```python
json.loads()
```

---

## Purpose

Describe what the function does.

_**Parses a JSON-formatted string (or bytes) and converts it into a corresponding Python object (dict, list, etc)**_


## Syntax

```python
json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, **kw)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|s   | Yes    |-     | str/bytes/bytearray |The JSON document to parse|
|object_hook | No |None | function | Function to transform decoded JSON objects (dicts)|
|parse_float | No | float | functions | Function used to parse JSON float literals |
|parse_int | No | int | function | Function used to parse JSON int literals|
|cls   | No | JSONDecoder | class | Custom JSON decoder class |


> **Questions to answer**
>
> - Which parameters are required?
_**s is required**_
> - Which parameters are optional?
_**object_hook; parse_float; parse_int; cls; are all optional**_
> - What happens if you omit an optional parameter?
_**standard decoding is used, JSON objects become plain dicts, numbers become native Python int/float**_
> - What default value is used?
_**parse_float=float, parse_int=int, clas=json.JSONDecoder**_

---

## Return Value

What does the function return?

*A Python object, typically a dict or list, but can be str, int, float, ool or None, depending on the JSON input**

## Example

import json

json_str = '{"name": "Bob", "age": 25, "hobbies": ["chess", "reading"]}'
data = json.loads(json_str)
print(data['hobbies'])

## Expected Output

['chess', 'reading']

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**now i understand the working of json file**
