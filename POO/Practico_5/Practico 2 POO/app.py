from cgitb import html
from datetime import datetime
from operator import methodcaller
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Receta, Ingredientes

app.secret_key = 'mysecretkey'


@app.route('/')
def inicio():
    return render_template('inicio.html')



#VALIDACION SESION DEL USUARIO
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = Usuario.query.filter_by(correo=request.form['correo']).first()
        if user and check_password_hash(user.clave, request.form['clave']):
            session["usuario"] = user.nombre
            session["usuario_id"] = user.id
            return render_template('menu_principal.html', nombre=session["usuario"], hora=datetime.now().hour)
        else:
            return render_template("error.html", error="Usuario o Contraseña incorrectos")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/logout', methods=["POST", "GET"])
def logout():
    if request.method == 'POST':
        if "usuario" in session:
            session.pop("usuario", None)
            session.pop("usuario_id", None)
            session.pop("receta_id", None)
            session.clear()
            return redirect(url_for('saludo'))    
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/inicio_sesion', methods=["POST", "GET"])
def inicio_sesion():
    return render_template('inicio_sesion.html')



@app.route('/menu_principal', methods=["POST", "GET"])
def menu_principal():
    if request.method == 'POST':
        if "usuario" in session:
            return render_template('menu_principal.html', nombre=session["usuario"], hora=datetime.now().hour)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")

#----------------------------------------------------------------------------------------------------------------------

#FUNCIONALIDADES DEL USUARIO

@app.route('/crear_receta', methods = ['POST','GET'])
def crear_receta():
    if request.method == 'POST':
        if "usuario" in session:
            #Crear receta
            return render_template('crear_receta.html', nombre=session["usuario"])
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/nueva_receta', methods = ['POST','GET'])
def nueva_receta():
    if request.method == 'POST':
        if "usuario" in session:
            if not request.form['nombre'] or not request.form['tiempo'] or  not request.form['fecha'] or not request.form['elaboracion']:
                return render_template('crear_receta.html', error="Faltan datos")
            else:
                #Añade receta a la base de datos
                receta = Receta(nombre = request.form['nombre'],tiempo = request.form['tiempo'] , fecha = request.form['fecha'], elaboracion = request.form['descripcion'], cantidadmegusta = 0, usuarioid = session["usuario_id"])
                db.session.add(receta)
                db.session.commit()
                #Obtiene ID de la receta filtrada por nombre de receta
                nombre = request.form['nombre']
                receta = Receta.query.filter_by(nombre = nombre).first()
                session['receta_id'] = receta.id
                return render_template('añadir_ingredientes.html', nombre=session["usuario"], recetaid = session['receta_id'])
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/añadir_ingredientes', methods = ['POST','GET'])
def añadir_ingredientes():
    if request.method == 'POST':
        if "usuario" in session:
            if not request.form['nombre'] or not request.form['cantidad'] or  not request.form['unidad']:
                return render_template('añadir_ingredientes.html', error="Faltan datos")
            else:
                #Añade ingrediente a la base de datos
                ingrediente = Ingredientes(nombre = request.form['nombre'], cantidad = request.form['cantidad'], unidad = request.form['unidad'], recetaid = session['receta_id'])
                db.session.add(ingrediente)
                db.session.commit()
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/listado_ordenado', methods = ['POST','GET'])
def listado_ordenado():
    if request.method == 'POST':
        if "usuario" in session:
            #Obtiene listado de recetas ordenado por cantidad de likes
            recetas = Receta.query.order_by(Receta.cantidadmegusta.desc()).all()
            return render_template('listado_ordenado.html', nombre=session["usuario"], recetas = recetas)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/consultar_receta', methods = ['POST','GET'])
def consulta_receta():
    if request.method == 'POST':
        if "usuario" in session:
            return render_template('consultar_receta.html', nombre=session["usuario"])
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")



@app.route('/consultar_portiempo', methods = ['POST','GET'])
def consulta_por_tiempo():
    if request.method == 'POST':
        if "usuario" in session:
            #Obtiene listado de recetas ordenado por tiempo de preparacion
            tiempo_input = request.form["tiempo"]
            recetas = Receta.query.all()
            #recetas_time = Receta.query.all()
            #{%if comentarios.tiempo < tiempo_cmp %}
            #   <li>{{comentarios.nombre}}</li>
            return render_template('consultar_portiempo.html', nombre=session["usuario"], tiempo_cmp = tiempo_input, recetas=recetas)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")

#REUTILIZABLES

@app.route('/likes', methods = ['POST','GET'])
def likes():
    post = Receta.query.filter_by(id=session['receta_id']).first()
    current_user = session["usuario_id"]
    if current_user is post.usuarioid:
        print("Es tu propio post")
    else:
        if request.form['like'] == 'like':
            post.cantidadmegusta = post.cantidadmegusta + 1
            db.session.commit()
        if request.form['unlike'] == 'unlike':
            post.cantidadmegusta = post.cantidadmegusta - 1
            db.session.commit()
    session.pop('receta_id', None)


@app.route('/receta_consultada', methods = ['POST','GET'])
def receta_consultada():
    if request.method == 'POST':
        if "usuario" in session:
            recetas_id = Receta.query.filter_by(nombre = request.form['nombre']).first()
            persona = Usuario.query.filter_by(id = recetas_id.usuarioid).first()
            session['receta_id'] = recetas_id.id
            ingredientes = Ingredientes.query.filter_by(recetaid = session['receta_id']).all()
            return render_template('receta.html', nombre = persona.nombre, recetas_id = session['receta_id'], ingredientes = ingredientes)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")
#---------------------------------------------------------------------------------------------------------------------

@app.route('/ingredientes', methods = ['POST','GET'])
def ingredientes():
    if request.method == 'POST':
        if "usuario" in session:
            nom_ingred = request.form['ingrediente']
            ingredientes = Ingredientes.query.all()
            return render_template('ingredientes.html', nombre=session["usuario"], ingredientes = ingredientes, nom_ingred = nom_ingred)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")


@app.route('/receta_consultada_ingredientes', methods = ['POST','GET'])
def receta_consultada_ingredientes():
    if request.method == 'POST':
        if "usuario" in session:
            recetas = Ingredientes.query.filter_by(recetaid = request.form['receta_id']).all()
            return render_template('receta_consultada_ingredientes.html', recetas = recetas)
        else:
            return render_template("error.html", error="No estas logueado")
    else:
        return render_template("error.html", error="Entrada invalida")

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    db.create_all()
    app.run(debug=true, port=5500)