# Function 4

## Function Name

```python
csv.DictWriter()
```

---

## Purpose

Describe what the function does.

_**Returns an object that writes dictionaries to a csv fileas rows, mapping dict keys to columns according to a required fieldnames sequence.**_


## Syntax

```python
csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|f   | Yes    |-     |file object with .write()| The destinationto write to|
|fieldnames | Yes | - | sequence of str |Column names, and order, to write|
|restval | No    |'' | any | Value written for keys missing from a given row's dict|
|extrasaction | No    |'raise' | {'raise', 'ignore'} | Behaviour when a dict has keys not in fieldnames|
|dialect | No    |'excel' | str/Dialect object | Preset formatting rules|


> **Questions to answer**
>
> - Which parameters are required?
_**f, fieldnames; are required**_
> - Which parameters are optional?
_**restval, extrasaction, dialect; are all optional**_
> - What happens if you omit an optional parameter?
_**missing keys are written as empty strings (''); if a row dict contains extra keys not in fieldnames, a ValueError is raised (because extrasaction defaults to 'raise')**_
> - What default value is used?
_**restval='', extrasaction='raise', dialect='excel'**_

---

## Return Value

What does the function return?

**A DictWriter object. unlike writer(), DictWriter requires an explicit call to .writeheader() to write the column-name header row; it is not automatic**

## Example

import csv

with open('output1.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

## Expected Output

name,age
Alice,30

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**quite tricky to compare with csv_writer*
