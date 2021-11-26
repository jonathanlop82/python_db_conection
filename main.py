from pymongo import MongoClient
import re

client = MongoClient('192.168.0.5', 27017) #192.168.0.5 27017

# docker run -d -p 27017:27017 --name mongodb mongo:latest

db = client['minicurso_python']


if __name__ == '__main__':
    regex = re.compile('Tiffany') #Like %Tiffany%

    users = db.users.find( {'username': regex})
    for user in users:
        print(user)


