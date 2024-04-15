import os  # Importation du module os pour interagir avec le système d'exploitation
import pwd  # Importation du module pwd pour obtenir des informations sur les utilisateurs
import sys  # Importation du module sys pour interagir avec le système
import time  # Importation du module time pour manipuler le temps
import logging  # Importation du module logging pour gérer les logs
from watchdog.observers import Observer  # Importation de la classe Observer pour surveiller les répertoires
from watchdog.events import FileSystemEventHandler  # Importation de la classe FileSystemEventHandler pour gérer les événements liés aux fichiers
from colorama import init, Fore, Style  # Importation de Colorama pour la coloration du texte

# Initialisation de Colorama
init()

# Activation/désactivation de l'affichage des logs dans le terminal
toggle_logs = False

# ASCII art représentant le logo de l'application
ascii_art = f"""
{Fore.RED}
....                                 :=*+:      :++=:                                .::::
....                              .=*#####*+==+*#####*=.                             .::::
...                             .=*####################*=.                           .::::
....                          :+*########################*+.                         .::::
....                        .+##########**#####*+*#########*=.                       .::::
....                      :+########*+--+#######*=-=*#########+:                     .::::
....                   :=*########+-. =*####+*####*- .-*########*=:                  .::::
...               .:=+*#######*+:.   +####*-  =#####=   .-+########*+-:.             .::::
....          :**##########*=:      +####*-    =#####-     .-+*#########***.         .::::
....         -*#########*=:        .#####+      *####*         :+*#########*-        .::::
....      :=*##########+.          -#####=      +####*.          :**#########*=:     .::::
....       .=*##########*+-        .#####+      *####*        .-+*##########*-.      .::::
....          +#############+-.     =####*-    +#####-     .=*#############=         .::::
....           --==*###########+-.   +#####=  +#####=   :=*##########**==-:          .::::
....                 :=+##########*=: =*####**####*: :=*#########*+-:                .::::
....                    .-*##########*=-+#######*=-=*#########*+-.                   .::::
....                       :+###########**######**###########+:                      .::::
....                         :+###########################*+.                        .::::
....                           .+#######################*=.                          .::::
....                             .=*##################*=.                            .::::
....                               .-*##*+-:..:-+###*-                               .::::
....                                  .:.        .:.                                 .::::
{Fore.RESET}{Fore.GREEN}

         ___       _ _      ___       ____    _   _   _ _ __   ___  _   _
        / _ \  ___(_) |   __| | ___  / ___|  / \ | | | | |_ \ / _ \| \ | |
 	   | | | |/ _ \ | |  / _` |/ _ \ \___ \ / _ \| | | | |_) | | | |  \| |
 	   | |_| |  __/ | | | (_| |  __/  ___) / ___ \ |_| |  _ <| |_| | |\  |
 	    \___/ \___|_|_|  \____|\___| |____/_/   \_\___/|_| \_\\___/|_| \_|

 {Fore.RESET}
"""

# Affichage de l'ASCII art
print(ascii_art)

# Affichage de l'en-tête de l'application
print(f"{Fore.CYAN}Oeil de Sauron - Surveillance de répertoires automatisée{Fore.RESET}\n")

# Version de l'application
print(f"{Fore.RED}VERSION - {Fore.RESET}V1.0")

# Auteurs de l'application
print(f"{Fore.RED}MADE BY - {Fore.RESET} lucmartin, yoanncaillard, nicolasboivin\n\n")

