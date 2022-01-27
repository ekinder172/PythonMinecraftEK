from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
rB = [12,34,76,32,71,26,54]
a = random.choice(rB)
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
mc.setBlock(x, y - 1, z, a)
