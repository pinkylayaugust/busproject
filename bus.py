#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, \
     request, url_for
import csv
app = Flask(__name__)

with open('E:/Frontiir/busproject/buslines.csv', encoding='utf-8') as f:
    bus = [line.split(',')[0] for line in f]

@app.route('/')
def index():
    return render_template(
        'select.html',
        data=bus)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    with open('E:/Frontiir/busproject/buslines.csv','r', encoding='utf-8') as f:
      reader = csv.reader(f)
      for row in reader:
        if row[0] != str(select):
          continue
        
        return render_template(
        'show.html',
        first=row[2], second=row[3],third=str(select))
if __name__=='__main__':
    app.run(debug=True)