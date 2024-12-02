import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split 

# Caminho para o dataset
file_path = "data/AmesHousing.csv"

# Carregar os dados
data = pd.read_csv(file_path)

# Escolhendo qual é o alvo
target = data.SalePrice

# RandomForest
random_forest_model = RandomForestRegressor(random_state=1)

# Exibir as primeiras linhas
print(data.head())  