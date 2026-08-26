# Function 3

## Function Name

```python
string.Template.safe_substitute()
```

---

## Purpose

Describe what the function does.

_**Works like substitute(), but tolerates missing placeholder values, instead of raising a KeyError, it leaves the original $identifier text unchanged in the output. Useful for partial or iterative template filling.**_


## Syntax

```python
string.Template.safe_substitute(mapping={}, /, **kwds)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|template |Yes(at Template() creation) | - | str | The template string cntaining $name placeholder|
|mapping | No   | {} (empty dict) | dict/Mapping | Dictionary of placeholder values |
|**kwds| No   | none | keyword arguments | Additional/override placeholder values |





> **Questions to answer**
>
> - Which parameters are required?
_**template is required**_
> - Which parameters are optional?
_**mapping and **kwds; are optioanl**_
> - What happens if you omit an optional parameter?
_**if a placeholder isn't found in mapping or kwds, that placeholder is left as-is (literal $name text) in the returned string instead of raising an error**_
> - What default value is used?
_**mapping={}**_

---

## Return Value

What does the function return?

**A new str with all resolvable placeholders substituted; unresolved placeholders remain in their original $identifier form.**

## Example

import string as str

t = str.Template('Hello, $name! Your balance is $${amount}.')
result = t.safe_substitute(name='Bob')
print(result)

## Expected Output

Hello, Bob! Your balance is ${amount}.

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
