from wtforms import (EmailField, Form, IntegerField, PasswordField,
                     StringField, validators)


class userForm(Form):
    id=IntegerField('id')
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo es requerido'),validators.length(min=4,max=10,message='Ingrese nombre valido')])
    apaterno=StringField('Apaterno',[validators.DataRequired(message='El campo es requerido')])
    email=EmailField('Correo',[validators.Email(message='Inbgresa un correo valido')])