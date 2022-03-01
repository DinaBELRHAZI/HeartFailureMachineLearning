import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from six import StringIO
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from graphviz import Source
import plotly.express as px
from sklearn.tree import export_graphviz

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

from IPython.display import Image
import pydotplus

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

data = data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'Sex', 'ChestPainType', 'RestingECG',
             'ExerciseAngina', 'ST_Slope', 'HeartDisease']]
print("\n", data.head(5))

plt.figure(figsize=(15, 10))
sns.heatmap(data.corr(), annot=True)
plt.show()

# *********************  FIN   ********** ENCODAGE DES LABELS  ***********************************


# ******************************* Entrainements et tests  *******************************************

print("\n\n ********************************* Entrainements et tests **************************************** \n")

X = data[["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak", "Sex", "ChestPainType", "RestingECG",
          "ExerciseAngina", "ST_Slope", ]]
y = data["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)

print("Il y a ", len(X_test), " X_test")
print("------------x test-----------")
print(X_test)

print("Il y a ", len(X_train), " X_train")
print("------------x train-----------")
print(X_train)

print("Il y a ", len(y_test), " y_test")
print("------------y test-----------")
print(y_test)

print("Il y a ", len(y_train), " y_train")
print("------------y train-----------")
print(y_train)

# ******************************* LOGISTIC REGRESSION  *******************************************


pun = LogisticRegression(random_state=0, multi_class='multinomial', penalty='none', solver='newton-cg').fit(X_train,
                                                                                                            y_train)
print("\n\n ********************************* LOGISTIC REGRESSION **************************************** \n")

# Le modèle apprend la relation entre les chiffres (x_train) et les étiquettes (y_train)
pun.fit(X_train, y_train)

# print("Prédire pour une observation \n")
# print(pun.predict(X_test[0].remodeler(1, -1)), "\n")

# print("Prédire pour une observation \n")
# print(pun.predict(X_test[0].reshape(1, -1)))

print("Prédire plusieurs observations (images) à la fois \n")
print(pun.predict(X_test[0:10]), "\n")

print("prediction: \n")
preds = pun.predict(X_test)

print(pun.score(X_test, y_test) * 100, " % des prédictions faites sont bonnes !")

# Confusion Matrix

y_pred = pun.predict(X_test)
cf_matrix = confusion_matrix(y_test, y_pred)
# print(cf_matrix)
disp = ConfusionMatrixDisplay(cf_matrix, display_labels=pun.classes_)
disp.plot()
plt.show()

# *****************    FIN      ************** LOGISTIC REGRESSION  *******************************************


# ******************************* ARBRE DE DECISION  *******************************************
from sklearn import tree

clf = tree.DecisionTreeClassifier(max_depth=16)
clf.fit(X_train, y_train)

# print("------------predict-----------")
# print(X[0:2])
# print(clf.predict(X[0:2]))
# print(y[0:8])
# print("------------predict--one ---------")

# print(X[0])
# print(clf.predict(
#     X[0].reshape(1, -1)))  # reshape() function takes a single argument that specifies the new shape of the array
# print(y[0:2])

plt.figure(figsize=(8, 6), dpi=80)
tree.plot_tree(clf, feature_names=["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak", "Sex",
                                   "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"],
               class_names=["HeartDisease", "Not HeartDisease"], filled=True)
plt.savefig('out2.pdf')
plt.show()

graph = Source(tree.export_graphviz(clf, out_file=None, filled=True,
                                    rounded=True,
                                    special_characters=True,
                                    feature_names=["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak",
                                                   "Sex",
                                                   "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"],
                                    class_names=["HeartDisease", "Not HeartDisease"]))
graph.format = 'png'
graph.render('dtree_render', view=True)

print("********************************* ARBRE DE DECISION **************************************** \n")
print("prediction: \n")
print(clf.predict(X_test))
print("Arbre de décision : ", clf.score(X_test, y_test) * 100, " % des prédictions faites sont bonnes !")

# --------------------------- DATA IN 3D -------------------------------------------------------------------

# Figure 1
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# dummy data (your actual data should go here)
x = data["Age"]
y = data['ST_Slope']
z = data['Oldpeak']
ax.scatter(x, y, z, c=data['HeartDisease'], marker="o", label='HeartDisease')
ax.legend()
ax.set_xlabel('Age')
ax.set_ylabel('ST_Slope')
ax.set_zlabel('Oldpeak')
plt.title("Plan en 3D des maladies cardiaques en fonction de l'âge, du ST_Slope et du oldpeak ",
          fontdict={'fontsize': 10})

plt.show()

# Figure 2
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection="3d")

x = data["Age"]
y = data['FastingBS']
z = data['Sex']
ax.scatter(x, y, z, c=data['HeartDisease'], marker="o", label=data['HeartDisease'])
ax.legend()
ax.set_xlabel('Age')
ax.set_ylabel('FastingBS')
ax.set_zlabel('Sex')
plt.title("Plan en 3D des maladies cardiaques en fonction de l'âge, du glycémie à jeun et du sex ",
          fontdict={'fontsize': 10})

plt.show()


