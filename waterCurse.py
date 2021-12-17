from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
t = 0
while t < 31:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    t += 1
    time.sleep(1)