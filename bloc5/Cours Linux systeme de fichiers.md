<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Le système de fichiers Linux](#le-systme-de-fichiers-linux)
	- [Arborescence de fichier](#arborescence-de-fichier)
	- [Le dossier personnel **home**](#le-dossier-personnel-home)
	- [Chemin absolu et relatif](#chemin-absolu-et-relatif)
- [Lignes de commande dans un terminal ![terminal](img/terminal.png)](#lignes-de-commande-dans-un-terminal-terminalimgterminalpng)

<!-- /TOC -->

# Le système de fichiers Linux
## Arborescence de fichier

* Sous Linux, pas d’unités logiques (C : D : . . . ) comme sous Windows.
* Une seule et unique arborescence.
* La racine de l’arborescence (point de départ d’une arborescence) est désignée par le symbole `/`.
* Linux distingue la casse (majuscule/minuscule)

![Arborescence de fichiers sous Linux](img/arborescence_fichiers_linux.png)

Pour informations :

* bin : contient des programmes (exécutables) susceptibles d'être utilisés par tous les utilisateurs de la machine.
* boot : fichiers permettant le démarrage de Linux.
* dev : fichiers contenant les périphériques. En fait – on en reparlera plus tard – ce dossier contient des sous-dossiers qui « représentent » chacun un périphérique. On y retrouve ainsi par exemple le fichier qui représente le lecteur CD.
* etc : fichiers de configuration.
* **home** : contient les répertoires personnels des utilisateurs.
* lib : dossier contenant les bibliothèques partagées (généralement des fichiers.so) utilisées par les programmes. C'est en fait là qu'on trouve l'équivalent des.dllde Windows.
* media : lorsqu'un périphérique amovible (comme une carte mémoire SD ou une clé USB) est inséré dans votre ordinateur, Linux vous permet d'y accéder à partir d'un sous-dossier demedia. On parle de montage.
* mnt : c'est un peu pareil quemedia, mais pour un usage plus temporaire.
* opt : répertoire utilisé pour les add-ons de programmes.
* proc : contient des informations système.
* root : c'est le dossier personnel de l'utilisateur « root ». Normalement, les dossiers personnels sont placés danshome, mais celui de « root » fait exception. En effet, comme je vous l'ai dit dans le chapitre précédent, « root » est le superutilisateur, le « chef » de la machine en quelque sorte. Il a droit à un espace spécial.
* sbin : contient des programmes système importants.
* tmp : dossier temporaire utilisé par les programmes pour stocker des fichiers.
* usr : c'est un des plus gros dossiers, dans lequel vont s'installer la plupart des programmes demandés par l'utilisateur.
* var : ce dossier contient des données « variables », souvent des logs (traces écrites de ce qui s'est passé récemment sur l'ordinateur)

## Le dossier personnel **home**

Linux est un système d'exploitation [multi-utilisateurs](https://fr.wikipedia.org/wiki/Multi-utilisateur). La philosophie de Linux est de bien respecter la confidentialité des données de chaque utilisateur (via un système de gestion des droits : voit TP ultérieur).

* Ainsi, **chaque utilisateur** de l'ordinateur possède son **dossier personnel**. Dans la salle, il n'y a qu'un utilisateur : **nsi**. Votre dossier "personnel" est donc `home/nsi/`. C'est celui dans lequel vous êtes positionné juste après vous être connecté. Si un autre utilisateur, par exemple, `Martin` se connecte, son dossier personnel serait `home/Martin/`
* C'est dans ce dossier que vous placerez vos fichiers personnels, à la manière du dossier *Mes documents* de Windows.
* Sauf informations contraires, c'est **le seul répertoire dans lequel vous devez aller**.

`~` représente votre dossier personnel (`/home/nsi/` dans notre cas).

## Chemin absolu et relatif

Un chemin représente le parcours pour aller d'un point de l'arborescence à un autre.

*  `.` représente le dossier courant (celui dans lequel vous êtes)
*  `..` représente le dossier parent
*  Linux utilise des `/` dans les chemins (alors que Windows utilise des `\` !!)

Il existe des chemins dits relatifs et des chemins dits absolus:

* Un **chemin relatif** est un chemin qui dépend du dossier courant
*  Un **chemin absolu** fonctionne quel que soit le dossier dans lequel on se trouve car il part toujours de la racine. Un chemin absolu est donc facile à reconnaître : il commence toujours par la racine `/`

![arborescence](img/arborescence_fichiers_linux.png)`

Exemple de chemins, imaginons qu'un utilisateur se situe dans le répertoire `documents` :

* Chemins absolus :
	* `/var` est le chemin pour aller vers `var`
	* `/home/francois/documents/cours` est le chemin pour aller vers `cours`

* Chemins relatifs :
	* `cours` ou `./cours` est le chemin pour aller vers `cours`
	* `..` est le chemin pour aller vers  `francois`
	*  `../../` est le chemin pour aller vers `home`
	* `../photos/` est le chemin pour aller vers  `photos`

Remarque : Sous Linux, on dit souvent que _**"Tout est fichiers"**_. Cela ne signifie pas que tout est écrit dans des fichiers sur le disque dur mais que tout est présenté symboliquement à l'utilisateur comme des fichiers. Ainsi Répertoire mais aussi clé USB etc... sont manipulables par l'utilisateur comme des fichiers. L'avantage c'est que cela donne à l'utilisateur une manière unique d'interagir avec n'importe quel élément !

# Lignes de commande dans un terminal ![terminal](img/terminal.png)

Principe :

* L’utilisateur tape des commandes sous forme de texte dans un terminal. Après avoir appuyé sur < ENTREE >, ces commandes sont analysées par le [shell](https://doc.ubuntu-fr.org/shel). Le shell désigne un **interpréteur de lignes de commandes** pouvant accéder aux services et interagir avec le noyau d'un système d'exploitation.
Il existe de nombreux interpréteurs de lignes de commandes, qui fonctionnent tous plus ou moins pareillement. Par défaut, le shell associé à un compte d'utilisateur dans Ubuntu est Bourne-Again Shell (Bash)
* Le shell parcourt le texte tapé par l’utilisateur, identifie les commandes et si la syntaxe est correcte, exécute la tâche associée, par exemple :
	* Lancer des programmes ou des applications.
	* Interroger le système et interagir avec lui.
	* Effectuer des tâches complexes grâce à des scripts (programme *"écrit en shell"*).
* Le shell peut renvoyer de l’information à l'écran ou dans un fichier, modifier un fichier, produire un message d’erreur...

Exemple de ligne de commandes : `martin@poste5:~$ ls -la essai`

La ligne de commande comporte une partie non interprétée `martin@poste5:~$` appelée le **prompt**. Le prompt fournit des informations utiles :

* le nom de l’utilisateur `martin`
* le nom de la machine : `poste5`
* le répertoire courant : `~`.
* le symbole `$` indique que l'utilisateur est connecté comme simple utilisateur  (on verra qu'il existe aussi un super-utilisateur)

Dans cet exemple, le prompt nous dit que *martin* est connecté comme *simple utilisateur* sur la machine *poste5* et se situe actuellement dans son *répertoire personnel*

Vient ensuite la commande proprement dite `ls -la essai`, qui sera interprétée par le **shell** :

* le nom de la commande est `ls`
* `-l` et `-a` sont les options (écrites avec des lettres). Plusieurs options peuvent être regroupées derrière le signe `-` (c'est le cas ici `-la`).
* essai est un argument.
