# Function 5

## Function Name

```python
Decimal.quantize()
```

---

## Purpose

Describe what the function does.

_**A method on Decimal objects (not a module-level function) that rounds a decimal to match the exponent (number of decimal places) of a given template value, using a specified rounding mode, commonly used to round monetary values to a fixed number of decimal places**_

## Syntax

```python
Decimal.quantize(exp, rounding=None, context=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| exp  | Yes | - | Decimal | Template value whose exponent determines the number of decimal places in the result |
| rounding | No | contxt's rounding mode | str (e.g ROUND_HALF_UP) | Rounding mode to use for this call |
| context | No | current thread's context | Context | Context to use for precision/trap checking |



> **Questions to answer**
>
> - Which parameters are required?
_**exp is required**_
> - Which parameters are optional?
_**rounding, context; are all optional**_
> - What happens if you omit an optional parameter?
_**uses the rounding mode and settings from the active context (default ROUND_HALF_EVEN), rather than a custom rounding mode**_
> - What default value is used?
_**rounding=None (falls back to context.rounding), context=None (falls back to getcontext())**_

---

## Return Value

What does the function return?

**A new Decimal rounded to match the number of decimal places of exp; raises InvalidOperation if the result would require more digits than the context's precision allows**

## Example

import decimal as dec

price = dec.Decimal('19.4567')
rounded = price.quantize(dec.Decimal('0.01'), rounding=dec.ROUND_HALF_UP)
print(rounded)

## Expected Output
19.46
## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's interesting to understand**