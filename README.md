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

* Créer un embedding des offres basé sur la description et/ou le titre (fastetxt, Glove, spacy) puis appliquer un modèle de classification (type RandomForest).  
**Amélioration**: Entrainer le modèle d'embedding sur un corpus specialisé. J'ai eu des problèmes avec les modèles Spacy français sur les termes anglais (ie data).
* Utiliser des modèles type tranformers


* Limitation générale: peu de texte pour décrire les postes dans le thesaurus
* Analyser la correlation entre les différents poste ?

* dur de différencier les postes proches (ie postes de develeppement)
    * **Piste**: Règles à base de mots clef pour certain poste ? (java, c++, .NET) 

# Approche

Mon approche à consisté à utiliser un modèle de work embedding (spacy) pour récupérer une représentation vectorielle des offres.  
J'ai dans un premier temps comparé les représentations vectorielles selon qu'on l'on ai appliqué le modèle d'embedding sur le titre, la description ou le titre et le description.  
J'ai ensuite tenté deux approches pour classifier les offres. 
* La première constite à appliqué directement un classifieur (ExtraTrees) sur la représentation vectorielle pour prédire le champ `internal_label`. 
* La deuxième approche à consisté à prédire d'abord le champ `sector_internal_label` (sur lequel nous avons de très bonne performance), puis de faire un deuxieme modèle qui prédit le champ `internal_label` à partir de la représentation vectorielle et des résultats du premier modèle. Tout cela dans le but de contraindre la classification pour qu'elle tienne compte du secteur.

## Résultat

La première observation que l'on peut faire est que le titre semble suffisant pour entrainer un modèle. Lorsque que l'on prend en compte la description, les performance des modèles sont moins bonnes.  
Ensuite une autre observation est que les modèles semblent donner de bon résultat:

* ~75% d'accuracy OOB sur la prédiction du champ `internal_label`
* ~95% d'accuracy OOB sur la prédiction du champ `sector_internal_label`

Les modèles ont cependant beaucoup de mal à distingué les postes similaires (ie Developpeur C++, Developpeur Java, ...).

## Pistes d'améliorations

# Arborescence
```
├── docs                            # sphynx doc
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