game = [['_','_','_'],['_','_','_'],['_','_','_']]
moves = [[0,0],[0,1],[0,2],[1,1],[1,2]]
for next in range(0, 5):
    if next % 2 == 0:
        symbol = 'x'
    else:
        symbol = 'o'
    game[moves[next][0]][moves[next][1]] = symbol
    for row in game:
        print(row)
    print()

#O Wins :)
game[2][1] = 'o'
for row in game:
    print(row)
print()

#Find smallest value
x = [25, 2, 142, 0, 54, -1]
kitty = x[0]
for num in x:
    if num < kitty:
        kitty = num
print("The smallest value in x is " + str(kitty))