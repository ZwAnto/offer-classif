# Classification d'offres d'emplois

# Idées

* Créer un embedding des offres basé sur la description et/ou le titre (tranformers, fastetxt/Glove ?, spacy) puis appliquer un modèle de classification  
**Amélioration**: Entrainer le modèle d'embedding sur un corpus specialisé. J'ai eu des problèmes avec les modèles Spacy sur les termes anglais (ie data).

* Limitation générale: peu de texte pour décrire les postes dans le thesaurus
* Analyser la correlation entre les différents poste ?

# Environnement
## Initialisation de l'environnement conda
```
make setup-conda-env
```
## Lancement d'un notebook jupyter
```
make start-notebook
```
# Utilisation
## Entrainement
```
conda activate offer-classif
python -m offerclassif train <path to offers_train.json> <path to job_thesorus.json> <output model file>
```
## Prediction
```
conda activate offer-classif
python -m offerclassif predict <path to offers_test_sample.json> <path to job_thesorus.json> <model file> <Optionnal output file for predicitons>
```