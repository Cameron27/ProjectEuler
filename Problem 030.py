print(sum([x for x in range(10, 1000000) if x == sum(y ** 5 for y in [int(y) for y in str(x)])]))