class Visitor:
    """Le premier visiteur est uniquement un template de visiteur.
    Il ne fait que parcourir le programme
    Il est uniquement fait pour pouvoir être hérité par les autres visiteurs.
    
    Le pretty printer situé plus bas, et les deux semantic Analyser sont ceux qu'ils faut lancer."""

    def visit(self, node):
        return node.accept(self)

    def visit_program(self, program_node):
        self.visit(program_node.main_class)
        for class_decl in program_node.classes:
            self.visit(class_decl)

    def visit_main_class(self, main_class_node):
        self.visit(main_class_node.statement)

    def visit_class(self, class_node):
        self.visit(class_node.name)

        if class_node.superclass:
            self.visit(class_node.superclass)

        for var_decl in class_node.var_declarations:
            self.visit(var_decl)
        for method_decl in class_node.method_declarations:
            self.visit(method_decl)

    def visit_method_declaration(self, method_declaration_node):
        for var_decl in method_declaration_node.var_declarations:
            self.visit(var_decl)
        for statement in method_declaration_node.statements:
            self.visit(statement)
        self.visit(method_declaration_node.expression)

    def visit_var_declaration(self, var_declaration):
        self.visit(var_declaration.type)
        self.visit(var_declaration.identifier)

    def visit_type():
        pass

    def visit_binary_expression():
        pass

    def visit_new_expression():
        pass

    def visit_expression_length():
        pass

    def visit_identifier(self, identifier_node):
        print("END OF SIMPLE VISIT")

    def visit_bool_expression():
        pass

    def visit_countery_expression():
        pass

    def visit_simple_expression(self, simple_expression_node):
        self.visit(simple_expression_node.identifier)

    def visit_this_expression():
        pass

    def visit_array_expression():
        pass

    def visit_method_call():
        pass

    def visit_statement():
        pass

    def visit_if_statement(self, if_statement):
        self.visit(if_statement.if_expression)
        self.visit(if_statement.if_statement)
        self.visit(if_statement.else_statement)

    def visit_while_statement():
        pass

    def visit_print_statement():
        pass

    def visit_assign_statement(self, assign_statement_node):
        self.visit(assign_statement_node.identifier)
        self.visit(assign_statement_node.expression)

    def visit_array_assign_statement():
        pass

    def visit_ie_statement(self, ie_statement_node):
        self.visit(ie_statement_node.identifier)
        self.visit(ie_statement_node.expression)


