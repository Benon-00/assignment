# Function 1

## Function Name

```python
collections.Counter()
```

---

## Purpose

Describe what the function does.

_**A dict subclass for counting hashable objects. Elements are stored as dictionary keys and their counts as dictioanry values, extremely useful for tallying frequencies**_


## Syntax

```python
collections.Counter(iterable_or_mapping=None, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|iterable_or_mapping | No   | None   | iterable, mapping, or None | Data to initialize counts from (a list/string counts elements, a dict sets counts directly)|
|**kwds | No   | None   | keyword args | Alternative way to seed counts e.g Counter (a=3, b=1)|




> **Questions to answer**
>
> - Which parameters are required?
_**None is required, Counter() with no arguments creates an empty counter**_
> - Which parameters are optional?
_**iterable_or_mapping;keyword arguments; are all optional**_
> - What happens if you omit an optional parameter?
_**returns an empty Counter object with no keys (count of any missing key defaults to 0, not KeyError)**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**A Counter object (dict subclass) mapping elements to their counts**

## Example

from collections import Counter

c = Counter('banana')
print(c)
print(c.most_common(2))

## Expected Output

Counter({'a': 3, 'n': 2, 'b': 1})
[('a', 3), ('n', 2)]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's a very interesting module**
