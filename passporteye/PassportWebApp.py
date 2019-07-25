from flask import render_template
from flask import request,escape
from flask import Flask,redirect

@app.route("/")
def hello():
        return "Hello World!"

if __name__ == "__main__":
    app.run()
