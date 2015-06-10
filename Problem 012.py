from Custom.Math import number_of_divisors
n = 1
c = 0
while True:
    c += n
    n += 1
    if number_of_divisors(c) >= 500:
        print(c)
        break
