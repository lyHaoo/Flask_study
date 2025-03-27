from flask import Flask,render_template,url_for
from Mongo.db_tools import MongoDB

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html",name=name,movies=movies)

@app.route("/index/<name>")
def show_name(name):
    return f"input name is {name}"

if __name__ == '__main__':
    name = 'Grey Li'
    mg = MongoDB()
    movies = mg.find_all()
    app.run(debug=True)