# Classe pour gérer les événements de surveillance personnalisés
class CustomLoggingEventHandler(FileSystemEventHandler):

    def __init__(self):
        # Initialisation du dictionnaire pour stocker les répertoires surveillés
        self.directories = {}
        super().__init__()

    # Méthode appelée pour tous les événements
    def on_any_event(self, event):
        # Obtention du nom d'utilisateur associé à l'événement
        username = self.get_username(event)
        global toggle_logs
        
        # Ignorer les événements "opened" et "closed"
        if event.event_type in ['opened', 'closed']:
            return
        
        # Gestion des événements selon leur type
        if event.event_type == 'modified':
            if not event.is_directory:
                file_path = event.src_path
                directory = os.path.dirname(file_path)
                if directory not in self.directories:
                    self.directories[directory] = {}               
                old_chmod = self.directories[directory].get(file_path, None)
                if os.path.exists(file_path):
                    chmod = os.stat(file_path).st_mode
                else:
                    # Le fichier ou le répertoire n'existe pas, donc nous n'avons pas de chmod à récupérer
                    return
                self.directories[directory][file_path] = chmod
                if old_chmod is None:
                    # Première modification de ce fichier, enregistrer le chmod initial
                    message = f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}. {Fore.CYAN}Chmod{Fore.RESET} défini sur {Fore.CYAN}{chmod:o}{Fore.RESET}'
                    if toggle_logs:
                        print(message)
                    logging.info(f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}. Chmod défini sur {chmod:o}')   
                elif chmod != old_chmod:
                    # Le fichier a déjà été modifié, afficher le changement de chmod
                    message = f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}. {Fore.CYAN}Chmod{Fore.RESET} changé de {Fore.RED}{old_chmod:o}{Fore.RESET} à {Fore.CYAN}{chmod:o}{Fore.RESET}'
                    if toggle_logs:
                        print(message)
                    logging.info(f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}. Chmod changé de {old_chmod:o} à {chmod:o}')
                    
        # Gestion de l'événement "moved"       
        elif event.event_type == 'moved':             
            if event.is_directory:                 
                action = 'dossier'                     
            else:                  
                action = 'fichier'             
            src_dir = '/'.join(event.src_path.split('/')[:-1])
            dest_dir = '/'.join(event.dest_path.split('/')[:-1])        
            if src_dir != dest_dir:
                # Le chemin source est différent du chemin de destination
                message = f'Utilisateur {username} a effectué l\'événement : {action} déplacé - {Fore.LIGHTGREEN_EX}{event.src_path}{Fore.RESET} vers {Fore.LIGHTGREEN_EX}{event.dest_path}{Fore.RESET}'               
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : {action} déplacé - {event.src_path} vers {event.dest_path}')
            else:
                # Les chemins source et destination sont identiques, donc il s'agit d'un renommage
                message = f'Utilisateur {username} a effectué l\'événement : {action} renommé - {Fore.LIGHTGREEN_EX}{event.src_path}{Fore.RESET} vers {Fore.LIGHTGREEN_EX}{event.dest_path}{Fore.RESET}'
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : {action} renommé - {event.src_path} vers {event.dest_path}')
                    
        # Gestion de l'événement "deleted"
        elif event.event_type == 'deleted':
            if event.is_directory:
                message = f'Utilisateur {username} a effectué l\'événement : dossier supprimé - {Fore.RED}{event.src_path}{Fore.RESET}'
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : dossier supprimé - {event.src_path}')
            else:
                message = f'Utilisateur {username} a effectué l\'événement : fichier supprimé - {Fore.RED}{event.src_path}{Fore.RESET}'
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : fichier supprimé - {event.src_path}')
                    
        # Gestion de l'événement "created"
        elif event.event_type == 'created':
            message = f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {Fore.LIGHTGREEN_EX} {event.src_path}{Fore.RESET}'
            if toggle_logs:
                print(message)
            logging.info(f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}')
            
        # Gestion de l'événement "property_modified"
        elif event.event_type == 'property_modified':
            if event.is_directory:
                message = f'Utilisateur {username} a effectué l\'événement : modification des propriétés du dossier - {Fore.CYAN}{event.src_path}{Fore.RESET}'
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : modification des propriétés du dossier - {event.src_path}')
            else:
                message = f'Utilisateur {username} a effectué l\'événement : modification des propriétés du fichier - {Fore.CYAN}{event.src_path}{Fore.RESET}'
                if toggle_logs:
                    print(message)
                logging.info(f'Utilisateur {username} a effectué l\'événement : modification des propriétés du fichier - {event.src_path}')
        else:
            # Gestion des autres types d'événements
            message = f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}'
            if toggle_logs:
                print(message)
            logging.info(f'Utilisateur {username} a effectué l\'événement : {event.event_type} - {event.src_path}')

    # Méthode pour obtenir le nom d'utilisateur associé à un événement
    def get_username(self, event):
        if os.path.exists(event.src_path):
            uid = os.stat(event.src_path).st_uid
            try:
                username = pwd.getpwuid(uid).pw_name
            except KeyError:
                username = "Système"
            return username
        else:
            return "Système"

