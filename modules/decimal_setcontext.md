# Function 3

## Function Name

```python
decimal.setcontext()
```

---

## Purpose

Describe what the function does.

_**Replaces the current thread's active decimal context with a new, fully-specified Context object, useful for applying a saved or custom configuration (precision, rounding, traps) all at once**_

## Syntax

```python
decimal.setcontext(context)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| context   | Yes       | -   | Context | The new Context object to install as the active context |



> **Questions to answer**
>
> - Which parameters are required?
_**context is required**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
_**since there are no optional parameters, omitting the required context raises a TypeError**_
> - What default value is used?
_**N/A**_

---

## Return Value

What does the function return?

**None, the function's effect is to set global (thread-local) state, not to return a value**

## Example

import decimal as dec

new_ctx = dec.Context(prec=3, rounding=dec.ROUND_DOWN)
dec.setcontext(new_ctx)

print(dec.Decimal(1) / dec.Decimal(3))
print(dec.getcontext().prec)

## Expected Output
0.333
3

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's interesting to understand**