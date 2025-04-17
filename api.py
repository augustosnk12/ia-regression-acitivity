from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

modelo = joblib.load('rent_model.pkl')

@app.route('/preview_rent', methods=['POST'])
def prever():
    try:
        dados = request.get_json()
        fire_insurance = dados.get('fire insurance')
        bathroom = dados.get('bathroom')
        parking_spaces = dados.get('parking spaces')

        if fire_insurance is None or bathroom is None or parking_spaces is None:
            return jsonify({'erro': 'Você deve informar fire insurance, bathroom e parking spaces.'}), 400

        entrada = pd.DataFrame([{
            'fire insurance': fire_insurance,
            'bathroom': bathroom,
            'parking spaces': parking_spaces
        }])

        resultado = modelo.predict(entrada)[0]

        return jsonify({'previsao_rent_amount': round(resultado, 2)})

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
