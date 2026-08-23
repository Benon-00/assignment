# Function 3

## Function Name

```python
itertools.permutations()
```

---

## Purpose

Describe what the function does.

_**Generates all possible orderings (permutations) of elements from an iterable, optioanally restricted to a specific length**_


## Syntax

```python
itertools.permutations(iterable, r=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|iterable   | Yes    | -     | iterable | The sequence of elements to permute |
|r  | No    | None(length of iterable) | int | Length of each permutation tuple |


> **Questions to answer**
>
> - Which parameters are required?
_**Iterable is required**_
> - Which parameters are optional?
_**r is optional**_
> - What happens if you omit an optional parameter?
_**if r is omitted, permutations of the full length of the input iterable are generated (all possible full-length orderings)**_
> - What default value is used?
_**r=None, which is treated internally as r=len(iterable)**_

---

## Return Value

What does the function return?

**Returns a permutations iterator that yields tuples, each representing one possible ordering of the selected elements (no element repeats within a single tuple unless th einput itself has duplicates)**

## Example

import itertools

x = itertools.permutations(['A', 'B', 'C'])

for p in x:
    print(p)

## Expected Output

('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I have seen how to break the for loop to make it clear to understand**
