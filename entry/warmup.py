side = int(input())

square = [[' ' for a in range(side)] for a in range(side)]

# there is a smarter way for this
for i in range(side):
    square[0][i] = '*'
    square[-1][i] = '*'
    square[i][0] = '*'
    square[i][-1] = '*'

for i in range(side):
    square[i][i] = '*'
    square[i][-i - 1] = '*'

for a in range(side):
    for b in range(side):
        print(square[a][b], end='')
    print('')
