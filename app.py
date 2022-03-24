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
    
    first_item = catalog[0]
    second_item = catalog[1]
    return render_template("catalog.html", one=first_item[0], two=second_item[0], name1=first_item[1], name2=second_item[1], price_one=first_item[2], price_two=second_item[2], id1=first_item[3], id2=second_item[3])


@app.route('/id/<id>')
def id(id):
    item = data.get_id(id)
    print(item)
    return render_template("id.html", img=item[0], name=item[1], type=item[3], price=item[2], style=item[8], material=item[7], origin=item[5], size=item[6], gender=item[4])


if __name__ == "__main__":
    app.run(debug=True)