from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 35
state = 6

mc.setBlock(10, 3, -4, 20, 6, -8, block,state)

def getWoolState(color):
    
    if color == "pink":
        blockState = 6
    elif color == "green":
        blockState = 13
    elif color == "light blue":
        blockState = 3
    elif color == "orange":
        blockState = 1
    return blockState
    
        
    
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x,pos.y,pos.z, 35, state)