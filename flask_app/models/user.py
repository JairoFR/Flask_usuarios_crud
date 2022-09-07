# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla user de nuestra base de datos
class User:   
    def __init__( self , data ):
        self.id = data['id']
        self.nombre= data['first_name']
        self.apellido = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('esquema_users').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuarios in results:
            users.append( cls(usuarios) )
        return users

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM users where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL('esquema_users').query_db(query, data)
        #if len(results) > 0:
        #    return cls(results[0])
        #else:
        #    return None
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, update_at ) VALUES ( %(nombre)s , %(apellido)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('esquema_users').query_db( query, data )     

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,update_at=NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_users').query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('esquema_users').query_db(query,data)