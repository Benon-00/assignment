# Function 2

## Function Name

```python
string.Template.substitute()
```

---

## Purpose

Describe what the function does.

_**Performs template-string substitution, replacing $identifier or ${identifier} placeholders in a Template object with values supplied via a mapping and/or keyword arguments. Raises an error if any placeholder is missing a value.**_


## Syntax

```python
string.Template.substitute(mapping={}, /, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|template |Yes(at Template() creation) | - | str | The template string cntaining $name placeholder|
|mapping | No   | {} (empty dict) | dict/Mapping | Dictionary of placeholder values |
|**kwds| No   | none | keyword arguments | Additional/override placeholder values |





> **Questions to answer**
>
> - Which parameters are required?
_**template is required**_
> - Which parameters are optional?
_**mapping and **kwds are technically optional parameters of substitute(), but every placeholder in the template must resolve to a value or a KeyError is raised**_
> - What happens if you omit an optional parameter?
_**if mapping is omitted, only keyword arguments are used to fill placeholders; if a placeholder has no corresponding key anywhere, a KeyError is raised (substitution fails, no partial fallback)**_
> - What default value is used?
_**mapping={}**_

---

## Return Value

What does the function return?

**A new str with all placeholders replaced by their corresponding values.**

## Example

import string as str

t = str.Template('Hello, $name! Yo have $count new messages.')
result = t.substitute(name='Alice', count=3)
print(result)

## Expected Output

Hello, Alice! Yo have 3 new messages.

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
