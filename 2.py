#android based advanced security system for women
#import all necessary packages
import android, time, datetime, sys, select, os, smtplib
#get additional required classes also
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#speech recognition
droid = android.Android()
(id,result,error)= droid.recognizeSpeech("Say something")
print (result)
time.sleep(int(3))
#condition for starting the security activites
if (result=="help"):
 now =datetime.datetime.now()
 t=now.strftime("%Y-%m-%d at %H:%M:%S") #gets current date and time 
 print ("Date & time:",t)
 start_time = time.time() #starts to count time elapsed during the process
 print(droid.getLine1Number().result,': This mobile number possessor is in danger. To help & Save, track this number. Please...') #gets mobile number which is at risk
 #sending mail of obtained information
 fromid = 'ptrial35@gmail.com'
 toid = 'ptrial35@gmail.com'
 msg = MIMEMultipart()
 msg['From'] = fromid
 msg['To'] = toid
 msg['Subject'] = "Help request"
 body = "I am at risk. Follow below details to help & save me. Please..."+" I am at risk from "+t+". My mobile number is "+droid.getLine1Number().result+". Track this number to locate & save me."
 msg.attach(MIMEText(body, 'plain'))
 s = smtplib.SMTP('smtp.gmail.com',587)
 s.ehlo()
 s.starttls()
 s.login(fromid,"cmruniversity")
 text = msg.as_string()
 s.sendmail(fromid, toid, text)
 s.quit()
 print('done')
 #loop to capture images
 shot=1
 while shot<=int(3):  
  droid.cameraCapturePicture("/storage/emulated/0/DCIM/Camera/"+str(shot)+".jpg")
  shot+=1
 #sending mail with attachment of captured images
 msg = MIMEMultipart()
 msg['From'] = fromid
 msg['To'] = toid
 msg['Subject'] = "Help request-proof pics"
 body = "Pics that say I am in danger."
 msg.attach(MIMEText(body, 'plain'))
 #loop to attach all 3 images in a single mail
 i=1
 while i<=3:
  filename =str(i)+".jpg"
  attachment = open("/storage/emulated/0/DCIM/Camera/"+str(i)+".jpg","rb")
  p= MIMEBase('application', 'octet-stream')
  p.set_payload((attachment).read())
  encoders.encode_base64(p)
  p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(p)
  i+=1
 s=smtplib.SMTP('smtp.gmail.com', 587)
 s.ehlo()
 s.starttls()
 s.login(fromid,"cmruniversity")
 text = msg.as_string()
 s.sendmail(fromid,toid,text)
 s.quit() 
 print('done')  
 print("--- %s seconds ---" % (time.time() - start_time)) #prints total time elapsed from start till here
 #gps activity starts
 droid.makeToast("fetching GPS data") #gets access to gps
 print("location data...")
 droid.startLocating() #starts getting gps data
 while True:    
  if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
   line = input()
   print("exit endless loop...")
   break    
  event = droid.eventWaitFor('location',10000).result #waits for gps data
  if event['name']== 'location': #location is extracted
  #trys for gps data which is exact
   try:           
    timestamp = repr(event['data']['gps']['time']) #gets time
    longitude = repr(event['data']['gps']['longitude']) #gets longitude
    latitude = repr(event['data']['gps']['latitude']) #gets latitude
    altitude = repr(event['data']['gps']['altitude']) #gets altitude
    speed = repr(event['data']['gps']['speed']) #gets speed
    accuracy = repr(event['data']['gps']['accuracy']) #gets accuracy
    loctype = "gps" #location type
  #if gps data fails, then gets location from network which is approximately true
   except KeyError:           
    timestamp = repr(event['data']['network']['time']) #gets time
    longitude = repr(event['data']['network']['longitude']) #gets longitude
    latitude = repr(event['data']['network']['latitude']) #gets latitude
    altitude = repr(event['data']['network']['altitude']) #gets altitude
    speed = repr(event['data']['network']['speed']) #gets speed
    accuracy = repr(event['data']['network']['accuracy']) #gets accuracy
    loctype = "net" #location type
   #total location data
   data = loctype + ";" + timestamp + ";" + longitude + ";" + latitude + ";" + altitude + ";" + speed + ";" + accuracy
   print(data)
   #getting geolocation/location address in words using above location data
   a=droid.geocode(latitude,longitude).result
   print(a)
   start_time = time.time()
   #sending mail with location details
   msg = MIMEMultipart()
   msg['From'] = fromid
   msg['To'] = toid
   msg['Subject'] = "Help request-location details"
   body = "My current gps/network location data is - "+loctype + ";" + timestamp + ";" + longitude + ";" + latitude + ";" + altitude + ";" + speed + ";" + accuracy +" . My location in words/names is - "+ str(a)+ " ."
   msg.attach(MIMEText(body, 'plain'))
   s = smtplib.SMTP('smtp.gmail.com',587)
   s.ehlo()
   s.starttls()
   s.login(fromid,"cmruniversity")
   text = msg.as_string()
   s.sendmail(fromid, toid, text)
   s.quit()
   print('done')
   print("--- %s seconds ---" % (time.time() - start_time)) #time elapsed while collecting location details and mailing the same
   time.sleep(30) #time difference between two location details
   #continue collecting location data
   print("location data continued...")
   #stop collecting location data
   droid.stopLocating()