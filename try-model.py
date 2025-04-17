import pandas as pd
import joblib

# Carregar o modelo salvo
modelo = joblib.load('rent_model.pkl')

novos_dados = pd.DataFrame({
    'fire insurance': [121],
    'bathroom': [3],
    'parking spaces': [3]
})

previsao = modelo.predict(novos_dados)
print(f"Previsão do aluguel: {previsao[0]:.2f}")