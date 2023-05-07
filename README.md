# Compilation_projet
COMPILATION
Réalisé par Elie Kouyoumdjian


Le projet présente le travail réalisé pour le cour de compilation.

Le sujet choisi est le front-end du mini-Java. Le  rendu du projet comprend: 

- un lexeur
-   un parseur
-   l'AST
-   Un pretty printer sous forme de visiteur
-   Un semantic Analyser sous forme de visiteur


Et aussi le dossier examples avec les programmes de mini-Java pour lequel j'ai teste le compilateur,
et le fichier constants.

Pour la grammaire, j'ai commencé par utiliser une grammaire très simple puis j'ai amélioré au fur et à mesure du déroulement du projet. Finalement je suis arrivé à la grammaire de mini-Java présente au lien suivant http://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html.


Dans les diiférents fichiers, les fonctions sont documentées. Pour tester les différents visiteurs il faut décommenter certaines ligne du fichier main.py, il l'est pour l'instant mis sur le pretty printer.
Le visiteur checker va provoquer des exceptions à chaque erreur qu'il trouve.

Pour lancer le programme, il faut run le fichier main.py et donner en arguments le fichier java, il y a 7 exemples dans le dossier examples.

