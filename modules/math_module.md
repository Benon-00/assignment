# Python Module Exploration

> **Student Name:Benon Nyabuto**  
> **Date:25/07/2026**  

---

# Module Name

Replace this heading with the name of your chosen Python module.

Example:

```python
math
```

---

# 1. Module Overview

## Purpose

Describe what the module is used for.

**_the math module provides essential functions to perform complex mathematics without writing code from scratch_**

## Why is this module important?

Explain why Python includes this module and what problems it helps solve.

**_Python includes it to give developers a fast and standard tool for advanced calculations. Without it, developers have to write complex code for basic operatons, that leads to slow operations._**

**_Problems it helps solve include:_**
**_1. eliminates the need for writing complex code for simple math operations i.e square root_**
**_2. simplifies calculus i.e distances, angles & shapes for game development_**
**_3. helps in data processing in machine learning i.e normalize, scaling & rounding continuous data_**
**_4. helps in simulations i.e creating predictive models_**

## Real-world Applications

List at least three practical applications.

1._**Video Games: to calculate smooth character movement & object transformation(scaling, rotation, location) in 2D/3D space i.e math.sin(), math.cos()**_
2.**_Geographic Navigation: used to calculate distances between GPS coordinates i.e math.radians()_**
3.**_Financial forecasting: to model interest rates like compounding interest/simple interest, to analyze stock market and predict population growth rates_**

---

# 2. Functions

Choose **five commonly used functions** from your module.

---

# Function 1

## Function Name

```python
math.sqrt()
```

---

## Purpose

Describe what the function does.

_**Returns the square root of a number**_

## Syntax

```python
math.sqrt(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 |  None         |  non-negative int or float          | The number to find the square root of            |

> **Questions to answer**
>
> - Which parameters are required?
_**the required parameter is x**_
> - Which parameters are optional?
_**None, since there's only one required parameter, x**_
> - What happens if you omit an optional parameter?
**_Since the only parameter is the required x, ommitting it gives a TypeError (which is to say that the function received an unexpected data type)_**
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it either returns an integer or float_**

## Example

**__import math_**

**_result = math.sqrt(25)_**
**_print(result)__**

## Expected Output

**_5.0_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

the interesting thing about this function is how simple it is to use. Considering I am familiar with a wide range of math operations, writing its python fucntion code, and understanding how it works is satisfactory.



# Function 2

## Function Name

```python
math.pow()
```

---

## Purpose

Describe what the function does.

_**Returns the raised value of x, when raised to the exponent y (x**y), always as a float**_

## Syntax

```python
math.pow(x, y)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 |  None         |   int or float    | The base number      |
| y         | Yes                 |  None         |   int or float  | The exponent           |

> **Questions to answer**
>
> - Which parameters are required?
_**the required parameter are x & y**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
**Ommitting either of the parameters gives a TypeError (which in this case is to say that the function didn't receive both parameters)_**
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns a float_**

## Example

**__import math_**

**_result = math.pow(2, 3)_**
**_print(result)__**

## Expected Output

**_8.0_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the expected results is a float, and not both int/float_**



# Function 3

## Function Name

```python
math.factorial()
```

---

## Purpose

Describe what the function does.

_**Returns the factorial of a non-negative integer (n!) i.e n! = n*(n-1)*(n-2)*(n-3)...**_

## Syntax

```python
math.factorial(n)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| n         | Yes                 |  None         |   non-negative int    | The number to compute the factorial of|

> **Questions to answer**
>
> - Which parameters are required?
_**the required parameter is n**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
**Since n is the only required parameter, ommitting it gives a TypeError (which in this case is to say that the function didn't receive the parameter n, or got an unexpected parameter)_**
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns an integer_**

## Example

**__import math_**

**_result = math.factorial(4)_**
**_print(result)__**

## Expected Output

**_24.0_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the factorial of 0 is 1 i.e 0! = 1_**



# Function 4

## Function Name

```python
math.gcd()
```

---

## Purpose

Describe what the function does.

_**Returns the greatest common divisor of the given interger(s)**_

## Syntax

```python
math.gcd(*integers)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| *integers | No, because one can leave it blank | Returns 0 if called with no arguments | int(one or more)    | The integersto find GCD of|

> **Questions to answer**
>
> - Which parameters are required?
_**at least 2 integers to give meaningful GCD**_
> - Which parameters are optional?
_*  All of them essentially, because you can pass zero, one or many integers**_
> - What happens if you omit an optional parameter?
_**The returned value defaults to 0 if no argument(s) are passed**_
> - What default value is used?
_*  0**_

---

## Return Value

What does the function return?

**_it returns a positive integer_**

## Example

**__import math_**

**_result = math.gcd(48, 60, 18)_**
**_print(result)__**

or 
**_result2 = math.gcd(-48, -60, -18)_** #since these are negative numbers, their absolute value |integer| are used to get the GCD
**_print(result2)__**

## Expected Output

**_6_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that even for negative integers, the absolute value is used to get the answer_**


# Function 5

## Function Name

```python
math.log()
```

---

## Purpose

Describe what the function does.

_**Returns the logarithm of x to the given base. If the base is not provided, it returns the natural logarithm (base e)**_

## Syntax

```python
math.log(x, base)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | non-negative(positive) int/float|The number to compute the logarithm of |
| base      | No                  | e (Euler's number = 2.71828) | non-negative(positive) int/float | The logarithmic base|

> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**base is optional**_
> - What happens if you omit an optional parameter?
_**The returned value is the natural log (base e)**_
> - What default value is used?
_**base defaults to Euler's number e = 2.718281828**_

---

## Return Value

What does the function return?

**_it returns a float_**

## Example

**__import math_**

**_result1 = round(math.log(100), 2)_**
**_result2 = math.log(100, 10)_**
**_print(result1)__**
**_print(result2)__**


## Expected Output

**_4.61_**
**_2_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the base doesn't have to be ten, it can be any number based on the question being solved**


# 3. Summary

Answer the following questions.

### Which function was the easiest to understand?
**_math.sqrt()_**

### Which function was the most difficult?

**_math.factorial()_**

### Which function do you think you will use the most?

**_math.log()_**

### What did you learn about required and optional parameters?

the required parameters have to be present, otherwise a TypeError will occur
the optional parameters 

### What did you learn about reading Python documentation?

**it is very detailed, and I have a lot of learning to do**

# References

**_https://docs.python.org/3/library/math.html_**


Include links to the official Python documentation and any other reputable sources you used.

Example:

- https://docs.python.org/3/library/random.html
