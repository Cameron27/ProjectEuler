from Custom.Math import is_prime

for d in range(1, 1000)[::-1]:
    if is_prime(d):
        period = 1
        while pow(10, period, d) != 1:
            period += 1
        if d-1 == period:
            break
print(d)
