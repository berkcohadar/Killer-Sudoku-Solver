def solve(bo,cages,possibles):
    update_possibles(possibles,bo)
    eliminate_possibilities(possibles,bo,cages)
    for i in possibles:
        if len(possibles[i]) == 1:
            if  valid(bo, [possibles[i][0]], [i]):
                bo[i[0]][i[1]] = possibles[i][0]
                possibles.pop(i)
                change=i
                break
    try:
        if change:
            if solve(bo,cages,possibles): # recursion
                return True
            else:
                bo[change[0]][change[1]] = 0 # back from recursion
                return False
    except:
        return True
def update_possibles(possibles,bo):
    for keys in possibles:
        # Check row
        for i in range(9):
            if bo[keys[0]][i] != 0:
                try:
                    possibles[keys].remove(bo[keys[0]][i])
                except:
                    pass

        # Check column
        for i in range(9):
            if bo[i][keys[1]] != 0:
                try:
                    possibles[keys].remove(bo[i][keys[1]])
                except:
                    pass

        # Check box
        box_x = keys[1] // 3
        box_y = keys[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] != 0:
                    try:
                        possibles[keys].remove(bo[i][j])
                    except:
                        pass
def find_sums(cage,bo):
    sum = cage[0]
    cells = cage[1]
    empty = []
    filled = []
    result=[]
    
    for cell in cells:
        sum -= bo[cell[1]][cell[0]]
        if bo[cell[1]][cell[0]] == 0:
            empty.append((cell[1],cell[0]))
        elif bo[cell[1]][cell[0]]:
            filled.append((cell[1],cell[0]))
    if len(empty)==1:
        result.append(sum)
    if len(empty)==2:
        for x in range(1,10):
            for y in range(1,10):
                if x+y == sum and x!=y: # x!=y is wrong
                    if valid(bo,(x,y),empty) or valid(bo,(y,x),empty):
                        for num in (x,y):
                            if num not in result:
                                result.append(num)
    if len(empty)==3:
        for x in range(1,10):
           for y in range(1,10):
               for z in range(1,10):
                   if x+y+z == sum and x!=y and x!=z and y!=z: # x!=y is wrong
                       if valid(bo,(x,y,z),empty) or valid(bo,(y,x,z),empty) or valid(bo,(y,z,x),empty) or valid(bo,(x,z,y),empty) or valid(bo,(x,z,y),empty) or valid(bo,(z,x,y),empty)or valid(bo,(z,y,x),empty):
                        for num in (x,y,z):
                            if num not in result:
                                result.append(num)
    if len(empty)==4:
        for x in range(1,10):
           for y in range(1,10):
               for z in range(1,10):
                   for i in range(1,10):
                       if x+y+z+i == sum and x!=y and x!=z and x!=i and y!=z and y!=i and z!=i: # x!=y is wrong
                            for num in (x,y,z,i):
                                if num not in result:
                                    result.append(num)
    return result
def eliminate_possibilities(possibles,bo,cages):
    for cage in cages:
        sums = find_sums(cage,bo)
        for cell in cage[1]:
            try:
                temp = []
                for i in sums:
                    if i in possibles[(cell[1],cell[0])] and valid(bo, [i], [(cell[1],cell[0])]):
                        temp.append(i)
                if possibles[(cell[1],cell[0])]:
                     possibles[(cell[1],cell[0])] = temp
            except:
                pass
def valid(bo, nums, poses):
    for i in range(len(bo[0])):
        for j in range(len(nums)):
            if bo[poses[j][0]][i] == nums[j] and poses[j][1] != i:
                return False
            if bo[i][poses[j][1]] == nums[j] and poses[j][0] != i:
                return False
    for x in range(len(nums)):
        box_x = poses[x][1] // 3
        box_y = poses[x][0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == nums[x] and (i,j) != poses[x]:
                    return False
    return True
def print_board(bo):
    print()
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("_______________________")

board2 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,7,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,6,0,3,0,9,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

possibles = {}
for i in range(9):
    for j in range(9):
        if board2[i][j] == 0:
            possibles[(i,j)] = [1,2,3,4,5,6,7,8,9]

cages = [
    [19,[[0,0],[0,1],[0,2],[1,1]]],
    [17,  [[1, 0],[2, 0],[3,0],[4,0]]],
    [21, [[5, 0],[6, 0],[7,0],[8,0]]],
    [21,  [[2,1],[3,1],[2,2]]],
    [11, [[3,2],[4,1],[4,2]]],
    [16, [[5,1],[6,1]]],
    [5, [[7,1],[8,1]]],
    [12, [[1,2],[0,3],[1,3]]],
    [11, [[5,2],[6,2],[5,3]]],
    [17,  [[7,2],[7,3],[6,3]]],
    [21, [[8,2],[8,3],[7,4],[8,4]]],
    [13,  [[2,3],[2,4]]],
    [11,  [[3,3],[4,3]]],
    [18, [[0,4],[0,5],[0,6],[1,4]]],
    [8, [[3,4],[4,4],[5,4]]],
    [15, [[6,4],[6,5]]],
    [13, [[1,5],[2,5],[1,6]]],
    [16, [[3,5],[3,6],[2,6]]],
    [17, [[4,5],[5,5]]],
    [13, [[7,5],[7,6],[8,5]]],
    [8, [[4,6],[4,7],[5,6]]],
    [16,  [[6,6],[6,7],[5,7]]],
    [22,  [[8,6],[8,7],[7,7],[8,8]]],
    [17, [[0,7],[1,7]]],
    [8, [[2,7],[3,7]]],
    [21, [[0,8],[1,8],[2,8],[3,8]]],
    [18, [[4,8],[5,8],[6,8],[7,8]]]]

print_board(board2)
solve(board2,cages,possibles)
print_board(board2)