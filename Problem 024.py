from itertools import permutations
count = 0
for x in permutations("0123456789"):
    count += 1
    if count == 1000000:
        print(''.join(x))
        break
