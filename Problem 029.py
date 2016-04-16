terms = [a ** b for a in range(2, 101) for b in range(2, 101)]
answers = []
for x in terms:
    if x not in answers:
        answers.append(x)
print(len(answers))
