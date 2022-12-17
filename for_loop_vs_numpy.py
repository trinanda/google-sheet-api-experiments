import time

import numpy as np

# record start time
start = time.time()

numpy_arr = np.array([1, 2, 3])
normal_arr = [1, 2, 3]

# for x in range(3):
#     print(x)
for x in numpy_arr:
  print(x)

end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")
