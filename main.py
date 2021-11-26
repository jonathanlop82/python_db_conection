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

class Store(peewee.Model):
    #user = peewee.ForeignKeyField(User, primary_key=True) #Relacion 1 a 1
    user = peewee.ForeignKeyField(User, related_name='stores') #Relacion 1 a muchos, 1 usuario tiene muchas tiendas
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name
def create_tables():
    if User.table_exists():
       User.drop_table()
    User.create_table()

    if Store.table_exists():
        Store.drop_table()
    Store.create_table()


def run():
    user = User.get(User.id==1)
    print(user)

    for store in user.stores:
        print(store)

    #Consulta Store 1
    store1 = Store.get(Store.id ==1)
    print(store1.user)


if __name__ == '__main__':
    run()