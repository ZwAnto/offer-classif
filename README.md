# Classification d'offres d'emploi

- [Idées](#Idées)
- [Approche](#Approche)
    * [Résultat](#Résultat)
    * [Pistes d'améliorations](#Pistes-d'améliorations)
- [Arborescence](#Arborescence)
- [Initialisation de l'environnement](#Initialisation-de-l'environnement)
    * [Developpement](#Developpement)
- [Utilisation](#Utilisation)
    * [Entrainement](#Entrainement)
    * [Prediction](#Prediction)

  
# Idées

En abordant le sujet et en parcourant rapidement les données, les idées qui me sont venues sont les suivantes :

* Créer un embedding des offres basé sur la description et/ou le titre (fastetxt, Glove, spacy) puis appliquer un modèle de classification (type RandomForest).  
    * **Amélioration**: Entrainer le modèle d'embedding sur un corpus specialisé. J'ai eu des problèmes avec les modèles Spacy français sur les termes anglais (ie data).
* Utiliser des modèles type tranformers
* Limitation générale: peu de texte pour décrire les postes dans le thesaurus
* Analyser la corrélation entre les différents poste/offre ?

# Approche

Mon approche à consisté à utiliser un modèle de word embedding (spacy) pour récupérer une représentation vectorielle des offres.  
Après avoir fait une rapide exploration du jeu de données (cf `notebooks/1. Exploration.ipynb`) j'ai comparé les représentations vectorielles selon qu'on l'on ai appliqué le modèle d'embedding sur le titre, la description ou la combinaison du titre et de la description (cf `notebooks/2. Embedding + TSNE.ipynb`).  

J'ai ensuite tenté deux approches pour classifier les offres (cf `notebooks/3. Prediction.ipynb`):
* La première consiste à appliquer directement un classifieur (ExtraTrees) sur la représentation vectorielle pour prédire le champ `internal_label`. 
* La deuxième approche à consisté à prédire d'abord le champ `sector_internal_label` (sur lequel nous avons de très bonne performance), puis de faire un deuxieme modèle qui prédit le champ `internal_label` à partir de la représentation vectorielle et des résultats du premier modèle. Tout cela dans le but de contraindre la classification pour qu'elle tienne compte du secteur.

## Résultats

La première observation que l'on peut faire est que le titre semble suffisant pour entrainer un modèle. Lorsque que l'on prend en compte la description, les performances des modèles diminuent.  
Ensuite une autre observation est que la deuxième approche semble donnée de bons réultats:

* ~75% d'accuracy OOB sur la prédiction du champ `internal_label`
* Plus de 90% de chances d'avoir le bon libellé dans le top 3.
* ~95% d'accuracy OOB sur la prédiction du champ `sector_internal_label`

Les modèles ont cependant beaucoup de mal à distinguer les postes avec des intitulés similaires (ie Developpeur C++, Developpeur Java, ...).
* **Piste**: Règles à base de mots clef pour certain poste ? (java, c++, .NET) 

## Pistes d'amélioration



# Arborescence
```
├── docs                            # sphynx doc
|   └── _build
|       └── html
|           └── index.html          # Page d'acceuil de la doc
├── notebooks
|   ├── 1. Exploration.ipynb        # Exploration notebook
|   ├── 2. Embedding + TSNE.ipynb   # Embedding exploration
|   └── 3. Prediction.ipynb         # Training and prediction notebook
├── offerclassif
|   ├── cli.py                      # CLI
|   ├── data.py                     # Data related functions
|   ├── embedding.py                # Embedding related functions
|   └── utils.py                    # Miscelanous functions
├── requirements
|   ├── dev.txt                     # Dev requirements
|   └── prod.txt                    # Prod requirements
├── Makefile                    
└── environnment.yml                # Conda environnement spec
```

# Initialisation de l'environnement
```
conda create --name <env_name> python=3.8
conda activate <env_name>

pip install git+https://github.com/ZwAnto/offer-classif.git
python -m spacy download fr_core_news_md
```
## Developpement
```
git clone https://github.com/ZwAnto/offer-classif.git
make setup-conda-env # create an environment call offer-classif and register ipython kernel
python -m spacy download fr_core_news_md
make start-notebook # to start a notebook server 
```
# Utilisation
## Entrainement
```
conda activate <env_name>
python -m offerclassif.cli train <path to offers_train.json> <path to job_thesorus.json> <output model file>
```
## Prediction
```
conda activate <env_name>
python -m offerclassif.cli predict <path to offers_test_sample.json> <path to job_thesorus.json> <model file> <Optionnal output file>
```