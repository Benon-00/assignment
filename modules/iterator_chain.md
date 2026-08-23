# Function 5

## Function Name

```python
itertools.chain()
```

---

## Purpose

Describe what the function does.

_**Combines multiple iterables into a single sequential iterator, yielding elemnts from the first iterable until it's exhausted, then moving to the next, and so on**_


## Syntax

```python
itertools.chain(*iterables)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|*iterables   | No    | - (empty chain if none given) | one or more iterables |Any number of iterables to be chained together in sequence |


> **Questions to answer**
>
> - Which parameters are required?
_**Techincally, none are required; chain() can be called with zero arguments, thouh this produces an empty iterator with no items**_
> - Which parameters are optional?
_**All arguments are optional in the sense that any number (including zero) can be passed via *iterables**_
> - What happens if you omit an optional parameter?
_**chain() returns an uterator that immediately raises StopIteration (yields nothing). If some are provided and others omitted, only the provided ones are chained**_
> - What default value is used?
_**the default behaviour with no arguments is to produce an empty iterator**_

---

## Return Value

What does the function return?

**Returns a chain iterator that yields elements from each input iterable in order, one after another, as if they were single continous iterable**

## Example

import itertools

x = itertools.chain(['a', 'b',], [1,2,3], (True, False))

for item in x:
    print(item)

## Expected Output

a
b
1
2
3
True
False

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I have seen how to break the for loop to make it clear to understand**
