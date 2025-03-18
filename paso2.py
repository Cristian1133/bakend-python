import mysql.connector 
try:
    Connection = mysql.connector.connect(
        host='localhost',
        database='tienda',
        user='root',
        password=''
    )
    if Connection.is_connected():
        db_info = Connection.get_server_info()
        print('Conexion al servidor MySQL version', db_info)
        cursor = Connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("Conectado a la base de datos: ", record)
        

except mysql.connector.Error as e:
    print('Error al conector a MySQL' , e)

finally:
    if (Connection.is_connected()):
        cursor.close()
        Connection.close()
        print("Conexion a MySQL cerrada.")