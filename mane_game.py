from itertools import chain

def find_point_in_board(board,number):
    location = []
    x_c = 0
    y_c = 0
    for y in board:
        x_c = 0
        for x in y:
            if (x == number):
                location.append([y_c,x_c])
            x_c += 1
        y_c += 1
    return location

def check_board_equal(list_board):
    a_board = list_board
    list_board = list(chain(*list_board))
    board_elem=set(list_board)
    board_elem.remove(0)
    for x in board_elem:
        if ((list_board.count(x) % 2) != 0):
            print(a_board)
            print("[E] The Number %s = %s is not even !" % (x,list_board.count(x)))
            exit()
    print("[!] Check Successful !")

def check_board_all_zero(board):
    for x in board:
        for y in x:
            if (y!=0):
                return False

    return True


def calculation_a_setps(board):

    if_only_one_round = True
    
    all_steps = []

    # add zero
    new_board = [[0]*21]
    for x in board:
        r = [0]
        for y in x:
            r.append(y)
        r.append(0)
        new_board.append(r)
    new_board.append([0]*21)

    # do ones
    while(True):
        print("-"*40)
        new_board,a_lists = calculation_a_setp(new_board)
        for x in a_lists:
            all_steps.append(x)

        if (len(a_lists) == 0 or if_only_one_round):
            print("[*] Calculated run step ")
            break
        #print(check_board_all_zero(new_board))

    return all_steps

def calculation_a_setp(board):

    check_board_equal(board)
    board_elem=set(list(chain(*board)))
    board_elem.remove(0)
    print(board_elem)
        
    step_lisrs = []

    # frist round
    for x in board_elem:
        elem_locations = find_point_in_board(board,x)
        lene = len(elem_locations)
        for x1 in range(lene):
            for x2 in range(x1+1,lene):
                if (check_one_if_connect(board,elem_locations[x1],elem_locations[x2])):
                    step_lisrs.append([elem_locations[x1],elem_locations[x2]])
                    print(" +  %s <--> %s" %(elem_locations[x1],elem_locations[x2]))
                    x1px,x1py = elem_locations[x1]
                    x2px,x2py = elem_locations[x2]
                    board[x1px][x1py] = 0
                    board[x2px][x2py] = 0

    return board,step_lisrs

def check_one_if_connect(board,pointa,pointb):  
    if (board[pointa[0]][pointa[1]] == 0 ) or (board[pointb[0]][pointb[1]] == 0 ) :
        return False 
    # H
    if (Horizontal(board,pointa,pointb)):
        return True
    # V 
    if (Vertical(board,pointa,pointb)):
        return True
    # 2 lines
    if (two_line(board,pointa,pointb)):
        return True
    # 3 lines
    if (three_line(board,pointa,pointb)):
        return True
    return False

def Horizontal(board,pointa,pointb):
    if (pointa[0]!=pointb[0]):
        return False
    if (pointa[1] > pointb[1]):
        for x in range(pointa[1]-1,pointb[1]-1,-1):
            if ([pointa[0],x]==pointb):
                return True
            if (board[pointa[0]][x]!=0):
                break
    else:
        for x in range(pointa[1]+1,pointb[1]+1,1):
            if ([pointa[0],x]==pointb):
                return True
            if (board[pointa[0]][x]!=0):
                break
    return False

def Vertical(board,pointa,pointb):
    if (pointa[1]!=pointb[1]):
        return False
    if (pointa[0] > pointb[0]):
        for x in range(pointa[0]-1,pointb[0]-1,-1):
            if ([x,pointa[1]]==pointb):
                return True
            if (board[x][pointa[1]]!=0):
                break
    else:
        for x in range(pointa[0]+1,pointb[0]+1,1):
            if ([x,pointa[1]]==pointb):
                return True
            if (board[x][pointa[1]]!=0):
                break
    return False

def two_line(board,pointa,pointb):
    if ((pointa[0] == pointb[0]) or (pointa[1]==pointb[1])):
        return False
    c1 = [pointa[0],pointb[1]]
    c2 = [pointb[0],pointa[1]]
    if (board[c1[0]][c1[1]]==0):
        if (( (Horizontal(board,pointa,c1)) and (Vertical(board,pointb,c1)) ) or ( (Vertical(board,pointa,c1)) and (Horizontal(board,pointb,c1)) )):
            return True
    if (board[c2[0]][c2[1]]==0):
        if (( (Horizontal(board,pointa,c2)) and (Vertical(board,pointb,c2)) ) or ( (Vertical(board,pointa,c2)) and (Horizontal(board,pointb,c2)) )):
            return True
    return False

def three_line(board,pointa,pointb):
    # up
    for y in range(pointa[0]-1,-1,-1):
        d = [y,pointa[1]]
        if (board[d[0]][d[1]]!=0):
            break
        if(two_line(board,d,pointb)):
            return True
    # down
    for y in range(pointa[0]+1,10,1):
        d = [y,pointa[1]]
        if (board[d[0]][d[1]]!=0):
            break
        if(two_line(board,d,pointb)):
            return True
    # left
    for x in range(pointa[1]-1,-1,-1):
        d = [pointa[0],x]
        if (board[d[0]][d[1]]!=0):
            break
        if(two_line(board,d,pointb)):
            return True
    # right
    for x in range(pointa[1]+1,21,1):
        d = [pointa[0],x]
        if (board[d[0]][d[1]]!=0):
            break
        if(two_line(board,d,pointb)):
            return True
    return False



