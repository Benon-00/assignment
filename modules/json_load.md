# Function 4

## Function Name

```python
json.load()
```

---

## Purpose

Describe what the function does.

_**Reads JSON data directly from an open file-like object and converts it into a Python object (the file-based counterpart to loads())**_


## Syntax

```python
json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, **kw)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|fp   | Yes    |-     | file-like object (supports .read()) | Source containing JSON text |
|object_hook | No |None | function | Function to transform decoded JSON objects (dicts)|
|parse_float | No | float | functions | Function used to parse JSON float literals |
|parse_int | No | int | function | Function used to parse JSON int literals|
|cls   | No | JSONDecoder | class | Custom JSON decoder class |


> **Questions to answer**
>
> - Which parameters are required?
_**fp is required**_
> - Which parameters are optional?
_**object_hook; parse_float; parse_int; cls; are all optional**_
> - What happens if you omit an optional parameter?
_**standard decoding is used, JSON objects become plain dicts, numbers become native Python int/float**_
> - What default value is used?
_**parse_float=float, parse_int=int, clas=json.JSONDecoder**_

---

## Return Value

What does the function return?

*A Python object, typically a dict or list, but can be str, int, float, bool or None, depending on the JSON input**

## Example

import json

with open("data.json", "r") as f:
    data = json.load(f)
    print(data['city'])

## Expected Output

Nairobi

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**now i understand the working of json file**
