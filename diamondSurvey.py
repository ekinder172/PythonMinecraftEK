from mcpi.minecraft import Minecraft
import sys
mc = Minecraft.create()
pos = mc.player.getTilePos()
x,y,z = pos.x ,pos.y,pos.z
a = 0
for i in range(0,49):
    diamond = mc.getBlock(x,y - a,z)
    print(diamond)
    a = a + 1
    if diamond == 56:
        message = "There are diamonds ", a , " blocks below you"
        mc.postToChat(message)
        sys.exit()
mc.postToChat("no diamonds")
    