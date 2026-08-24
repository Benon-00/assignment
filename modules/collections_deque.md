# Function 5

## Function Name

```python
collections.deque()
```

---

## Purpose

Describe what the function does.

_**A list-like container implemented as a double-ended queue, supportint fast(O(1)) appends and pops from both the left and right ends; much faster than a list for these operations**_


## Syntax

```python
collections.deque(iterable=(), maxlen=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|iterable | No | () (empty) | iterable | Initial elements to populate the deque |
|maxlen | No | None | int or None | Maximum size, when full, adding an item discards one from the opposite end|


> **Questions to answer**
>
> - Which parameters are required?
_**None**_
> - Which parameters are optional?
_**iterable, maxlen; are all optional**_
> - What happens if you omit an optional parameter?
_**iterable=() creates an empty deque; maxlen=None means the deque has unbounded size (grows witout discarding elements)**_
> - What default value is used?
_**iterable=(), maxlen=None**_

---

## Return Value

What does the function return?

**A deque object**

## Example

import collections as cl

dq = cl.deque([1,2,3], maxlen=3)
dq.append(4)
dq.appendleft(0)
print(dq)

## Expected Output

deque([0, 2, 3], maxlen=3)

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's a very interesting function**
