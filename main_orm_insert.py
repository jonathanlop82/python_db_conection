import peewee
import datetime


HOST = '192.168.0.5'
PORT = 33060
USER = 'root'
PASSWORD = 'secret'
DATABASE = 'minicurso_python'

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=PORT, user=USER, passwd=PASSWORD)

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50, null=True)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'


def run():

    if User.table_exists():
        User.drop_table()
    User.create_table()

    # Como insertar una tubla en la tabla users
    user = User()
    user.username = 'jonathan'
    user.password = '123456'
    user.email = 'jonathanlop82@gmail.com'
    user.save()

    # 2
    user = User(username='jlopez', password='p4ssw0rd',email='jonathan@hotmail.com')
    user.save()

    #3 enviando un diccionario 
    user = {'username':'cf','password':'123456'}
    user = User(**user)
    user.save()

    #4 Utilizando metodo de clase create()
    user = User.create(username='jonjon', password='password', email='jona@outlok.com')

    #5 Utilizando insert()

    query = User.insert(username='jonjon2', password='password2', email='jona2@outlok.com')
    query.execute()


if __name__ == '__main__':
    run()