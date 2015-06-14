def alphabetical_value(word):
    letter_value = {y: x + 1 for x, y in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    return sum([letter_value[z] for z in word])

txt = open('Problem 022.txt').read()
txt = txt.split(',')
txt = [y.replace('"', '').replace(' ', '') for y in txt]
txt.sort()
print(sum([alphabetical_value(x) * (txt.index(x) + 1) for x in txt]))
