from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    # llamar al método de clase get all para obtener todos los users
    users = User.get_all()
    print(users)
    return render_template("index.html", template_users=users)

@app.route('/crear_user')
def crear_user():
    return render_template('new_users.html')


@app.route('/agregar', methods=['POST'])
def agregar_usuario():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    print(data)
    # Pasamos el diccionario de datos al método save de la clase User
    User.save(data)
    # redirigir después de guardar en la base de datos
    return redirect('/')

@app.route('/ver_user/<id>')
def ver_user(id):
    return render_template('ver_user.html', user=User.get_by_id(id))

@app.route('/editar_user/<id>')
def editar_user(id):
    return render_template('new_users_edit.html', user=User.get_by_id(id))

@app.route("/user/actualizar/", methods=["POST"])
def user_actualizar_procesar():
    print(request.form)
    id = request.form['id']
    User.update(request.form)

    return redirect("/") 

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/')

