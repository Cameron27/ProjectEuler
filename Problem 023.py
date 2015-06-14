from Custom.Math import divisors
abundant_numbers = set([x for x in range(2, 28123) if sum(divisors(x)) > x])

def is_not_sum_of_abundant_numbers(n):
    for x in abundant_numbers:
        if x > n:
            return True
        elif n - x in abundant_numbers:
            return False
    return True

possible = [y for y in range(1, 28123) if is_not_sum_of_abundant_numbers(y)]
print(sum(possible))
