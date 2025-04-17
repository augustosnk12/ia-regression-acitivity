import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import joblib

df = pd.read_csv("rent.csv")

variaveis = ['fire insurance', 'bathroom', 'parking spaces']
X = df[variaveis]
y = df['rent amount']

# Divide os dados em treino e teste (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo de Regressão Linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Faz previsões
y_pred = modelo.predict(X_test)

# Avaliação do modelo
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n📊 Acurácia: {r2:.4f}")

# Salvar o modelo
joblib.dump(modelo, 'rent_model.pkl')
