from flask import Flask,jsonify, render_template, request
import mysql.connector
from mysql.connector import Error

def consultas():
        try:
           connection = mysql.connector.connect(
            host='localhost',
            database='tienda',
            user='root',
            password=''
            )
           if connection.is_connected():
                select_query = "SELECT * FROM clientes"
                cursor = connection.cursor()
                cursor.execute(select_query)
                resultados = cursor.fetchall()
                return resultados

        except Error as e:
            print("Error durante la conexión a MySQL", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("Conexión a MySQL cerrada")      

app = Flask(__name__)

@app.get('/api/v1/users') 
def home():
    datos=[]
    resultados = consultas()
    for fila in resultados:
        id = fila[0]
        nombre = fila[1]
        data = {"id":id,"nombre":nombre}
        datos.append(data)

    return jsonify(datos) , 200, {'Access-Control-Allow-Origin':'*'}

if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run(debug=True)      