# CutiePi-RPI-Musicbox
Raspberry PI Python app <br>
<br>
Grandbaby's first PI - Music Box <br>
<br>
Simple Python3 script developed for Version 2 of a Raspberry Pi music box project @ http://ventures.tpedersen.net/errata/raspberrypi/cutiepi.  Simply plays a series of sounds (wav files) and flashes LEDs when button is pressed.  Sound files are hardcoded, swaped in/out for different occasions - e.g. Christmas sounds, current favortie creature - like Elmo.  Used a large button and LED light bar to attract/hold baby's attention.  Script also runs in harmony with Shairport-Sync ... waits until shairport is done playing before playing one of its own sounds.<br>
<br>
Default GPIO assigments/usage:<br>
Red LED @ GPIO 17 <br>
Green LED @ GPIO 27 <br>
Blue LED @ GPIO 4 <br>
Button @ GPIO 2 <br>
<br>
Sound files must be in /home/pi/cutiepi/cutiesounds to facilitate running the script as a service - edits required if you move stuff around - will play with alternatives to absolute names in future.  CutiePi Cycles thru playing sound1.wav, sound2.wav, sound3.wav and song.wav each time button is pressed.  LEDs blink while sound is playing.<br>
<br>
Run time arguments<br>
debug - displays a bunch of stuff<br>
sim - run w/o GPIO.  Enter key to simulate button press. <br>
