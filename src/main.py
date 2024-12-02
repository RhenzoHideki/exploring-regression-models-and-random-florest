import pandas as pd

# Caminho para o dataset
file_path = "data/AmesHousing.csv"

# Carregar os dados
data = pd.read_csv(file_path)

# Exibir as primeiras linhas
print(data.head())