import os
from flask_app.config.mysqlconnection import connectToMySQL

class User:  

    modelo = 'usuarios'

    def __init__( self , data ):
        self.id = data['id']
        self.nombre= data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.modelo};"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuarios in results:
            users.append( cls(usuarios) )
        return users

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        #if len(results) > 0:
        #    return cls(results[0])
        #else:
        #    return None
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save(cls, data ):
        query = f"INSERT INTO {cls.modelo} ( nombre , apellido , email , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data )     

    @classmethod
    def update(cls,data):
        query = f"UPDATE {cls.modelo} SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        return resultado

    @classmethod
    def destroy(cls,data):
        query  = f"DELETE FROM {cls.modelo} WHERE id = %(id)s;"
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)