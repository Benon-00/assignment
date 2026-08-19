# Function 5

## Function Name

```python
Path.is_file()
```

---

## Purpose

Describe what the function does.

_**Checks whether the path points to a regular file (as opposed to a directory, symlink to nowhere, socket, etc), following symlinks by default**_


## Syntax

```python
Path.is_file(*, follow_symlinks=True)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|follow_symlinks |No   | True | bool | Whether to resolve symlinks before checking type|



> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**follow_symlinks is optional**_
> - What happens if you omit an optional parameter?
_**symlinks are followed, so a symlink pointing to a regular file returns True**_
> - What default value is used?
_**follow_symlinks=True**_

---

## Return Value

What does the function return?

**bool; True if the path exists and is a regular file, False otherwise.**

## Example

from pathlib import Path

new_dir = Path("example.txt")
new_dir.write_text('hello')
print(new_dir.is_file())

## Expected Output

True

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this module requires considerable understanding**