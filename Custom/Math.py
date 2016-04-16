def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    try:
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
    except TypeError:
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
    squrot = int(n ** 0.5)
    for x in range(1, squrot + 1):
        if n % x == 0:
            count += 1
    if squrot ** 2 == n:
        return count * 2 - 1
    else:
        return count * 2

def divisors(y):
    output = [1]

    largest = int(y ** 0.5)
    if largest * largest == y:
        output.append(largest)
    else:
        largest += 1

    for x in range(2, largest):
        if y % x == 0:
            output.append(x)
            output.append(int(y / x))
    return output

def index_of_fib_number_with_limit(limit):
    a = 0
    b = 1
    count = 1
    while True:
        count += 1
        a, b = b, a + b
        if b > limit:
            return count

