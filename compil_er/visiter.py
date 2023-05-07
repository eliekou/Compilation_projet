class Visitor:
    """Le premier visiteur est uniquement un template de visiteur.
    Il ne fait que parcourir le programme"""

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
        print_str = self.visit(program.main_class)
        for class_decl in program.classes:
            print_str += self.visit(class_decl)
        print(print_str)

    def visit_main_class(self, main_class):
        """
        MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"
        """

        return (
            "class Main {\n\tpublic static void main (String args[]) {\n\t"
            + "\t"
            + self.visit(main_class.statement)
            + "\n\t}\n}"
        )

    def visit_class(self, class_):
        """ClassDeclaration	::=	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )* "}"""
        print_str2 = []
        for var_decl in class_.var_declarations:
            if var_decl is not None:
                print_str2 += "\n\t" + self.visit(var_decl)
        print_str3 = []
        print("class_parent", class_.parent)
        print("Method Declarations", class_.method_declarations)
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
            binary_expression.left
            + " "
            + binary_expression.op
            + " "
            + binary_expression.right
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
        return (
            str((ie_statement.identifier)) + "=" + str((ie_statement.expression)) + ";"
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
        print("3VISITING WHILE STATEMENT")
        stats = []
        print("while_statement", while_statement.body)
        if while_statement.body is not None:
            for stat in while_statement.body:
                print("stat", stat)
                if stat is not None:
                    stats.append(self.visit(stat))
                    print("stata", stat)

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


class SemanticAnalyzer2(Visitor):

    """
    Le visiteur Analyseur Sémantique va visiter le programme et vérifier certaines erreurs possibles:

    - la répitition de deux fois le meme nom de classe
    - la répitition de deux fois le meme nom de méthode
    - la répitition de deux fois le meme nom de variable comme declaration dans le Main
    - l'héritage d'une classe Parent non définie dans le meme programme
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
        self.visit(main_class.statement)

    def visit_class(self, class_):
        print("VISIT CLASS DECLARATION")

        if str(class_.name) in str(self.class_names):
            raise Exception("Class name already defined")

        else:
            self.class_names.append(class_.name)

        if class_.parent is not None:
            if str(class_.parent) not in str(self.class_names):
                raise Exception("Parent class not defined'")
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
            raise Exception("Method name already defined for another method")
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
        print("self.method_names\n", self.method_names)

    def visit_var_declaration(self, var_decl):
        """On va vérifier que le nom de la variable n'est pas déja utilisé et que les types des objets
        sont les bons."""

        if str(var_decl.identifier) in str(self.var_names):
            raise Exception("Variable name already defined")
        else:
            self.var_names.append(var_decl.identifier)

        if var_decl.type.tag not in [
            "TYPE_INT",
            "boolean",
            "int[]",
            "TYPE_ID",
            "TYPE_STRING",
        ]:
            raise Exception("Unknown type: " + str(var.type))
        if var_decl.identifier.tag not in ["IDENTIFIER"]:
            raise Exception("Unknown type: " + str(var_decl.identifier))
        return str(var_decl.type) + " " + str(var_decl.identifier) + ";\n"

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

    def visit_ie_statement(self, ie_statement):
        if ie_statement.identifier.tag not in ["IDENTIFIER"]:
            raise Exception("Unknown type: " + str(ie_statement.identifier))

        return (
            str((ie_statement.identifier)) + "=" + str((ie_statement.expression) + ";")
        )

    def visit_if_statement(self, if_statement):
        else_1 = []
        if if_statement.Else is not None:
            else_1.append(self.visit(if_statement.Else))

        return (
            "\tif ("
            + self.visit(if_statement.cond)
            + ") {\n\t\t\t\t"
            + self.visit(if_statement.body)
            + "\n\t\t\t}"
            + "\n\t\t\telse {\n\t\t\t\t "
            + "\n\t".join(else_1)
            + "}\n"
        )

    def visit_simple_expression(self, simple_expr):
        return "\t" + str(simple_expr.identifier)

    def visit_Integer(self):
        return self.value


"""    def visit_var_declaration(self, var_decl):
        return str(var_decl.type) + "=" + str(var_decl.identifier)"""
