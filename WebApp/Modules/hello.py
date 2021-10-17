from WebApp import app
@app.route("/")
@app.route("/Modular")
def hello_world():
    return "<h1>Hola desde Aplicacion Modular!</h1>"