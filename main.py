from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import g


import forms
from flask import flash
app = Flask(__name__)
app.secret_key='esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/")
def index():
    return render_template("index.html")

@app.before_request
def before_request():
    g.prueba='hola'
    print('Antes de ruta 1')


@app.route("/alumnos", methods=("GET", "POST"))
def alumnos():
    print('dentro de ruta 2')
    valor = g.prueba
    print("Valor es: {}".format(valor))
    nom = ''
    apaterno = ''
    correo = ''
    alum_forms = forms.UserForm(request.form)
    if request.method == 'POST' :
        nom = alum_forms.nombre.data
        apaterno = alum_forms.apaterno.data
        correo = alum_forms.email.data
        messages = 'Bienvenido {}'.format(nom)
        flash(messages)
        print("Nombre: {}".format(nom))
        print("apaterno: {}".format(apaterno))
        print("correo: {}".format(correo))
    return render_template("alumnos.html", form=alum_forms, nom=nom, apa=apaterno, c=correo)

@app.after_request
def after_request(response):
    print('despues de ruta 3')
    return response

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


@app.route("/hola")
def func():
    return "<h1>Hola desde saludo</h1>"


@app.route("/saludo")
def func1():
    return "<h1>Hola desde saludo -UTL Bien</h1>"


@app.route("/nombre/<string:nom>")
def func3(nom):
    return "<h1>Hola </h1>"+nom


@app.route("/numero/<int:num1>")
def numero(num1):
    return "<h1>Numero es {}</h1>".format(num1)


@app.route("/user/<string:nomb>/<int:id>")
def user(nomb, id):
    return "Id: {} nombre {}".format(id, nomb)


@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    return "la suma es: {} + {} = {}".format(num1, num2, num1+num2)


@app.route("/multiplicar", methods=("GET", "POST"))
def mult():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
    else:
        return '''
        <form  action="/multiplicar" method="POST">
        <label>N1:</label>
        <input type="text" name="n1">
        <label>N2:</label>
        <input type="text" name="n2">
        <input type="submit">
        </form>
        '''


@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")


@app.route("/resultado", methods=("GET", "POST"))
def multe():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> El resultado es: {}</h1>".format(str(int(num1)*int(num2)))


if __name__ == "__main__":
    app.run(debug=True)
