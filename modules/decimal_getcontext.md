# Function 2

## Function Name

```python
decimal.getcontext()
```

---

## Purpose

Describe what the function does.

_**Returns the current active decimal Context object for the running thread, which controls precision, rounding mode, and enabled traps (signals) for all decimal arithmetic in that thread**_

## Syntax

```python
decimal.getcontext()
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| none    |        |    | | This function takes no parameters|



> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
_**N/A**_
> - What default value is used?
_**N/A**_

---

## Return Value

What does the function return?

**The current thread's Context object, which can be inspected or mutated (e.g getcontext().prec = 6)**

## Example

import decimal as dec

ctx = dec.getcontext()
print(ctx.prec)

ctx.prec = 4
print(dec.Decimal(1) / dec.Decimal(3))

## Expected Output
28
0.3333

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's interesting to understand**