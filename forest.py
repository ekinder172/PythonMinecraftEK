from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    #write code to spawn a tree
    pos = mc.player.getTilePos()
    x = pos.x + 1
    y = pos.y
    z = pos.z + 1
    mc.setBlocks(x , y, z, x, y + 4, z, 17)
    mc.setBlocks(x - 2, y + 3, z - 2, x + 2, y + 5, z + 2, 18)
    mc.setBlocks(x - 1, y + 5, z - 1, x + 1, y + 6, z + 1, 18)
    mc.setBlocks(x, y + 6, z, x, y + 7, z, 18)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
growTree(x + 7, y, z)
growTree(x + 13, y, z)
growTree(x + 19, y, z)
growTree(x + 25, y, z)
growTree(x + 31, y, z)
growTree(x + 37, y, z)
growTree(x + 43, y, z)
growTree(x + 49, y, z)