# Function 2

## Function Name

```python
csv.writer()
```

---

## Purpose

Describe what the function does.

_**Returns a writer object used to write rows of data to a csv file, converting each row (a list/iterable) into a properly delimited/quoted line.**_


## Syntax

```python
csv.writer(csvfile, dialect='excel', **fmtparams)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|csvfile    | Yes    |-     |file object/iterable of strings |The source to read from (an open file or any iterable yielding lines)|
|dialect   | No    |'excel' |str/Dialect object |Preset formatting rules (delimiter, quoting, etc)|
|delimiter | No    |,(frm dialect) | str(1 char) |Preset formatting rules (delimiter, quoting, etc)|
|quotechar | No    |"(from dialect) | str(1 char) | Character used to quote fields|
|quoting | No | csv.QUOTE_MINIMAL| int(constant) | Quoting policy |
|lineterminator | No | \r\n(from dialect) | str | String to terminate lines with |


> **Questions to answer**
>
> - Which parameters are required?
_**csvfile is required**_
> - Which parameters are optional?
_**dialect, and any fmtparams; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**dialect='excel', quotig=csv.QUOTE_MINIMAL**_

---

## Return Value

What does the function return?

**A writer object with .writerow() and .writerows() methods; these methods return the return value of the underlying file's write() call (typically an int; number of characters written), not the writer itself**

## Example

import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])

## Expected Output

name,age
Alice,30

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**doesn't use the print() line**
