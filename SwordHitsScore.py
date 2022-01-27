from mcpi.minecraft import Minecraft
mc = Minecraft.create()


import time


name = ""
scoreboard = {}

while True:
    # Get the player's name
    name = input("What is your name? ")
    
    #Break loop if name is exit
    if name == "exit":
        break
    mc.postToChat("GO!")
    
    time.sleep(6)
    blockHits = mc.events.pollBlockHits()
    
    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is "+ str(blockHitsLength))
    scoreboard[name] = blockHitsLength
    print(scoreboard)