# Function 3

## Function Name

```python
Path.mkdir()
```

---

## Purpose

Describe what the function does.

_**Creates a new directory at the given path**_


## Syntax

```python
Path.mkdir(mode=0o777, parents=False, exists_ok=False)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|mode | No    | 0o777 | int(octal)| Permission bits for the new directory (subject to unmask)|
|parents | No    | False | bool | If True, create any missing parent directories|
|exist_ok | No    | False | bool | If True, don't raise an error if the directory already exists|



> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**mode, parents, exist_ok; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**mode=0o777; parents=False; exist_ok=False**_

---

## Return Value

What does the function return?

**a bool**

## Example

from pathlib import Path

new_dir = Path("output/reports")
new_dir.mkdir(parents=True, exist_ok=True)
print(new_dir.exists())

## Expected Output

True

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this module requires considerable understanding**