# Function 4

## Function Name

```python
os.remove()
```

---

## Purpose

Describe what the function does.

_**Deletes a single file at the specified path. It cannot be used to delete a directory; use os.rmdir or shutil.rmtree() for that**_


## Syntax

```python
os.remove(path, *, dir_fd=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
| path      | Yes    |-     | str, bytes, or path-like object  |Path of the file to delete|
| dir_fd    | No     |None  | int(file descriptor)  | Directory file descriptor used to resolve a relative path|


> **Questions to answer**
>
> - Which parameters are required?
_**path is required**_
> - Which parameters are optional?
_**dir_fd is optional**_
> - What happens if you omit an optional parameter?
_**relative paths are resolved against the current working directory, as normal (most platforms don't support dir_fd anyway)**_
> - What default value is used?
_**dir_fd=None**_

---

## Return Value

What does the function return?

**The file is deleted as a side effect; nothing is returned. Raises FileNotFoundError if the file doesn't exist, or IsADirectoryError if path points to a directory**

## Example

import os

os.remove('old_file.txt')
print(os.path.exists('old_file.txt'))'))

## Expected Output

FileNotFoundError

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is easy to understand**
