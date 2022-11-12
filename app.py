from flask import Flask,render_template,request
import pandas as pd
import pickle
import gspread
import sys
import logging
app=Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
model=pickle.load(open('model.pkl','rb'))
@app.route('/'):
def hi():
    return "HI"
if __name__=='__main__':
    app.run(debug=True)
