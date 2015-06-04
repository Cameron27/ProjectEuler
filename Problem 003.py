from Custom.Math import is_prime
print([x for x in range(3, int(600851475143 ** 0.5)) if 600851475143 % x == 0 and is_prime(x)][-1])
