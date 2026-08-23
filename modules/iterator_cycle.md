# Function 2

## Function Name

```python
itertools.cycle()
```

---

## Purpose

Describe what the function does.

_**Repeats the elements of an iterable indefinetely, looping back to the beginning once the end is reached; useful for round-robin style iterations**_


## Syntax

```python
itertools.cycle(iterable)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|iterable   | Yes    | -     | iterable(list, tuple, str, etc) | The sequence of elements to cycle through repeatedly |


> **Questions to answer**
>
> - Which parameters are required?
_**Iterable is required**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**Not applicable, there are no optional parameters to omit. Omitting iterable itself raises a TypeError since it is required**_
> - What default value is used?
_**No default values exist for this function**_

---

## Return Value

What does the function return?

*Returns a cycle iterator that yields elements from the iterable endlessly, looping back to the start after exhausting it (infinite iterator, must be limited manaully)**

## Example

import itertools

x = itertools.cycle(['A', 'B', 'C'])
counter = 0

for i in x:
    if counter >= 7:
        break
    print(i)
    counter += 1

## Expected Output

A
B
C
A
B
C
A

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I have seen how to break the for loop to make it clear to understand**
