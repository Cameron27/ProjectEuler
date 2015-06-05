def problem_9():
    for x in range(1, 1001):
        for y in range(1, 1001 - x):
            if x ** 2 + y ** 2 == (1000 - x - y) ** 2:
                return x * y * (1000 - x - y)

print(problem_9())
