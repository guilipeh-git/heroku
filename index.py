#pip freeze > requirements.txt

from flask import Flask

app = Flask("__name__")

@app.route("/")
def t():
    return "hello world!!!"

if(__name__ == "__main__"):
    app.run(debug=True,port=5000)