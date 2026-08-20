# Function 5

## Function Name

```python
os.path.join()
```

---

## Purpose

Describe what the function does.

_**Intelligently joins one or more path components into a single path string, using the correct path separator for the current operating system**_


## Syntax

```python
os.path.join(path, *paths)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
| path      | Yes    |-     | str, bytes, or path-like object  |The first (base) path component|
| *paths    | No     |-(none appended) | str, bytes, or path-like object(s) |Additional path components to append, in order|


> **Questions to answer**
>
> - Which parameters are required?
_**path is required**_
> - Which parameters are optional?
_**paths is optional; zero or more additional components can be passed**_
> - What happens if you omit an optional parameter?
_**the function simply returns path unchanged, since there's nothing else to join**_
> - What default value is used?
_**N/A**_

---

## Return Value

What does the function return?

**A single string representing the combined path, joined with the OS-appropriate separator.**

## Example

import os

path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)

## Expected Output

folder\subfolder\file.txt

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is easy to understand**
