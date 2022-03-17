from flask import Flask, render_template
app = Flask(__name__)
from data_base import DATA
data = DATA()


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/<style>')
def style(style):
    return render_template("types.html", style=style)


@app.route('/<style>/<type>')
def type(style, type):
    catalog = data.get_catalog(style, type)
    
    return render_template("catalog.html")
    

    
app.run(host="0.0.0.0")