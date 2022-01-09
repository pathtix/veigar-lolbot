from flask import Flask,render_template
from app.functions import APIKEY, ApiError, getId

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Merhaba</h1>"

@app.route("/home")
def about():
  summonerName = "pathrix" # there will be a search box and its data will be summoner name
  print(getId(summonerName))
  return "<h2> selam </h2>"