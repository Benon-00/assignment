# Function 3

## Function Name

```python
csv.DictReader()
```

---

## Purpose

Describe what the function does.

_**Returns an object that maps each row of a csv file to an OrderedDict/dict, using the first row (or a supplied fieldnames) as keys, convenient for accessing columns by name instead of index**_


## Syntax

```python
csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|f   | Yes    |-     |file object/iterable of strings |The source to read from |
|fieldnames | No    |None(uses first row of file) |sequence of str|Column names to use as dict keys |
|restkey | No    |None | any(typically str) | Key to store extra values if a row has more fields than fieldnames |
|restval | No    |None | any | Value to use for missing fields if a row has fewer fields than fieldnames|
|dialect | No    |'excel' | str/Dialect object | Preset formatting rules|


> **Questions to answer**
>
> - Which parameters are required?
_**f is required**_
> - Which parameters are optional?
_**fieldnames; restkey; restval; dialect; are all optional**_
> - What happens if you omit an optional parameter?
_**the first row of the file is consumed and used as the field names; missing/extra fields aren't specially handled(extras dropped, and restval/restkey remain None)**_
> - What default value is used?
_**fieldnames=None, restkey=None, restval=None, dialect='excel'**_

---

## Return Value

What does the function return?

**A DictReader object, an iterator; each iteration yields one row as a dict (mapping column name->value)**

## Example

import csv

with open('output.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

## Expected Output

Alice 30

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
