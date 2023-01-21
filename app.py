from flask import Flask , render_template
import lib
from lib import backcountry,evo 

app = Flask(__name__)

@app.route("/")
def landing():
    skis = backcountry.scrape_backcountry()
    return render_template("index.html",skis=skis)

@app.route("/skis")
def skis():
    skis = backcountry.scrape_backcountry()
    products_from_evo = evo.scrape_evo()
    fulllist = skis + products_from_evo
    return render_template("skis.html",skis=fulllist)


