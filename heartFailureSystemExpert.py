import dk as dk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read Data
df = pd.read_csv('heart.csv')

print(df.head())


def demander(fait, question='Est-il vrai que'):
    REPONSES = {'o': True, 'n': False, }
    while True:
        question = ""
        question = "%s '%s' ?[o/n] " % (question, fait)
        choice = input(question).lower()
        # if choice in REPONSES.keys():
        #     return REPONSES[choice]
        # else:
        #     print("Merci de répondre avec 'o' ou 'n'.")

        if choice == "o":
            question = "Avez-vous plus de 50 ans " % (question, fait)
            if choice == "o":
                return "Vous avez peut être une maladie du coeur "
            else:
                print("Vous avez peut de chance d'avoir un problème au coeur")



print(demander("Etes-vous un homme"))
