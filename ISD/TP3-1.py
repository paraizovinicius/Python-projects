import pandas as pd

# Abre o arquivo unpopspotify.csv
df = pd.read_csv("C:\\Users\\parai\\Downloads\\unpopular_songs_full.csv")

# Statistiques basiques
for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        continue
    mean = df[col].mean()
    std = df[col].std()
    min = df[col].min()
    max = df[col].max()

    print(f"{col}: moyen={mean}, standard error={std}, minimum={min}, maximum={max}")

print()


# % des données manquantes
for col in df.columns:
    na_count = df[col].isna().sum()
    na_percent = na_count / len(df) * 100

    print(f"{col}: porcentage de données manquantes={na_percent:.2f}%")
    
    
print()

# Afficher la matrice de corrélation linéaire entre les colonnes numériques
correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()

# Analyser la corrélation entre "popularity" et "key"
correlation_popularity_key = correlation_matrix.loc["popularity", "key"]
print(f"\nCorrélation entre 'popularity' et 'key': {correlation_popularity_key}")