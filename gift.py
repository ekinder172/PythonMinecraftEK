from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 71
y = 8
z = 106
gift = mc.getBlock(x,y,z)

if gift == 57:
    mc.postToChat("Thank for the diamond")
    
elif gift == 6:
    mc.postToChat("I guess a tree sapling is as good as diamonds")
    

else:
    mc.postToChat("Bring a gift to" + str(x) + "," + str(y) + "," + str(z))