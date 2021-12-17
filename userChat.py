from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    userInput = input("Enter a command: ")
    if userInput == "Exit":
        mc.postToChat("Ok Nerd")
        break
        
    elif userInput != "Exit":
        mc.postToChat("Ok then Imma keep talking then")
        time.sleep(1)
        mc.postToChat("why does Psalm where a nike jumpsuit every day???")
    print(userInput)
print("Loop Exited")
    
    
    