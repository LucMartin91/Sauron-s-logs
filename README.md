
# Oeil de Sauron - Surveillance de Répertoires Automatisée

## Table des Matières

- [Installation]
- [Utilisation]
Afficher plus
Oeil_de_Sauron_-_README.md
4 Ko
﻿
LeakData 自殺
leakdata
# Oeil de Sauron - Surveillance de Répertoires Automatisée

## Table des Matières

- [Installation]
- [Utilisation]
- [Fonctionnalités]
- [Gestion des Répertoires]
- [Gestion des Journaux]
- [Dépendances]
- [Exemples]
- [Dépannage]

## Introduction

L'application "Oeil de Sauron" est un script Python conçu pour la surveillance automatisée des répertoires. Il utilise des événements du système de fichiers pour suivre les modifications, créations, suppressions et déplacements de fichiers et de répertoires.

## Installation

Pour installer les dépendances nécessaires au fonctionnement de l'Oeil de Sauron, exécutez la commande suivante dans votre environnement Python:

```bash
pip install watchdog colorama
```

## Utilisation

Pour démarrer le script, exécutez le fichier principal depuis votre terminal:
```python
python3 oeildesauron.py
```

## Fonctionnalités

- **Surveillance en Temps Réel** : Détecte les modifications, créations, suppressions, et déplacements de fichiers et de répertoires.
- **Journalisation des Activités** : Enregistre les actions effectuées par les utilisateurs sur les fichiers surveillés, incluant les modifications de permissions (chmod).
- **Affichage Coloré des Logs** : Utilise `colorama` pour améliorer la lisibilité des logs dans le terminal.
- **Commandes Interactives** : Permet d'ajouter et de retirer des répertoires de la surveillance, de lister les répertoires surveillés, et de basculer l'affichage des logs.

### Détail des Fonctions

 `add_directory(directory)`
Ajoute un répertoire à la liste des répertoires surveillés. Vérifie si le répertoire existe et n'est pas déjà surveillé, puis crée un observateur pour ce répertoire.


 `remove_directory(directory)`
Retire un répertoire de la surveillance. Si le répertoire est spécifié avec "*", tous les répertoires sont retirés.


 `list_directories()`
Affiche une liste de tous les répertoires actuellement surveillés et leurs changements de permissions respectifs.


 `toggle_log()`
Active ou désactive l'affichage des logs dans le terminal. Cette fonction est utile pour contrôler la visibilité des activités en temps réel.

## Gestion des Répertoires

Les répertoires surveillés sont enregistrés dans un fichier `directories.txt` pour permettre la récupération de l'état de surveillance à chaque lancement du script. Si ce fichier n'existe pas lors du démarrage, il est automatiquement créé lors de l'ajout du premier répertoire à la liste. En cas de suppression du fichier pendant l'exécution, celui-ci sera recréé automatiquement lors de la prochaine commande `add`

## Gestion des Journaux

Les logs sont enregistrés automatiquement dans `sauron.log`. Si le fichier log est supprimé alors que l'application est en cours d'exécution, l'application affichera une erreur critique et demandera à l'utilisateur de redémarrer l'application. Cette mesure préventive assure qu'aucune donnée n'est perdue en cas de suppression accidentelle du fichier de logs.

## Dépendances

L'Oeil de Sauron utilise plusieurs modules externes pour fonctionner correctement :

- `watchdog` : Surveillance des répertoires.
- `colorama` : Pour la coloration des textes dans le terminal.

## Exemples

Ajouter un répertoire à surveiller :
``` bash
> Entrez une commande : add <chemin_du_répertoire>
```

Supprimer un répertoire de la surveillance :
``` bash
> Entrez une commande : remove <chemin_du_répertoire>
```

Lister les répertoires actuellement surveillés :
``` bash
> Entrez une commande : list
```

## Dépannage

- **Journaux manquants** : Assurez-vous que `sauron.log` existe dans le répertoire de l'application. Si supprimé, redémarrez l'application.
- **Erreurs de permission** : Exécutez l'application avec les permissions appropriées pour accéder aux répertoires spécifiés.

## Contributeurs

- Luc MARTIN
- Yoan CAILLARD
- Nicolas BOIVIN
