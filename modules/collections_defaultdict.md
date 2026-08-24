# Function 2

## Function Name

```python
collections.defaultdict()
```

---

## Purpose

Describe what the function does.

_**A dict subclass that calls a 'default factory' function to automatically supply a value for a missing key, instead of raising KeyError.**_


## Syntax

```python
collections.defaultdict(default_factory=None, /, [...])
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|default_factory | No   | None   | callable or None | Function called with no args to produce a value for missing keys (e.g list, int, set)|
|*args/**kwargs | No   | None   | any | Initial items, same as passed to dict()|




> **Questions to answer**
>
> - Which parameters are required?
_**None is required**_
> - Which parameters are optional?
_**default_factory; initialable arguments; are all optional**_
> - What happens if you omit an optional parameter?
_**missing key access still raises KeyError just like a normal dict, the auto-fill behaviour is disabled**_
> - What default value is used?
_**default_factory=None**_

---

## Return Value

What does the function return?

**A defaultdict object (dict subclass)**

## Example

import collections as cl

dd = cl.defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(dd)

## Expected Output

defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's a very interesting function**
