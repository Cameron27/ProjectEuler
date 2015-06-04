def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, int(n ** 0.5)):
        if n % x == 0:
            return False
    return True

def max(list):
    answer = 0
    for x in list:
        if x > answer:
            answer = x
    return answer
