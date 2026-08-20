# Function 2

## Function Name

```python
os.listdir()
```

---

## Purpose

Describe what the function does.

_**Returns a list of the names of entries (files and subdirectories) contained in the given directory**_


## Syntax

```python
os.listdir(path='.')
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
| path      | No                 |'.' (current directory) | str, bytes, or path-like object  |The directory whose contents should be listed|


> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**path is optional**_
> - What happens if you omit an optional parameter?
_**os.listdir() lists the contents of the current working directory ('.')**_
> - What default value is used?
_**'.'**_

---

## Return Value

What does the function return?

**a list of strings, each the name of a file or directory entry (not including . or .., and not including the full path; just the entry name)**

## Example

import os

print(os.listdir())

## Expected Output

['datetime_module.md', 'example.py', 'md_done', 'os_getcwd.md', 'os_listdir.md', 'os_mkdir.md', 'os_path_join.md', 'os_remove.md', 'py_done']

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is easy to understand**
