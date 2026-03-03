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