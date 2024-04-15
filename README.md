Sarko
sarko1313
En ligne

Sarko — 11/04/2024 23:18
Le truc fonctionne bien
mais faut faire en sorte que les logs soient stockés dans un fichier de log sauvegardé
Et que au lieu d'avoir les chmod (10644 etc) dans les notifs, on ai plutôt des phrases compréhensibles de ce qui s'est passé
(quel changement de permissions pour quel groupe, pour l'owner ou pour others, etc)
Ntumba a forcé a vouloir ca
LeakData 自殺 — 11/04/2024 23:23
Ok je ferais, j'ai pas mal de taffe demain donc sûrement samedi
LeakData 自殺 — 13/04/2024 18:19
import os

import pwd

import sys

Afficher plus
message.txt
12 Ko
J'ai modifié dis moi si ca te vas
Sarko — 13/04/2024 18:59
J’suis en tchop
Ca stock les logs dans un fichier et c’est plus des 10664 ou des merdes comme ça c devenu genre lisible en mode tél personne a changé telle perm pour tel groupe ?
Si c ça c parfait smr
LeakData 自殺 — 13/04/2024 19:05
Oklm voit ça taleur
Sarko — Hier à 15:52
Jv voir ça là là
Sarko — Hier à 19:08
Ton script affiche mort les erreurs de mon côté
T'as testé de ton côté ?
LeakData 自殺 — Hier à 19:08
oui$
yavais des erreursm
pas reussi a corriger meme avec hpt
je sais pas comment ajouter l'event listener sans erreurs
Sarko — Hier à 19:09
ca affiche plus quand je supp un dossier ou des fichiers aussi
Et les events ne s'affichent plus du tout
ah peut etre dans le fichier log
ah nan vide dcp aussi
Sarko — Hier à 19:52
ca me clc
LeakData 自殺 — Hier à 20:15
Le event listener ça fou la merde
Sarko — Hier à 21:52
J'ai réussi à faire les logs sans erreur c'est bon
Sarko — Aujourd’hui à 10:31
Mais au final on a rien à lui rendre
LeakData 自殺 — Aujourd’hui à 11:51
Mais les logs moi ils se mettaient
Sarko — Aujourd’hui à 11:52
Jsp jsuis en train de bosser sur le script encore là
Je fais en sorte qu’on ai une commande qui affiche les logs dans le terminal en plus de les stocker dans un fichier de logs
J’ai réglé les erreurs mtn ca stock dans un fichier log ça affiche plus dans le tchat
J’utilise plus chat gpt y’a un moment où ça devient trop compliqué je code à la main
C plus long mais je suis sûr de sque je fais
Sarko — Aujourd’hui à 12:39
Est ce que vous pouvez gérer le projet de ramsamy là avec les vm et tout ?
J'ai pas le temps trop de bosser dessus là puisqu'il faut que je finisse le script sauron + faire la doc et la présentation pptx
LeakData 自殺 — Aujourd’hui à 14:43
et
Sarko — Aujourd’hui à 16:34
je commente le code et j'te l'envoie
LeakData 自殺 — Aujourd’hui à 16:34
op
Sarko — Aujourd’hui à 16:34
Faudra pas oublier de parler des frameworks utilisés notamment watchdog qui est le principal pour la remontée des logs
tfcn je t'apprends rien tu sais faire
LeakData 自殺 — Aujourd’hui à 16:50
je vais faire ca en pro tu vas kiffer
jsais que j'ai deja rien fais sur le projet j'ai add 10 lignes ca marchait pas
Sarko — Aujourd’hui à 16:54
oklm reuf l'important c'est qu'on en voit le bout
j'tenvoie ça dans 2min jrègle un bug
Sarko — Aujourd’hui à 17:03
quand je faisais list ca m'affichait pas les fichiers créés dans le répertoire depuis la dernière commande list ou ca supprimait pas ceux que j'avais supprimé du système
Sarko — Aujourd’hui à 17:14
import os  # Importation du module os pour interagir avec le système d'exploitation
import pwd  # Importation du module pwd pour obtenir des informations sur les utilisateurs
import sys  # Importation du module sys pour interagir avec le système
import time  # Importation du module time pour manipuler le temps
import logging  # Importation du module logging pour gérer les logs
from watchdog.observers import Observer  # Importation de la classe Observer pour surveiller les répertoires
Afficher plus
message.txt
22 Ko
On est synchro
Code final pour la prez
LeakData 自殺 — Aujourd’hui à 17:15
op
Sarko — Aujourd’hui à 17:16
J'ai géré toutes les erreurs normalement on aura jamais de crash ou une connerie
LeakData 自殺 — Aujourd’hui à 17:51
Type de fichier joint : acrobat
Oeil_de_Sauron_-_README.pdf
74.42 KB
voila
Sarko — Aujourd’hui à 17:51
letmecheck
LeakData 自殺 — Aujourd’hui à 17:51
dis moi si ca te vas ou si y'a pas assez
Sarko — Aujourd’hui à 17:51
az
LeakData 自殺 — Aujourd’hui à 17:51
mais apres je peux pas trop faire une doc technique c du code quoi
j'ai mis toutes les commandes normalement
j'ai ptetre forcé en mettant dans fonctionnalités ET dans exemples mais ca fais un peu plus fournis
Sarko — Aujourd’hui à 17:52
Ouais nan pas assez le reuf faut expliquer les fonctions ce qu'elles font etc
et pour les journaux manquants c'est géré automatiquement dans le script par exemple on peut expliquer comment et pourquoi
genre tu vois on peut expliquer chaque fonction du script avec un screen de la fonction, les dépendances entre fonctions etc
C'est nrv la partie installation etc c parfait pour le début
LeakData 自殺 — Aujourd’hui à 17:53
pas de screen gros c un readme
Sarko — Aujourd’hui à 17:54
C'est + un document d'exploitation q'uil faut
je pensais pas tu pouvais pas mettre de screen
sinon comme on fait avant avec les balises ''' et on copie colle la fonction
fin sur discord c 
 comme ca genre 
`
LeakData 自殺 — Aujourd’hui à 17:55
je vais mettre le detail des fonctions
gestion de journaux
Sarko — Aujourd’hui à 17:55
directories etc
psq les répertoires sont stockés dans un fichier aussi, et récupérés à chaque lancement de script
et si il existe pas il est créé
et si il est supprimé en cours de route il se recrée automatiquement prochaine fois qu'on add un répertoire à la liste
par exempke
genre c baleze un document d'exploitation
LeakData 自殺 — Aujourd’hui à 18:14
Je vois pas quoi ajouter de plus
Type de fichier joint : acrobat
Oeil_de_Sauron_-_README.pdf
82.38 KB
au pire faudrait que je commente le code en mettant du détail +++++
mais la c'est deja pas mal complet
Sarko — Aujourd’hui à 18:17
Bah expliquer les spécificités de chaque fonction en montrant le code
LeakData 自殺 — Aujourd’hui à 18:17
mais comment ca montrer le code
ya TOUT dans le readme
tu lis avec ton anus
Sarko — Aujourd’hui à 18:18
Par exemple dans list
LeakData 自殺 — Aujourd’hui à 18:18
Image
Image
Image
Sarko — Aujourd’hui à 18:19
Avant d’afficher la liste, le script vérifie si la liste qui va être affichée contient pas un fichier qui existe plus ou si un nouveau fichier a été créé dans le répertoire y est pas, alors il l’ajoute à l’affichage
Par exemple
Ou encore
Si sauron.log est supprimé, telle partie du script fait qu’à la prochaine commande entrée on affichera un message d’erreur avec une coupure du script en cours
Ou par exemple qu’est ce qui faut que quand tu remove un directory ça le supprime de la liste dans l’affichage et ça le supprime aussi dans le fichier directoires ou les répertoires sont stockés, ce genre de trucs
Ou comment est ce que les fichiers sauron.log & directoires sont gérés
C’est de ça que j’te parle depuis le début en + de ce que t’as déjà fais qui est très bien
C’est ça la doc d’exploitation
LeakData 自殺 — Aujourd’hui à 18:30
mais ajouter ca ca ferais trop brouillon sur le doc
c'est pas du tout le but des docs comme ca
ca sinon on le met en + dans le code
Sarko — Aujourd’hui à 18:33
bon vsi nsm j'vais l'ajouter dans le powerpoint avec Yoan t'occupe
Sarko — Aujourd’hui à 18:41
tpx me l'envoyer en .md ?
LeakData 自殺 — Aujourd’hui à 18:41
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
