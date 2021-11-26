from pymongo import MongoClient

client = MongoClient('192.168.0.5', 27017) #192.168.0.5 27017

# docker run -d -p 27017:27017 --name mongodb mongo:latest

db = client['minicurso_python']


if __name__ == '__main__':
    # Update and delete
    db.users.update( {'age':39} , {'$set': {'age':24} } )  #Solo actualiza un registro

    db.users.update_many( {'age':24} , {'$set': {'age':40} } ) # Para actualizar varios registros


    #eliminar registros

    db.users.delete_many({'age':39})


