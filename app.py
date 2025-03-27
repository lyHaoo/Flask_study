from flask import Flask


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/index")
def index():
    return "welcome to index."

@app.route("/index/<name>")
def show_name(name):
    return f"input name is {name}"

if __name__ == '__main__':
    app.run(debug=True)