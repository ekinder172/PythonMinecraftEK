from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from flask import Flask
app = Flask(__name__)
@app.route("/")
def showCoord():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    return (x,y,z)
app.run()
    