from flask import Flask
app = Flask(__name__)


@app.route('/main')
def main():
    return 'доброе утро даша!'


app.run(debug=True, host="0.0.0.0")
