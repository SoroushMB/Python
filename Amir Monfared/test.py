# Algorithms Designing
# T --> A (90)(70) --> T = 90s
# 3A --> 3 * 90 = 270s = 3T
# T/2 --> 45s - 35s
# Time (Decrease), Hardware Resources (Decrease)
x = 1 # T
while x <= 5: # 1 - 2 - 3 - 4 - 5 - 6 = 6T
    x += 1 # 2 - 3 - 4 - 5 - 6 = 5T
# 10T = (5 + 4 + 1)T
"""
i = 1 --> (1)T
while i <= n: --> (n + 1)T
    i += 1 --> (n)T

Result : 1 + n + (n-1)
"""
"""
if ---:
    ...
if ---:
    ...
if ---:
    ...
    
if ---:
    ...
elif ---:
    ...
else:
    ...
"""