# Python Module Exploration

> **Student Name: Benon Nyabuto**  
> **Date: 25/August/2026**  

---

# Module Name

Replace this heading with the name of your chosen Python module.

Example:

```python
decimal
```

---

# 1. Module Overview

## Purpose

Describe what the module is used for.

The decimal module is a built-in Python library used for fixed-point and floating-point arithmetic. It provides a highly accurate alternative to Python's native float data type, allowing programs to perform decimal math exactly the way humans do by hand


## Why is this module important?

Explain why Python includes this module and what problems it helps solve.

Python includes the decimal module to solve the inherent precision limitations of standard coputer binary floating-point arithmetic(float). Because computers represent numbers in base-2 (binary) rather than base-10 (decimal), certain common numbers cannot be stored precisely. For example, in native Python, evaluating 0.1+0.2 results in 0.30000000000000004, which can ruin critical calculations.

The decimal module solves this problem by using base 1- arithmetic, meaing numbers like 0.1 are represented exactly as written. It gives developers full control over exact rounding rules, allows changes to the global level of mathematical precision (e.g. tracking up to 28 or more significant digits), and handles industry-mandated legal and financial mathematical standards without error.

## Real-world Applications

List at least three practical applications.

1. Banking and Financial Ledger Calculations: Financial systems use it to process invoices, calculated compound interesr, and apply taxes, ensuring that transactions match legal accounting regulations down to the fraction of a cent.

2. E-commerce Point Of Sale (POS) System: Online retail platforms use it to calculate discounts, shipping costs, and localized sales taxes (like VAT) to prevent micro-rounding errors that could alter a cusotmer's final receipt total.

3. Scientific Instruments and High-Precision Labs: Physiscs and engineering simulators use it when measuring miniscule physical quantities, where an inaccurate trailing decimal place could throw off the trajectory of a model or ruin a sensitive chemical formula.
---

# 2. Functions

Choose **five commonly used functions** from your module.

all functions found in the modules directory


# 3. Summary

Answer the following questions.

### Which function was the easiest to understand?



### Which function was the most difficult?



### Which function do you think you will use the most?


### What did you learn about required and optional parameters?



### What did you learn about reading Python documentation?



# References

Include links to the official Python documentation and any other reputable sources you used.

Example:

- https://docs.python.org/3/library/decimal.html#decimal.Decimal
