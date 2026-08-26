# Function 4

## Function Name

```python
string.Formatter().format()
```

---

## Purpose

Describe what the function does.

_**Provides the same functionality as str.format(), but as method on a Formatter calss instance, useful when you need to customize or subclass formatting behaviour. It formats a string containing {} replacement fields using positional and keyword arguments**_


## Syntax

```python
string.Formatter().format(format_string, /, *args, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|format_string |Yes | - | str | The string containing {} placeholders |
|*args | No   | None | Positional arguments | Values for positional/auto-numbered placeholders |
|**kwargs | No   | none | keyword arguments | Values for named placeholders |

> **Questions to answer**
>
> - Which parameters are required?
_**format_string is required**_
> - Which parameters are optional?
_**args and **kwargs; are optioanl**_
> - What happens if you omit an optional parameter?
_**if no args.kwargs are given but format string has no placholders, it simply returns the strings unchanged; if placeholders exist and their corresponding values are missing, a TypeError is raised (no silent default)**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**A new str with all {} placeholders replaced by their corresponding formatted values**

## Example

import string as str

fmt = str.Formatter()
result = fmt.format('{0} scored {1} points', 'Alice', 42)
print(result)

## Expected Output

Alice scored 42 points

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
