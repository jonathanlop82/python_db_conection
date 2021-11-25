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
    # Cantidad de usuarios
    count = User.select().count()
    print(count)
    
    #Limitar los registros mostrados
    users = User.select().where(User.id > 1).limit(2)
    for user in users:
        print(user)

    #Ordenar
    print("###Ordenar###")
    users = User.select().where(User.id > 1).order_by(User.username.desc())
    for user in users:
        print(user)

    print("###Retornando el  ultimo registro##")
    user = User.select().order_by(User.id.desc()).limit(1).get()
    print(user)



if __name__ == '__main__':
    run()