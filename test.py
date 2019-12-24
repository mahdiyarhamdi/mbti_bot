#!/usr/bin/env python
# -*- coding: utf-8 -*- import csv 
import csv
import time
import requests
import  email
import smtplib  
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEImage import MIMEImage

dicts = {}
dicts_Fname = {}
dicts_Lname = {}
dicts_Email = {}
dicts_phone = {}
dicts_mobile = {}
dicts_birthday = {}
dicts_madrak = {}
dicts_job = {}
dicts_position = {}
dicts_method = {}
dicts_goal = {}
dicts_expect = {}
dicts_ie = {}
dicts_sn = {}
dicts_tf = {}
dicts_pj= {}
dicts_tip= {}




dicts[390473938]=11222
dicts_Fname[390473938] = 1
dicts_Lname[390473938] = 'l'
dicts_Email[390473938] = 'e'
dicts_phone[390473938] = 'p'
dicts_mobile[390473938] = 'm'
dicts_birthday[390473938] = 'b'
dicts_madrak[390473938] = 'ma'
dicts_job[390473938] = 'j'
dicts_position[390473938] = 'po'
dicts_method[390473938] = 'me'
dicts_goal[390473938] = 'g'
dicts_expect[390473938] = 'ex'
dicts_ie[390473938] = "q"
dicts_sn[390473938] = "q"
dicts_tf[390473938] = "q"
dicts_pj[390473938]= "q"
dicts_tip[390473938]= "q"


listF = []
listF.append(('chat ID','state','first name','last name','e-mail','phone no.','mobile no.','birthday date','degree','job','post','way of introdution','goal','expect','ie','sn','tf','pj','tip'))


def inserTolist(i):
    listF.append((i,dicts[i],dicts_Fname[i],dicts_Lname[i],dicts_Email[i],dicts_phone[i],dicts_mobile[i],dicts_birthday[i],dicts_madrak[i],dicts_job[i],dicts_position[i],dicts_method[i],dicts_goal[i],dicts_expect[i],dicts_ie[i],dicts_sn[i],dicts_tf[i],dicts_pj[i],dicts_tip[i]))

def readFromlist():
    tmp=0
    for i in range(0,len(listF)):
        if i==0: 
            continue
        tmp=listF[i][0]
        dicts[tmp] = listF[i][1]
        dicts_Fname[tmp] = listF[i][2]
        dicts_Lname[tmp] = listF[i][3]
        dicts_Email[tmp] = listF[i][4]
        dicts_phone[tmp] = listF[i][5]
        dicts_mobile[tmp] = listF[i][6]
        dicts_birthday[tmp] = listF[i][7]
        dicts_madrak[tmp] = listF[i][8]
        dicts_job[tmp] = listF[i][9]
        dicts_position[tmp] = listF[i][10]
        dicts_method[tmp] = listF[i][11]
        dicts_goal[tmp] = listF[i][12]
        dicts_expect[tmp] = listF[i][13]
        dicts_ie[tmp] = listF[i][14]
        dicts_sn[tmp] = listF[i][15]
        dicts_tf[tmp] = listF[i][16]
        dicts_pj[tmp] = listF[i][17]
        dicts_tip[tmp] = listF[i][18]

        

def saveToCSV():
    with open('person.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(listF)
    csvFile.close()
def loadFormCSV():    
    with open('person.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for item in reader:
            listF.append(item)





inserTolist(390473938)
inserTolist(390473938)
inserTolist(390473938)
saveToCSV()
# inserTolist(1)
# inserTolist(1)
# inserTolist(1)
# inserTolist(1)
# listF = {}
# print(22222222222222222)
print(listF)
loadFormCSV()
# print(33333333333333333)
print(listF[0][0])
readFromlist()
print(dicts_tip)

# msg = MIMEMultipart()
# msg.attach(MIMEText(file("sample.pdf").read()))
# fromaddr = 'mahdiyarhamdi@gmail.com'  
# toaddrs  = 'madiyarhamdi@outlook.com'  


# # Credentials (if needed)  
# username = 'mahdiyarhamdi@goole.com'  
# password = 'hamdi@0912'  

# # The actual mail send  
# server = smtplib.SMTP('smtp.gmail.com:587')  
# server.starttls()  
# server.login(username,password)  
# server.sendmail(fromaddr, toaddrs, msg)  
# server.quit()  

# # URL = 'http://smsg.ir/index2.php?goto=webservice/json&method=send&arg1=ali&arg2=maedeh&arg3=09397201006&arg4=30001341213594&arg5=به به!'
# # # requests.get(URL)
# # i = 390473938
# # i2 = i/100000


# # print(i2)
#!/usr/bin/env python
# import smtplib

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# import smtplib, ssl

# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# sender_email = "mahdiyarhamdi@gmail.com"
# password = "hamdi@0912"

# # Create a secure SSL context
# context = ssl.create_default_context()

# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit() 



# # me == my email address
# # you == recipient's email address
# me = "mahdiyarhamdi@gmail.com"
# you = "mahdiyarhamdi@outlook.com"

# # Create message container - the correct MIME type is multipart/alternative.
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "Link"
# msg['From'] = me
# msg['To'] = you

# # Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
# html = """\
# <html>
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you?<br>
#        Here is the <a href="https://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """

# # Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')
# part2 = MIMEText(html, 'html')

# # Attach parts into message container.
# # According to RFC 2046, the last part of a multipart message, in this case
# # the HTML message, is best and preferred.
# msg.attach(part1)
# msg.attach(part2)

# # Send the message via local SMTP server.
# s = smtplib.SMTP('localhoost')
# s.login('mahdiyarhamdi@gmail.com','hamdi@0912')
# # sendmail function takes 3 arguments: sender's address, recipient's address
# # and message to send - here it is sent as one string.
# s.sendmail(me, you, msg.as_string())
# s.quit()


# Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# fp = open('tst.txt', 'rb')

# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()

# me = 'mahdiyarhamdi@outlook.com'
# you = 'mahdiyarhamdi@gmailco'
# msg['Subject'] = 'The contents of ' 
# msg['From'] = me
# msg['To'] = you

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()
