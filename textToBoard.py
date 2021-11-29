from blockClass import OptimalBlock, blocks
from boardClass import Board


def textToBoard(file_name, win_name, win_x, win_y):
    f = open(file_name, 'r')
    txt = f.read()
    boardLines = txt.split('\n')

    names = blocks.keys()
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
                if not x == len(boardLines)-1:
                    peek = boardLines[y][x + 1]
                if peek == cell:
                    vertical = 0
                boardBlocks.append(OptimalBlock(1, vertical, x, y, cell))
                continue

            # thus, cell is in names, so let's find it and incr that length
            blocks[cell].length += 1

    for i in range(len(boardBlocks)):
        if boardBlocks[i].name == win_name:
            boardBlocks[0], boardBlocks[i] = boardBlocks[i], boardBlocks[0]

    return Board(len(boardLines[0]), len(boardLines), boardBlocks, boardBlocks[0], win_x, win_y)


# textToBoard('boards/board.txt', 'x', 4, 2)
print('')
