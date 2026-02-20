from flask import Flask, flash, g, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

import forms
from config import DevelopmentConfig
from models import Alumnos, db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()



@app.route("/", methods=['GET','POST'])
@app.route("/index")
def index():
    create_form=forms.userForm(request.form)
    alumno=Alumnos.query.all()
    return render_template("index.html", form=create_form,alumno=alumno)



@app.route("/Alumnos",  methods=['GET','POST'])
def alumnos():
    create_form=forms.userForm(request.form)
    if request.method=="POST":
        alum=Alumnos(nombre=create_form.nombre.data,
                     aPaterno=create_form.apaterno.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos.html", form=create_form)

@app.route("/detalles", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id=request.args.get('id')
        nombre=alum1.nombre
        apaterno=alum1.aPaterno
        email=alum1.email
    return render_template("detalles.html", nombre=nombre,apaterno=apaterno,email=email)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()