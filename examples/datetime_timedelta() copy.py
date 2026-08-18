## Example

import datetime as dt

today = dt.date.today()
delta = dt.timedelta(days=10, hours=5)
future_date = today + delta
print(future_date)

