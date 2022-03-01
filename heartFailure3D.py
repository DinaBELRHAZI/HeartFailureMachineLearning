# Python program to demonstrate scatter
# plot
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import plotly.express as px

# Read Data
df = pd.read_csv('heart.csv')

print(df.head())

# show shape
# L'ensemble de données comporte donc 918 lignes et 12 colonnes.
print(df.shape, "\n")

New_Stats = df
# Convertir une variable catégorielle en variables factices/indicatrices.
data = pd.get_dummies(New_Stats["Sex"])
print("DUMMIES : \n")
print(data.head(5))

# Suppression colonne Sex
New_Stats.drop('Sex', axis='columns')

print("NEW STATS sans colonne sex : \n", New_Stats.head(5))

# ******************************* ENCODAGE DES LABELS  *******************************************

le = LabelEncoder()
label_Sex = le.fit_transform(df["Sex"])
label_ChestPainType = le.fit_transform(df["ChestPainType"])
label_RestingECG = le.fit_transform(df["RestingECG"])
label_ExerciseAngina = le.fit_transform(df["ExerciseAngina"])
label_STSlope = le.fit_transform(df["ST_Slope"])

print("\n", le.classes_)

# Suppression colonne Sex
data = df.drop("Sex", axis='columns')
# Insertion des valeurs encodé du label Sex
data["Sex"] = label_Sex
# Affiche les 5 premières lignes du tableu data
print("\n", data.head(5))

# Suppression colonne ChestPainType
data = data.drop("ChestPainType", axis='columns')
# Insertion des valeurs encodé du label ChestPainType
data["ChestPainType"] = label_ChestPainType
# Affiche les 5 premières lignes du tableu data
print("\n", data.head(5))

# Suppression colonne RestingECG
data = data.drop("RestingECG", axis='columns')
# Insertion des valeurs encodé du label RestingECG
data["RestingECG"] = label_RestingECG
# Affiche les 5 premières lignes du tableu data
print("\n", data.head(5))

# Suppression colonne ExerciseAngina
data = data.drop("ExerciseAngina", axis='columns')
# Insertion des valeurs encodé du label ExerciseAngina
data["ExerciseAngina"] = label_RestingECG
# Affiche les 5 premières lignes du tableu data
print("\n", data.head(5))

# Suppression colonne ST_Slope
data = data.drop("ST_Slope", axis='columns')
# Insertion des valeurs encodé du label ST_Slope
data["ST_Slope"] = label_STSlope
# Affiche les 5 premières lignes du tableu data
print("\n", data.head(5))

# plot = px.scatter_3d(data, x='Age',
#                      y='FastingBS',
#                      z='Sex',
#                      color='HeartDisease')
#
# plot.show()

plot = px.scatter_3d(data, x='Age',
                     y='RestingECG',
                     z='Oldpeak',
                     color='HeartDisease', symbol='ExerciseAngina',
                     opacity=1)
plot.update_layout(template="plotly_dark", margin=dict(l=5, r=0, b=0, t=10))
plot.show()
