from classifierApp import ktm
from flask import Flask, render_template, request, jsonify
import asyncio
import requests
import io
from werkzeug.utils  import secure_filename
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# @app.route("/")
# async def hello_world():]
#     cyrus = await ktm()
#     myWebSite = "<p>Jesus Infame --> {} </p>\n".format(cyrus)
#     myWebSite += "<p>Hello, World!</p>"
#     return myWebSite

@app.route('/')
def home():
    return render_template("index.html")
    
# @app.route('/call-python-function') 
# async def call_python_function(): 
#     print("Ga(ll)y Chi Legge")
#     image = request.files['image']

#     print("Ricci omozigote")
#     image = Image.open(image)
#     print("Gennaro Infame")
#     img_io = BytesIO()
#     cyrus = await ktm(img_io)

#     return {'result': cyrus} 

@app.route('/call-python-function', methods=['GET']) 
async def call_python_function(): 
    print("Ga(ll)y Chi Legge")
    image = request.files['image']
    return {'result': 'status'} 
