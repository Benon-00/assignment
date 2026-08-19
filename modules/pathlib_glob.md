# Function 4

## Function Name

```python
Path.glob()
```

---

## Purpose

Describe what the function does.

_**Finds all paths in a directory matching a given wildcard pattern (similar to shell-style globbing), returning a generator/iterator of matching Path objects**_


## Syntax

```python
Path.glob(pattern, *, case_sensitive=None, recurse_symlinks=False)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|pattern | Yes    | None | str | Glob pattern to match (e.g '*.txt', '**/*.py')|
|case_sensitive | No    | None (platform-dependent) | bool or None | Force case-sensitive/insensitive matching|
|recurse_symlinks | No    | False  | bool | Whether ** recurses into symlinked directories |



> **Questions to answer**
>
> - Which parameters are required?
_**pattern is required**_
> - Which parameters are optional?
_**case_sensitive; recurse_symlinks; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**case_sensitive=None; recurse_symlinks=False**_

---

## Return Value

What does the function return?

**the Path objects in the specified category**

## Example

from pathlib import Path

for file in Path('.').glob('*.py'):
    print(file)

## Expected Output

test.py
testSpyder.py

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this module requires considerable understanding**