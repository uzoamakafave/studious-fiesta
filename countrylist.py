from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    countries = ["Nigeria","Tunisia","UK","Germany"]
    return render_template('countrylist.html', countries = countries)

    
app.run()
    