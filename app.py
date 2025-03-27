from flask import Flask,render_template,url_for,request,flash,redirect
from Mongo.db_tools import MongoDB
# 用于生成密码散列值和验证面膜
from werkzeug.security import generate_password_hash,check_password_hash
import json

app = Flask(__name__)
app.config["DEBUG"] = True
mg = MongoDB()

@app.route("/index")
@app.route("/")
def index():
    name = 'Grey Li'
    movies = mg.find_all()
    return render_template("index.html",name=name,movies=movies)

@app.route('/add',methods=['POST'])
def add_one():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        data = {
            'title':title,
            'year':year
        }
        if mg.add_one(data):
            return "insert ok."

@app.route('/get_data',methods=['GET'])
def get_by_query():
    title = request.args.get('title')
    query = {'title':title}
    ans = mg.find_by_query(query)
    return ans

@app.route('/regist',methods=['POST'])
def regist():
    account =request.form.get('account')
    pwd = request.form.get('passwd')
    pwd_hash = generate_password_hash(pwd)
    type = request.form.get('type')
    mg.change_col("user")
    insert_dict = {'account':account,'password':pwd_hash,"type":type}
    if mg.add_one(insert_dict):
        return "regist success."
    return "regist falied"

@app.route("/check_pwd",methods=['GET'])
def check_pwd():
    account = request.args.get("account")
    pwd = request.args.get("pwd")
    query = {
        "account":account
    }
    mg.change_col("user")
    user_info = mg.find_by_query(query)
    pwd_hash = user_info['password']
    ans = check_password_hash(pwd_hash,pwd)
    if ans:
        return "verify success."
    return "verify failed"

if __name__ == '__main__':
    app.run(debug=True)