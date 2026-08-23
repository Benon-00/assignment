# Function 4

## Function Name

```python
itertools.combinations()
```

---

## Purpose

Describe what the function does.

_**Generates all possible combinations of a specified length from an iterable, where order does not matter and elemets are not repeated**_


## Syntax

```python
itertools.combinations(iterable, r=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|iterable   | Yes    | -     | iterable | The sequence of elements to permute |
|r  | Yes    | - | int | Length of each combination tuple |


> **Questions to answer**
>
> - Which parameters are required?
_**Both iterable and r are required**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**Not Applicable; omitting either of the required parameters raises a TypeError**_
> - What default value is used?
_**No default value exist; both parameters must be explicityl supplied**_

---

## Return Value

What does the function return?

**Returns a combinations iterator that yields tuples of length r, containing unique combinations of elements in sorted order (based on their position in th einput), with no repeated elements within a tuple**

## Example

import itertools

x = itertools.combinations(['A', 'B', 'C'], 2)

for c in x:
    print(c)

## Expected Output

('A', 'B')
('A', 'C')
('B', 'C')

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I have seen how to break the for loop to make it clear to understand**
