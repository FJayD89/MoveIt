from blockClass import *


def makeMove(move, blocks_setup):
    blockName = move[0]
    magnitude = move[1]
    # either create a new block when 'moving' it
    # movingBlock = blocks_setup[blockName]
    # blocks_setup[blockName] = makeMovedBlock(magnitude, movingBlock)

    # or just change the pos of the existing one
    blocks_setup[blockName].pos[blocks_setup[blockName].vertical] += magnitude

    return blocks_setup


def makeMovedBlock(magnitude, block):
    newBlock = fromBlock(block)
    newBlock.pos[newBlock.vertical] += magnitude
    return newBlock


def equivalent(move_list1, move_list2, blocks_setup):

    activeBlockList = dict(blocks_setup)

    for move in move_list1:
        makeMove(move, activeBlockList)

    setup1 = dict(activeBlockList)

    activeBlockList = dict(blocks_setup)

    for move in move_list2:
        makeMove(move, activeBlockList)

    setup2 = dict(activeBlockList)

    eqiv = list(setup2.values()) == list(setup1.values())

    return eqiv


def spaceEmpty(blocks_setup, pos):
    for block in [block for block in blocks_setup.values() if block.pos[1-block.vertical] == pos[1-block.vertical]]:
        if block.pos[block.vertical] <= pos[block.vertical] <= block.pos[block.vertical] + block.length - 1:
            return False
    return True


def pathClear(blocks_setup, moving_block_name, board_size, direction):
    # get the block from the name
    moving_block = blocks_setup[moving_block_name]
    # init maximum path length to the edge of the board
    pathLength = (board_size[moving_block.vertical] - moving_block.length)*(direction+1)/2 \
        - moving_block.pos[moving_block.vertical]
    pathLength = abs(pathLength)
    # loops through all board_blocks except for the moving one
    for block in [block for block in blocks_setup.values() if not block.name == moving_block.name]:
        # if block is ahead or behind enough, if dir = 1 need to add the length
        difference = block.pos[moving_block.vertical] - moving_block.pos[moving_block.vertical]\
                     - direction - (moving_block.length-1) * (1 + direction) / 2
        if direction * difference >= 0:
            if abs(difference) < pathLength:   # if checking the block is going to actually yield new info
                if block.vertical == 1 - moving_block.vertical:  # if perpendicular
                    lowest_pos = block.pos[block.vertical]
                    if lowest_pos <= moving_block.pos[1-moving_block.vertical] <= lowest_pos + block.length-1:  # if in line of sight
                        # pathLength = abs(difference) - (1 + direction) / 2
                        pathLength = abs(difference)
                        continue
                # if not perpendicular, check if in same line
                if block.pos[1-moving_block.vertical] == moving_block.pos[1-moving_block.vertical]:
                    # if dir = -1, subtract the block legth
                    pathLength = abs(difference) - (block.length-1)*(-direction+1)/2

    return int(pathLength)


def pathBlocked(blocks_setup, moving_block_name, direction):
    # get the block from the name
    moving_block = blocks_setup[moving_block_name]

    # loops through all board_blocks except for the moving one
    for block in [block for block in blocks_setup.values() if not block.name == moving_block.name]:
        # if block is ahead or behind enough, if dir = 1 need to add the length
        difference = block.pos[moving_block.vertical] - moving_block.pos[moving_block.vertical] \
                     - direction - (moving_block.length - 1) * (1 + direction) / 2
        if direction * difference >= 0:
            if block.vertical == 1 - moving_block.vertical:  # if perpendicular
                lowest_pos = block.pos[block.vertical]
                if lowest_pos <= moving_block.pos[1 - moving_block.vertical] \
                        <= lowest_pos + block.length - 1:  # if in line of sight
                    return True
            # if not perpendicular, check if in same line
            if block.pos[1 - moving_block.vertical] == moving_block.pos[1 - moving_block.vertical]:
                return True

    return False


def moveCheck(blocks_setup, board_size, move):
    name = move[0]
    magnitude = move[1]
    block = blocks_setup[name]
    half = (block.length - 1) / 2
    pos = list(block.pos)
    pos[block.vertical] = block.pos[block.vertical] + half*(1 + abs(magnitude)/magnitude) + magnitude
    if not 0 <= pos[block.vertical] <= board_size[block.vertical] - 1:
        return False
    return spaceEmpty(blocks_setup, pos)


def moves(blocks_setup, board_size, last_move):
    possibleMoves = []
    for blockName in list(blocks_setup.keys()):
        if blockName == last_move[0]:
            continue
        for direction in [1, -1]:
            clear = pathClear(blocks_setup, blockName, board_size, direction)
            shifts = list(range(clear+1)[1:])
            newMoves = [[blockName, direction*shift] for shift in shifts]
            possibleMoves += newMoves
            # if clear >= 1:
            #     possibleMoves.append([blockName, direction])

    return possibleMoves


def winCheck(blocks_setup, win_name, win_pos, exit_direction):
    # global checksMade
    # checksMade += 1
    win_block = blocks_setup[win_name]
    if win_block.pos[win_block.vertical] == win_pos:
        return True

    if not pathBlocked(blocks_setup, win_name, exit_direction):
        print('Path wasn\'t blocked')
        return True

    return False


def boardWriteOut(blocks_setup):
    # will maybe be added
    pass
