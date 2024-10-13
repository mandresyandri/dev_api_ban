import get_data as gd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Bienvenue à l'API des adresses. Utilisez les endpoints pour obtenir des données.",
        "endpoints": {
            "/<code_insee>": "Obtenir les données pour un code INSEE spécifique.",
            "/is_update": "Vérifie si les données ont été mises à jours."
        }
    }), 200

@app.route("/<int:code_insee>", methods=["GET"])
def get_data_by_insee(code_insee):
    try:
        data = gd.data_request(code_insee)
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"error": "Données non trouvées pour le code INSEE fourni."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/is_update", methods=["GET"])
def is_update():
    try:
        data = gd.data_request(92048) 
        for item in data:
            if (item['nom_voie'] == "Place Henry Wolf") and (item['code_postal'] == 92190):
                return jsonify({
                    "Alerte" : "Les codes postaux n'ont pas encore été modifiés",
                    "Action": f"Le code postal pour '{item['nom_voie']}' doit être 92360."
                    }), 400
        return jsonify({
            "message": "Adresse mlf modifiée."
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)