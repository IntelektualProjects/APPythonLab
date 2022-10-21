# binomial coefficient formula (a + b)! / b! * a!
# combination formula

import time
import math
start = time.time()

a = 20
b = 20
ans = math.factorial(a + b) / (math.factorial(b) * math.factorial(a))
print(ans)
end = time.time()
print("Time", end - start)