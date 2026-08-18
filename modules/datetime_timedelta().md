# Function 5

## Function Name

```python
datetime.timedelta()
```

---

## Purpose

Describe what the function does.

_**Represents a duration, the difference between two dates or times, and can be used to perform date/time arithmetic (addinig/subtracting time spans)**_


## Syntax

```python
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| days      | No    |0    | int/float |Number of days|
| seconds   | No    |0    | int/float |Number of seconds|
| microseconds | No  |0    | int/float |Number of microseconds|
| milliseconds | No    |0    | int/float |Number of milliseconds|
| minutes      | No    |0    | int/float |Number of minutes|
| hours        | No    |0    | int/float |Number of hours|
| weeks        | No    |0    | int/float |Number of weeks|



> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**all parameters are optional**_
> - What happens if you omit an optional parameter?
_**any unit not supplied contributes zero to the total duration. Calling datetime.timedelta() with no arguments returns a zero-length duration (0:00:00)**_
> - What default value is used?
_**all parameters default to 0**_

---

## Return Value

What does the function return?

**a date object representing today's date (year, month, day only- no time component)**

## Example

import datetime as dt

today = dt.date.today()
delta = dt.timedelta(days=10, hours=5)
future_date = today + delta
print(future_date)

## Expected Output

2026-08-28

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is easy to understand**
