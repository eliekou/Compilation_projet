class Visitor:
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
        """if class_node.superclass:
            self.visit(class_node.superclass)"""
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


"""Le visiteur Pretty printer avec les classes implémentées permet l'affichage du code Java,
avec les bonnes indentations et les accolades."""


class PrettyPrinter(Visitor):
    def visit_program(self, program):
        print_str = self.visit(program.main_class)
        for class_decl in program.classes:
            print_str += self.visit(class_decl)
        print(print_str)
        # print("class " + program.main_class.name + " {\n public static void main (String[] " + program.main_class + ") {\n" )

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
        print("Method Declarations", class_.method_declarations)
        for method_declarations in class_.method_declarations:
            if method_declarations is not None:
                print_str3 += self.visit(method_declarations)
        # print("STR3", print_str3)
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

    def visit_system_out_println(self, system_out_println):
        a = self.visit(system_out_println.expr)

        return "System.out.println(" + str(system_out_println.expr) + ");"

    def visit_ie_statement(self, ie_statement):
        # return self.visit(ie_statement.expression)

        return str((ie_statement.identifier)) + "=" + str((ie_statement.expression))

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

    def visit_var_declaration(self, var_decl):
        return str(var_decl.type) + "=" + str(var_decl.identifier)


"""class SemanticAnalyser(Visitor):
    def __init__(self):
        self.current_class = None
        self.current_method = None
        self.current_scope = None
        self.current_type = None
        self.current_var = None
        self.current_statement = None
        self.current_expression = None
        self.current_identifier = None
        self.current_method_declaration = None
        self.current_var_declaration = None
        self.current_main_class = None

    def visit_program(self, program):

        self.current_class = program.main_class
        self.visit(program.main_class)
        for class_decl in program.classes:
            self.current_class = class_decl
            self.visit(class_decl)"""


class SemanticAnalyser(Visitor):
    def __init__(self):
        self.DICT_statement = []
        self.DICT_expression = []
        self.DICT_identifier = []
        self.DICT_var_declaration = []
        self.DICT_method_declaration = []
        self.DICT_method_var_declaration = []
        self.DICT_method_statement = []
        self.DICT_main_class = []
        self.DICT_class = []
        self.DICT_program = []

    def __str__(self):
        return (
            "Statement: "
            + str(self.DICT_statement)
            + "\nExpression: "
            + str(self.DICT_expression)
            + "\nIdentifier: "
            + str(self.DICT_identifier)
            + "\nVar Declaration: "
            + str(self.DICT_var_declaration)
            + "\nMethod Declaration: "
            + str(self.DICT_method_declaration)
            + "\nMethod Var Declaration: "
            + str(self.DICT_method_var_declaration)
            + "\nMethod Statement: "
            + str(self.DICT_method_statement)
            + "\nMain Class: "
            + str(self.DICT_main_class)
            + "\nClass: "
            + str(self.DICT_class)
            + "\nProgram: "
            + str(self.DICT_program)
        )

    def visit_program(self, program):
        print_str = self.visit(program.main_class)
        self.DICT_main_class.append(print_str)
        for class_decl in program.classes:
            print_str += self.visit(class_decl)
            self.DICT_class.append(print_str)

        # print("class " + program.main_class.name + " {\n public static void main (String[] " + program.main_class + ") {\n" )

    def visit_main_class(self, main_class):
        """
        MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"
        """
        """print("Main class statement\n", main_class.statement)
        print("Visit Main class statement\n", self.visit(main_class.statement))"""

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
                self.DICT_var_declaration.append(print_str2)
        print_str3 = []

        for method_declarations in class_.method_declarations:
            if method_declarations is not None:
                print_str3 += self.visit(method_declarations)
                self.DICT_method_declaration.append(print_str3)
        """for i in print_str2:
            if i != "\n\t":
                self.DICT_var_declaration.append(i)"""

        """self.DICT_method_declaration.append(print_str3)"""
        return (
            "\nclass "
            + str(class_.name)
            + " {\n"
            + "".join(print_str2)
            + "\n\t"
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
                    self.DICT_method_var_declaration.append(self.visit(var_decl))
        if method.statements is not None:
            for statement in method.statements:
                if statement is not None:
                    statements.append(self.visit(statement))
                    self.DICT_method_statement.append(self.visit(statement))
        if method.return_expression is not None:
            for return_expression1 in method.return_expression:
                if return_expression1 is not None:
                    return_expression.append(self.visit(return_expression1))

        return (
            "\tpublic "
            + str(method.type)
            + str(method.name)
            + "\t\t".join(var_declarations)
            + "\n\t".join(statements)
            + "\n\t\t\treturn "
            + "".join(return_expression)
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

    def visit_system_out_println(self, system_out_println):
        # print(type(system_out_println.expr))

        a = self.visit(system_out_println.expr)

        return "System.out.println(" + str(system_out_println.expr) + ");"

    def visit_ie_statement(self, ie_statement):
        # return self.visit(ie_statement.expression)

        return str((ie_statement.identifier)) + "=" + str((ie_statement.expression))

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

    def visit_var_declaration(self, var_decl):
        return str(var_decl.type) + "=" + str(var_decl.identifier)

    def visitProgram(self, prog):
        for obs in prog.DICT_ASSIGNMENT:
            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier assignment '#{obs}'"
            """else:
                self.DICT_{args}.append(obs)"""

        for obs in prog.Loutput:
            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier assignment '#{obs}'"
            """else:
                self.DICT_{args}.append(obs)"""
            if obs in DICT_OUTPUT:
                pass

        for obs in prog.Lassignment:
            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : duplicate identifier assignment '#{obs}'"
            """else:
                self.DICT_{args}.append(obs)"""


class SemanticAnalyzer2(Visitor):
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

    def visit_var(self, var):
        """On va vérifier que le nom de la variable n'est pas déja utilisé et que les types des objets
        sont les bons."""

        if var.name in self.var_names:
            raise Exception("Variable name already defined")
        else:
            self.var_names.append(var.name)

        if var.type.tag not in [
            "TYPE_INT",
            "boolean",
            "int[]",
            "TYPE_ID",
            "TYPE_STRING",
        ]:
            raise Exception("Unknown type: " + str(var.type))
        if var.name.tag not in ["TYPE_IDENTIFIER"]:
            raise Exception("Unknown type: " + str(var.name))
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

        return str((ie_statement.identifier)) + "=" + str((ie_statement.expression))

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

    def visit_var_declaration(self, var_decl):
        return str(var_decl.type) + "=" + str(var_decl.identifier)
