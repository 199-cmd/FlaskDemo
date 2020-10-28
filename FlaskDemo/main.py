from flask import Flask,render_template,json,flash,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

with open('config.json', 'r') as c:
    parameter = json.load(c)["parameter"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = parameter['local_uri']
app.secret_key = 'super-secret-key'
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    
@app.route('/')
def home():
	return render_template('index.html',parameter=parameter)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, email = email, phone = phone, message = message, date= datetime.now())
        db.session.add(entry)
        db.session.commit()

        flash("Thank You We will get back to you soon...","success")
    return render_template('index.html',parameter=parameter)