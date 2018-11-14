import pyglet
from pyglet.gl import *
import datetime
import math
import time
#from pyglet.gl import GL_AMBIENT_AND_DIFFUSE, glBegin, glClearColor
window = pyglet.window.Window(resizable= True, width = 800, height = 800, caption = "Clock" )


def hourhandxy(length):
    now = datetime.datetime.now()
    timeH = ((now.hour + now.minute/60))
    if timeH > 12 :
        timeH -= 12
    if 3<timeH<6 or  9<timeH<12:
        angle = 90 -  (timeH  % 3) * 30
    else :
        angle = 0 -  (timeH  % 3) * 30
    #print (angle, "angle")
    #print (timeH, "hours")
    x = round((math.sin(math.radians(angle))) * length)
    y = round((math.cos(math.radians(angle))) * length)
    if 0<=timeH<3:
        return (-x, (y))
    if 3<=timeH<6:
        return (x,-abs(y))
    if 6<=timeH<9:
        return (-abs(x),-abs(y))
    if 9<=timeH<12:
        return (-abs(x),y)

def minutehandxy(length):
    now = datetime.datetime.now()
    timeM = (now.minute )
    if 15<timeM<30 or  45<timeM<60:
        angle = 90 -   (timeM  % 15)  * 6
    else :
        angle = (timeM  % 15)  * 6
    x = round((math.sin(math.radians(angle))) * length)
    y = round((math.cos(math.radians(angle))) * length)
    if 0<=timeM<15:
        return (x,y)
    if 15<=timeM<30:
        return (x,-abs(y))
    if 30<=timeM<45:
        return (-abs(x),-abs(y))
    if 45<=timeM<60:
        return (-abs(x),y)

    
def secondhandxy(length):
    now = datetime.datetime.now()
    timeS = (now.second + now.microsecond/1000000)
    if 15<timeS<30 or  45<timeS<60:
        angle = 90 -   (timeS  % 15)  * 6
    else :
        angle = (timeS  % 15)  * 6
    x = round((math.sin(math.radians(angle))) * length)
    y = round((math.cos(math.radians(angle))) * length)
    if 0<=timeS<15:
        return (x,y)
    if 15<=timeS<30:
        return (x,-abs(y))
    if 30<=timeS<45:
        return (- abs(x),- abs(y))
    if 45<=timeS<60:
        return (-abs(x),y)

def timetocolor():
    now = datetime.datetime.now()
   # return  (((round(now.second + now.microsecond/1000000*(4.25)))/100))
    b =  round((((1.666666 *( now.second + now.microsecond/1000000))/100)),2)
    a = 1-b 
   
    return (a,b)
frame = 0
def update_frame(x , y):
    global frame
    if frame == None :
        frame = 0
    else:
        frame += 1
   

@window.event



def on_draw():
    
    pyglet.gl.glClearColor(timetocolor()[0],timetocolor()[0],timetocolor()[0],timetocolor()[0])
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(4)
    glBegin(GL_LINES)
    
    
    gl.glColor3f(timetocolor()[1], timetocolor()[1], timetocolor()[1])
    glVertex2i(+window.width//2,window.height//2)
    glVertex2i( hourhandxy(window.width//4)[0] +window.width//2, hourhandxy(window.height//4)[1] +window.height//2)
    
    
    gl.glColor3f(timetocolor()[1], timetocolor()[1],timetocolor()[1] )
    glVertex2i(+window.width//2,+window.height//2)
    glVertex2i( minutehandxy(window.width//3)[0] +window.width//2, minutehandxy(window.height//3)[1] +window.height//2)

    gl.glColor3f(timetocolor()[1], timetocolor()[1],timetocolor()[1])
    glVertex2i(+window.width//2,+window.height//2)
    glVertex2i( secondhandxy(window.width//2.2)[0] +window.width//2, secondhandxy(window.height//2.2)[1] +window.height//2)

    glEnd()
    
pyglet.clock.schedule(update_frame, 1/500)              
pyglet.app.run()


    
