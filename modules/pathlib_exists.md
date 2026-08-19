# Function 2

## Function Name

```python
Path.exists()
```

---

## Purpose

Describe what the function does.

_**Checks whether the path points to an existing file or directory on disk (following symlinks by default)**_


## Syntax

```python
Path.exists(*, follow_symlinks=True)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|follow_symlinks| No    | True | bool | Whether to resolve symlinks before checking existence|


> **Questions to answer**
>
> - Which parameters are required?
_**none is required, called on an existing Path instance with no mandatory arguments**_
> - Which parameters are optional?
_**follow_symlinks is optional**_
> - What happens if you omit an optional parameter?
_**symlinks are followed, so a broken symlink target check reflects the target's existnece, not the link itself**_
> - What default value is used?
_**follow_symlinks=True**_

---

## Return Value

What does the function return?

**a bool; True if the path exists, False otherwise**

## Example

from pathlib import Path

p = Path('file.txt')
print(p.exists())


## Expected Output

False

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this module requires considerable understanding**