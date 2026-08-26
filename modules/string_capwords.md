# Function 1

## Function Name

```python
string.capwords()
```

---

## Purpose

Describe what the function does.

_**Splits a tring into words, capitalizes the first letter of each word, and joinsthem back together using a specified (or default) separator. It's a more forgiving alternative to str.title() because it correctly handles words already containing uppercase letters and collapses runs of whitespace**_


## Syntax

```python
string.capwords(s, sep=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|--------------------|---------------|--------------------|-------------|
|s|Yes   | -   |str |The input string to capitalize |
|sep | No   | None   | string or None | Separator used to split and rejoin words|




> **Questions to answer**
>
> - Which parameters are required?
_**s is required**_
> - Which parameters are optional?
_**sep; is optional**_
> - What happens if you omit an optional parameter?
_**if sep=None, the function splits on arbitrary runs of whitespace (using str.split()'s default behaviour), strips leading/trailing whitespace, and rejoins the words using a single space**_
> - What default value is used?
_**sep=None**_

---

## Return Value

What does the function return?

**A new str with each word's first character capitalized and the rest lowercased, joined by sep (or a single space if sep is None)**

## Example

import string as str

result = str.capwords('hello world from PYTHON')
print(result)

## Expected Output

Hello World From Python

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
