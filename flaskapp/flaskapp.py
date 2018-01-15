from flask import Flask, render_template, redirect, request, jsonify,make_response,send_from_directory,current_app
import json
import Driver
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sort/<col_name>')

def app_sort(col_name,methods=["GET","POST"]):
    df = Driver.sort(col_name)
    df.to_excel('./data/sorted_repo.xlsx')
    uploads = os.path.join(current_app.root_path, 'data')
    return send_from_directory(directory=uploads, filename='sorted_repo.xlsx')
##    print df.head()

if __name__ == "__main__":
    app.run(debug=True)

