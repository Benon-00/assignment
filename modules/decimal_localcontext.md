# Function 4

## Function Name

```python
decimal.localcontext()
```

---

## Purpose

Describe what the function does.

_**A context manager that creates a temporary copy of the active (or supplied) context for use within a with block. ANy chnages made inside the block are automatically dicarded when the block exists, leaving the original context untouched; the recommended way to apply temporary precision/rounding changes**_

## Syntax

```python
decimal.localcontext(ctx=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| ctx   | No | current thread's context | Context | Base context to copy for the with block |
| prec  | No | inherited from ctx | int | Override precision for this block (keyword arg, Pythin 3.11+)|
| rounding  | No | inherited from ctx | str | Override rounding mode for this block (keyword arg. Python 3.11+) |



> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**ctx, prec, rounding; are all optional**_
> - What happens if you omit an optional parameter?
_**a copy of the current active context is used unmodified inside the with block, and reverted automatically afterwards**_
> - What default value is used?
_**ctx=None (copies the currently active context)**_

---

## Return Value

What does the function return?

**A context maanager object; used with with...as ctx, ctx is the temporary Context copy active for the block's duration**

## Example

import decimal as dec

print(dec.getcontext().prec)

with dec.localcontext() as ctx:
    ctx.prec = 2
    print(dec.Decimal(1) / dec.Decimal(7))

print(dec.getcontext().prec)

## Expected Output
28
0.14
28
## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's interesting to understand**