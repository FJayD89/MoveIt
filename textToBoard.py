from blockClass import OptimalBlock, allBlocks
from betterSearch import moves


def textToBoard(file_name, win_name):
    f = open(file_name, 'r')
    txt = f.read()
    boardLines = txt.split('\n')
    lineLength = len(boardLines[0])
    names = allBlocks.keys()
    boardBlocks = []

    for y in range(len(boardLines)):
        for x in range(len(boardLines[0])):

            cell = boardLines[y][x]

            if cell == '.':
                continue

            # if there is a char not yet found
            if cell not in names:
                # check verticality and create a somewhat empty new optimalBlock
                vertical = 1
                peek = '.'
                if not x == lineLength-1:
                    peek = boardLines[y][x + 1]
                if peek == cell:
                    vertical = 0
                boardBlocks.append(OptimalBlock(1, vertical, x, y, cell))
                continue

            # thus, cell is in names, so let's find it and incr that length
            allBlocks[cell].length += 1

    # find winBlock index and make it first in the list
    # relies on there being a block with the win_name
    winBlock = 0
    for i in range(len(boardBlocks)):
        if boardBlocks[i].name == win_name:
            winBlock = boardBlocks[i]
            boardBlocks[0], boardBlocks[i] = boardBlocks[i], boardBlocks[0]

    # create a dict name:block
    boardBlocks = {block.name: block for block in boardBlocks}

    return [[len(boardLines[0]), len(boardLines)], boardBlocks, txt]


if __name__ == "__main__":
    board = textToBoard('boards/' + input('Enter the filename:'), input('Enter winName:'))
    print(moves(board[1], board[0]))
