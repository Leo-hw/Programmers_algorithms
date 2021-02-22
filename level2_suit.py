import math
import numpy as np

n = np.random.randint(1, 10000000)

print(n)
def cal(n):
    while(True):
        battery = 1
        if n % 2 == 0:
            number = n/2

        else:
            if n == 1:
                number = (n-1)/2
                battery += 1
                break
    print(battery)
    return battery

cal(n)


