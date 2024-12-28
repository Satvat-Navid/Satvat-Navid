from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is my First webpage. Hello World "

@app.route("/index")
def index():
    return "This the Index page "




if __name__=="__main__":
    app.run(debug=True)
