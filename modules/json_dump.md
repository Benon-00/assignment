# Function 2

## Function Name

```python
json.dump()
```

---

## Purpose

Describe what the function does.

_**Serializes a Python object as JSON and writes it directly to an open file-like oject (rather than returning a string)**_


## Syntax

```python
json.dump(obj, fp, *, skipkeys=False, indent=None, sort_keys=False, default=None, **kw)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|obj    | Yes    |-     | dict/list/str/int/float/bool/None |The Python object to serialize|
|fp    | Yes    |-     | file like object (supports .write()) | Destination to write the JSON text|
|skipkeys | No  | False | bool | Skip dict keys that aren't a basic type instead of raising TypeError|
|indent | No  | None | int/str/None| Pretty-print with this indent level; None means compact output|
|separators | No  | , or : | tuple(str,str) | Item and Key separators|
|sort_keys | No  | False | bool | Sort dictionary keys alphabetically in output|
|default | No  | None | function | Function called for objects that aren't natively serializable|
|ensure_ascii | No  | True | bool | Escape all non-ASCII charcaters if True|


> **Questions to answer**
>
> - Which parameters are required?
_**obj, fp; are required**_
> - Which parameters are optional?
_**skipkeys, indent, separators, sort_keys, default, ensure_ascii; are all optional**_
> - What happens if you omit an optional parameter?
_**output is compact(no extra whitespace/newlines), keys stay in insertion order, non-ASCII characters are escaped, and non-serializable objects raise a TypeError**_
> - What default value is used?
_**Indent=None(comapct single-Line string), sort_keys=False, ensure_ascii-True**_

---

## Return Value

What does the function return?

**None, the function writes to fp in place and returns nothing**

## Example

import json

data = {'name': 'Alice', 'age': 30, 'active': True}
result = json.dump(data, indent=2, sort_keys=False)
print(result)

## Expected Output

{
    "city": "Nairobi",
    "population": 4397073
}

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**now i understand the working of json file**
