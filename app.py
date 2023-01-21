from flask import Flask , render_template
import lib
from lib import backcountry 

app = Flask(__name__)

@app.route("/")
def landing():
    skis = backcountry.scrape_backcountry()
    return render_template("index.html",skis=skis)

@app.route("/skis")
def skis():
    skis = backcountry.scrape_backcountry()
    return render_template("skis.html",skis=skis)


