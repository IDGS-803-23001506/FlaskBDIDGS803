from wtforms import (EmailField, Form, IntegerField, PasswordField,
                     StringField, validators)


class userForm(Form):
    id=IntegerField('id')
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo es requerido'),validators.length(min=4,max=10,message='Ingrese nombre valido')])
    apellidos=StringField('Apellidos',[validators.DataRequired(message='El campo es requerido')])
    email=EmailField('Correo',[validators.Email(message='Inbgresa un correo valido')])
    telefono=StringField('Telefono',[validators.DataRequired(message='El campo es requerido'),validators.length(min=10,max=10,message='Ingrese telefono valido')])

class maesForm(Form):
    matricula=IntegerField('Matricula')
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo es requerido'),validators.length(min=4,max=10,message='Ingrese nombre valido')])
    apellidos=StringField('Apellidos',[validators.DataRequired(message='El campo es requerido')])
    especialidad=EmailField('Especialidad',[validators.Email(message='Inbgresa un correo valido')])
    email=StringField('Email',[validators.DataRequired(message='El campo es requerido'),validators.length(min=10,message='Ingrese telefono valido')])
    
class cursoForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido'), validators.length(min=4, max=150, message='Ingrese un nombre valido')])
    descripcion = StringField('Descripcion', [validators.DataRequired(message='El campo es requerido'), validators.length(min=5, message='Ingrese una descripcion valida')])
    maestro_id  = IntegerField('Maestro Id', [validators.DataRequired(message='Seleccione un maestro')])