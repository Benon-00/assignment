# Function 1

## Function Name

```python
csv.reader()
```

---

## Purpose

Describe what the function does.

_**Creates a single new directory at the specified path. Raises an error if the directory already exists or if any intermediate parent directories in the path don't exist (for creating nested directories, use os.makedirs())**_


## Syntax

```python
csv.reader(csvfile, dialect='excel', **fmtparams)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|csvfile    | Yes    |-     |file object/iterable of strings |The source to read from (an open file or any iterable yielding lines)|
|dialect   | No    |'excel' |str/Dialect object |Preset formatting rules (delimiter, quoting, etc)|
|delimiter | No    |,(frm dialect) | str(1 char) |Preset formatting rules (delimiter, quoting, etc)|
|quotechar | No    |"(from dialect) | str(1 char) | Character used to quote fields|
|skipinitialspace | No | False | bool | Ignore whitespace after delimiter|



> **Questions to answer**
>
> - Which parameters are required?
_**csvfile is required**_
> - Which parameters are optional?
_**dialect, and any fmtparams; are all optional**_
> - What happens if you omit an optional parameter?
_**uses their default values**_
> - What default value is used?
_**dialect='excel'**_

---

## Return Value

What does the function return?

**A reader object; an iterator; each iteration yields one row as a list of strings.**

## Example

import csv

with open('IBM Attrition.csv', newline='') as f:
    reader = csv.reader(f)
    for column in reader:
        print(column)

## Expected Output

the rows values

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**pandas is easier to use with csv compare to the csv itself**
