from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
count = 0
def makeMelon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    randx = random.randint(-6,6)
    randz = random.randint(-6,6)

    mc.setBlock(x+ randx,y,z + randz, 103)
    time.sleep(2)


while count<=6:
    makeMelon()
    count+= 1




