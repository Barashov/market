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
    print(catalog)
    first_item = catalog[0]
    second_item = catalog[1]

    return render_template("catalog.html", two="../static/img/1.jpg", name1=first_item[1], name2=second_item[1])


if __name__ == "__main__":
    app.run(debug=True)