import mysql.connector 
try:
    Connection = mysql.connector.connect(
        host='localhost',
        database='tienda',
        user='root',
        password=''
    )
    if Connection.is_connected():
     cursor = Connection.cursor()
     insert_query = "INSERT INTO clientes (id_cliente, nombre) VALUES (%s, %s)" 
     valores_a_insertar = (10, "cliente 7")
     cursor.execute(insert_query, valores_a_insertar)
     Connection.commit()
     
        

except mysql.connector.Error as e:
    print('Error al conector a MySQL' , e)

finally:
    if (Connection.is_connected()):
        cursor.close()
        Connection.close()
        print("Conexion a MySQL cerrada.")