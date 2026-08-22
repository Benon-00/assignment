# Function 1

## Function Name

```python
json.dumps()
```

---

## Purpose

Describe what the function does.

_**Serializes a Python object (dict, list, str, int, etc) into a JSON-formatted string**_


## Syntax

```python
json.dumps(obj, *, skipkeys=False, indent=None, sort_keys=False, default=None, **kw)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|obj    | Yes    |-     | dict/list/str/int/float/bool/None |The Python object to serialize|
|skipkeys | No  | False | bool | Skip dict keys that aren't a basic type instead of raising TypeError|
|indent | No  | None | int/str/None| Pretty-print with this indent level; None means compact output|
|separators | No  | , or : | tuple(str,str) | Item and Key separators|
|sort_keys | No  | False | bool | Sort dictionary keys alphabetically in output|
|default | No  | None | function | Function called for objects that aren't natively serializable|
|ensure_ascii | No  | True | bool | Escape all non-ASCII charcaters if True|


> **Questions to answer**
>
> - Which parameters are required?
_**obj is required**_
> - Which parameters are optional?
_**skipkeys, indent, separators, sort_keys, default, ensure_ascii; are all optional**_
> - What happens if you omit an optional parameter?
_**output is compact(no extra whitespace/newlines), keys stay in insertion order, non-ASCII characters are escaped, and non-serializable objects raise a TypeError**_
> - What default value is used?
_**Indent=None(comapct single-Line string), sort_keys=False, ensure_ascii-True**_

---

## Return Value

What does the function return?

**A str containing the JSON representation of obj.**

## Example

import json

data = {'name': 'Alice', 'age': 30, 'active': True}
result = json.dumps(data, indent=2, sort_keys=False)
print(result)

## Expected Output

{
  "name": "Alice",
  "age": 30,
  "active": true
}

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**now i understand the working of json file**
