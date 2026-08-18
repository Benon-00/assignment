# Function 1

## Function Name

```python
datetime.datetime.now()
```

---

## Purpose

Describe what the function does.

_**Returns the current local date & time, optionally attcahed to a specific timezone**_


## Syntax

```python
datetime.datetime.now(tz=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| tz    | No       | None     | tzinfo object | Timezone to convert the result to|


> **Questions to answer**
>
> - Which parameters are required?
_**none is required; can be called with zero arguments.**_
> - Which parameters are optional?
_**tz is optional**_
> - What happens if you omit an optional parameter?
_**returns the current local date/time, based on the system clock**_
> - What default value is used?
_**tz=None**_

---

## Return Value

What does the function return?

**a datetime object representing the current date and time**

## Example

import datetime as dt

print(dt.datetime.now())


## Expected Output

2026-08-18 09:51:23.688073

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**