from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks = [48,67,4,4,4,4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10
for i in range(height):
    brokenWall.append([])
    for e in range(0, width):
        brokenWall[i].append(brokenBlock())

for row in brokenWall:
    for blocks in row:
        mc.setBlock(x, y, z, blocks)
        x += 1
    y += 1
    x = pos.x