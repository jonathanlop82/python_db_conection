from pymongo import MongoClient

client = MongoClient('192.168.0.5', 27017) #192.168.0.5 27017

# docker run -d -p 27017:27017 --name mongodb mongo:latest

db = client['minicurso_python']


if __name__ == '__main__':
    # consultas
    users = db.users.find()
    for user in users:
        print(user)

    # consulta de un solo registro
    print("Consulta de un solo registro")
    users = db.users.find({'username':'python'})
    for user in users:
        print(user)


    # consulta de un solo registro
    print("Contando")
    users = db.users.find({'age':39}).count()
    print(users)

    print("AND")
    users = db.users.find({"$and": [ {"username":"python"},{"age":39}]})
    for user in users:
        print(user)


    print("Obtener un registro en concreto")
    user = db.users.find_one() #Para obtener el primer registro
    print(user)


