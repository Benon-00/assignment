# Function 5

## Function Name

```python
csv.register_dialect()
```

---

## Purpose

Describe what the function does.

_**Registers a custom dialect(a named set of CSV formatting parameters like delimiter, quote character, etc) under a given name, so it can be reused by name in reader(), writer(), DictReader(), or DictWriter().**_


## Syntax

```python
csv.register_dialect(name, dialect=None, **fmtparams)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|name  | Yes    |-     | str | The name to register the dialect under |
|dialect | No   | None | Dialect class/instance | An existing dialect class to base this one on|
|delimiter | No |,| str (1 char) | Field separator |
|quotechar | No |" | str (1 char) | Quote Character |
|doublequote | No | True | bool | Whether quote chars are doubled inside quoted fields |
|skipinitialspace | No | False | bool | Ignore whitespace after delimiter |
|lineterminator | No | \r\n | str | String used to terminate lines |
|quoting | No | csv.QUOTE_MINIMAL | int(constant) | Quoting policy |



> **Questions to answer**
>
> - Which parameters are required?
_**name**_
> - Which parameters are optional?
_**dialect and all fmtparams (delimiter, quotechar, doublequote, skipinitialspace, lineterminator, quoting, escapechar)**_
> - What happens if you omit an optional parameter?
_**the new dialect falls back to the standard defaults for anything not specified**_
> - What default value is used?
_**matches the built-in 'excel' dialect's values for nay unspecified fmtparams**_

---

## Return Value

What does the function return?

**None. The dialect is registered in the module's internal dialect registry (usbale afterwards by passing its name string to reader()/writer())**

## Example

import csv

csv.register_dialect('pipes', delimiter='|', quoting=csv.QUOTE_MINIMAL)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='pipes')
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])

## Expected Output

A file output.csv is created containing:
name|age
Alice|30

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it'll take time to grasp*
