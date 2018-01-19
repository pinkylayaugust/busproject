#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, \
     request, url_for
import csv
app = Flask(__name__)
with open('E:/Frontiir/busproject/bus_stops.csv', encoding='utf-8') as f:
    bus = [line.split(',')[0] for line in f]

@app.route('/')
def index():
    return render_template(
        'bstopselect.html',
        data=bus)

@app.route('/test',methods = ['POST', 'GET'])
def test():   
   if request.method == 'POST':
      result = request.form['comp_select']
      
      with open('E:/Frontiir/bus.csv','r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
          if row[0] != result:
            continue       
          
      return render_template("bstopshow.html",data = result)

    
if __name__=='__main__':
    app.run(debug=True)