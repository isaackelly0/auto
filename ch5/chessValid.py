def isValidChessBoard(obj):
    valid = True
    validPieces = ['wpawn','bpawn','wknight','bknight','wbishop','bbishop','wrook','brook','wqueen','bqueen','wking','bking']
    validBoard = correctBoard()
    count = {
        'white' : 0,
        'black' : 0,
        'wpawn' : 0,
        'bpawn' : 0
    }
    for space, piece in obj.items():
        count.setdefault(piece, 0)
        count[piece] += 1    
        if piece[0] == 'w':
            count['white'] += 1
        elif piece[0] == 'b':
            count['black'] += 1
        if piece not in validPieces:
            valid = False
            break
        elif space not in validBoard:
            valid = False
            break
    if 'wking' not in count or 'bking' not in count:
        valid = False
    if count['wpawn'] > 8 or count['bpawn'] > 8 or count['wking'] != 1 or count['bking'] != 1 or count['white'] > 16 or count['black'] > 16:
        valid = False
    if len(obj) > len(validBoard):
        valid = False
    return valid

def correctBoard():
    letters = ['a','b','c','d','e','f','g','h']
    numbers = ['1','2','3','4','5','6','7','8']
    board = []
    for number in numbers:
        for letter in letters:
            board.append(number+letter)
    return board