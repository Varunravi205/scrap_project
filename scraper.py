import requests
import re
url=input("Enter the url you want to scrape: ")
p=requests.get(url)
phone_regex="\\+?[1-9][0-9]{7,14}"
phones=[]
for re_match in re.findall(phone_regex,p.text):
   if re_match not in phones:
       phones.append(re_match)

email_regex=r"[\w\.-]+@[\w\.-]+"
mails=[]
for re_match in re.findall(email_regex,p.text):
    if re_match not in mails:
        mails.append(re_match)


for i in phones:
    print(i)
for i in mails:
    print(i)

