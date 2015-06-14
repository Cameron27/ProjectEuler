from Custom.Math import divisors
amicable_numbers = []
for x in range(2, 10000):
    sum_of_divisors = sum(divisors(x))
    if x == sum(divisors(sum_of_divisors)) and x != sum_of_divisors:
        amicable_numbers.append(x)
print(sum(amicable_numbers))
