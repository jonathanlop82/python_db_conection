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
    
    def __str__(self):
        return self.username


def run():
    # Consultando registros # get() solo trae un registro
    user = User.select().where(User.id > 1).get() # Select * from users;
    print(user.id,end=" ")
    print(user.username,end=" ")
    print(user.password)

    # Select * from users where emai is Null
    user = User.select().where( User.email >> None).get()
    print(user)

    ## Consultando valoder desde una lista
    users_list = ['cf','jonjon']
    users = User.select().where( User.username << users_list)
    for user in users:
        print(user)
    
    # select @ from users where user like '%jonjon%'
    users = User.select().where( User.username.contains('jon'))
    for user in users:
        print(user)

    print("###")
    # select * from users where user like 'jon%'
    users = User.select().where( User.username.endswith('jon')) #startswith('jon')
    for user in users:
        print(user)


if __name__ == '__main__':
    run()