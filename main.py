board_list = list(range(1,10))

def draw_board(board_list):
    print ("-------------")
    for i in range(3):
        print ("|", board_list[0+i*3], "|", board_list[1+i*3], "|", board_list[2+i*3], "|")
        print ("-------------")

def put(board_list):
    counter = 0
    x = 9
    win = True
    while win:
        if counter % 2 == 0:
            print('Select the index to put X')
            draw_board(board_list)
            index = int(input())
            for i in range(x):
                if board_list[index-1] == index:
                    board_list.pop(index-1)
                    board_list.insert(index-1, 'X')
                    draw_board(board_list)
                    break;
                elif board_list[index-1] == 'X':
                    print('Occupied. Select other one.')
                    put(board_list)
                else:
                    print('No. From 1 to 9')
                    put(board_list)
            counter += 1

        else:
            print('Select the index to put Y')
            draw_board(board_list)
            index = int(input())
            for i in range(x-1):
                if board_list[index-1] == index:
                    board_list.pop(index-1)
                    board_list.insert(index-1, 'Y')
                    draw_board(board_list)
                    break;
                elif board_list[index-1] == 'Y':
                    print('Occupied. Select other one.')
                    put(board_list)
                else:
                    print('No. From 1 to 9')
                    put(board_list)
            counter += 1

        if counter > 3:
            if diagonal(board_list) == 'X win by diagonal' or straight(board_list) == 'X win by line':
                print('X win')
                win = False
                break;
            if diagonal(board_list) == 'Y win by diagonal' or straight(board_list) == 'Y win by line':
                print('Y win')
                win = False
                break;
        if counter == 9:
            print('friendship')
            win = False
            break;


def diagonal(board_list):
    #di = True
    #for i in range(3):
    if board_list[0] == 'X' and  board_list[4]== 'X' and  board_list[8]== 'X':
       return 'X win by diagonal'
    if board_list[2] == 'X' and  board_list[4]== 'X' and  board_list[6]== 'X':
        return 'X win by diagonal'
    if board_list[2] == 'Y' and  board_list[4]== 'Y' and  board_list[6]== 'Y':
        return 'Y win by diagonal'
    if board_list[0] == 'Y' and board_list[4] == 'Y' and board_list[8] == 'Y':
        return 'Y win by diagonal'
    return None;

def straight(board_list):
   # str = True
    if board_list[0]=='X' and board_list[1] =='X' and board_list[2]=='X':
        return 'X win by line'
    if board_list[3] =='X' and board_list[4]=='X' and board_list[5]=='X':
         return 'X win by line'
    if board_list[6] == 'X' and board_list[7] == 'X' and board_list[8] == 'X':
        return 'X win by line'
    if board_list[0] == 'X' and board_list[3] == 'X' and board_list[6] == 'X':
        return 'X win by line'
    if board_list[1] == 'X' and board_list[4] == 'X' and board_list[7] == 'X':
        return 'X win by line'
    if board_list[3] == 'X' and board_list[5] == 'X' and board_list[8] == 'X':
        return 'X win by line'

    if board_list[0] == 'Y' and board_list[1] == 'Y' and board_list[2] == 'Y':
        return 'Y win by line'
    if board_list[3] == 'Y' and board_list[4] == 'Y' and board_list[5] == 'Y':
        return 'Y win by line'
    if board_list[6] == 'Y' and board_list[7] == 'Y' and board_list[8] == 'Y':
         return 'Y win by line'
    if board_list[0] == 'Y' and board_list[3] == 'Y' and board_list[6] == 'Y':
        return 'Y win by line'
    if board_list[1] == 'Y' and board_list[4] == 'Y' and board_list[7] == 'Y':
        return 'Y win by line'
    if board_list[2] == 'Y' and board_list[5] == 'Y' and board_list[3] == 'Y':
        return 'Y win by line'

    return None;

put(board_list)
