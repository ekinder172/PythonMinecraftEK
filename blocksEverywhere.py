from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def randomBlockLocations(blockType, repeats):
    count = 0
    while count < repeats:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x,z)
        mc.setBlock(x,y,z, 41)
        count += 1
    return count
        

randomBlockLocations(41, 10)
randomBlockLocations(41, 37)
randomBlockLocations(41, 102)







