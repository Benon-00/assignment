# Function 1

## Function Name

```python
pathlib.Path()
```

---

## Purpose

Describe what the function does.

_**Constructs a new Path object representing a filesystem path (file or directory), which can then be used with all other pathlib methods. It auto-detects the OS and returns either a PosixPath or WindowsPath.**_


## Syntax

```python
pathlib.Path(*pathsegments*)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|pathsegments| No    | ''(current directory, .)|str/os.PathLike (variadic) | One or more path components to join together|


> **Questions to answer**
>
> - Which parameters are required?
_**none is required, Path() can be called with zero arguments**_
> - Which parameters are optional?
_**pathsegments is optional**_
> - What happens if you omit an optional parameter?
_**calling Path() with no arguments returns a Path representing the current directory (.)**_
> - What default value is used?
_**'.' (empty path segments resolve to the current directory reference)**_

---

## Return Value

What does the function return?

**a concrete Path subclass instance, WindowsPath on Windows**

## Example

from pathlib import Path

p = Path('folder', 'subfolder', 'file.txt')
print(p)


## Expected Output

folder\subfolder\file.txt

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this module requires considerable understanding**