class PrettyPrinter(Visitor):
    """Le visiteur Pretty printer avec les classes implémentées permet l'affichage du code Java,
    avec les bonnes indentations et les accolades."""

    def visit_program(self, program):
        print("\n######## Pretty Printer #######\n")
        print_str = self.visit(program.main_class)
        for class_decl in program.classes:
            print_str += self.visit(class_decl)
        print(print_str)

    def visit_main_class(self, main_class):
        """
        MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" (Statement)* "}" "}"
        """
        #Dans la grammaire choisie, la classe Main peut avoir plusieurs statements.


        print_statements = []
        for stat in main_class.statements:
            if stat is not None:
                print_statements += "\n\t" + self.visit(stat)
        if main_class.statements is not None:
            return (
                "class Main {\n\tpublic static void main (String args[]) {\n\t"
                + "\t"
                + "".join(print_statements)
                + "\n\t}\n}"
            )

    def visit_class(self, class_):
        """ClassDeclaration	::=	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"""
        print_str2 = []
        for var_decl in class_.var_declarations:
            if var_decl is not None:
                print_str2 += "\n\t" + self.visit(var_decl)
        print_str3 = []

        for method_declarations in class_.method_declarations:
            if method_declarations is not None:
                print_str3 += self.visit(method_declarations)

        if class_.parent is not None:
            return (
                "\nclass "
                + str(class_.name)
                + " extends "
                + str(class_.parent)
                + " {\n"
                + "".join(print_str2)
                + "\n\t"
                + "".join(print_str3)
                + "}\n"
            )

        return (
            "\nclass "
            + str(class_.name)
            + " {\n"
            + "".join(print_str2)
            + " \n"
            + "\n"
            + "".join(print_str3)
            + "}\n"
        )

    def visit_method_declaration(self, method):
        """MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"""

        var_declarations = []
        statements = []
        return_expression = []

        if method.var_declarations is not None:
            for var_decl in method.var_declarations:
                if var_decl is not None:
                    var_declarations.append(self.visit(var_decl))
        if method.statements is not None:
            for statement in method.statements:
                if statement is not None:
                    statements.append(self.visit(statement))
        if method.return_expression is not None:
            for return_expression1 in method.return_expression:
                if return_expression1 is not None:
                    return_expression.append(self.visit(return_expression1))

        return (
            "\tpublic "
            + str(method.type)
            + " "
            + str(method.name)
            + "{\n\n\t\t"
            + "\t\t".join(var_declarations)
            + "\n\t\t"
            + "\n\n\t".join(statements)
            + "\n\t\t\treturn "
            + "".join(return_expression)
            + ";"
            + "\n\t\t\t}\n"
        )

    def visit_var(self, var):
        return var.type + " " + var.name + ";\n"

    def visit_type(self, type_):
        return type_.name

    def visit_binary_expression(self, binary_expression):
        return (
            str(binary_expression.left)
            + str(binary_expression.op.value)
            + str(binary_expression.right)
        )

    def visit_new_expression(self, new_expression):
        return "new " + new_expression.name + "()"

    def visit_expression_length(self, expression_length):
        return expression_length.name + ".length"

    def visit_identifier(self, identifier):
        return identifier.id

    def visit_bool_expression(self, bool_expression):
        return str(bool_expression.value)

    def visit_lenght_expression(self, lenght_expression):
        return str(lenght_expression.name) + ".length"

    def visit_countery_expression(self, countery_expression):
        return "!" + str(countery_expression.name)

    def visit_system_out_println(self, system_out_println):
        a = self.visit(system_out_println.expr)

        return "System.out.println(" + str(system_out_println.expr) + ");"

    def visit_ie_statement(self, ie_statement):
        return str((ie_statement.identifier)) + "=" + str((ie_statement.expression))

    def visit_if_statement(self, if_statement):
        body_1 = []
        else_1 = []

        if if_statement.body is not None:
            for body in if_statement.body:
                if body is not None:
                    body_1.append(self.visit(body))
        if if_statement.else_body is not None:
            for else_ in if_statement.else_body:
                if else_ is not None:
                    else_1.append(self.visit(else_))

        return (
            "\tif ("
            + self.visit(if_statement.cond)
            + ") {\n\t\t\t\t"
            + "\n\t\t\t\t".join(body_1)
            + ";"
            + "\n\t\t\t}"
            + "\n\t\t\telse {\n\t\t\t\t "
            + "\n\t".join(else_1)
            + ";"
            + "}\n"
        )

    def visit_while_statement(self, while_statement):
        stats = []
        print("while_statement", while_statement.body)
        if while_statement.body is not None:
            for stat in while_statement.body:
                if stat is not None:
                    stats.append(self.visit(stat))

        return (
            "\twhile ("
            + self.visit(while_statement.cond)
            + ") {\n\t\t\t\t"
            + "\n\t\t\t\t".join(stats)
            + "\n\t\t\t}"
            + "\n"
        )

    def visit_simple_expression(self, simple_expr):
        return "\t" + str(simple_expr.object)

    def visit_Integer(self):
        return self.value

    def visit_var_declaration(self, var_decl):
        return str(var_decl.type) + str(var_decl.identifier) + ";\n"


