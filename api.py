from flask import Flask

webapp = Flask("flaskapp")

@webapp.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    webapp.run(debug=True)
    pass
