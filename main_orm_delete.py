import peewee
from models import (CategoriesProduct, User, Store, Product, Category)

def create_tables():
    if CategoriesProduct.table_exists():
        CategoriesProduct.drop_table()


    if Category.table_exists():
        Category.drop_table()
    
    if Product.table_exists():
        Product.drop_table()
    
    
    if Store.table_exists():
        Store.drop_table()
    

    if User.table_exists():
       User.drop_table()
    
    
    User.create_table()
    Store.create_table()
    Product.create_table()
    Category.create_table()
    CategoriesProduct.create_table()

    
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
    Product.create(store_id=1, name='mayonesa', description='mayonesa', price=2.9, stock=3)

    Product.create(store_id=2, name='Soda', description='Dieta', price=4.5, stock=10)
    Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=6.5, stock=8)
    Product.create(store_id=2, name='Salsa', description='chile habanero', price=7.5, stock=2)
    Product.create(store_id=2, name='Mostaza', description='Mostaza', price=5.5, stock=5)

def insert_categories():
    Category.create(name='Liquidos', description='liquidos')
    Category.create(name='Embutidos', description='embutidos')
    Category.create(name='Snacks', description='snacks')
    Category.create(name='Aderezos', description='aderezos')
    Category.create(name='Carnes', description='carnes')

def insert_categories_products():
    CategoriesProduct.create(category_id=1, product_id=2) #liquidos --> Leche
    CategoriesProduct.create(category_id=1, product_id=5) #liquidos --> soda
    CategoriesProduct.create(category_id=1, product_id=7) #liquidos --> Salsa

    CategoriesProduct.create(category_id=2, product_id=3) #liquidos --> Leche

    CategoriesProduct.create(category_id=3, product_id=6) #liquidos --> Leche

    CategoriesProduct.create(category_id=4, product_id=4) #liquidos --> Leche
    CategoriesProduct.create(category_id=4, product_id=8) #liquidos --> Leche

    CategoriesProduct.create(category_id=5, product_id=3) #liquidos --> Leche

def create_schema():
    create_tables()
    insert_users()
    insert_stores()
    insert_products()
    insert_categories()
    insert_categories_products()

def run():
    
    jamon = Product.get(Product.name == 'Jamon')

    jamon.delete_instance(recursive=True)


if __name__ == '__main__':
    run()