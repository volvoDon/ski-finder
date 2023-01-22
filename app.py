from flask import Flask , render_template
import lib
from lib import backcountry,evo,database_portal 

app = Flask(__name__)

@app.route("/")
def landing():
    fulllist = database_portal.get_all()
    return render_template("skis.html",skis=fulllist)

@app.route("/skis")
def skis():
    skis = backcountry.scrape_backcountry()
    products_from_evo = evo.scrape_evo()
    fulllist = skis + products_from_evo
    return render_template("skis.html",skis=fulllist)

@app.route("/qwertyuiop1234567890update")
def update():
    #you will need to figure out how to add commision based link to end of each row
    skis = backcountry.scrape_backcountry()
    products_from_evo = evo.scrape_evo()
    fulllist = skis + products_from_evo
    database_portal.clear_db()
    for item in fulllist:
        database_portal.add_row(item)
    return "this is just a utility"




