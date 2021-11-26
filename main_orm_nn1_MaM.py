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

class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store, related_name='products')
    price = peewee.DecimalField(max_digits=5, decimal_places=2) #100.00
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return self.name



def create_tables():
    if Product.table_exists():
        Product.drop_table()
    
    
    if Store.table_exists():
        Store.drop_table()
    

    if User.table_exists():
       User.drop_table()
    
    
    User.create_table()
    Store.create_table()
    Product.create_table()

    
def insert_users():
    User.create(username='jonathan', password='password', email='jon@jonathanlopez.xyz')
    User.create(username='jonathan_jr', password='password', email='jonjr@jonathanlopez.xyz')

def insert_stores():
    Store.create(user_id=1, name='Tienda 1', address='Panama')
    Store.create(user_id=2, name='Tienda 2', address='Brisas del Golf')

def insert_products():
    Product.create(store_id=1, name='Pan', description='Pan Integral', price=5.5, stock=5)
    Product.create(store_id=1, name='Leche', description='Baja en grasa', price=15.5, stock=7)
    Product.create(store_id=1, name='Jamon', description='de pavo', price=30.9, stock=3)

    Product.create(store_id=2, name='Soda', description='Dieta', price=4.5, stock=10)
    Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=6.5, stock=8)
    Product.create(store_id=2, name='Salsa', description='chile habanero', price=7.5, stock=2)

def create_schema():
    create_tables()
    insert_users()
    insert_stores()
    insert_products()

def run():
    create_schema()

    user = User.get(User.id == 1)
    for store in user.stores:
        for product in store.products:
            print(product)


if __name__ == '__main__':
    run()