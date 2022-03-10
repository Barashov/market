from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


app.run(host="0.0.0.0")