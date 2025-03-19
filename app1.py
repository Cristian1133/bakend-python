from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite que cualquier origen acceda a la API

def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
    )



# Endpoint para solicitar un permiso (solo docentes)
@app.post('/api/v1/solicitar_permiso')
def solicitar_permiso():
    datos = request.json
    id_usuario = datos.get('id_usuario')
    motivo = datos.get('motivo')
    
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO permisos (id_usuario, motivo) VALUES (%s, %s)", (id_usuario, motivo))
        conexion.commit()
        return jsonify({"mensaje": "Permiso solicitado exitosamente"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conexion.close()

# Endpoint para obtener permisos pendientes (para coordinador)
@app.get('/api/v1/permisos_pendientes')
def listar_permisos_pendientes():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, id_usuario, motivo, fecha_solicitud FROM permisos WHERE estado = 'pendiente'")
        permisos = cursor.fetchall()
        return jsonify([{ "id": p[0], "id_usuario": p[1], "motivo": p[2], "fecha_solicitud": p[3]} for p in permisos]), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conexion.close()

# Endpoint para aprobar o rechazar permisos
@app.post('/api/v1/gestionar_permiso')
def gestionar_permiso():
    datos = request.json
    id_permiso = datos.get('id_permiso')
    estado = datos.get('estado')
    
    if estado not in ['aprobado', 'rechazado']:
        return jsonify({"error": "Estado no válido"}), 400
    
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("UPDATE permisos SET estado = %s WHERE id = %s", (estado, id_permiso))
        conexion.commit()
        return jsonify({"mensaje": "Permiso actualizado"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conexion.close()

if __name__ == '__main__': 
    app.run(debug=True)
