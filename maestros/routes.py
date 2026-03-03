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

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"