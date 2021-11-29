from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = "This is the default message."
mc.postToChat(message)
myMessage=input("Enter something")
mc.postToChat(myMessage)