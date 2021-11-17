from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

posx = 10
posy = 100
posz = 100
mc.player.setTilePos(posx, posy, posz)
time.sleep(10)
posx = 25
posy = 100
posz = 70
mc.player.setTilePos(posx, posy, posz)