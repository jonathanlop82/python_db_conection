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
    user = User.get( User.id == 5)
    print(user)

    # Actualizando un campo
    user.active = False
    user.save()
    #2 metodo de clase update()
    query = User.update(active=True).where(User.id == 1)
    query.execute()

    # Borrar un registro
    user.delete_instance()
    
    


if __name__ == '__main__':
    run()