from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = "This is the default message."
mc.postToChat(message)
username = input("Please enter your username")
myMessage=input("Enter something")
mc.postToChat(username + ": " + myMessage)