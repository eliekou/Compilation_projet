class Class:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.var_declarations = []
        self.method_declarations = []

    def __str__(self):
        var_str = "\n".join([str(var) for var in self.var_declarations])
        method_str = "\n".join([str(method) for method in self.method_declarations])

        return "Class" + str(self.name) + "{\n" + var_str + method_str + "}"

    def accept(self, visitor):
        return visitor.visit_class(self)


class Identifier:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)

    def accept(self, visitor):
        print("TZTTZTZT")
        return visitor.visit_identifier(self)


class Vardeclaration:
    def __init__(self, type, identifier):
        self.type = type
        self.identifier = identifier

    def __str__(self):
        return str(self.type) + str(self.identifier) + ";"

    def accept(self, visitor):
        return visitor.visit_var_declaration(self)


class MethodDeclaration:
    def __init__(self, name, type1, params):
        self.name = name
        self.type = type1
        self.parameters = params
        self.var_declarations = []
        self.statements = []
        self.return_expression = []

    def __str__(self):
        var_str = "\n".join([str(var) for var in self.var_declarations])
        return_str = "\n".join([str(ret) for ret in self.return_expression])
        params = "\n".join([str(param) for param in self.parameters])
        statements = "\n".join([str(stat) for stat in self.statements])

        return (
            "\npublic "
            + (str(self.name))
            + "("
            + params
            + ")"
            + "{\n"
            + var_str
            + " "
            + statements
            + "\nreturn "
            + return_str
            + "}"
        )

    def accept(self, visitor):
        return visitor.visit_method_declaration(self)


class Param:
    def __init__(self, type1, name):
        self.type = type1
        self.identifier = name

    def __str__(self):
        return str(self.type) + str(self.identifier)

    def accept(self, visitor):
        return visitor.visit_param(self)


"""On va maintenant définir les différents Statement qui héritent de la classe abstraite Statement"""


class Statement:
    pass


class ie_Statement(Statement):
    """Va concerner les statement de type identifier = expression"""

    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return str(self.identifier) + "=" + str(self.expression) + ";\n"

    def accept(self, visitor):
        return visitor.visit_ie_statement(self)


class If_stat(Statement):
    def __init__(self, cond):
        self.cond = cond
        self.body = []
        self.else_body = []

    def __str__(self):
        return (
            "if ("
            + str(self.cond)
            + "){\n"
            + "\n".join([str(stat) for stat in self.body])
            + "} "
            + "else {\n"
            + "\n".join([str(stat) for stat in self.else_body])
            + "}"
        )

    def accept(self, visitor):
        return visitor.visit_if_statement(self)


class While_stat(Statement):
    def __init__(self, cond):
        self.cond = cond
        self.body = []

    def __str__(self):
        return (
            "while ("
            + str(self.cond)
            + ") {\n"
            + "\n".join([str(stat) for stat in self.body])
            + "}"
        )

    def accept(self, visitor):
        return visitor.visit_while_statement(self)


class System_out_println(Statement):
    def __init__(self, expr):
        self.expr = expr

    
    def __str__(self):
        return "System.out.println(" + str(self.expr) + ");"

    def accept(self, visitor):
        return visitor.visit_system_out_println(self)


class Type:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return str(self.type)

    def accept(self, visitor):
        return visitor.visit_type(self)


class Integer:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, visitor):
        return visitor.visit_Integer(self)


class MainClass:
    def __init__(self):
        self.statements = []

    def accept(self, visitor):
        return visitor.visit_main_class(self)


class ClassDeclaration:
    def __init__(
        self, identifier, superclass=None, var_declarations=[], method_declarations=[]
    ):
        self.identifier = identifier
        self.superclass = superclass
        self.var_declarations = var_declarations
        # VarDeclaration is like a new expression
        self.method_declarations = method_declarations

    def __str__(self):
        return (
            "class"
            + str(self.identifier)
            + "{"
            + str(self.Vardeclaration)
            + str(self.MethodDeclaration)
            + "}"
        )

    def accept(self, visitor):
        return visitor.visit_class_declaration(self)


"""On va maintenant définir les différentes expressions qui héritent toutes de la classe Expression"""


class Expression:
    def __init__(self, object1):
        self.object = object1


class BinaryExpression(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op

    def __str__(self):
        return str(self.left) + str(self.op) + str(self.right)

    def accept(self, visitor):
        return visitor.visit_binary_expression(self)


class new_expression(Expression):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "new" + str(self.identifier) + "();"

    def accept(self, visitor):
        return visitor.visit_new_expression(self)


class new_array_expression(Expression):
    pass


class expression_length(Expression):
    def __init__(self, object1):
        self.object = object1

    def __str__(self):
        return str(self.object) + ".length"

    def accept(self, visitor):
        return visitor.visit_expression_length(self)


# Boolean expression


class bool_expression(Expression):
    def __init__(self, bool1):
        self.object = bool1

    def __str__(self):
        return str(self.object)

    def accept(self, visitor):
        return visitor.visit_bool_expression(self)


class countery_expression(Expression):
    def __init__(self, ob1):
        self.object = ob1

    def __str__(self):
        return "!" + str(self.object)

    def accept(self, visitor):
        return visitor.visit_countery_expression(self)


class lenght_expression(Expression):
    def __init__(self, ob1):
        self.object = ob1

    def __str__(self):
        return str(self.object) + ".length"

    def accept(self, visitor):
        return visitor.visit_lenght_expression(self)


class int_expression(Expression):
    def __init__(self, int1):
        self.int = int1

    def __str__(self):
        return str(self.int)

    def accept(self, visitor):
        return visitor.visit_int_expression(self)


class simple_expression(Expression):
    def __init__(self, identifier):
        self.object = identifier

    def __str__(self):
        return str(self.object)

    def accept(self, visitor):
        return visitor.visit_simple_expression(self)


class Program:
    def __init__(self, main_class, classes):
        self.classes = classes
        self.main_class = main_class

    def __str__(self):
        return (
            "\nclass MainClass {\n public static void main (String [] args){\n"
            + str(self.main_class)
            + "\n}"
            + "\n"
            + str(self.classes)
        )
