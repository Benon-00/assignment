# Function 3

## Function Name

```python
collections.OrderedDict()
```

---

## Purpose

Describe what the function does.

_**A dict subclass that remembers the order in which keys were first inserted, and provides extra order-realted methods (e.g move_to_end()). Since Python 3.7, regular dicts aso preserve insertion order, but OrderDict still offers additional ordering operations and explicit order-sensitive equality checks**_


## Syntax

```python
collections.OrderedDict(other=(), /, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|other | No   | () (empty)   | mapping or iterable of key/value pairs | Initial data to populate the ordered dict|
|**kwds | No   | None | keyword args | Additional key/value pairs (order not guaranteed if used alone before Python 3.7 semantics, but preserved when combined with other)|




> **Questions to answer**
>
> - Which parameters are required?
_**None is required**_
> - Which parameters are optional?
_**other; **kwds; are all optional**_
> - What happens if you omit an optional parameter?
_**creates an empty OrderedDict**_
> - What default value is used?
_**other=()**_

---

## Return Value

What does the function return?

**An OrderedDict object (dict subcalss) preserving insertion order**

## Example

import collections as cl

od = cl.OrderedDict()
od['one']=1
od['two']=2
od['three']=3

od.move_to_end('one')
print(od)

## Expected Output

OrderedDict({'two': 2, 'three': 3, 'one': 1})

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's a very interesting function**
