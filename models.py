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
        return '{name} - ${price}'.format(name=self.name, price=self.price)

class Category(peewee.Model):
    name = peewee.CharField(max_length=50)
    description = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'categories'

    def __str__(self):
        return self.name


class CategoriesProduct(peewee.Model):
    product = peewee.ForeignKeyField(Product, related_name='categories')
    category = peewee.ForeignKeyField(Category, related_name='products')


    class Meta:
        database = database
        db_table = 'categories_products'

    def __str__(self):
        return "{} - {}".format(self.product, self.category)