from flask import Flask, render_template
from Scraper import PageScraper
app = Flask(__name__)

consolelist, maxprice, minprice = PageScraper()

@app.route("/")
def home():
    return render_template("home.html", len=len(consolelist), consoles=consolelist, max=maxprice, min=minprice)
    
if __name__ == "__main__":
    app.run(debug=True)