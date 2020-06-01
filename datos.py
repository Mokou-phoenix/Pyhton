from flask import Flask,jsonify,render_template,request,redirect
from conectar import *
import pymysql
app=Flask(__name__)

@app.route("/")
def presentacion():
    return render_template('inicio.html')

@app.route("/<name>")
def saludo(name):
    return "hola don/doña " + str(name)

@app.route("/add",methods=["POST"])
def add():
    nombre=request.form.get("nombre")
    apellido=request.form.get("apellido")
    conecta=conect()
    conecta.ejecutarsql("INSERT INTO alumno (nombre,apellido) Values('"+nombre+"','"+apellido+"')")
    datos=conecta.devolverdatos()
    conecta.realizarcambios()
    print(datos)
    return redirect("/all")

@app.route("/update", methods=["POST"])
def update():
    id=request.form.get("id")
    nombre=request.form.get("nombre")
    apellido=request.form.get("apellido")
    conecta=conect()
    conecta.ejecutarsql("UPDATE alumno SET nombre='"+nombre+"',apellido='"+apellido+"' Where idalumno="+id)
    conecta.realizarcambios()
    return redirect("/all")

@app.route("/delete",methods=["GET","POST"])
def delete():
    id=request.form.get("id")
    conecta=conect()
    conecta.ejecutarsql("DELETE FROM alumno WHERE idalumno="+id)
    datos=conecta.devolverdatos()
    conecta.realizarcambios()
    print(datos)
    return redirect("/all")

@app.route("/list")
def listadoalumno():
    conecta=conect()
    conecta.ejecutarsql("SELECT * FROM alumno")
    datos=conecta.devolverdatos()
    resp=jsonify(datos)
    conecta.cerrarbase()
    return resp

@app.route("/all")
def listall():
    conecta=conect()
    conecta.ejecutarsql("SELECT * FROM alumno")
    data=conecta.devolverdatos()
    conecta.cerrarbase()
    return render_template('index.html', datos=data)

if __name__ == "__main__":
#app.run(debug=True, host='0.0.0.0', port=8000)
    app.run()
    