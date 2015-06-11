months = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
day = 2
count = 0
for y in range(1, 101):
    for x in range(12):
        if day == 7:
            count += 1
        elif day > 7:
            day -= 7
        day += months[x]
        if y % 4 == 0 and x == 1:
            day += 1
print(count)
