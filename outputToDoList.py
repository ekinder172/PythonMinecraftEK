from mcpi.minecraft import Minecraft
mc = Minecraft.create()

 



toDoList = open("/home/pi/PythonMinecraftEK/textFile/toDoList.txt" , "r")

for line in toDoList:
    
    mc.postToChat(toDoList.readline())
    
    