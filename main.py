from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

contact = [
  {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16) 99922-1122'},
  {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16) 99922-3333'}
]



class Users (db.Model) :
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(100))
  created_at = db.Column(db.String(100))
  uodated_at = db.Column(db.String(100))

class contacts (db.Model) : 
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(100))
  image = db.Column(db.String(100))
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(100))
  uodated_at = db.Column(db.String(100))




@app.route('/')
def index():
  todos = Users.query.all()
  rotas = contacts.query.all()
  return render_template('index.html',todos = todos, contact = contact, new_contacts = rotas )

@app.route('/create', methods = ['POST'])
def create():
 name = request.form.get('name')
 email = request.form.get('email')
 phone = request.form.get('phone')
 new_contacts = contacts(name = name, email = email, phone = phone)
 db.session.add(new_contacts)
 db.session.commit()
 return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
 todo = contacts.query.filter_by(id=id).first()
 db.session.delete(todo)
 db.session.commit()
 return redirect('/')
  
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
 name = request.form.get('name')
 email = request.form.get('email')
 phone = request.form.get('phone')
 new_contacts = contacts.query.filter_by(id=id).first()
 new_contacts.name = name
 new_contacts.email = email
 new_contacts.phone = phone
 db.session.commit()
 return redirect('/')

if __name__ == '__main__':
  db.create_all()
  app.run(host= '0.0.0.0', port=8080)