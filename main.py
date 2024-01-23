from flask import Flask,request,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

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


@app.route("/multiplicar",methods=("GET","POST"))
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


@app.route("/resultado",methods=("GET","POST"))
def multe():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> El resultado es: {}</h1>".format(str(int(num1)*int(num2)))

if __name__ == "__main__":
    app.run(debug=True)
