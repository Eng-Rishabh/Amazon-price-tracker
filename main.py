import bs4
import urllib.request
import ssl
import smtplib
import time

min_wanted_price = 1e9
url = "https://www.amazon.in/Redgear-Gaming-Semi-Honeycomb-Windows-Gamers/dp/B08CHZ3ZQ7/ref=sr_1_12?brr=1&qid=1657107993&rd=1&sr=8-12&th=1"
user_mail = 'put_your_mail'
current_price = min_wanted_price


def price(url):
    global current_price
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(page, "html.parser")
    prices = soup.find(class_="a-price-whole").get_text()
    price = float((((prices.replace(",", "")).replace("र", "")).replace("\"\" ", "")).replace(".", ""))
    if(current_price < price):
        current_price = price;
        return price
    else:
        return 0


def sending_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    with open('interface', 'r') as file:
        mail_id_used = file.readline()
        word_to_open = file.readline()
    server.login(mail_id_used, word_to_open)
    subject = 'Price Fell Down'
    body = f"Check the amazon link {url}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        mail_id_used,
        user_mail,
        msg
    )
    server.quit()

sending_mail();



# while True:
#     if(price(url)):
#         sending_mail()
#     time.sleep(25000)