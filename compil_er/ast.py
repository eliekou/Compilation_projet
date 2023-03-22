class Class:
    def __init__(self,Vardeclaration, MethodDeclaration, name):
        self.name = name
        self.Vardecl = Vardeclaration
        self.Methoddelc = MethodDeclaration
    def __str__(self):
        return("Class" + str(self.name) + "{" + str(Vardecl) + str(MethodDeclaration) + "}")