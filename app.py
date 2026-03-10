from flask import Flask, flash, g, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

import alumnos
import forms
from alumnos.routes import alumnos
from config import DevelopmentConfig
from cursos.routes import cursos
from maestros.routes import maestros
from models import Alumnos, db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()



@app.route("/", methods=['GET','POST'])
@app.route("/index")
def index():
    create_form=forms.userForm(request.form)
    alumno=Alumnos.query.all()
    return render_template("index.html", form=create_form,alumno=alumno)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()