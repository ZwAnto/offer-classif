# offer-classification

# Idées

* Créer un embedding des offres basé sur la description + titre puis appliquer un modèle de classification (tranformers, fastetxt/Glove ?)
    * limites : Peu efficace si énormement de classes à prédire -> predire d'abord le secteur puis le label ?
    * Entrainer le modèle d'embedding sur un corpus specialisé

* Créer un embedding (fasttext/Glove, bert) des offres (titre+description) + TSNE + gaussian mixture par label

* Limitation générale: peu de texte pour décrire les postes dans le thesaurus, analyser la correlation entre les différents poste ?

