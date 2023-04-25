class Class:
    def __init__(self, name):
        self.name = name
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


# Abstract class Statement
class Statement:
    pass


class ie_Statement(Statement):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return str(self.identifier) + "=" + str(self.expression) + ";\n"

    def accept(self, visitor):
        return visitor.visit_ie_statement(self)


class If_stat(Statement):
    def __init__(self, cond, body, Else):
        self.cond = cond
        self.body = body
        self.Else = Else

    def __str__(self):
        return (
            "if ("
            + str(self.cond)
            + "){\n"
            + str(self.body)
            + "} "
            + "else {\n"
            + str(self.Else)
            + "}"
        )

    def accept(self, visitor):
        return visitor.visit_if_statement(self)


class System_out_println(Statement):
    def __init__(self, expr):
        self.expr = expr

    # def __str__(self):
    #     return "System.out.println(" + str(self.expr) + ");"

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
    def accept(self,visitor):
        return visitor.visit_Integer(self)


class MainClass:
    def __init__(self, statement):
        self.statement = statement

    """def __str__(self):
        return (
            "class Main"
            + "{ public static void main (String []) {}"
            + str(self.statement)
            + "}"
        )"""

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
        return visitor.visit_class(self)


class Expression:
    pass


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
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return str(self.identifier) + ".length"

    def accept(self, visitor):
        return visitor.visit_expression_length(self)


# Boolean expression


class bool_expression(Expression):
    def __init__(self, bool):
        self.bool = bool

    def __str__(self):
        return str(self.bool)

    def accept(self, visitor):
        return visitor.visit_bool_expression(self)


class countery_expression(Expression):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "!" + str(self.identifier)

    def accept(self, visitor):
        return visitor.visit_countery_expression(self)


class simple_expression(Expression):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return str(self.identifier)

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
