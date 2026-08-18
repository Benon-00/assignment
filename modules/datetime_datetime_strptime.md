# Function 2

## Function Name

```python
datetime.datetime.strptime()
```

---

## Purpose

Describe what the function does.

_**Parses a string representing a date/tiime according to a specified format and converts it into a datetime object.**_


## Syntax

```python
datetime.datetime.strptime(date_string, format)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|date_string | Yes       | None     | str | The date/time text to parse |
|format | Yes       | None     | str | Format code string (e.g '%Y-%m-%d') describing how to interpret date_string|

> **Questions to answer**
>
> - Which parameters are required?
_**date_string & format are required**_
> - Which parameters are optional?
_**none is optional**_
> - What happens if you omit an optional parameter?
_**Since there are no optional parameters, omitting the required parameters raises a TypeError**_
> - What default value is used?
_**No default value exists for this function's parameters**_

---

## Return Value

What does the function return?

**a datetime object corresponding to the parsed string**

## Example

import datetime as dt

X = dt.datetime.strptime('18-08-2026', '%d-%m-%Y')
print(X)


## Expected Output

2026-08-18 00:00:00

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the key differentiator to understand this is:converting a date string into a date format**