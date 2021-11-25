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
    try:
        user = User.get(User.id ==10)
        print(user)
    except User.DoesNotExist as error:
        print("Usuario no existe")
    

    ## Validando usando Select
    user = User.select().where(User.id == 10).first()
    print(user)
    if user:
        print("El usuario existe")
    else:
        print("No existe")

    #Utilizando metodo exists
    flag = User.select().where(User.id == 10).exists()
    if flag:
           print("El usuario existe")
    else:
        print("No existe")

if __name__ == '__main__':
    run()