# Fonction pour supprimer un répertoire de la surveillance
def remove_directory(directory):
    global observers
    global event_handler
    global toggle_logs
    
    # Supprimer tous les répertoires surveillés si "*" est spécifié
    if directory == "*":
        for observer in observers.values():
            observer.stop()
            observer.join()
        observers.clear()
        event_handler.directories.clear()
        print(f"{Fore.GREEN}Tous les répertoires ont été retirés de l'Oeil de Sauron.{Fore.RESET}")
        logging.info(f"Tous les répertoires ont été retirés de l'Oeil de Sauron")
        save_directories_to_file()
        return

    if directory in event_handler.directories:
        # Arrêter l'observateur associé au répertoire
        observers[directory].stop()
        observers[directory].join()
        del observers[directory]
        del event_handler.directories[directory]
        print(f"{Fore.GREEN}Répertoire {Fore.RESET} {directory!r} {Fore.GREEN} retiré de{Fore.RESET}{Fore.RED} l'Oeil de Sauron{Fore.RESET}")
        logging.info(f"Répertoire {directory!r} retiré de l'Oeil de Sauron")
        save_directories_to_file()
    else:
        print(f"{Fore.RED}Le répertoire{Fore.RESET} {directory!r}{Fore.RED} n'est pas listé dans l'Oeil de Sauron{Fore.RESET}")
        logging.info(f"Tentative de suppression de surveillance ratée : Le répertoire {directory!r} n'est pas listé dans l'Oeil de Sauron ")


# Fonction pour ajouter un répertoire à la surveillance
def add_directory(directory):
    global observers
    global event_handler
    
    # Vérifier si le répertoire existe
    if not os.path.exists(directory):
        print(f"{Fore.RED}Le répertoire spécifié n'existe pas.{Fore.RESET}")
        logging.info(f"Tentative d'ajout de surveillance échoué : Le répertoire {directory!r} n'existe pas.")
        return
    
    # Vérifier si le répertoire est déjà surveillé
    if directory in event_handler.directories:
        print(f"{Fore.RED}Le répertoire '{directory}' est déjà en cours de surveillance.{Fore.RESET}")
        logging.info(f"Tentative d'ajout de surveillance échoué : Le répertoire {directory!r} est déjà en cours de surveillance.")
        return
    
    # Créer un nouvel observateur pour ce répertoire
    observer = Observer()
    observer.schedule(event_handler, directory)
    observer.start()
    observers[directory] = observer
    
    # Stocker les chmods initiaux des fichiers et répertoires dans le répertoire
    event_handler.directories[directory] = {}
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            dir_path = os.path.join(root, d)
            try:
                event_handler.directories[directory][dir_path] = os.stat(dir_path).st_mode
            except PermissionError:
                print(f"{Fore.YELLOW}Permission denied: {dir_path}{Fore.RESET}")
            except FileNotFoundError:
                print(f"{Fore.YELLOW}File not found: {dir_path}{Fore.RESET}")
        for f in files:
            file_path = os.path.join(root, f)
            try:
                event_handler.directories[directory][file_path] = os.stat(file_path).st_mode
            except PermissionError:
                print(f"{Fore.YELLOW}Permission denied: {file_path}{Fore.RESET}")
            except FileNotFoundError:
                print(f"{Fore.YELLOW}File not found: {file_path}{Fore.RESET}")
    
    logging.info(f"Répertoire {directory!r} ajouté à l'Oeil de sauron")
    print(f"Répertoire {Fore.CYAN}{directory!r}{Fore.RESET} ajouté à l'Oeil de sauron")
    save_directories_to_file()


# Fonction pour lister les répertoires en cours de surveillance
def list_directories():
    global event_handler
    print(f"\n{Fore.BLUE}Liste des répertoires en cours de surveillance :{Fore.RESET}")
    
    # Parcours de tous les répertoires surveillés
    for directory, files_and_dirs in event_handler.directories.items():
        print(f"{Style.BRIGHT}{directory}{Style.RESET_ALL}:")
        items_to_remove = []  # Liste pour stocker les éléments à retirer
        
        # Parcours de tous les fichiers et répertoires dans le répertoire surveillé
        for item, chmod in files_and_dirs.items():
            # Vérifier si le fichier ou le répertoire existe toujours
            if not os.path.exists(item):
                items_to_remove.append(item)  # Ajouter l'élément à retirer s'il n'existe plus
            else:
                # Afficher le fichier ou le répertoire avec son chmod
                print(f"   - {item} - Chmod: {Fore.CYAN}{chmod:o}{Fore.RESET}")
        
        # Retirer les éléments de la liste qui n'existent plus
        for item in items_to_remove:
            del files_and_dirs[item]
        
        # Vérifier et ajouter de nouveaux éléments créés depuis la dernière vérification
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                dir_path = os.path.join(root, d)
                # Vérifier si le répertoire n'est pas déjà dans la liste surveillée
                if dir_path not in files_and_dirs:
                    try:
                        # Ajouter le répertoire à la liste avec son chmod et l'afficher
                        files_and_dirs[dir_path] = os.stat(dir_path).st_mode
                        print(f"   - {dir_path} - Chmod: {Fore.CYAN}{files_and_dirs[dir_path]:o}{Fore.RESET}")
                    except PermissionError:
                        print(f"{Fore.YELLOW}Permission denied: {dir_path}{Fore.RESET}")
                    except FileNotFoundError:
                        print(f"{Fore.YELLOW}File not found: {dir_path}{Fore.RESET}")
            for f in files:
                file_path = os.path.join(root, f)
                # Vérifier si le fichier n'est pas déjà dans la liste surveillée
                if file_path not in files_and_dirs:
                    try:
                        # Ajouter le fichier à la liste avec son chmod et l'afficher
                        files_and_dirs[file_path] = os.stat(file_path).st_mode
                        print(f"   - {file_path} - Chmod: {Fore.CYAN}{files_and_dirs[file_path]:o}{Fore.RESET}")
                    except PermissionError:
                        print(f"{Fore.YELLOW}Permission denied: {file_path}{Fore.RESET}")
                    except FileNotFoundError:
                        print(f"{Fore.YELLOW}File not found: {file_path}{Fore.RESET}")
    print("\n\n")



