## Example

import collections as cl

dq = cl.deque([1,2,3], maxlen=3)
dq.append(4)
dq.appendleft(0)
print(dq)

