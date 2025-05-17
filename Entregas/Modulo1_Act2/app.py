# Adriel L Lamboy
# R00581571
# COMP2052

from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /
@app.route("/", methods=["GET"])
def home():
    return "Bienvenido al inicio de mi API Capstone"


@app.route("/info", methods=["GET"])
def info():
    return "Esta es la informacion basica de la app del modulo 1 utilizando flask "

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    mensaje_usuario = data.get("mensaje", "No hay mensaje")
    return {
        "respuesta": f"Hola, tu mensaje se envio con exito: '{mensaje_usuario}' Success!"
    }




if __name__ == "__main__":
    app.run(debug=True)