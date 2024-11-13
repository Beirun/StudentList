from flask import Flask, render_template, url_for, request, redirect
from dbhelper import *

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    data: list = getprocess("SELECT idno FROM students;")
    idnos:list =[]
    for fields in data:
        idnos.append(fields[0])
    return render_template('index.html', idnos=idnos)


@app.route('/save', methods=['POST'])
def save():
    idno = request.form['idnoentered'] 
    lastname = request.form['lastnameentered'] 
    firstname = request.form['firstnameentered'] 
    course = request.form['courseentered'] 
    level = request.form['levelentered'] 
    image = 'static/images/'+idno+'.jpg'
    postprocess("INSERT INTO students (idno,lastname,firstname,course,level,image) VALUES ('"+idno+"','"+lastname+"','"+firstname+"','"+course+"','"+level+"','"+image+"');")
    return redirect(url_for('index'))

@app.route('/saveimage', methods=['POST'])
def saveimage():
    image = request.files['webcam'] 
    idno = request.args.get('idno')
    image.save('static/images/'+idno+'.jpg')
    return redirect(url_for('index'))

@app.route('/list')
def list():
    data: list = getprocess("SELECT idno,lastname,firstname,course,level,image FROM students;")
    return render_template('list.html',students=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')