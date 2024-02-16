import requests
from bs4 import BeautifulSoup
import smtplib 
from email.message import EmailMessage

#Scrap Price And Title From Amazaon
url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response=requests.get(url=url)

soup=BeautifulSoup(response.text,"html.parser")

all_price=soup.find_all(class_="a-offscreen")
title=soup.find(id="productTitle")
price=float(all_price[1].getText()[1:])

print(price)

#Prepare Email Message Using EmailMessage()
sender_mail = 'saeedhuzaifa678@gmail.com'    
receivers_mail = ['saeedhuzaifa333@gmail.com']    
message = EmailMessage()
message['From'] = sender_mail
message['To'] = ', '.join(receivers_mail)
message['Subject'] = "subject"

body = f"""\
{title.text.strip()} 
is Now Less Than 100$ And You can Buy This Product By Following This Link
{url}
"""
message.set_content(body)
 
print(message) 
#send Email if Price Match
if(price<100):
    try:    
        password = "Your PassWord"    
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)    
        smtpObj.login(sender_mail,password)    
        smtpObj.sendmail(sender_mail, receivers_mail, message.as_string())    
        print("Successfully sent email")    
    except Exception as e:    
        print("Error: unable to send email")
        print(e) 