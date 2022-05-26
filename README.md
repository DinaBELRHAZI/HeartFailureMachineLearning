# Prédictions concernant les maladies cardiaques

## Installation du projet

1. Téléchargez le projet
2. Installez les plugins 
3. Lancez la commande "choco install graphviz" dans un powerShell (Administrateur) puis redémarrez votre pc 


## Etude des correlations entre plusieurs variables

Les variables : 
- Age : âge du patient [années].
- Sex : sexe du patient 
  1. M : Male 
  2. F : Female
  
- ChestPainType : type de douleur thoracique 
    1. TA : Angine typique 
    2. ATA : Angine atypique
    3. NAP : Douleur non angineuse
    4. ASY : Asymptomatique
  
- RestingBP : pression artérielle au repos [mm Hg].
- Cholestérol : cholestérol sérique [mm/dl].
- FastingBS : glycémie à jeun 
  1. 1 : si FastingBS > 120 mg/dl 
  2. 0 : sinon
- RestingECG : résultats de l'électrocardiogramme au repos 
  1. Normal : normal 
  2. ST : présentant une anomalie de l'onde ST-T (inversions de l'onde T et/ou élévation ou dépression du segment ST de > 0,05 mV) 
  3. HVG : présentant une hypertrophie ventriculaire gauche probable ou certaine selon les critères d'Estes]

- FCM : fréquence cardiaque maximale atteinte [Valeur numérique comprise entre 60 et 202].
- ExerciseAngina : angine de poitrine induite par l'exercice 
  1. Y : Oui 
  2. N : Non
  
- Oldpeak : oldpeak = ST [Valeur numérique mesurée en dépression].
- ST_Slope : la pente du segment ST du pic d'exercice 
  1. Up : en pente ascendante 
  2. Flat : plat 
  3. Down : en pente descendante
  
- HeartDisease : classe de sortie 
  1. 1 : maladie cardiaque 
  2. 0 : normal

### Représentations des corrélations des variables 

Voici quelques exemples :


### Représentation en 3D  


## Analyse des prédictions

Calculer la matrice de confusion pour évaluer la précision d'une classification.
![matrice-confusion](img/matrice-confusion.png)



![X](img/x-train-X-test.png)

![Y](img/y-train-y-test.png)


![Logistic-regression-prediction](img/Logistic-regression-prediction.png)

![Arbre-decision](dtree_render.png)
![Arbre-decision-prediction](img/arbre-decision-prediction.png)

## Résutats




