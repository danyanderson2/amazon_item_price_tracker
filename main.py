from bs4 import BeautifulSoup
import requests
import smtplib
import lxml
from dotenv import load_dotenv
import os

# Hi. If you aren't a knowledgeable programmer, no need going further down into the file
#######################################################################################################################################
load_dotenv()
# navigate to your item on amazon and copy its url as the value of the variable below
ITEM_URL="https://www.amazon.com/HP-Omen-Gaming-i7-14700HX-Keyboard/dp/B0D45T6N91/ref=sr_1_1?crid=228I3IVYDFWXR&dib=eyJ2IjoiMSJ9.EATTxNmIzHGEg-F6lHn0JDq3J3NI6yd-4J6Q1JQTwhgYORPHWeqPXutBYh6JubNxTG9KiJ6OW_sGZtFRG51SCBotcyxq74TAySPDcv6lBPDAYt3SCbYonTM1KBUzVCwjd47hLmhz75CZwqh1Bp4ZXdIPve3YrEGeCD04asezAXVkHVsShyGbqHOmQCvL-4Xbe_aaxYj4QC7jpD9OfM-f1A-OauNMnXFLV5N26yXXjDE.yNjAJnpHxir4NxRZCAk3npnOqyaZjC-BEupq3N6y7IY&dib_tag=se&keywords=hp+laptop+64+gb+ram+2+tb+ssd+nvidia+GPU&qid=1720921789&sprefix=hp+laptop+64+gb+ram+2+tb+ssd+nvidia+gpu%2Caps%2C252&sr=8-1"
USER=os.environ.get('EMAIL')      # your email address here
RECIPIENT=os.environ.get('EMAIL') # typically still your own email address if sending to yourself
PASSWORD= os.environ.get('GMAIL_APP_PASSWORD')
PRICE_LOWER_BOUND = 1000
PRICE_UPPER_BOUND = 1800
YOUR_NAME = 'Dany'
ITEM_NAME = 'HP - laptop'
######################################################################################################################################3

# using beautiful soup to get hold of the price of the item on amazing item listings page
headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Forwarded-For":"41.251.254.145",
    "x-forwarded-proto":"https"
}
response=requests.get(ITEM_URL, headers=headers)
web_page=response.text
soup=BeautifulSoup(web_page,"lxml")
price=soup.find(name="span", class_="a-price-whole")
text=price.getText().split(".")
# print(len(text[0]))
in_words=[]

# Remove any non_digit characters that might be in the item price
for n in text[0]:
    if n in "1234567890":
        in_words.append(n)
words="".join(in_words)
item_price = int(words)
print(item_price) # price you are expected to receive (provided it falls in your range)
# print(PASSWORD)


if PRICE_LOWER_BOUND <= item_price <= PRICE_UPPER_BOUND:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER,password=PASSWORD)
        # connection.sendmail(
        #     to_addrs=USER,
        #     from_addr=RECIPIENT,
        #     msg=f"Subject: New price alert !!!\n\nHey {YOUR_NAME},\n\nYour {ITEM_NAME}'s price right now is ${item_price}"
        # )
        print("code ran!")