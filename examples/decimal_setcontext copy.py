## Example

import decimal as dec

new_ctx = dec.Context(prec=3, rounding=dec.ROUND_DOWN)
dec.setcontext(new_ctx)

print(dec.Decimal(1) / dec.Decimal(3))
print(dec.getcontext().prec)

