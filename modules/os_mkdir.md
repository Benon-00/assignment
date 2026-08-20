# Function 3

## Function Name

```python
os.mkdir()
```

---

## Purpose

Describe what the function does.

_**Creates a single new directory at the specified path. Raises an error if the directory already exists or if any intermediate parent directories in the path don't exist (for creating nested directories, use os.makedirs())**_


## Syntax

```python
os.mkdir(path, mode=0o777, *, dir_fd=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
| path      | Yes    |-     | str, bytes, or path-like object  |Path/name of the new directory to create|
| mode      | No     |0o777 | int(octal)  |Permission bits for the new directory (subject to the current unmask)|
| dir_fd    | No     |None     | int(file descriptor)  | A directory file descriptor used to resolve relative paths againsts, instead of the current directory|

> **Questions to answer**
>
> - Which parameters are required?
_**path is required**_
> - Which parameters are optional?
_**mode, dir_fd are optional**_
> - What happens if you omit an optional parameter?
_**relative paths are resolved against the current working directory, as normal (most platforms don't support dir_fd anyway)**_
> - What default value is used?
_**mode=0o777; dir_fd=None**_

---

## Return Value

What does the function return?

**The function creates the directory as a side effect; it does not return anything meaningful.**

## Example

import os

os.mkdir('new_folder')
print(os.path.exists('new_folder'))

## Expected Output

Boolean: True.
A new folder named new_folder is created in the current working directory; if it already exists, a FileExistsError is raised instead.

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is easy to understand**
