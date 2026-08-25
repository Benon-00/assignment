## Example

import decimal as dec

price = dec.Decimal('19.4567')
rounded = price.quantize(dec.Decimal('0.01'), rounding=dec.ROUND_HALF_UP)
print(rounded)

