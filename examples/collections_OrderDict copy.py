## Example

import collections as cl

od = cl.OrderedDict()
od['one']=1
od['two']=2
od['three']=3

od.move_to_end('one')
print(od)

