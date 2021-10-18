import blockClass


def emptyZoz(x):
    ret = []
    for i in range(x):
        ret.append('.')
    return ret


class Board:
    board = []
    cmds = {'l': [0, -1],
            'u': [1, 0],
            'r': [0, 1],
            'd': [-1, 0]
            }
    OGs = []

    def blockCheck(self, block):
        # assumes block is wholly inside the board
        for segment in range(block.length):
            segmentX = block.x + (1 - block.vertical)*segment
            segmentY = block.y + block.vertical*segment
            if not self.board[segmentX][segmentY] == '.':
                return False
        return True

    def addBlock(self, block):
        for i in range(block.height):
            for j in range(block.width):
                self.board[j + block.x][i + block.y] = block.name

    def addOptimalBlock(self, block):
        for i in range(block.length):
            self.board[(1-block.vertical)*i + block.x][block.vertical*i + block.y] = block.name

    def emptyBoard(self):
        self.board = []
        for i in range(self.width):
            self.board.append(emptyZoz(self.height))

    def winCheck(self):
        # win condition: block name is at the correct x/y and not to the left or the top of said x/y
        if self.board[self.winX][self.winY] == self.winBlock and \
                not self.board[self.winX-1][self.winY] == self.winBlock and \
                not self.board[self.winX][self.winY-1] == self.winBlock:
            return True
        return False

    def update(self):
        self.emptyBoard()
        for block in self.blocks:
            isBlock = type(block) is blockClass.Block
            if isBlock:
                self.addBlock(block)
            else:
                self.addOptimalBlock(block)

    def __init__(self, width, height, blocks, win_block, win_x, win_y):
        self.width, self.height, self.blocks, self.winBlock, self.winX, self.winY = \
            width, height, blocks, win_block.name, win_x, win_y

        available = True

        relevantPos = (1 - win_block.vertical) * win_block.x + win_block.vertical * win_block.y
        relevantWinPos = (1 - win_block.vertical) * self.winX + win_block.vertical * self.winY
        distToExit = relevantWinPos - relevantPos
        self.winDirection = int(distToExit / (2 * abs(distToExit)) + 0.5)
        self.emptyBoard()

        # standard = int(blocks[0])

        # standard block procedure
        # for block in self.blocks:
        #     for i in range(block.height):
        #         for j in range(block.width):
        #             if not self.board[j + block.x][i + block.y] == '.':
        #                 available = False
        #                 badBlock = block.name

        # optimal block procedure
        for block in self.blocks:
            for i in range(block.length):
                if not self.board[(1 - block.vertical) * i + block.x][block.vertical * i + block.y] == '.':
                    available = False
                    print(block.name + ' is not in an available position')

        if available:
            self.update()

    def writeOut(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[j][i], end='')
            print('')
        print('')

    def moveCheck(self, block, cmd):
        moveCheck = True

        newX = block.x + self.cmds[cmd][0]
        newY = block.y + self.cmds[cmd][1]

        # out of bounds check
        if newX + block.width-1 >= self.width or newX < 0 or \
                newY + block.height-1 >= self.height or newY < 0:
            print('Movement is out of bounds!')
            return False

        # collision checks
        if cmd == 'u':
            for i in range(block.width):
                if not self.board[block.x + i][newY] == '.':
                    moveCheck = False

        if cmd == 'd':
            for i in range(block.width):
                if not self.board[block.x + i][newY + (block.height-1)] == '.':
                    moveCheck = False

        if cmd == 'l':
            for i in range(block.height):
                if not self.board[newX][block.y + i] == '.':
                    moveCheck = False

        if cmd == 'r':
            for i in range(block.height):
                if not self.board[newX - (block.width-1)][block.y + i] == '.':
                    moveCheck = False

        if not moveCheck:
            print('Movement causes collision!')
        return moveCheck

    def moveBlock(self, block, cmd):

        if self.moveCheck(block, cmd):
            # print('valid')
            block.x += self.cmds[cmd][0]
            block.y += self.cmds[cmd][1]
            self.update()
            self.writeOut()
        else:
            self.writeOut()

    def reset(self):
        self.blocks = self.OGs
        self.update()

    def moves(self):
        moves = []
        for block in self.blocks:
            for cmd in self.cmds.keys():
                if self.moveCheck(block, cmd):
                    moves.append(block.name + cmd)

        return moves
