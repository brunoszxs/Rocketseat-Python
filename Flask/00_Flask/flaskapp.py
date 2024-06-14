from flask import Flask

flaskapp = Flask(__name__)

@flaskapp.route("/")
def hello_flask():
    return "Hello Flask!"

if __name__ == "__main__":
    flaskapp.run(debug=True)