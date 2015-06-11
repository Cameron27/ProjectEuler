answer = 0
maxCount = 0
for x in range(1, 1000000):
    start = x
    count = 1
    while True:
        if x == 1:
            if count > maxCount:
                maxCount = count
                answer = start
            break
        elif x % 2 == 0:
            x = int(x / 2)
        else:
            x = x * 3 + 1
        count += 1
print(answer)
