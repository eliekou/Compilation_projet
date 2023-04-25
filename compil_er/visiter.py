class Visitor:
    def visit(self, node):
        return node.accept(self)

    def visit_program(self, program_node):
        self.visit(program_node.main_class)
        for class_decl in program_node.class_declarations:
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

    def visit_method():
        pass

    def visit_var():
        pass

    def visit_type():
        pass

    def visit_binary_expression():
        pass

    def visit_new_expression():
        pass

    def visit_expression_length():
        pass

    def visit_identifier():
        pass

    def visit_bool_expression():
        pass

    def visit_countery_expression():
        pass

    def visit_simple_expression():
        pass

    def visit_this_expression():
        pass

    def visit_array_expression():
        pass

    def visit_method_call():
        pass

    def visit_statement():
        pass

    def visit_if_statement():
        pass

    def visit_while_statement():
        pass

    def visit_print_statement():
        pass

    def visit_assign_statement():
        pass

    def visit_array_assign_statement():
        pass

    def visit_ie_statement():
        pass


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
        print_str3 = []

        for method_declarations in class_.method_declarations:
            if method_declarations is not None:
                print_str3 += self.visit(method_declarations)
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
            + "{\n\t\t"
            + "\t\t".join(var_declarations)
            + "\n\t\t"
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


class SemanticAnalyser:
    def __init__(self):
        self.DICT_INPUT = []
        self.DICT_OUTPUT = []
        self.DICT_ASSIGNMENT = []

    def visitProgram(self, prog, args):
        for obs in prog.Linput:
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

        for obs in prog.Lassignment:
            if obs in DICT_INPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier input '#{obs}'"
            if obs in DICT_OUTPUT:
                raise "ERROR at #{obs} : wrong identifier and duplicate identifier output '#{obs}'"
            if obs in DICT_ASSIGNMENT:
                raise "ERROR at #{obs} : duplicate identifier assignment '#{obs}'"
            """else:
                self.DICT_{args}.append(obs)"""
