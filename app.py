from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/hello/<user>")
# def hello(user):
#     return render_template("hello.html", user_name=user)

# @app.route('/user/<string:username>')
# def username(username):
#     return 'i am ' + username

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)