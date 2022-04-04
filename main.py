from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = [
  {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16) 99922-1122'},
  {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16) 99922-3333'}
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    contacts = contacts
  )

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({
    'name': name,
    'email' : email,
    'phone': phone
  })
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  contacts.pop(id)
  return redirect('/')
  

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  contacts[index]['name'] = name
  email = request.form.get('email')
  contacts[index]['email'] = email
  phone = request.form.get('phone')
  contacts[index]['phone'] = phone
  return redirect('/')



if __name__ == '__main__':
  app.run(host= '0.0.0.0', port=8080)