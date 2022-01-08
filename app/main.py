from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Merhaba</h1>"

@app.route("/home")
def about():
  return render_template("main.html")