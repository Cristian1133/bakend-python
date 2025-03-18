import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',       # O la dirección de tu servidor MySQL
        user='root',      # Reemplaza con tu usuario de MySQL
        password=''  # Reemplaza con tu contraseña de MySQL
    )
    if connection.is_connected():
        print('Conexión exitosa.')
        # No olvides cerrar la conexión una vez que hayas terminado con ella.
        connection.close()  
except mysql.connector.Error as e:
    print('Error al conectar a MySQL:', e)