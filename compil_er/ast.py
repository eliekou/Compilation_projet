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
