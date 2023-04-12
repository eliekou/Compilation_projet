class Class:
    def __init__(self, name = None):
        self.name = name
        self.var_declarations = []
        self.method_declarations = []
    def __str__(self):
        return("Class" + str(self.name) + "{" + str(self.var_declarations) + str(self.method_declarations) + "}")
class Identifier:
    def __init__(self,id):
        self.id = id
    def __str__(self):
        return(str(self.id))

class Vardeclaration:
    def __init__(self,type,identifier):
        self.type = type
        self.identifier = identifier
    def __str__(self):
        return(str(self.type)+str(self.identifier) + ";")

class MethodDeclaration:
    def __init__(self,fname,ftype,vardecl,expr):
        self.fname = fname
        self.ftype = ftype
        self.vardecl = vardecl
        self.expr = expr
    def __str__(self):
        return (str(self.id))
#Abstract class Statement
class Statement():
    pass


class ie_Statement(Statement):
    def __init__(self,identifier,expression):
        self.identifier = identifier
        self.expression = expression
    def __str__(self):
        return(str(self.identifier) + "=" + str(self.expression) + ";\n")
class If_stat(Statement):

    def __init__(self,cond,body,Else):
        self.cond = cond 
        self.body = body
        self.Else = Else

    def __str__(self):
        return("if (" + str(self.cond ) + "){" +str(self.body)+ "} " + "else {" + str(self.Else) + "}" )
class System_out_println(Statement):
    def __init__(self,expr):
        self.expr = expr
    def __str__(self):
        return("System.out.println(" + str(self.expr) + ");")
class Type:
    def __init__(self,type):
        self.type = type
    def __str__(self):
        return(str(self.type))


class MainClass:
    def __init__(self,identifier,statement):
        self.identifier = identifier
        self.statement = statement
    def __str__(self):
        return("class" + str(self.identifier) + "{ public static void main (String []) {}" + str(self.statement) + "}")
"""class ClassDeclaration:
    def __init__(self,identifier,Vardeclaration,MethodDeclaration):
        self.identifier = identifier
        self.Vardeclaration = Vardeclaration
        self.MethodDeclaration = MethodDeclaration
    def __str__(self):
        return("class" + str(self.identifier) + "{" + str(self.Vardeclaration) + str(self.MethodDeclaration) + "}")
"""

class Expression:
    pass

class BinaryExpression(Expression):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    def __str__(self):
        return(str(self.left) + str(self.op) + str(self.right))

class new_expression(Expression):
    def __init__(self,identifier):
        self.identifier = identifier
    def __str__(self):
        return("new" + str(self.identifier) + "();")

class new_array_expression(Expression):
    pass
class expression_length(Expression):
    def __init__(self,identifier):
        self.identifier = identifier
    def __str__(self):
        return(str(self.identifier) + ".length")

#Boolean expression

class bool_expression(Expression):
    def __init__(self,bool):
        self.bool = bool
    def __str__(self):
        return(str(self.bool))
class countery_expression(Expression):
    def __init__(self,identifier):
        self.identifier = identifier
    def __str__(self):
        return("!" + str(self.identifier))
class Program:
    def __init__(self, main_class, classes = []):
        self.classes = classes
        self.main_class = main_class
    def __str__(self):
        return(str(self.classes)  + "\nclass MainClass {\n public static void main (String [] args){\n"+ str(self.main_class)+ "\n}" + str(self.classes)  )