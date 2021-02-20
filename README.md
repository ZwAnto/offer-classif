# Classification d'offres d'emplois

- [Idées](#Idées)
- [Approche](#Approche)
- [Résultat](#Résultat)
- [Arborescence](#Arborescence)
- [Initialisation de l'environnement](#Initialisation-de-l'environnement)
    * [Developpement](#Developpement)
- [Utilisation](#Utilisation)
    * [Entrainement](#Entrainement)
    * [Prediction](#Prediction)

  
# Idées

* Créer un embedding des offres basé sur la description et/ou le titre (tranformers, fastetxt/Glove ?, spacy) puis appliquer un modèle de classification.
**Amélioration**: Entrainer le modèle d'embedding sur un corpus specialisé. J'ai eu des problèmes avec les modèles Spacy français sur les termes anglais (ie data).

* Limitation générale: peu de texte pour décrire les postes dans le thesaurus
* Analyser la correlation entre les différents poste ?

* dur de différencier les postes proches (ie postes de develeppement)
    * **Piste**: Règles à base de mots clef pour certain poste ? (java, c++, .NET) 

# Approche

# Résultat

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
make setup-conda-env
make start-notebook # to start notebook server 
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
python -m offerclassif.cli predict <path to offers_test_sample.json> <path to job_thesorus.json> <model file> <Optionnal output file for predicitons>
```