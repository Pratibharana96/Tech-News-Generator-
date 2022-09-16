from flask import Flask,url_for,render_template, request
from bs4 import BeautifulSoup
import requests
import html2canvas 
app = Flask(__name__)
@app.route('/',methods = ["Get","POST"])
def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    outerData = soup.find_all("div",class_="widget-listing",limit=6)
    #print(outerData)
    finalnews=""
    for data in outerData :
        news=data.div.div.a["title"]
        finalnews += '\u2022 '+news+'\n'
    # print(finalnews)
    return render_template("index.html", News=finalnews)


