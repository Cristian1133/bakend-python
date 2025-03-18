import mysql.connector 
try:
    Connection = mysql.connector.connect(
        host='localhost',
        database='tienda',
        user='root',
        password=''
    )
    if Connection.is_connected():
        select_query = "SELECT * FROM clientes"
        cursor = Connection.cursor()
        cursor.execute(select_query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

except mysql.connector.Error as e:
    print('Error al conector a MySQL' , e)

finally:
    if (Connection.is_connected()):
        cursor.close()
        Connection.close()
        print("Conexion a MySQL cerrada.")