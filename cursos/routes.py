from flask import redirect, render_template, request, url_for

import forms
from models import Curso, Maestros, db

from . import cursos


@cursos.route("/cursos")
def listadoCursos():
    create_form = forms.cursoForm(request.form)
    lista_cursos = Curso.query.all()
    return render_template("cursos/listadoCursos.html", form=create_form, cursos=lista_cursos)


@cursos.route("/insertarCurso", methods=['GET', 'POST'])
def crearCurso():
    create_form = forms.cursoForm(request.form)
    maestros = Maestros.query.all()
    if request.method == "POST":
        cur = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))
    return render_template("cursos/insertarCurso.html", form=create_form, maestros=maestros)


@cursos.route("/detallesCurso", methods=['GET', 'POST'])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        nombre = cur.nombre
        descripcion = cur.descripcion
        maestro = cur.maestro.nombre + ' ' + cur.maestro.apellidos
        alumnos = cur.alumnos
    return render_template("cursos/detalleCurso.html",
                           nombre=nombre,
                           descripcion=descripcion,
                           maestro=maestro,
                           alumnos=alumnos)


@cursos.route("/modificarCurso", methods=['GET', 'POST'])
def modificar():
    create_form = forms.cursoForm(request.form)
    maestros = Maestros.query.all()
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = cur.nombre
        create_form.descripcion.data = cur.descripcion
        create_form.maestro_id.data = cur.maestro_id
    if request.method == 'POST':
        id = create_form.id.data
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        cur.nombre = create_form.nombre.data
        cur.descripcion = create_form.descripcion.data
        cur.maestro_id = create_form.maestro_id.data
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))
    return render_template("cursos/modificarCurso.html", form=create_form, maestros=maestros)


@cursos.route("/eliminarCurso", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.cursoForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        cur = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = cur.nombre
        create_form.descripcion.data = cur.descripcion
        create_form.maestro_id.data = cur.maestro_id
    if request.method == 'POST':
        id = request.args.get('id')
        cur = Curso.query.get(id)
        db.session.delete(cur)
        db.session.commit()
        return redirect(url_for('cursos.listadoCursos'))
    return render_template("cursos/eliminarCurso.html", form=create_form)