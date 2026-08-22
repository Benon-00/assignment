# Function 5

## Function Name

```python
json.JSONDecodeError()
```

---

## Purpose

Describe what the function does.

_**used for error handling when parsing fails. It is documented here as the 5th commonly used member.**_


## Syntax

```python
json.JSONDecodeError(msg, doc, pos)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|msg   | Yes    |-     | str | Unformatted error message describibg the problem |
|doc   | Yes    |-     | str | The full JSON document (or fragment) being parsed|
|pos   | Yes    |-     | int | The index in doc where parsing failed |


> **Questions to answer**
>
> - Which parameters are required?
_**msg, doc, pos; are all required**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
_**N/A; there are no optional parameters; omitting any required arguments raises a TypeError when constructing the exception directly.**_
> - What default value is used?
_**no defaults exsit for any parameter**_

---

## Return Value

What does the function return?

*N/A; it's an exception class, not a function- when raised, it carries these useful attributes: .msg(message), .doc(document string), .pos(character index), .lineno(line number), .colno(column number)**

## Example

import json

bad_json = '{"name": "Aice", "age": }' #invalid JSON (missing value)
try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e.msg} at line {e.lineno}, column {e.colno}")

## Expected Output

Failed to parse JSON: Expecting value at line 1, column 25

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**now i understand the working of json file**
