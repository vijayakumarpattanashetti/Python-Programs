#import all necessary packages
import time, datetime, sys, select, smtplib
import RPi.GPIO as GPIO
#get additional required classes also
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
fromid='tormundg998@gmail.com'
toid = 'tormundg998@gmail.com'
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login(fromid,"#D0054321")
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if dist>=11 and dist<=13.5:
                now =datetime.datetime.now()
                t=now.strftime("%Y-%m-%d at %H:%M:%S")
                msg = MIMEMultipart()
                msg['From'] = fromid
                msg['To'] = toid
                msg['Subject'] = "Smart Bin Info"
                body = "Smart Bin is reaching half full. Please take care. "+t
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s.sendmail(fromid, toid, text)
                print('done')
            if dist>=0 and dist<=6:
                now =datetime.datetime.now()
                t=now.strftime("%Y-%m-%d at %H:%M:%S")
                msg = MIMEMultipart()
                msg['From'] = fromid
                msg['To'] = toid
                msg['Subject'] = "Smart Bin Info"
                body = "Smart Bin is almost full. Please take care. "+t
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s.sendmail(fromid, toid, text)
                print('done')
            time.sleep(3)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
