# Function 1

## Function Name

```python
itertools.count()
```

---

## Purpose

Describe what the function does.

_**Creates an infinite iterator that generates evenly spaced numbers starting from a given value; commonly used for generating sequential IDs or as a counter in loops.**_


## Syntax

```python
itertools.count(start=0, step=1)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|start   | No    | 0     | int/float |The number to start counting from|
|step   | No    | 1     | int/float |The increment between successive values|



> **Questions to answer**
>
> - Which parameters are required?
_**None is required**_
> - Which parameters are optional?
_**start, stop; are all optional**_
> - What happens if you omit an optional parameter?
_**the start begines form 0, and by step 1**_
> - What default value is used?
_**start=0; step=1**_

---

## Return Value

What does the function return?

*Returns a count iterator object that produces an infinite sequences of numbers (must be stopped manually e.g with break or zip/islice)**

## Example

import itertools

x = itertools.count(10, 5)

for i in x:
    if i >30:
        break
    print(i)

## Expected Output

10
15
20
25
30

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I have seen how to break the for loop to make it clear to understand**
