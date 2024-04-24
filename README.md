
# Oeil de Sauron - Surveillance de Répertoires Automatisée

## Table des Matières

- [Dépendances]
- [Utilisation]
- [Fonctionnalités]
- [Gestion des Répertoires]
- [Gestion des Journaux]
- [Dépendances]
- [Exemples]
- [Dépannage]

## Introduction

L'application "Oeil de Sauron" est un script Python conçu pour la surveillance automatisée des répertoires. Il utilise des événements du système de fichiers pour suivre les modifications, créations, suppressions et déplacements de fichiers et de répertoires.

## Dépendances
Ce script est réservé aux systèmes d'exploitation LINUX.
Pour installer les dépendances nécessaires au fonctionnement de l'Oeil de Sauron, exécutez la commande suivante dans votre environnement Python:

```bash
pip install watchdog colorama
```

## Utilisation

Pour démarrer le script, exécutez le fichier principal depuis votre terminal:
```python
python3 sauron.py
```
Assurez vous de récupérer le contenu de key.txt pour pouvoir entrer votre mot de passe et accéder au script. Ce fichier key.txt peut être hébergé sur un autre serveur pour éviter à n'importe quel utilisateur d'y avoir accès. Vous pourrez modifier les premières lignes du code concernant le mot de passe en conséquence.
## Fonctionnalités

- **Surveillance en Temps Réel** : Détecte les modifications, créations, suppressions, et déplacements de fichiers et de répertoires.
- **Journalisation des Activités** : Enregistre les actions effectuées par les utilisateurs sur les fichiers surveillés, incluant les modifications de permissions (chmod).
- **Affichage Coloré des Logs** : Utilise `colorama` pour améliorer la lisibilité des logs dans le terminal.
- **Commandes Interactives** : Permet d'ajouter et de retirer des répertoires de la surveillance, de lister les répertoires surveillés, et de basculer l'affichage des logs.

### Détail des Fonctions

 `add_directory(directory)`
Ajoute un répertoire à la liste des répertoires surveillés. Vérifie si le répertoire existe et n'est pas déjà surveillé, puis crée un observateur pour ce répertoire. Si le répertoire est déjà en cours de surveillance, une sortie terminal utilisateur vous l'indiquera. Pareil si vous entrez le chemin d'un répertoire inexistant. Cette fonction ajoute ce répertoire au fichier "directories.txt", et crée ce dernier s'il est inexistant dans le répertoire courant où vous excécutez le script.


 `remove_directory(directory)`
Retire un répertoire de la surveillance. Si le répertoire est spécifié avec "*", tous les répertoires sont retirés. Cette fonction vérifie si le répertoire à supprimer est dans la liste de surveillance, au quel cas le script nous renverra dans le terminal une erreur stipulant que le répertoire en question n'est pas présent dans la liste de surveillance.


 `list_directories()`
Affiche une liste de tous les répertoires actuellement surveillés et leurs changements de permissions respectifs. A chaque excécution de cette commande, la fonction vérifie que la liste qui va être affichée correspond bien aux répertoires surveillés, et si un fichier du ou des répertoires surveillés a été supprimé ou si un nouveau fichier a été créé dans l'un d'eux, alors il est ajouté ou supprimé dans l'affichage de la liste à jour.


 `toggle_log()`
Active ou désactive l'affichage des logs dans le terminal. Cette fonction est utile pour contrôler la visibilité des activités en temps réel. Cependant, les logs restent systématiquement stockés dans le fichier sauron.log qui est initialisé à chaque lancement du script s'il n'existe pas déjà. 

## Gestion des Répertoires

Les répertoires surveillés sont enregistrés dans un fichier `directories.txt` pour permettre la récupération de l'état de surveillance à chaque lancement du script. Si ce fichier n'existe pas lors du démarrage, il est automatiquement créé lors de l'ajout du premier répertoire à la liste. En cas de suppression du fichier pendant l'exécution, celui-ci sera recréé automatiquement lors de la prochaine commande `add`. Cependant, la liste sera donc vidée et mise à jour après la suppression de ce fichier.

## Gestion des Journaux

Les logs sont enregistrés automatiquement dans `sauron.log`. Si le fichier log est supprimé alors que l'application est en cours d'exécution, l'application affichera une erreur critique et demandera à l'utilisateur de redémarrer l'application, dès l'excécution de sa prochaine commande. Cette mesure préventive assure l'avertissement à l'utilisateur lors d'une suppression du fichier de logs.

## Dépendances

L'Oeil de Sauron utilise plusieurs modules externes pour fonctionner correctement :

- `watchdog` : bibliothèque Python qui permet de surveiller les modifications apportées aux fichiers et répertoires dans un système de fichiers. Il offre une API simple mais puissante pour détecter les événements tels que la création, la modification, le déplacement et la suppression de fichiers ou de répertoires.

 
- `colorama` : bibliothèque Python conçue pour simplifier la coloration du texte dans le terminal. Elle offre une interface simple et portable pour ajouter des couleurs au texte affiché dans le terminal, ce qui améliore la lisibilité et permet de mettre en évidence certaines parties importantes de la sortie.

## Exemples

Ajouter un répertoire à surveiller :
``` bash
> Entrez une commande : add <chemin_du_répertoire>
```
Le chemin demandé est le chemin accessible depuis la racine. Selon vos droits d'accès, certians fichiers ou dossiers ne seront pas surveillables. Le script vous affichera donc une erreur orange stipulant "permission denied"

Supprimer un répertoire de la surveillance :
``` bash
> Entrez une commande : remove <chemin_du_répertoire>
```
Il est possible d'utiliser l'argument * plutôt qu'un chemin pour vider entièrement la liste de surveillance. Ca aura par conséquent pour effet de vider le fichier directories.txt, qui stock les répertoires surveillés en temps réel.

Lister les répertoires actuellement surveillés :
``` bash
> Entrez une commande : list
```

activer ou désactiver l'affichage des logs directement dans le terminal (avec couleurs :
``` bash
> Entrez une commande : toggle_logs
```
## Dépannage

- **Journaux manquants** : Assurez-vous que `sauron.log` existe dans le répertoire de l'application. Si supprimé, l'application se fermera après un message d'erreur lors de votre prochaine exécution de commande.
- **Erreurs de permission** : Exécutez l'application avec les permissions appropriées pour accéder aux répertoires spécifiés.
- **Fichiers temporaires** : Si vous ajoutez des répertoires trop larges, qui peuvent contenir énormément de fichiers temporaires, votre fichier de log peut très vite être spammé de notifications.


## Contributeurs

- Luc MARTIN
- Yoan CAILLARD
- Nicolas BOIVIN
