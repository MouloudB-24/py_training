"""
Les **carrés** sont des structures géométriques régulières composées de 4 côtés de longueur visuellement égale, 
où chaque paire de côtés adjacents est orthogonale l’une à l’autre. Dans ce puzzle, ta tâche est d’identifier (« voir ») 
le nombre de carrés dans une figure donnée.

Ce puzzle utilise des caractères ASCII pour « dessiner » des figures contenant des carrés. Plus précisément, 
les lignes horizontales sont représentées par `-`, tandis que les lignes verticales sont représentées par `|`. 
Un caractère `+` indique le point d’intersection entre `-` et `|`, ce qui représente une connexion à la fois horizontale et verticale.

Pour garantir l’égalité visuelle des côtés d’un carré, un carré de hauteur verticale `h` doit avoir une longueur horizontale de `2h - 1` ; avec `h > 1`.

### Différentes tailles de carrés

(Ce sont juste des exemples ; les carrés peuvent être aussi grands que la grille le permet)

```
                           +-------+
                 +-----+   |       |
         +---+   |     |   |       |
   +-+   |   |   |     |   |       |
   +-+   +---+   +-----+   +-------+
h   2      3        4          5
```

### Pour compter les carrés complètement fermés :

* Les coins des carrés doivent être des caractères `+`.
* Chaque côté horizontal d’un carré doit être composé de caractères `-` et/ou `+`.
* Chaque côté vertical d’un carré doit être composé de caractères `|` et/ou `+`.

### Exemples de non-carrés

```
            +---+
            |   |
+---+   +---+   |
|       |       |
+---+   +-------+
```

Note que certains carrés peuvent être adjacents ou se chevaucher, et peuvent donc avoir des côtés qui se croisent.

### Exemples de figures et leur nombre de carrés

```
+-------+       +-------+   +---+---+   +-+           +-----+
|       |       |       |   |   |   |   +-+-+-+       |  +--+--+
|       |   +---+       |   +---+---+     +-+ +---+   |  |  |  |
|       |   |   |       |   |   |   |     +---+   |   +--+--+  |
+-------+   +---+-------+   +---+---+         +---+      +-----+
    1             2             5            4             2
```

### Entrée

* Ligne 1 : Deux entiers séparés par un espace, `R` et `C`, représentant le nombre de lignes et de colonnes de l’entrée.
* Lignes suivantes (R lignes) : Une ligne de longueur `C` représentant la figure.

### Sortie

Un seul entier représentant le nombre total de carrés (toutes tailles confondues) dans la figure.

### Contraintes

* 1 ≤ R, C ≤ 100
* L’entrée ne contient que les caractères `|`, `-`, `+`, des espaces et des retours à la ligne.
"""