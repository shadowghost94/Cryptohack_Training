ints = [14, 6, 11]
tableau = []

for x in ints:
    for i in range(28):
        if ((i*i)%29 == x):
            tableau.append([x,i])

print(tableau)
