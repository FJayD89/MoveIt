from blockClass import *


def makeMove(move, blocks_setup):
    name = move[0]
    blocks_setup[name] = moveBlock(move[1], blocks_setup[name])
    return blocks_setup


def moveBlock(magnitude, block):
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


def pathClear(blocks, moving_block_name, board_size, direction):
    # get the block from the name
    moving_block = blocks[moving_block_name]
    # init maximum path length to the edge of the board
    pathLength = (board_size[moving_block.vertical] - moving_block.length)*(direction+1)/2 \
        - moving_block.pos[moving_block.vertical]
    pathLength = abs(pathLength)
    # loops through all board_blocks except for the moving one
    for block in [block for block in blocks.values() if not block.name == moving_block.name]:
        # if block is ahead or behind enough, if dir = 1 need to add the length
        difference = block.pos[moving_block.vertical] - moving_block.pos[moving_block.vertical]\
                     - direction - (moving_block.length-1) * (1 + direction) / 2
        if direction * difference >= 0:
            if difference < pathLength:   # if checking the block is going to actually yield new info
                if block.vertical == 1 - moving_block.vertical:  # if perpendicular
                    lowest_pos = block.pos[block.vertical]
                    if lowest_pos <= moving_block.pos[1-moving_block.vertical] <= lowest_pos + block.length-1:
                        pathLength = abs(difference) - (1 + direction) / 2
                    break
                # if not perpendicular, check if in same line
                if block.pos[1-moving_block.vertical] == moving_block.pos[1-moving_block.vertical]:
                    # if dir = -1, subtract the block legth
                    pathLength = abs(difference) - block.length*(-direction+1)/2

    return pathLength


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


def moves(blocks_setup, board_size):
    possibleMoves = []
    for blockName in list(blocks_setup.keys()):
        for magnitude in [1, -1]:
            move = [blockName, magnitude]
            if moveCheck(blocks_setup, board_size, move):
                possibleMoves.append(move)

    return possibleMoves

# test commit


def winCheck(win_name, win_pos):
    # global checksMade
    # checksMade += 1
    if allBlocks[win_name].x == win_pos[0] and \
            allBlocks[win_name].y == win_pos[1]:
        return True
