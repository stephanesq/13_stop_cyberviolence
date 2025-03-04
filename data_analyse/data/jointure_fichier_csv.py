import pandas as pd

# Définir le chemin
path = './13_stop_cyberviolence/data_analyse/'

# Chargement des données

dim_etablissement = pd.read_csv(path+'data/DIM_ETABLISSEMENT.csv')
dim_commune = pd.read_csv(path+'data/DIM_COMMUNE.csv', low_memory=False)
dim_classe = pd.read_csv(path+'data/DIM_CLASSE.csv')
dim_enseignant = pd.read_csv(path+'data/DIM_ENSEIGNANT.csv')
dim_eleve = pd.read_csv(path+'data/DIM_ELEVE.csv')
fact_reponse = pd.read_csv(path+'data/FACT_REPONSE.csv')
dim_reponse = pd.read_csv(path+'data/DIM_REPONSE.csv')
dim_score = pd.read_csv(path+'data/DIM_SCORE.csv')
dim_question = pd.read_csv(path+'data/DIM_QUESTION.csv')

# Jointures
df = fact_reponse.merge(dim_eleve, left_on='ID_REPONDANT', right_on='ID_ELEVE', how='inner') \
    .merge(dim_classe, on='ID_CLASSE', how='inner') \
    .merge(dim_enseignant, on='ID_CLASSE', how='inner') \
    .merge(dim_reponse, on='KEY_REPONSE', how='inner') \
    .merge(dim_question, on='KEY_QUESTION', how='inner') \
    .merge(dim_score, on='KEY_REPONSE', how='inner')
#    .merge(dim_etablissement, on='ID_ETABLISSEMENT', how='inner') \
#    .merge(dim_commune, left_on='ZIPCODE', right_on='code_commune_INSEE', how='inner') \

df.head()