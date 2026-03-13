from flask import redirect, render_template, request, url_for

import forms
from models import Alumnos, Curso, db

from . import alumnos


@alumnos.route("/alumnos")
def listadoAlumnos():
    create_form=forms.userForm(request.form)
    alumno=Alumnos.query.all()
    return render_template("alumnos/listadoAlumnos.html", form=create_form,alumno=alumno)



@alumnos.route("/insertarAlumnos",  methods=['GET','POST'])
def crearAlumnos():
    create_form=forms.userForm(request.form)
    if request.method=="POST":
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data,
                     telefono=create_form.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.listadoAlumnos'))
    return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id=request.args.get('id')
        nombre=alum1.nombre
        apellidos=alum1.apellidos
        email=alum1.email
        telefono=alum1.telefono
        curso=alum1.cursos if alum1.cursos else 'No hay cursos'
    return render_template("alumnos/detalles.html", nombre=nombre,apellidos=apellidos,email=email, telefono=telefono, curso=curso)

@alumnos.route("/modificar", methods=['GET','POST'])
def modificar():
    create_form=forms.userForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono
    if request.method=='POST':
        id=create_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellidos=create_form.apellidos.data
        alum1.email=create_form.email.data
        alum1.telefono=create_form.telefono.data
        db.session.add(alum1)
        db.session.commit()
        return redirect (url_for('alumnos.listadoAlumnos'))
    return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/eliminar", methods=['GET','POST'])
def eliminar():
    create_form=forms.userForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono
    if request.method=='POST':
        id=request.args.get('id')
        alum1=Alumnos.query.get(id)
        db.session.delete(alum1)
        db.session.commit()
        return redirect (url_for('alumnos.listadoAlumnos'))
    return render_template("alumnos/eliminar.html", form=create_form)

@alumnos.route("/inscribirAlumno", methods=['GET', 'POST'])
def inscribir():
    if request.method == 'GET':
        id = request.args.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        todos_cursos = Curso.query.all()

        inscritos_ids = [c.id for c in alum.cursos]
        return render_template("alumnos/inscribir.html",
                               alumno=alum,
                               cursos=todos_cursos,
                               inscritos_ids=inscritos_ids)

    if request.method == 'POST':
        id = request.form.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        seleccionados = request.form.getlist('cursos')

        alum.cursos = []
        for curso_id in seleccionados:
            curso = Curso.query.get(int(curso_id))
            if curso:
                alum.cursos.append(curso)

        db.session.commit()
        return redirect(url_for('alumnos.listadoAlumnos'))

    return redirect(url_for('alumnos.listadoAlumnos'))