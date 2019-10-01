from flask import Flask, render_template, jsonify, redirect
import yaml
import os
import optparse

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)



@app.route('/')                                         #Es la ruta "home"
def index():
    #return render_template('index.html')
    return render_template("index.html")




if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