# Fonction pour activer ou désactiver l'affichage des logs dans le terminal
def toggle_log():
    global toggle_logs
    if toggle_logs:
        toggle_logs = False
        print(f"{Fore.RED}Affichage des logs dans le terminal désactivé{Fore.RESET}")
    else:
        toggle_logs = True
        print(f"{Fore.GREEN}Affichage des logs dans le terminal activé{Fore.RESET}")  

# Fonction pour afficher l'aide
def print_help():
    print(f"\n{Fore.YELLOW}Liste des commandes disponibles :{Fore.RESET}\n")
    print(f"{Fore.CYAN}add {Fore.RESET}<répertoire> : Ajoute un répertoire à surveiller.")
    print(f"{Fore.CYAN}remove {Fore.RESET}<répertoire> (ou * pour supprimer toute la liste): Supprime un répertoire de la surveillance.")
    print(f"{Fore.CYAN}list {Fore.RESET}: Affiche la liste des répertoires en cours de surveillance.")
    print(f"{Fore.CYAN}toggle_logs {Fore.RESET}: Affiche ou cache les logs directement depuis le terminal")
    print(f"{Fore.CYAN}help {Fore.RESET}: Affiche cette aide.\n\n")

# Fonction pour sauvegarder les répertoires surveillés dans un fichier
def save_directories_to_file():
    with open("directories.txt", "w") as file:
        for directory in event_handler.directories:
            file.write(directory + '\n')

# Fonction pour charger les répertoires surveillés depuis un fichier au démarrage
def load_directories_from_file():
    try:
        with open("directories.txt", "r") as file:
            directories = file.readlines()
            for directory in directories:
                add_directory(directory.strip())
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Aucun fichier de surveillance trouvé. Un nouveau fichier sera créé lors de l'ajout du premier répertoire.{Fore.RESET}")

# Configuration des logs
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='\n%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler("sauron.log", mode='a')])

    observers = {}
    event_handler = CustomLoggingEventHandler()

    # Charger les répertoires à surveiller depuis le fichier au démarrage
    load_directories_from_file()
    
    try:
        while True:
            time.sleep(1)
            command = input(f"{Fore.GREEN}> Entrez une commande {Fore.RESET} (add <répertoire>, remove <répertoire>, list, help...){Fore.GREEN}:{Fore.RESET} ")
            # Vérification de l'existence du fichier de logs
            if not os.path.exists("sauron.log"):
                print(f"{Fore.RED}ERREUR CRITIQUE:{Fore.RESET} Le fichier {Fore.CYAN}sauron.log{Fore.RESET} a été supprimé. Expulsion du programme imminente.")
                exit()
                        
            if command.strip().lower().startswith("add "):
                directory = command.split(maxsplit=1)[1].strip()             
                add_directory(directory)
            elif command.strip().lower().startswith("remove "):
                directory = command.split(maxsplit=1)[1].strip()
                remove_directory(directory)
            elif command.strip().lower() == "list":
                list_directories()
            elif command.strip().lower() == "help":
                print_help()
            elif command.strip().lower() == "toggle_logs":
                toggle_log()
            else:
                print(f"{Fore.RED}Commande inconnue. Utilisez la commande 'help' pour obtenir la liste des commandes disponibles. {Fore.RESET}")

    # Arrêt des observateurs en cas d'interruption par l'utilisateur
    except KeyboardInterrupt:
        for observer in observers.values():
            observer.stop()
            observer.join()
