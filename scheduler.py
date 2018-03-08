#email scheduler
import smtplib #import smtp library
s = smtplib.SMTP('smtp.gmail.com', 587) # start SMTP session 
s.starttls() # have TLS for security
s.login("353prv@gmail.com", "password") # authentication
message = "hlo" # type the message 
s.sendmail("353prv@gmail.com", "353prv@gmail.com", message) # send the mail 
print("DONE")
s.quit() # end the session
