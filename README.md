# CutiePi-RPI-Musicbox
Raspberry PI Python app 

Grandbaby's first PI - Music Box

Simple Python3 script developed for Version 2 of a Raspberry Pi music box project @ http://ventures.tpedersen.net/errata/raspberrypi/cutiepi.  Simply plays a series of sounds (wav files) and flashes LEDs when button is pressed.  Sound files are hardcoded, I swap in/out sounds for different occasions - e.g. Christmas sounds, current favoirtie creature - like Elmo, etc.  Used a large button and LED light bar to attract/hold baby's attention.  Script also runs in harmony with Shairport-Sync ... waits until shairport is done playing before playing one its sounds.

Default GPIO assigments/usage:
Red LED @ GPIO 17 
Green LED @ GPIO 27 
Blue LED @ GPIO 4
Button @ GPIO 2

Sound files must be in /home/pi/cutiepi/cutiesounds to facilitate running the script as a service.
Cycles thru playing sound1.wav, sound2.wav, sound3.wav and song.wav each time button is pressed.  LEDs blink while sound is playing.

Run time arguments
debug - displays a bunch of stuff
sim - run w/o GPIO.  Enter key to simulate button press. 


