from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/<style>')
def style(style):
    return render_template("types.html", style=style)


app.run(host="0.0.0.0")