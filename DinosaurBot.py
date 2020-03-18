from numpy import *
from PIL import ImageGrab, ImageOps
import pyautogui as py

#this code should be played on the website http://www.trex-game.skipser.com/

def pressSpace():
    py.keyDown('space')
    py.keyUp('space')

def IMG(): 
    Box=(488,407,576 ,441)   
    #This code for the box works differently on different computers, because of dimensions                              
    #Box=(974,882,1077,812)
    #Box=(167,390,270,420)   
    image=ImageGrab.grab(Box)
    image=ImageOps.grayscale(image)
    arr=array(image.getcolors())
    return arr.sum()
                        
def main():   
    x=0         
    while(1): 
        if(IMG() !=3337):
            pressSpace()
            x=x+1
            print(f"      Jumping "+str(x)+" times")


main()

