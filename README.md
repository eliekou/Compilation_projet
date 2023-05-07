# Compilation_projet
COMPILATION
Réalisé par Elie Kouyoumdjian
https://github.com/eliekou/Compilation_projet


Le projet présente le travail réalisé pour le cours de compilation.


## RENDU
Le sujet choisi est le front-end du mini-Java. Le  rendu du projet comprend: 

- un lexeur
-   un parseur
-   l'AST
-   Un pretty printer sous forme de visiteur
-   Un semantic Analyser sous forme de visiteur


Et aussi le dossier examples avec les programmes de mini-Java écrit pour lequel j'ai teste le compilateur,
et le fichier constants contenant les léxèmes.

Pour tous les fichiers exemples, la chaine fonctionne et on peut observer les résultats des deux visiteurs,
le Pretty printer et le Semantic Analyser.



Pour la grammaire, le mini-Java n'ayant pas de grammaire officielle,  j'ai commencé par utiliser une grammaire très simple puis j'ai amélioré au fur et à mesure du déroulement du projet. Finalement je suis arrivé à la grammaire de mini-Java présente au lien suivant http://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html, de manière légèrement modifiée (voir grammaire choisi plus bas).

## DOCUMENTATION 
Dans les différents fichiers, les fonctions sont commentées. Pour tester les différents visiteurs il faut décommenter certaines ligne du fichier main.py, il l'est pour l'instant mis sur le pretty printer.
Le visiteur checker va provoquer des exceptions à chaque erreur qu'il trouve.

Pour lancer le programme, il faut run le fichier main.py et donner en arguments le fichier java, il y a 8 exemples dans le dossier examples.

Voici la grammaire finalement choisi, légèrement modifiée par rapport au lien donné plus haut:


# GRAMMAR:

Program::= MainClass ( ClassDeclaration )* <EOF>

MainClass ::= "class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"

ClassDeclaration ::= "class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"

VarDeclaration ::= Type Identifier ";"

MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"






Type	::=	"int" "[" "]"
|	"boolean"
|	"int"
|	Identifier




Statement	::=	"{" ( Statement )* "}"
|	"if" "(" Expression ")" "{" Statement "}" "else" {" Statement "}"
|	"while" "(" Expression ")" "{" Statement "}" 
|	"System.out.println" "(" Expression ")" ";"
|	Identifier "=" Expression ";"
|	Identifier "[" Expression "]" "=" Expression ";"


Expression	::=	Expression ( "&&" | "<" | "+" | "-" | "*" ) Expression
|	Expression "[" Expression "]"

|	Expression "." "length"

|	Expression "." Identifier "(" ( Expression ( "," Expression )* )? ")"
|	<INTEGER_LITERAL>
|	"true"
|	"false"
|	Identifier

|	"new" "int" "[" Expression "]"
|	"new" Identifier "(" ")"
|	"!" Expression
|	"(" Expression ")"

Identifier	::=	<IDENTIFIER>
