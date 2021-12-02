from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 82
y = 6
z = 113
melon = 103
block = mc.getBlock(x, y, z)

noMelon = block == melon

mc.postToChat("You need to get some food: " + str(noMelon))