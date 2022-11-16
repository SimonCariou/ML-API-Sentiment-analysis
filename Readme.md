# Projet 2 - Review Analysis

## Choix d'architecture

Les différents modèles de Machine learning entraînés dans nôtre Notebook du projet 1 ont été sauvegardés en utilisant la librairie joblib et ont été placés dans un dossier à la racine du dossier de l'API. Nous avons fait de même avec les fichiers de performances car ils nécessitent d'avoir le jeu de test sous la main. Nous avons choisi arbitrairement 4 différentes métriques que nous mettons à disposition des utilisateurs qui utilisent les endpoints performances (Plus de détail dans la partie 2 "Implémentation de l'API").

Les fichiers de performances sauvegardés par joblib sont des fichiers JSON qui ont la forme suivante:
```
{
    "recall_score": AA,
    "accuracy_score": BB,
    "f1_score": CC,
    "precision_score": DD
}
```

Ce qui permet à l'API de les retourner directement dans ce format.

## Implémentation de l'API

L'API permet de retourner le sentiment associé à une phrase ainsi que d'accéder aux performances de 4 différents modèles de machine learning, choisis et entraînés sur le jeu de données de test.

Les abréviations/acronymes suivants seront utilisés dans la définition des endpoints:
- Logistic Regression (`log_reg`)
- Decision Tree Classifier (`decision_tree`)
- Multinomial Naive Bayes (`MNB`)
- Stochastic Gradien Classifier (`SGD`) 

### Sentiment d'une phrase, calculé par les différents modèles

GET: + paramètre: `{"sentence": "xxxx"}` qui retourne le sentiment de la phrase donnée en paramètre. Le sentiment peut être:
* 0: Phrase à connotation négative
* 1: Phrase à connotation positive. 

Notre API propose 4 endpoints différents correspondant à l'évaluation du sentiment d'une phrase selon les 4 modèles de machine learning choisis.

Les différents endpoints permettent à l'utilisateur (authentifié) d'accéder aux ressources suivantes:
```
/sentiment/log_reg
/sentiment/decision_tree
/sentiment/multinomial_nb
/sentiment/sgd_classifier
```

Chacun de ces endpoints retourne un JSON de la forme:

```
{
     "sentence": sentence_given_as_a_parameter,
     "sentiment": 0 || 1 (with 0: negative sentence and 1: positive sentence)
}
```

### Performances des différents modèles

Notre API propose 4 endpoints différents permettant d'accéder aux métriques des 4 modèles utilisés pour l'entraînement sur le jeu de données de test.

GET: Retourne: `accuracy_score`, `f1_score`, `recall_score` & `precision_score` pour le modèle/endpoint sélectionné.
```
/performances/log_reg
/performances/decision_tree
/performances/multinomial_nb
/performances/sgd_classifier
```

Chacun de ces endpoints retourne un JSON de la forme:
```
{
    "recall_score": AA,
    "accuracy_score": BB,
    "f1_score": CC,
    "precision_score": DD
}
```

## Implémentation des tests

### Test de l’authentification des utilisateurs

L’authentification de chaque utilisateur est testée, un test supplémentaire sur un utilisateur inconnu est également réalisé pour vérifier l’erreur retournée.
Test des différents endpoints:

#### Test des endpoints sentiment

```
/sentiment/log_reg
/sentiment/decision_tree
/sentiment/multinomial_nb
/sentiment/sgd_classifier
```

Chaque endpoint “sentiment” est testé avec une phrase positive et une phrase négative puis avec des users authentifiés et non authentifiés et enfin si la réponse reçue correspond à la réponse attendue à savoir "sentiment": 0 ou "sentiment": 1.

#### Test des endpoints performances

```
/performances/log_reg
/performances/decision_tree
/performances/multinomial_nb
/performances/sgd_classifier
```
Chaque endpoint “performances” est testé. Une vérification est réalisée sur le JSON reçu, une vérification de l'authentication du user.

## Containerization de l'API et des Tests

Les images de l’API et des tests sont insérées dans des containers lancés à l’aide de Docker Compose (`docker-compose.yml`):
- Lancement de 3 containers:
    - **API**:
        - *image API*: ml-api-sentiment-analysis
        - *container API*: my_api_sentiment_analysis
    - **Test API - Sentiment prediction**:
        - *image test*: tests-api-sentiment
        - *container test*: tests-api-sentiment
     - **Test API - Performances**:
        - *image test*: tests-api-performances
        - *container test*: tests-api-performances

les containers de test ne sont lancés qu’une fois que celui de l’API est opérationnel.

## Déploiement avec Kubernetes

Nous avons fait le choix d'héberger notre image d'API dans un répertoire privé dans le dockerhub afin d'en cacher sa visibilité au grand public. Cette décision nous a amené à créer un secret permettant aux fichiers de configuration Kubernetes de s'authentifier pour la télécharger.
Ce secret (`imagePullSecrets`) est en fait un json contenant les informations de login rentrées en se loggant sur le docker hub avec le terminal (`docker login`) que nous avons encodé en base64.

Avant toute chose, pour lancer le processus de déploiement de l'API sur les 3 pods comme demandé, il va falloir créer le déploiement, le secret, le service et l'ingress, à l'aide de ces commandes:

```
kubectl create -f sentiment-analysis-api-deployment.yml
kubectl create -f registry-pull-secret.yml
kubectl create -f sentiment-analysis-api-ingress.yml
kubectl create -f sentiment-analysis-api-service.yml 
```
