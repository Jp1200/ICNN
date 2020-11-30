from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# First impotrd an instance of the flask
# class
#  The arguement is the name of applications
#  moule or package
#  When we use the route()
#  decorator to flask what Url shoul trigger
#  opur function
