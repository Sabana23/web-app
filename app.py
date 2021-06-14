from flask import Flask,render_template,request
import pandas as pd
import csv
import os

app = Flask(__name__)

UPLOAD_FOLDER=os.path.join('Templates','1.jpg')
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


@app.route('/',methods=['GET','POST'])
def home():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'1.jpg')
    return render_template('home.html',user_image=pic1)
   

@app.route('/data',methods=['GET','POST'])
def data():
    if request.method =='POST':
        f=request.form['csvfile']
        data=[]
        with open(f) as file:
            csvfile =csv.reader(file)
            for row in csvfile:
                data.append(row)
        data = pd.DataFrame(data)       
        return render_template('data.html',data=data.to_html(header=False , index=False))



if __name__ == '__main__':
    app.run(debug=True)
