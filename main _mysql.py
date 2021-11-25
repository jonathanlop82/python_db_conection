import MySQLdb

HOST = '192.168.0.5'
PORT = 33060
USER = 'root'
PASSWORD = 'secret'
DATABASE = 'minicurso_python'


USER_TABLE = """CREATE TABLE users(
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
                )"""

DROP_USER = " DROP TABLE IF EXISTS `users`"

SHOW_TABLES = "SHOW TABLES"

INSERT_USER = "INSERT INTO users (username , password) VALUES ( '{username}','{password}')"

SELECT_USER = "SELECT * FROM users WHERE id = {id}"

UPDATE_USER = "UPDATE users SET username='{username}', password='{password}' WHERE id = {id} "

DELETE_USER = "DELETE FROM users WHERE id = {id}"

def run():
    try:
        #Para conectar a la base de datos
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE, PORT)

        cursor = connection.cursor()
        #cursor.execute(DROP_USER)
        #cursor.execute(USER_TABLE)

        # cursor.execute(SHOW_TABLES)
        ###Para mostrar las tablas en la pantalla
        # tables = cursor.fetchall()  
        # # Se recorre las tablas 
        # for table in tables:
        #     print(table[0])

        #username = input("ingrese el username ")
        #password = input("ingrese el password ")
        
        
        ####Insertar una tupla en la tabla
        # query = INSERT_USER.format(username=username, password=password)
        # print(query)

        # try:
        #     cursor.execute(query)
        #     connection.commit()
        # except: #Si ocurre algun error durante la insercion
        #     connection.rollback()

        query = UPDATE_USER.format(username='codigofacilito', password='123', id=1)

        
        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()

        query = DELETE_USER.format(id=2)

        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()
        
        query = SELECT_USER.format(id=1)
        cursor.execute(query)
        users = cursor.fetchall()
        for user in users:
            print(user)

        connection.close()
    except MySQLdb.Error as error:
        print(error)



if __name__ == '__main__':
    run()