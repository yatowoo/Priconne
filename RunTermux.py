import subprocess
from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def playsound():
  if request.method == 'GET':
    return 'Welcome to Priconne'

if __name__ =='__main__':
  app.run(debug=True)