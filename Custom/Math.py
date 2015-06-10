def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    i = 0
    while count != n:
        i += 1
        if is_prime(i):
            count += 1
    return i

def number_of_divisors(n):
    count = 0
    squroot = int(n ** 0.5)
    for x in range(1, squroot + 1):
        if n % x == 0:
            count += 1
    if squroot ** 2 == n:
        return count * 2 - 1
    else:
        return count * 2
