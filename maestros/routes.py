from flask import redirect, render_template, request, url_for

import forms
from models import Alumnos, Maestros, db

from . import maestros


@maestros.route("/maestros", methods=['GET', 'POST'])
def listado_maestros():
    create_form = forms.maesForm(request.form)
    lista_maestros = Maestros.query.all()

    return render_template(
        "maestros/listadoMaes.html",
        form=create_form,
        maestros=lista_maestros
    )

@maestros.route("/insertMaestros",  methods=['GET','POST'])
def insert_maestros():
    create_form=forms.maesForm(request.form)
    if request.method=="POST":
        maes=Maestros(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     especialidad=create_form.especialidad.data,
                     email=create_form.email.data)
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))
    return render_template("maestros/insertMaestros.html", form=create_form)

@maestros.route("/detallesMaestros", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        matricula=request.args.get('matricula')
        maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        matricula=request.args.get('id')
        nombre=maes.nombre
        apellidos=maes.apellidos
        especialidad=maes.especialidad
        email=maes.email
    return render_template("maestros/detalleMaestros.html", nombre=nombre,apellidos=apellidos,especialidad=especialidad, email=email)

@maestros.route("/eliminarMastros", methods=['GET','POST'])
def eliminar():
    create_form=forms.maesForm(request.form)
    if request.method=='GET':
        matricula=request.args.get('matricula')
        maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        create_form.matricula.data=request.args.get('matricula')
        create_form.nombre.data=maes.nombre
        create_form.apellidos.data=maes.apellidos
        create_form.especialidad.data=maes.especialidad
        create_form.email.data=maes.email
    if request.method=='POST':
        matricula=request.args.get('matricula')
        maes=Maestros.query.get(matricula)
        db.session.delete(maes)
        db.session.commit()
        return redirect (url_for('maestros.listado_maestros'))
    return render_template("maestros/eliminarMaestros.html", form=create_form)

@maestros.route("/actualizarMaestros", methods=['GET','POST'])
def modificar():
    create_form=forms.maesForm(request.form)
    if request.method=='GET':
        matricula=request.args.get('matricula')
        maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        create_form.matricula.data=request.args.get('matricula')
        create_form.nombre.data=maes.nombre
        create_form.apellidos.data=maes.apellidos
        create_form.especialidad.data=maes.especialidad
        create_form.email.data=maes.email
    if request.method=='POST':
        matricula=create_form.matricula.data
        maes=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        maes.nombre=create_form.nombre.data
        maes.apellidos=create_form.apellidos.data
        maes.especialidad=create_form.especialidad.data
        maes.email=create_form.email.data
        db.session.add(maes)
        db.session.commit()
        return redirect (url_for('maestros.listado_maestros'))
    return render_template("maestros/actualizarMaestros.html", form=create_form)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

