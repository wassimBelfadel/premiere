Le langage CSS (Cascading Style Sheets) décrit la présentation et la mise en forme des documents HTML.

Le CSS est un langage très puissant et complexe qui permet de faire des design très riche. Consulter le site  [CSS Zen Garden](http://www.csszengarden.com/tr/francais/) pour en avoir un aperçu.

# Mise en place d'un fichier CSS

Une feuille de style est en fait contenue dans un simple fichier texte d'extension .css, souvent appelé `style.css`.

Ce fichier est lié au document HTML auquel la feuille de style doit s'appliquer, par l'intermédiaire d'une unique balise `<link>` placée dans l'en-tête (balises `<head>`) du fichier .html décrivant la page :

```html
	<head>
		.......................

		<link rel="stylesheet" href="style.css"/>		
		......................		
	</head>
```
# Contenu d'un fichier CSS

## Les règles de style

Le fichier CSS contient la description de l'ensemble **des règles de style** qui permettront la mise en page du fichier HTML lié.

```css
sélecteurA {
  propriete_1: attribut_1;
  propriete_2: attribut_2;
  ........
  }

sélecteurB {
  propriete_1: attribut_1;
  propriete_2: attribut_2;
  ........
  } 			     		
```

* Une **règle de style** (par exemple `propriete_1: attribut_1;`) est constituée du nom d'une **propriété** de présentation (couleur, police, espacement des caractères, taille de l'image, positionnement d'un paragraphe...) suivie de son **attribut** (en gros sa "valeur" : rouge, Arial, 3 pixels, en haut à droite...)  


* Les règles de style à appliquer sur un même élément HTML sont regroupées par **blocs de règles**, délimités par des **accolades { }**.


* un **sélecteur** permet de désigner le (ou les) élément(s) HTML au(x)quel(s) les propriétés concernées doivent être appliquées.

## Un exemple
**Les propriétes css : sur quoi peuvent-elles porter ?**
...Un très grand nombre de choses !! Et ces propriétés dépendent de l'élément sur lequel elles s'appliquent. Les principales sont disponibles dans `/premiere/Outils_et_environnement_informatiques/memento_CSS`. Mais il en existe un nombre gigantesque !!

**Activité :** Appliquer ces blocs de règles CSS sur le document HTML "Tim Berners Lee" (en utilisant ATOM)

```css
a {
  color : red;
  }

strong {
  font-size : 10px;
  font-weight: bold;
  }

img {
  width: 50%;
  border: solid blue 2px;
  }			     		
```

# Les sélecteurs

**Activité :** Appliquer ces blocs de règles CSS sur le document HTML "Tim Berners Lee" (en utilisant Les outils de développeur de Firefox)

## Nom de balise
Un sélecteur permet de définir sur quel élément HTML va s'appliquer le bloc de règles de style. Le plus souvent, un sélecteur est un **nom de balise**. Le bloc de règles s'applique alors **à toutes les balises concernées sans exception**. Ainsi dans l'exemple précédent, tous les liens apparaisent en rouge !

*Mais si on veut que seuls certains liens soient rouges, comment on fait ?...*  
$\Longrightarrow$ Enormément de possibilités. Nous n'en verrons que 2 : utilisation d'**identifiant** et de **classe**.


## Identifiant d'un élément HTML

Dans le code HTML, le nom de l’identifiant est indiqué dans la balise d'ouverture de l'élément que l'on veut mettre en forme par un **attribut de balise `id`**.    
**Attention : un identifiant est unique** (Autrement dit, une seule balise peut porter cet identifiant)

Exemple :

Dans le code HTML, on identifie le paragraphe concerné. Le nom de l'identifiant (ici "important") est bien sûr au choix du développeur
```html
<p id="important">Ceci est un paragraphe qui est important</p>
```
Dans le fichier CSS, le sélecteur est alors l'id précédé du symbole `#`  
Seul le paragraphe "important" sera en rouge et avec une taille de caractères de 15 pixels. Les autres ne sont pas concernés par ce bloc de règles CSS

```css
#important {
  color : red;
  font-size: 15px;
  }
```


## Une classe d'éléments HTML

On désigne ainsi un ensemble d'éléments HTML (même de nature différente) sur lesquels on veut appliquer les mêmes règles de style.

Dans le code HTML, le nom de la classe est indiqué dans la balise d'ouverture de l'élément que l'on veut mettre en forme par un **attribut de balise `class`**.

Exemples :

```html
<p>paragraphe pas concerné</p>
<p class="decaler">1er paragraphe concerné</p>
<p>paragraphe pas concerné</p>
<p>paragraphe pas concerné</p>					
<p class="decaler">2ème paragraphe concerné</p>
<p>paragraphe pas concerné</p>
```
Dans le fichier CSS, le sélecteur est le nom de la classe précédé d'un `.`  
Seuls les 2 paragraphes concernés seront affectés par la propriété : "rajouer une marge extérieur à gauche de 50px"
```css
.decaler {
  margin-left : 50px
  }
```

## Les priorités entre sélecteurs

Parfois, un élément HTML est affecté par plusieurs bloc de règles CSS qui peuvent rentrer en conflit les unes aves les autres. Dans ce cas, CSS effectue un "savant calcul" de priorité pour savoir quelle(s) règle(s) l'emport(ent).

Très grossièrement, on peut retenir que _"plus le sélecteur est "contraignant", plus forte est sa priorité..."_

**Exemple :**

```html
<p>paragraphe pas concerné</p>
<p class="decaler">1er paragraphe concerné</p>
<p>paragraphe pas concerné</p>
<p>paragraphe pas concerné</p>					
<p class="decaler">2ème paragraphe concerné</p>
<p>paragraphe pas concerné</p>
```

```css
.decaler {
  margin-left : 50px
  }

p{
  margin-left: 10px;
  }
```

Dans ce cas, il y a un "conflit" sur les règles concernant les 2 paragraphes de la classe "decaler". En effet :
* Ils sont de la classe "decaler" donc ils sont concernés par la règle `margin-left : 50px`
* Ce sont des paragraphes : donc ils sont concernés par la règle `margin-left : 10px`

$\Longrightarrow$ Dans ce cas, c'est la règle `margin-left : 50px` qui s'applique car le sélecteur `.decaler` est plus "contraignant" que le sélecteur `p`

# Une mauvaise pratique : "Le CSS dans l'HTML"




# Avertissement

Ce cours ne présente que des notions élémentaires de CSS. N'y figurent pas notamment :
* Le positionnement des éléments sur une page web
* Un catalogue exhaustif de tous les sélecteurs CSS possibles
* Le calcul des priorités des sélecteurs CSS
* Et toutes les "propriétés avancées" du CSS (animation, mediaQueries...)

De plus les propriétés CSS sont gigantesques. Pour aller plus loin, vous devez faire preuve d'AUTONOMIE ET CHERCHER PAR VOUS-MEME. Le premier endroit où chercher est le site du [Mozilla Development Network ou MDN](https://developer.mozilla.org/fr/).** Il y a d'autres ressources disponibles dans `/premiere/Outils_et_environnement_informatiques/Bibliographie_webographie` et dans `/premiere/Outils_et_environnement_informatiques/memento_CSS`  
