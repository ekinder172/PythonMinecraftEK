from mcpi.minecraft import Minecraft
mc = Minecraft.create()


import pickle


def sortPair(val1,val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2
    
def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)
    
    
    width = x2 - x1
    height = y2 - y1
    length = z2 - z1
    
    structure = []
    
    print("please wait...")
    
    for row in range(0, height):
        structure.append([])
        for column in range(0, width):
            structure[row].append([])
            for depth in range(0, length):
                block = mc.getBlock(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)
                
    return structure

input("Move to the first position and press ENTER in this window")
pos1 = mc.player.getTilePos()
x1, y1, z1 = pos1.x, pos1.y, pos1.z

input("Move to the opposite corner and press enter in this window")
pos2 = mc.player.getTilePos()
x2, y2, z2 = pos2.x, pos2.y, pos2.z


structure = copyStructure(x1, y1, z1, x2, y2, z2)
pickleFile = open("/home/pi/Documents/minecraft_programs/pickleFile.txt", "wb")
pickle.dump(structure, pickleFile)
pickleFile.close()