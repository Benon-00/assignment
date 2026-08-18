# Function 3

## Function Name

```python
datetime.datetime.strftime()
```

---

## Purpose

Describe what the function does.

_**Formats a datetime object into a human readable string according to a specified format**_


## Syntax

```python
datetime.datetime.strftime(format)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|format | Yes       | None     | str | Format code string describibg the desired output layout (e.g '%Y-%m-%d %H:%M%S') |


> **Questions to answer**
>
> - Which parameters are required?
_**format is required**_
> - Which parameters are optional?
_**none is optional**_
> - What happens if you omit an optional parameter?
_**Since there are no optional parameters, omitting the required parameters raises a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**a datetime object corresponding to the parsed string**

## Example

import datetime as dt

x = dt.datetime.now()
xformatted = x.strftime('%A, %B, %d, %Y - %I:%M %p')
print(xformatted)

## Expected Output

Tuesday, August, 18, 2026 - 10:20 AM

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**discovered new arguents like %A, %B etc. I have researched more on them, and realized the below**
%A: Full weekday name (e.g., Sunday, Monday)%B: Full month name (e.g., January, August)%d: Day of the month as a zero-padded number (e.g., 01, 18)
%Y: Four-digit year (e.g., 2026)
%y: Two-digit year without century (e.g., 26)
%m: Two-digit month as a number (e.g., 08 for August)
%b: Abbreviated month name (e.g., Aug)
%a: Abbreviated weekday name (e.g., Tue)
%H: Hour in 24-hour clock format (e.g., 13 for 1 PM)
%I: Hour in 12-hour clock format (e.g., 01 for 1 PM)
%M: Minute as a zero-padded number (e.g., 05)
%S: Second as a zero-padded number (e.g., 42)
%p: Locale’s equivalent of AM or PM