class SemanticAnalyzer(Visitor):

    """
    Le visiteur Analyseur Sémantique va visiter le programme et vérifier certaines erreurs possibles:

    - la répétition de deux fois le meme nom de classe
    - la répitition de deux fois le meme nom de méthode
    - la répitition de deux fois le meme nom de variable comme declaration dans le Main
    - l'héritage d'une classe Parent non définie dans le meme programme
    - l'utilisation d'une variable non préalablement déclarée

    Dans chacun des ces cas, il y aura une exception qui sera raise.
    """

    def __init__(self):
        self.class_names = []
        self.method_names = []
        self.var_names = []

    def visit_program(self, program):
        self.visit(program.main_class)
        for class_decl in program.classes:
            print("class_decl\n")
            self.visit(class_decl)

    def visit_main_class(self, main_class):
        if main_class.statements is not None:
            for stat in main_class.statements:
                if stat is not None:
                    self.visit(stat)

    def visit_class(self, class_):
        if str(class_.name) in str(self.class_names):
            raise Exception(f"Class name {class_.name} already defined")

        else:
            self.class_names.append(class_.name)

        if class_.parent is not None:
            if str(class_.parent) not in str(self.class_names):
                raise Exception(f"Parent class {class_.parent} not defined'")
            else:
                self.class_names.append(class_.parent)
        for var in class_.var_declarations:
            self.visit(var)

        for method in class_.method_declarations:
            self.visit(method)

    def visit_method_declaration(self, method):
        """MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"""
        """On va vérifier que le nom de la méthode n'est pas déjà utilisé"""

        var_declarations = []
        statements = []
        return_expression = []

        if str(method.name) in str(self.method_names):
            raise Exception(
                f"Method name {method.name} already defined for another method"
            )
        else:
            self.method_names.append(method.name)

        if method.var_declarations is not None:
            for var_decl in method.var_declarations:
                if var_decl is not None:
                    self.visit(var_decl)
        if method.statements is not None:
            for statement in method.statements:
                if statement is not None:
                    self.visit(statement)
        if method.return_expression is not None:
            for return_expression1 in method.return_expression:
                if return_expression1 is not None:
                    self.visit(return_expression1)

    def visit_var_declaration(self, var_decl):
        """On va vérifier que le nom de la variable n'est pas déja utilisé et que les types des objets
        sont les bons."""

        if str(var_decl.identifier) in str(self.var_names):
            raise Exception(
                f"Variable name {var_decl.identifier.value} already defined in another declaration"
            )
        else:
            self.var_names.append(var_decl.identifier)

        if var_decl.type.tag not in [
            "TYPE_INT",
            "boolean",
            "int[]",
        ]:
            raise Exception("Unknown type: " + str(var.type))
        if var_decl.identifier.tag not in ["IDENTIFIER"]:
            raise Exception("Unknown type: " + str(var_decl.identifier))

    def visit_type(self, type_):
        return type_.name

    def visit_binary_expression(self, binary_expression):
        return (
            binary_expression.left
            + " "
            + binary_expression.op
            + " "
            + binary_expression.right
        )

    def visit_new_expression(self, new_expression):
        return "new " + str(new_expression.name) + "()"

    def visit_expression_length(self, expression_length):
        return expression_length.name + ".length"

    def visit_identifier(self, identifier):
        if identifier.id.tag not in ["IDENTIFIER"]:
            raise Exception(
                "Unknown type: "
                + str(identifier.id)
                + "Was expecting type IDENTIFIER got "
                + str(identifier.id.tag)
            )

    def visit_bool_expression(self, bool_expression):
        return str(bool_expression.value)

    def visit_system_out_println(self, system_out_println):
        if system_out_println.expr.tag not in [
            "IDENTIFIER",
        ]:
            raise Exception("Unknown type: " + str(system_out_println.expr))
        a = self.visit(system_out_println.expr)

        return "System.out.println(" + str(system_out_println.expr) + ");"

    def visit_ie_statement(self, ie_statement):
        """On vérifie que l'on ne peut pas faire de déclaration sur une variable non déclarée"""

        if ie_statement.identifier.tag not in ["IDENTIFIER"]:
            raise Exception("Unknown type: " + str(ie_statement.identifier))
        if str(ie_statement.identifier) not in str(self.var_names):
            print(self.var_names)
            raise Exception(
                f"Variable {ie_statement.identifier.value} is not yet defined, cannot be used. "
            )
        return (
            str((ie_statement.identifier))
            + "="
            + str((ie_statement.expression))
            + (";")
        )

    def visit_if_statement(self, if_statement):
        body_1 = []
        else_1 = []

        if if_statement.body is not None:
            for body in if_statement.body:
                if body is not None:
                    body_1.append(self.visit(body))
        if if_statement.else_body is not None:
            for else_ in if_statement.else_body:
                if else_ is not None:
                    else_1.append(self.visit(else_))

    def visit_while_statement(self, while_statement):
        stats = []
        print("while_statement", while_statement.body)
        if while_statement.body is not None:
            for stat in while_statement.body:
                if stat is not None:
                    stats.append(self.visit(stat))

    def visit_simple_expression(self, simple_expr):
        return "\t" + str(simple_expr.object)

    def visit_Integer(self):
        return self.value


