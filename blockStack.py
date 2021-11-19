from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = 0
x = 6
y = 5
z = 28
blockType = 103
mc.setBlock(x, y, z, blockType)
while p < 3:
    p += 1
    y += 1
    mc.setBlock(x, y, z, blockType)
