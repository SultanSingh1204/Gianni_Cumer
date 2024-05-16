from classifierApp import ktm
from flask import Flask, render_template, request, jsonify
import asyncio
import requests

app = Flask(__name__)

# @app.route("/")
# async def hello_world():
#     cyrus = await ktm()
#     myWebSite = "<p>Jesus Infame --> {} </p>\n".format(cyrus)
#     myWebSite += "<p>Hello, World!</p>"
#     return myWebSite

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/call-python-function') 
async def call_python_function(): 
    print("Ga(ll)y Chi Legge")
    cyrus = await ktm()
    #print(cyrus)

    return {'result': cyrus} 
