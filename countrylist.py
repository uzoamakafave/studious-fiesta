from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    countries = ["Nigeria","Tunisia","UK","Germany"]
    return render_template('countrylist.html', countries = countries)

if __name__ == '__main__  ' :
    app.run(host="0.0.0.0", port=5001)

    