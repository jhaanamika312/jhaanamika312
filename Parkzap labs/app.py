# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:11:43 2021

@author: DELL
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()