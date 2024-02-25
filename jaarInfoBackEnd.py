# Program: Container logic that will be deployed to Azure Web Page
# Author: JAAR
# Date: 02/23/2024
# CS 135 Azure Fundamentals

# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
