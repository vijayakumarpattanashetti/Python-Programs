#Motion Detection + Capturing pic
from gpiozero import MotionSensor
import time, os
pir=MotionSensor(4)
time.sleep(3)
if pir.motion_detected:
    print("Motion Detected")
    os.system("fswebcam -F 3 --fps 20 -r 800*600 /home/pi/Desktop/v.jpg")
    print("Intruder Alert")
else:
    print("Needn't worry.")