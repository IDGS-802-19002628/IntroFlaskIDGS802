from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class UserForm(Form):
    nombre = StringField("Nombre")
    email = EmailField("Correo")
    apaterno = StringField("apaterno")
    materias = SelectField(choices=[("Espanol", "Esp",), ("Mat", "matematicas"), ('Ingles', 'ING')])

    radios = RadioField('Curso', choices=[('1', '1'), ('2','2'), ('3','3')])

    