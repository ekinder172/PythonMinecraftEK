from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 41
y = 2
z = 42
air = 0
gift = mc.getBlock(x,y,z)
if gift != 0:
    if gift == 57:
        mc.setBlocks(x-1,y,z+1, air)
        
    
    

else:
    mc.postToChat("Place an offering on the pedestal")
    