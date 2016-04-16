import time
x = time.time()

from Custom.Math import is_prime
highest = 0
product = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while True:
            if is_prime(n ** 2 + a * n + b):
                n += 1
            else:
                if n > highest:
                    highest = n
                    product = a * b
                break
print(product)
