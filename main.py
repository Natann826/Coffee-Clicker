from flask import Flask, render_template, url_for, request, redirect
import matplotlib.pyplot as plt
from flask_jsglue import JSGlue

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

app.run() 