class SemanticAnalyser2(Visitor):

    """On fait un second analyseur sémantique qui respecte plus le système de clé-hash
    Cela permet de prendre en compte les différents scopes pour les déclarations de variables.

    On va donc créer une table de symboles qui va contenir les classes déclarées, les différentes variables déclarées au sein de ces 
    classes ou des méthodes de ces classes.
    """

    def __init__(self):
        self.symbols_table = {}
        self.visit_class_current = None
        self.visit_method_current = None
        self.place = None

    def visit_program(self, program):
        # self.symbols_table.append({})

        self.visit(program.main_class)

        for class_decl in program.classes:
            
            self.visit(class_decl)
        print(self.symbols_table)#Affichage du dictionnnaire crée pendant la visite du programme
    def visit_main_class(self, main_class):
        class_main_table = {}
        self.symbols_table["Main"] = class_main_table
        self.visit_class_current = "Main"
        if main_class.statements is not None:
            for stat in main_class.statements:
                if stat is not None:
                    self.visit(stat)

    def visit_class(self, class_):
        check = self.symbols_table.get(class_.name.value)

        if check:
            raise Exception(f"Class name {class_.name} already defined")
            #Cas d'une répitition de deux fois le meme nom.

        class_name = class_.name.value
        class_table = {}
        self.symbols_table[class_name] = class_table
        self.visit_class_current = class_name  # On garde en mémoire la classe visitée actuellement
        

        for var in class_.var_declarations:
            self.visit_method_current = None
            self.visit(var)
        for method in class_.method_declarations:
            self.visit(method)

    def visit_method_declaration(self, method):
        """MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"""
        """On va vérifier que le nom de la méthode n'est pas déjà utilisé"""
        self.visit_method_current = method.name.value

        method_name = method.name.value
        method_table = {}
        class_table = self.symbols_table[self.visit_class_current]
        class_table[method_name] = method_table

        

        if method.var_declarations is not None:
            for var_decl in method.var_declarations:
                if var_decl is not None:
                    self.visit(var_decl)
        if method.statements is not None:
            for statement in method.statements:
                if statement is not None:
                    self.visit(statement)
        if method.return_expression is not None:
            for return_expression1 in method.return_expression:
                if return_expression1 is not None:
                    self.visit(return_expression1)

    def visit_var_declaration(self, var_decl):
        """On va vérifier que le nom de la variable n'est pas déja utilisé et que les types des objets
        sont les bons."""
        var_name = var_decl.identifier.value
        if self.visit_method_current is not None:
            method_table = self.symbols_table[self.visit_class_current][
                self.visit_method_current
            ]
            # On est dans le cas d'une déclaration de variables au sein d'une méthode
        else:
            method_table = self.symbols_table[self.visit_class_current]

            # On est dans le cas d'une déclaration de variables en dehors d'une méthode
        
        if var_name in method_table:
            raise Exception(
                f"Variable name {var_decl.identifier.value} already defined in another declaration"
            )
        method_table[var_name] = var_decl.type

        if var_decl.type.tag not in [
            "TYPE_INT",
            "boolean",
            "int[]",
        ]:
            raise Exception("Unknown type: " + str(var.type))
        if var_decl.identifier.tag not in ["IDENTIFIER"]:
            raise Exception("Unknown type: " + str(var_decl.identifier))
        

    def visit_ie_statement(self, ie_statement):
        """On vérifie que l'on ne peut pas faire de déclaration sur une variable non déclarée"""

        var_name_used = ie_statement.identifier.value

        class_table = self.symbols_table[self.visit_class_current]
        # Key2 va vérifier la déclaration au niveau de la méthode
        if self.visit_method_current is not None:
            method_table = self.symbols_table[self.visit_class_current][
                self.visit_method_current
            ]
            key2 = method_table.get(var_name_used)
        else:
            method_table = None
            key2 = None

        # Key va vérifier la déclaration au niveau de la classe
        key = class_table.get(var_name_used)
        

        if key2 is None and key is None:
            # Cas ou la variables n'a jamais été déclarée
            raise Exception(
                f"Variable {ie_statement.identifier.value} is not yet defined, cannot be used. "
            )
        else:
            pass
        

    def visit_if_statement(self, if_statement):
        body_1 = []
        else_1 = []

        if if_statement.body is not None:
            for body in if_statement.body:
                if body is not None:
                    body_1.append(self.visit(body))
        if if_statement.else_body is not None:
            for else_ in if_statement.else_body:
                if else_ is not None:
                    else_1.append(self.visit(else_))

    def visit_simple_expression(self, simple_expr):
        return "\t" + str(simple_expr.object)

    def visit_Integer(self):
        return self.value

    def visit_type(self, type_):
        return type_.name

    def visit_binary_expression(self, binary_expression):
        return (
            binary_expression.left
            + " "
            + binary_expression.op
            + " "
            + binary_expression.right
        )

    def visit_new_expression(self, new_expression):
        return "new " + str(new_expression.name) + "()"

    def visit_expression_length(self, expression_length):
        return expression_length.name + ".length"

    def visit_identifier(self, identifier):
        if identifier.id.tag not in ["IDENTIFIER"]:
            raise Exception(
                "Unknown type: "
                + str(identifier.id)
                + "Was expecting type IDENTIFIER got "
                + str(identifier.id.tag)
            )
        return identifier.id

    def visit_bool_expression(self, bool_expression):
        return str(bool_expression.value)

    def visit_system_out_println(self, system_out_println):
        if system_out_println.expr.tag not in [
            "IDENTIFIER",
        ]:
            raise Exception("Unknown type: " + str(system_out_println.expr))
        a = self.visit(system_out_println.expr)

        return "System.out.println(" + str(system_out_println.expr) + ");"
