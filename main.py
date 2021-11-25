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

def run():
    try:
        #Para conectar a la base de datos
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE, PORT)

        cursor = connection.cursor()
        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

        cursor.execute(SHOW_TABLES)
        #Para mostrar las tablas en la pantalla
        tables = cursor.fetchall()  
        # Se recorre las tablas 
        for table in tables:
            print(table[0])

        connection.close()
    except MySQLdb.Error as error:
        print(error)



if __name__ == '__main__':
    run()