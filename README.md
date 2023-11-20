# PYTHON EXERCICES TP's


**PLAN :**
- [Série N°1](#serie-n1) 
- [Série N°2](#serie-n2) 
- [Série N°3](#serie-n3) 
- [Série N°4](#serie-n4) 



<a id="serie-n1"></a>  

## Série N°1

### Exercice 1

Ecrire, compiler et visualiser le résultat de ce programme
```python
  a=input("Saisir une valeur ") 
  b=a+1 
  print(b)
```

Interpréter/ corriger le résultat.

### Exercice 2
Ecrire un programme qui prend ==l’âge== et la taille de l’utilisateur et les affiches dans un message par exemple :  
**Vous avez 21 ans et vous mesurez 1.81 m.**

### Exercice 3
Ecrire un programme qui demande à l’utilisateur de saisir une distance (en kilomètre) et le temps (minute) nécessaire pour la parcourir ; votre programme doit calculer la vitesse (en mètre par seconde). Pour rappelle la vitesse= distance/temps

### Exercice 4
Ecrire un programme au quel on fournit un nombre de seconde et on le convertir en heure minute et seconde par exemple : 4510 secondes= 1h 15 min 10 sec

### Exercice 5
Ecrire un programme qui qui affiche en fonction d’une valeur saisie l’un des messages suivants :  
- ”Ce nombre est pair”
- ”Ce nombre est impair, mais est multiple de 3”
- ”Ce nombre n’est ni pair ni multiple de 3”


### Exercice 6
Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est négatif ou positif. Attention toutefois : on ne doit pas calculer le produit des deux nombres.

### Exercice 7
Ecrire un programme qui permet à l’utilisateur de saisir deux nombre ainsi qu’une opération soi + pour l’addition, - pour la soustraction, * pour la multiplication, ou / pour la division. Le programme doit retourner le résultat adéquat à l’opération choisi

### Exercice 8
Ecrire un programme qui permet de saisir 4 notes au clavier, ainsi que leurs coefficients respectives, et affiche la moyenne de ces notes:  
- **note 1** : 12
- **coefficient** : 2
- **note 2** : 15.25
- **coefficient** : 1
- **note 3** : 13.5
- **coefficient** : 4
- **note 4** : 8.75
- **coefficient** : 3
- moyenne de ces 4 notes : 11.95, semestre validé  

Votre programme doit afficher aussi si le semestre est validé (la note >=10), rattrapage (10>note>=7) ou non
validé (note<7)

### Exercice 9
Ecrire un programme qui permet de saisir le nom, le prix et la quantité des articles qui constitue une facture.  
(Le nombre d’article est fixé à 2).  
Le programme doit calculer le totale de la facture. N’oublier pas d’ajouter la TVA pour chaque article (20%)
(MontantTTC=MontantHT + Montant HT*0.2). Votre programme doit afficher le montant totale de chaque
article ainsi que le totale.  
Exemple d’exécution :  
![ex9](assets/tp1-ex9.png)

### Exercice 10
Ecrire un programme qui demande à l’utilisateur de saisir un login et un mot de passe (deux chaines de
caractères). Le programme doit tester si les deux chaines sont égales à « admin » « admin » si c’est le cas on affiche un message de bienvenue sinon on affiche un message à l’utilisateur lui informant que le login et le mot de passe saisie sont incorrecte.

### Exercice 11
Créer un programme qui calcule l’indice de masse corporelle (IMC) avec IMC=Pois/taille2
Afficher un message qui contient l’interprétation du résultat  

| IMC | Interprétation |
| --- | -------------- |
| + de 40 | obésité morbide ou massive |
| 35 à 40 | obésité sévère |
| 30 de 35 | obésité modérée |
| 25 de 30 | Surpoids |
| 18.5 de 25 | corpulence normale |
| 16.5 à 18.5 | Maigreur |
| - de 16.5 | Famine |

### Exercice 12
Ecrire un programme qui calcule le salaire des employées d’une société. L’utilisateur doit saisir le grade et le nombre d’heure qu’a travaillé l’employé le payement se fait à base de la grille tarifaire suivante :

| Grade | Traif horaire | Prime |
| ----- | ------------- | ----- |
| A | 200dh | 1000dh pour chaque 20 heures de travail |
| B | 150dh | 800dh pour chaque 20 heures de travail |
| C | 120dh | 500dh pour chaque 15 heures de travail |
| D | 100dh | 350dh pour chaque 15 heures de travail |
| E | 80dh | 100dh pour chaque 10 heures de travail |

___
<a id="serie-n2"></a>

## Série N°2

### Exercice 1
Ecrire un programme qui calcule la valeur de la somme : **a+aa+aaa+aaaa** pour un chiffre que
l’utilisateur saisi au clavier.  
Exemple si l’utilisateur saisi 9 le programme doit afficher **9+99+999+9999= 11106**

### Exercice 2
Écrire un programme qui affiche la suite de symboles suivante, la taille du triangle doit être saisi par
l’utilisateur:  

![ex2](assets/tp2-ex2.png)

### Exercice 3
Ecrire un programme qui génère aléatoirement un entier entre **1 et 100** et à l'utilisateur de deviner ce
nombre en **7 essais**. Le programme vous signale si le nombre que l'utilisateur a saisi est **très grand**,
**très petit**, ou s'il a trouvé le bon nombre, ainsi que le nombre d’essai de l’utilisateur, l’interface du jeu est comme suit :  

![ex3](assets/tp2-ex3.png)

### Exercice 4
Soit L une liste qui contient les nombres suivants : **{1,-30,0,-2,500,4,2,100}**, écrire un programme qui permet de créer une nouvelle liste M qui contient les nombres négatifs au début de la liste M et les nombres positifs à la fin de la liste M en gardant leurs ordres.

### Exercice 5
Écrire un programme Python qui permet d'insérer une valeur val dans une liste L triée.

### Exercice 6
Ecrire un programme qui supprime toutes les occurrences d’un nombre choisi par l’utilisateur

### Exercice 7
Ecrire un programme qui supprime tous les redoublants d’une liste L sans ajouter des listes supplémentaires.  
**L=[1,2,5,8,6,2,5,9,1,8,8]** devient **[1, 2, 5, 8, 6, 9]**

### Exercice 8
Ecrire un programme qui recherche un nombre saisi par l’utilisateur dans une liste. Votre programme doit retourner **le nombre d’occurrences** ainsi que **les indices** (position) de **chaque occurrence**.

### Exercice 9
Ecrire un programme qui permet de convertir plusieurs valeurs *« euro en dirham (mad) »* ou *l’inverse*.  
- Votre programme doit demander à l’utilisation de choisir la direction de la convention **« euro en mad »** ou **« mad en euro »**
- Ensuite l’utilisateur va saisir autant de valeur qu’il veut. La saisie va **s’arrêter** dès que l’utilisateur a saisi **un nombre négatif**.
- Finalement votre programme affiche les valeurs converties dans la monnaie souhaitée.

1 mad= 0.092 euro  
1 euro = 10.86 mad

### Exercice 10
Ecrire un programme qui calcule l’intersection de deux listes L1 et L2 qui la stocke dans une 3eme liste L3. Exemple :  
L1= [1,3,6,78,35,88,55]  
L2= [12,24,35,24,88,120,155]  
L3= [35,88]

### Exercice 11
Ecrire un programme qui fait une transformation miroir d’une liste  
Exemple la liste **L= [8, 24, 48, 2, 16]** le résultat attendu est : **[16, 2, 48, 24, 8]**

___
<a id="serie-n3"></a>

## Série N°3

### Exercice 1

Ecrire une fonction somme qui prend en paramètres 2 **entiers m et n** et qui retourne la **somme** des entiers de m à n *(on supposera que m < n)*.  
Par exemple, somme(5,8) donne 26 (= 5 + 6 + 7 + 8).


### Exercice 2

#### Équation du second degré :

1. On se propose de travailler à nouveau sur les équations du second degré en utilisant cette fois- ci des fonctions.  
Réaliser les fonctions suivantes (en utilisant les noms imposés):
- Calcul du discriminant : *delta()*
- Calcule du nombre de solutions :*NombreRacine()*
- Affiche le nombre de solutions :*AfficheNombreRacine()*
- Calcule les racines de l’équation : *Racine1()*, *Racine2()*

2. Ecrire une fonction *conversion_temps(h, m, s)* qui prend en paramètre un horaire écrit sous forme **(heures ,minutes, secondes)** et retourne cet horaire converti en secondes.

3. En utilisant cette fonction saisir deux horaires (heures, minutes, secondes) et calculer le temps écoulé entre les deux (en secondes).

4. Ecrire une fonction *conversion_distance(km, m, cm)* qui prend en paramètre une distance écrite sous forme **(Km ,m, cm)** et retourne cette distance en mètres.

5. Ecrire une fonction vitesse qui prend en paramètre une distance sous forme (Km ,m, cm) et un temps sous forme (heures ,minutes, secondes) et qui retourne la vitesse en **m/s**.  

***N.B:** On utilisera les fonctions **conversion_temps(h, m, s)** et conversion_distance(km, m, cm)*

___
<a id="serie-n4"></a> 

## Série N°4

### Exercice 1

Ecrivez une classe *Point* avec les attributs suivants :  
**x** : L'abscisse du point;  
**y** : L'ordonnée du point.  

La classe *Point* doit contenir les accesseurs (get) et mutateurs (set) et aussi une méthode **\_\_str\_\_()** donnant une représentation du point.  

Ecrivez une classe *Rectangle* héritant de Point avec les attributs suivants :  
*longueur* : La longueur du rectangle;
*largeur* : La largeur du rectangle.
La classe *Rectangle* doit contenir des accesseurs (get) et mutateurs (set) et aussi les méthodes suivantes :  
**aire()**: Donne l'aire du rectangle;  
**\_\_str\_\_()**: Donne une représentation du rectangle (surcharge).  

Ecrivez une classe *Parallelepipede* héritant de Rectangle avec les attributs suivants :  
**hauteur** : La hauteur du parallélépipède.  
La classe Parallelepipede doit contenir des accesseurs (get) et mutateurs (set) et aussi les les méthodes suivantes :  
**aire()** : Donne l'aire du parallélépipède (surcharge);  
**volume()** : Donne le volume du parallélépipède;  
**\_\_str\_\_()**: Donne une représentation du parallélépipède (surcharge).  
Tester les classes.

### Exercice 2

Ecrivez une classe *Batiment* avec les attributs suivants :  
**adresse** : L'adresse du bâtiment.
La classe *Batiment* doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs. La classe Batiment doit contenir une méthode **\_\_str\_\_** donnant une représentation du bâtiment.  

Ecrivez une classe *Maison* héritant de Batiment avec les attributs suivants :  
**nbPieces** : Le nombre de pièces de la maison.
La classe *Maison* doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs. La classe Maison doit contenir une méthode **\_\_str\_\_ ** donnant une représentation de la maison.  

Ecrivez une classe *Immeuble* héritant de Bâtiment avec les attributs suivants :  
**nbAppart** : Le nombre d'appartements de l'immeuble.  
La classe Immeuble doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs. La classe Immeuble doit contenir une méthode **\_\_str\_\_** donnant une représentation de l'immeuble.  
Tester les classes.

### Exercice 3

Ecrivez une classe abstraite *Employe* avec les attributs suivants :  
**nom** : Le nom de famille de l'employé;  
**prenom** : Le prénom de l'employé.  

La classe *Employe* doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs et les méthodes suivantes :  
**\_\_str\_\_** : Retourne une représentation d'un employé;  
**gains()** : Retourne le salaire (abstraite).  

Ecrivez une classe *Patron* héritant de Employe avec les attributs suivants :  
**salaire** : Le salaire mensuel.  
La classe Patron doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs et les méthodes suivantes :  
**\_\_str\_\_**: Retourne une représentation du patron;  
**gains()** : Retourne le salaire du patron.  

Ecrivez une classe *TravailleurCommission* héritant de Employe avec les attributs suivants :    
**salaire** : Le salaire mensuel de base;  
**commission** : Montant de la commission par article vendus;  
**quantite** : Nombre d'articles vendus par mois.  

La classe *TravailleurCommission* doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs et les méthodes suivantes :  
**\_\_str\_\_**: Retourne une représentation du travailleur à la commission;  
**gains()** : Retourne la rétribution totale du travailleur à la commission.  

Ecrivez une classe *TravailleurHoraire* héritant de Employe avec les attributs suivants :  
**retribution** : La rétrubution horaire;  
**heures** : Le nombre d'heures de travail par mois.  

La classe *TravailleurHoraire* doit contenir des accesseurs (get) et mutateurs (set) pour les différents attributs et les méthodes suivantes :
**\_\_str\_\_**: Retourne une représentation du travailleur horaire;  
**gains()**: Retourne la rétribution totale du travailleur horaire.  
Tester les classes. Utilisez les propriétés du polymorphisme.