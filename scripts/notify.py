import smtplib
from email.mime.text import MIMEText

def notify():
  print("Sending notification...")
  msg = MIMEText("This is a notification from Flask APP")
  msg["Subject"] = "Flask App Notification"
  msg["From"] = "renecruz.0711@gmail.com"
  msg["To"] = "cgrfruz01@gmail.com"
  
  with smtplib.SMTP("gmail.com") as server:
    server.login("renecruz.0711@gmail.com", "Mayhem-1920892")
    server.sendmail(msg["From"], msg["To"], msg.as_string())
  print("Notification sent")
  
if __name__=="__main__":
  notify() 