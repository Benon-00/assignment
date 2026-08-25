## Example

import decimal as dec

ctx = dec.getcontext()
print(ctx.prec)

ctx.prec = 4
print(dec.Decimal(1) / dec.Decimal(3))

