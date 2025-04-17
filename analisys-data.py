import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("rent.csv")

# Calcular a correlação com a variável alvo
correlation = df.drop(columns=['id']).corr(numeric_only=True)
target_corr = correlation['rent amount'].drop('rent amount').sort_values(ascending=False)

# Imprimir correlações
print("\nCorrelação das variáveis com 'rent amount':\n")
print(target_corr)

# Plotar a correlação
plt.figure(figsize=(10, 6))
sns.barplot(x=target_corr.values, y=target_corr.index, palette='coolwarm')
plt.title("Correlação com a variável 'rent amount'", fontsize=14)
plt.xlabel("Coeficiente de Correlação", fontsize=12)
plt.ylabel("Variáveis", fontsize=12)
plt.grid(True, axis='x', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
