# Function 5

## Function Name

```python
string.Template.get_identifiers()
```

---

## Purpose

Describe what the function does.

_**Returns a list of the distinct placeholder idnetifiers names that appear in the template string, without performing any substitution. Useful for validating that all needed values are availabl before calling substitute().**_


## Syntax

```python
string.Template.get_identifiers()
```
---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|template |Yes (at Template () creation) | - | str | The template string to inspect |


> **Questions to answer**
>
> - Which parameters are required?
_**template is required**_
> - Which parameters are optional?
_**None, get_identifiers()takes no extra arguments**_
> - What happens if you omit an optional parameter?
_**N/A, since there are no optional parameters on this method**_
> - What default value is used?
_**N/A**_

---

## Return Value

What does the function return?

**A list of unique str identifiers names found in the template, in the order they first appear**

## Example

import string as str

t = str.Template("Dear $name, your order #$order_id has shipped to $name's address.")
result = t.get_identifiers()
print(result)

## Expected Output

['name', 'order_id']

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
