spiral = [[0 for a in range(1001)] for b in range(1001)]
iteration = 1
loop_size = 3
y = int(len(spiral) / 2)
x = y

spiral[y][x] = iteration
iteration += 1
x += 1

while loop_size <= len(spiral):
    for loop1 in range(loop_size - 2):
        spiral[y][x] = iteration
        y += 1
        iteration += 1
    for loop2 in range(loop_size - 1):
        spiral[y][x] = iteration
        x -= 1
        iteration += 1
    for loop3 in range(loop_size - 1):
        spiral[y][x] = iteration
        y -= 1
        iteration += 1
    for loop4 in range(loop_size):
        spiral[y][x] = iteration
        x += 1
        iteration += 1
    loop_size += 2

print(sum([spiral[i][i] for i in range(len(spiral))]) + sum([spiral[len(spiral) - j - 1][j] for j in range(len(spiral))]) - 1)
