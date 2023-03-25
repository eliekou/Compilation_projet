class Class:
    def __init__(self,Vardeclaration, MethodDeclaration, name):
        self.name = name
        self.Vardecl = Vardeclaration
        self.Methoddelc = MethodDeclaration
    def __str__(self):
        return("Class" + str(self.name) + "{" + str(Vardecl) + str(MethodDeclaration) + "}")


class Vardeclaration:
    def __init__(self,type,identifier):
        self.type = type
        self.identifier = identifier
    def __str__(self):
        return(str(self.type)+str(self.identifier) + ";")
class Identifier:
    def __init__(self,id):
        self.id = id
    def __str__(self):
        return(str(self.id))
class MethodDeclaration:
    def __init__(self,fname,ftype,vardecl,expr):
        self.fname = fname
        self.ftype = ftype
        self.vardecl = vardecl
        self.expr = expr
    def __str__(self):
        return (str(self.id))

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
class ClassDeclaration:
    def __init__(self,identifier,Vardeclaration,MethodDeclaration):
        self.identifier = identifier
        self.Vardeclaration = Vardeclaration
        self.MethodDeclaration = MethodDeclaration
    def __str__(self):
        return("class" + str(self.identifier) + "{" + str(self.Vardeclaration) + str(self.MethodDeclaration) + "}")
class Program:
    def __init__(self,classes,ClassDeclaration):
        self.classes = classes
        self.ClassDeclaration = ClassDeclaration
    def __str__(self):
        return(str(self.classes) + str(self.ClassDeclaration))