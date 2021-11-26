from pymongo import MongoClient

client = MongoClient('192.168.0.5', 27017) #192.168.0.5 27017

# docker run -d -p 27017:27017 --name mongodb mongo:latest

db = client['minicurso_python']

if __name__ == '__main__':
    user = {'username':'Jonathan','age':39, 'password':'123456'}

    db.users.insert(user)  #Para insertar un solo usuarios

    user2 = {'username':'Jonathan_jr','age':39, 'password':'123456'}
    user3 = {'username':'Tiffany','age':39, 'password':'123456'}

    db.users.insert_many( [user2, user3] ) #Para insertar varios usuarios
    python = {'username':'python','age':39, 'password':'123456'}
    result = db.users.insert_one( python )
    print( result.inserted_id )



