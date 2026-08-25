# Function 1

## Function Name

```python
decimal.Decimal()
```

---

## Purpose

Describe what the function does.

_**The constructor for the Decimal class, creates a new decimal number from an integer, string, float, tuple, or another Decimal. This is the core object the rest of the module operates on**_

## Syntax

```python
decimal.Decimal(value='0', context=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| value     | No       | '0'     | int/str/float/tuple/Decimal |The numeric value to convert into a Decimal|
| context | No | current thread's context | Context | Context used for validating the value (rarely needed for simple construction)|


> **Questions to answer**
>
> - Which parameters are required?
_**none is required, calling Decimal() with no arguments is valid**_
> - Which parameters are optional?
_**value, context; are optional**_
> - What happens if you omit an optional parameter?
_**Decimal() returns Decimal('0'); context defaults to the active thread's current context**_
> - What default value is used?
_**value='0', context=None**_

---

## Return Value

What does the function return?

**A new Decimal object representing the given value exactly (strings are recommended over floats to avoid inheriting binary floatinig-point imprecision)**

## Example

import decimal as dec

a = dec.Decimal('3.14')
b = dec.Decimal(10)
c = dec.Decimal((0, (1,4,1,4), -2))   #signs(0==+ve, 1==-ve), digits, decimalposition
print(a,b,c)


## Expected Output
3.14 
10 
14.14
## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**