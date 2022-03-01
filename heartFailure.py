import dk as dk
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Informations sur les attributs :

# Age : âge du patient [années].
# Sex : sexe du patient [M : Male, F : Female].
# ChestPainType : type de douleur thoracique [TA : Angine typique, ATA : Angine atypique, NAP : Douleur non angineuse, ASY : Asymptomatique].
# RestingBP : pression artérielle au repos [mm Hg].
# Cholestérol : cholestérol sérique [mm/dl].
# FastingBS : glycémie à jeun [1 : si FastingBS > 120 mg/dl, 0 : sinon].
# RestingECG : résultats de l'électrocardiogramme au repos [Normal : Normal : normal, ST : présentant une anomalie de l'onde ST-T (inversions de l'onde T et/ou élévation ou dépression du segment ST de > 0,05 mV), HVG : présentant une hypertrophie ventriculaire gauche probable ou certaine selon les critères d'Estes].
# FCM : fréquence cardiaque maximale atteinte [Valeur numérique comprise entre 60 et 202].
# ExerciseAngina : angine de poitrine induite par l'exercice [Y : Oui, N : Non].
# Oldpeak : oldpeak = ST [Valeur numérique mesurée en dépression].
# ST_Slope : la pente du segment ST du pic d'exercice [Up : en pente ascendante, Flat : plat, Down : en pente descendante].
# HeartDisease : classe de sortie [1 : maladie cardiaque, 0 : normal].


# Read Data
df = pd.read_csv('heart.csv')

print(df.head())

# show shape
# L'ensemble de données comporte donc 918 lignes et 12 colonnes.
print(df.shape, "\n")

# Informations du tableau ( column, Non-Null Count, Dtype)
print("Info = ", df.info())

# description des données
print("\n *************** Description de données ******************")
print(df.describe(include='all'))

# Vérifier les valeurs nulles
print("\n *************** Valeurs nulles ? ******************")
print(df.isnull().sum())

print("\n ****************************************************************** \n")

non_numerical_data = [f for f in df.columns if df[f].dtype == 'O']
print("Caractéristiques catégorielles : ", non_numerical_data)

numerical_data = [f for f in df.columns if df[f].dtype != 'O']
print("Caractéristiques numériques : ", numerical_data)

# Ces caractéristiques ont plus de 25 instances numériques distinctes.
numerical_data_continuous = [f for f in numerical_data if df[f].nunique() > 25]
print("Caractéristiques numériques continues : ", numerical_data_continuous)

# Ces caractéristiques ont moins de 25 instances numériques distinctes.
numerical_data_discrete = [f for f in numerical_data if df[f].nunique() < 25]
print("Caractéristiques numériques discrètes : ", numerical_data_discrete)

print("\n ****************************************************************** \n")

print(df)

# **************************************************

for f in non_numerical_data:
    sns.countplot(x=f, data=df)
    plt.title(f + ' count plot')
    plt.show()

# Résultats
# 1) Le nombre d'hommes souffrant de maladies cardiaques est nettement supérieur à celui des femmes.
# 2) Le type de douleur thoracique chez les personnes souffrant de maladies cardiaques est principalement l'ASY.
# 3) L'ECG de repos de la plupart des personnes souffrant de maladies cardiaques est normal.
# 4) La majorité des personnes n'ont pas eu une angine de poitrine à l'effort.
# 5) La pente ST de la plupart des personnes souffrant de cardiopathie est plate.


# ----------------------------------

for f in numerical_data_discrete:
    sns.countplot(x=f, data=df)
    plt.title(f + ' count plot')
    plt.show()

# Résultats
# La plupart des personnes souffrant de maladies cardiaques ont une glycémie à jeun faible.

# ----------------------------------

for f in numerical_data_continuous:
    sns.displot(x=df[f])
    print('la valeur médiane pour les caractéristiques ' + f + ' est de ', df[f].median())
    plt.axvline(df[f].mean(), linestyle='--', color="red")
    plt.axvline(df[f].median(), linestyle='--', color="yellow")
    plt.title(f + ' distribution plot')
    plt.show()

# ----------------------------------


plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), annot=True)
plt.show()

dt = pd.DataFrame()
dt = df.groupby(['Age'])[['HeartDisease']].sum()
sns.lineplot(x='Age', y='HeartDisease', data=dt)
plt.show()

# résultats
# Il semble que les personnes ayant entre la cinquantaine et soixantaine
# soient les plus susceptibles de souffrir d'une maladie cardiaque.

# Diagramme à barres verticales

dt = dt.sort_values(by=['HeartDisease'], ascending=False)[:10]  # 10 premiers éléments
dt.plot.barh()
plt.show()

dt1 = df.groupby(['Cholesterol'])[['HeartDisease']].sum()
sns.lineplot(x='Cholesterol', y='HeartDisease', data=dt1)
plt.legend("HeartDisease en fonction de l'âge")
plt.show()

dt2 = df.groupby(['RestingECG'])[['HeartDisease']].sum()
sns.lineplot(x='RestingECG', y='HeartDisease', data=dt2)
plt.legend("HeartDisease en fonction des résultats de l'électrocardiogramme au repos")
plt.show()
# Résultat: la majorité des personnes malades ont un résultat de l'électrocardiogramme au repos

dt3 = df.groupby(['ExerciseAngina'])[['HeartDisease']].sum()
sns.lineplot(x='ExerciseAngina', y='HeartDisease', data=dt3)
plt.legend("HeartDisease en fonction de la présence ou non d'une angine de poitrine induite par l'exercice")
plt.show()
# Résultat: la majorité des personnes malades ont une angine de poitrine induite par l'exercice

dt4 = df.groupby(['Oldpeak'])[['HeartDisease']].sum()
sns.lineplot(x='Oldpeak', y='HeartDisease', data=dt4)
plt.legend("HeartDisease en fonction de la Valeur numérique mesurée en dépression (ST)")
plt.show()
# Résultat: Les malades ont une valeur numérique mesurée en dépression entre 0 et 4

dt5 = df.groupby(['ST_Slope'])[['HeartDisease']].sum()
sns.lineplot(x='ST_Slope', y='HeartDisease', data=dt5)
plt.legend("HeartDisease en fonction de la Valeur numérique mesurée en dépression (ST)")
plt.show()

# Résultat: Plus la pente du segment ST du pic d'exercice est plate plus il y a de malades


sns.scatterplot(x='Cholesterol', y='Age', hue='Sex', data=df)
plt.axvline(129, linestyle='--', color="red")
plt.axhline(53, linestyle='--', color="red")
plt.show()
#
# sns.scatterplot(x='Cholesterol', y='RestingBP', hue='Sex', data=df)
# plt.axvline(129, linestyle='--', color="red")  # normal level for LDL
# plt.axhline(120, linestyle='--', color="red")  # normal resting BP
# plt.show()
#
# sns.scatterplot(x='RestingECG', y='ExerciseAngina', hue='HeartDisease', data=df)
# plt.axvline(1, linestyle='--', color="red")
# plt.axhline(1, linestyle='--', color="red")
# plt.show()

sns.pairplot(df, hue='HeartDisease')
