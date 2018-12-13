import sys
import time
import pygame.mixer
from gpiozero import Button
from gpiozero import LED
from pygame.mixer import Sound

# -- Change History --
# Dec 2017 - V3 - Added Simulation_Mode ('sim' in arg) to use with no GPIO
#               - Simplify Versioning: ABS dir changed to /home/pi/cutiepi/
# --------------------

red = LED(17)
green = LED(27)
yellow = LED(22)
blue = LED(4)
button = Button(2)
Debug_mode = False
Simulation_mode = False

def LightsOut():
    red.off()
    green.off()
    blue.off()
    yellow.off()

def LightBlinker(delay,led1,led2,led3,led4):
    led1.blink()
    time.sleep(.15)
    led2.blink()
    time.sleep(.15)
    led3.blink()
    time.sleep(.15)
    led4.blink()

def Wait_for_Button():
    if Simulation_mode:
        try:
            input("Press ENTER to simulate button press")
        except SyntaxError:
            pass
    else:
        button.wait_for_press()
        
def Play(sound_file):
    if Debug_mode:
        print ("playing song")
    mixer_init = False
    
    while not mixer_init:
        try:
            if Debug_mode:
                print ("attempting to init mixer")
            pygame.mixer.init()
            if Debug_mode:
                print ("mixer init complete")
            mixer_init = True

        except:
            if Debug_mode:
                print ("Waiting for mixer")
            time.sleep(10)

        continue
        
    pygame.mixer.init()
    sound = Sound(sound_file)
    sound.play()
    if Debug_mode:
        print ("waiting for song")
    while pygame.mixer.get_busy():
        if button.is_pressed:
            if Debug_mode:
                print ("Button!  Stopping Sound!")
            if button.is_pressed:
                if Debug_mode:
                    print ("button was pressed after stop - wating")
                button.wait_for_release()
                break
        continue
    if Debug_mode:
        print ("stopping current sound")
    sound.stop()
    pygame.mixer.quit()

# main

args = sys.argv

if 'debug' in args:
    print ("running in debug mode")
    Debug_mode = True

if 'sim' in args:
    print ("running in simulation mode - no button!")
    Simulation_mode = True
    
LightsOut()

while True:
    
    Wait_for_Button()
    if Debug_mode:
        print ("1st Button press ... blinking lights")
    LightBlinker(.15,yellow,green,blue,red)
    Play("/home/pi/cutiepi/cutiesounds/sound1.wav")
    LightsOut()
        
    Wait_for_Button()
    if Debug_mode:
        print ("2nd Button press ... blinking lights")
    LightBlinker(.15,green,red,yellow,blue)
    Play("/home/pi/cutiepi/cutiesounds/sound2.wav")
    LightsOut()

    Wait_for_Button()
    if Debug_mode:
        print ("3rd Button press ... blinking lights")
    LightBlinker(.15,blue,yellow,red,green) 
    Play("/home/pi/cutiepi/cutiesounds/sound3.wav")
    LightsOut()
    
    Wait_for_Button()
    if Debug_mode:
        print ("4nd Button press ... blinking lights")
    LightBlinker(.15,red,blue,green,yellow)
    Play("/home/pi/cutiepi/cutiesounds/song.wav")
    Wait_for_Button()
    LightsOut()

    continue
