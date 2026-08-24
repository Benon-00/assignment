# Function 4

## Function Name

```python
collections.namedtuple()
```

---

## Purpose

Describe what the function does.

_**A factory function that creates a new tuple subclass with named fields, allowing access to elements by name (e.g point.x) in addition to index, while reamianing lightweight and immutable like a regular tuple.**_


## Syntax

```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|typename | Yes | - | str | Name of the new tuple subclass |
|field_names | Yes | - | str/list/tuple of str | Names of the fields (e.g 'x y' or ['x', 'y'])|
|rename | No | False | bool | If True, auto-replaces invalid field names with positional names|
|defaults | No | None | Iterable or None | Default values applied to the rightmost fields|
|module | No | None | str | Sets __module__ attribute of the resulting class|




> **Questions to answer**
>
> - Which parameters are required?
_**typename, field_names are required**_
> - Which parameters are optional?
_**rename, defaults, module; are all optional**_
> - What happens if you omit an optional parameter?
_**invalid names raises ValueError instead of being auto-fixed; no-fields get default values, so all must be supplied; module is auto-detected from caller's frame**_
> - What default value is used?
_**rename=False, defaults=None, module=None**_

---

## Return Value

What does the function return?

**A new class (subclass of tuple) with the specified named fields; instantiating that class returns a namedtuple instance**

## Example

import collections as cl

Point = cl.namedtuple('Point', ['x', 'y'], defaults=[0,0])
p1 = Point(3,4)
p2 = Point()
print(p1, p1.x, p1.y)
print(p2)

## Expected Output

Point(x=3, y=4) 3 4
Point(x=0, y=0)

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's a very interesting function, tricky to understand**
