#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', titulo='Flask!')

@app.route('/jinja.html')
def jinja():
    return render_template('jinja.html')