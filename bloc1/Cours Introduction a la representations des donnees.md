---
title: Introduction à la représentation des données
date: avril 2020
author: R. Seynave
---

# Introduction à la représentation des données

## 3 constats

1. Une machine informatique traite des DONNEES (nombres, texte, image, son, vidéo, etc...)

2. Pour traiter ces données, une machine informatique exécute des [PROGRAMMES](https://fr.wikipedia.org/wiki/Programme_informatique)

3. Une machine informatique ne sait utiliser que des nombres binaires (BIT 0/1)

**Pourquoi la machine utilise uniquement des 0 et des 1 ?**

La raison est technologique : Tous les constituants d'un ordinateur (Le [processeur](https://fr.wikipedia.org/wiki/Processeur), les [mémoires](https://fr.wikipedia.org/wiki/M%C3%A9moire_(informatique))...) sont fabriqués à base de transistors.  
Or un [transistor](https://fr.wikipedia.org/wiki/Transistor) est un _"nano-interrupteur électronique"_ ne pouvant prendre que 2 états : ouvert / fermé.  
En informatique, on appelle [bit](https://fr.wikipedia.org/wiki/Bit) (abbréviation de _**B**inary dig**IT**_) cette unité la plus fondamentale qui ne peut prendre que 2 valeurs, désignées le plus souvent par les chiffres 0 et 1.
Souvent la machine traite les bits non pas individuellement mais par paquet, le plus souvent par paquet de 8 bits.

**Définition : Un [octet](https://fr.wikipedia.org/wiki/Octet) est un groupe de 8 bits**. Ex : `10100011` est un octet.

## 2 conclusions

**Conclusion 1 :** Toutes les données (nombres, texte, image, son, vidéo, ...) sont donc stockées dans la machine comme une suite de bits

![code binaire](img/codeBinaire.jpg)

Ainsi l'octet `11000111` peut très bien représenter :
* l'entier 199
* ou le caractère Ç
* ou l'entier -57
* ou un niveau de gris d'un pixel d'une image
* ou un _"bout"_ d'une musique
* ou un _"bout"_ d'une vidéo
* ou un _"bout"_ d'un programme écrit en langage machine
* etc....

> QUESTION : Comment des données aussi diverses que des nombres, du texte, une image, etc... peuvent-être uniquement codées en machine par des 1 et des 0 ?  
Une fois qu'on a un octet, comment la machine sait-elle ce qu'il représente ?

1. Un octet pris _"isolément"_ est incompréhensible par un humain ou par la machine !!

=>Pour qu'un octet devienne _"compréhensible"_, il faut donner à l'humain ou à la machine **le système de codage**, qui formalise la façon dont on va représenter les _"données réelles"_ (texte, nombres, image, etc...) en une suite abstraite de 0 et de 1

Il existe de très nombreux système de codage. Si on reprend l'exemple précédent :

L'octet `11000111` représente :
* l'entier 199 avec le codage **Binaire naturel**
* le caractère Ç avec le codage **ASCII**
* l'entier -57 avec le codage **Complément à 2**

2. En programmation, le **[TYPE](https://fr.wikipedia.org/wiki/Type_(informatique))** d'un objet définit son système de codage. Ainsi le **TYPE** :
  * donne la méthode pour passer d'une suite de 0 et de 1 en une _"donnée réelle"_ (texte, nombres, image, etc...)
  * définit les opérations possibles pour chaque donnée. Aisni on ne peut pas faire les mêmes opérations avec une donnée de type **entier** et une donnée de type **texte** (par exemple l'opérateur **soustraction** est possible avec des **entiers** mais est impossible avec du **texte**)

**Conclusion 2 :** Les programmes sont eux-mêmes stockés comme une suite de bit. 
Donc le seul langage réellement compréhensible par la machine est le langage binaire,
aussi appelé [langage machine](https://fr.wikipedia.org/wiki/Langage_machine)
