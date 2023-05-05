# -*- encoding: utf-8 -*-

import logging
from ast import Program
from ast import *
import ast

logger = logging.getLogger(__name__)
class1 = []
classDeclaration = []


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            print("")
            # self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()

        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            program_node = self.parse_program_2()
        except ParsingException as err:
            logger.exception(err)
            raise
        return program_node

    def parse_type(self):
        if self.show_next().tag == "TYPE_INT":
            type1 = self.expect("TYPE_INT")

        if self.show_next().tag == "TYPE_IDENTIFIER":
            type1 = self.expect("TYPE_IDENTIFIER")

        return type1

        # Your code here!
        # self.expect("R_CURL_BRACKET")

    def parse_assignment(self):
        self.expect("SYSTEM")
        self.expect("PUNCTUATION")
        self.expect("OUT")
        self.expect("PUNCTUATION")
        self.expect("PRINTLN")
        # self.expect("PUNCTUATION")
        self.expect("L_PAREN")
        self.expect("GUILLEMET")
        while self.show_next().tag != "GUILLEMET":
            # program_node.ClassDeclaration.Vardeclaration .append.()
            self.expect("IDENTIFIER")
        self.expect("GUILLEMET")
        self.expect("R_PAREN")

        self.expect("TERMINATOR")

    def parse_Vardeclaration(self):
        self.expect("TYPE_INT")
        self.expect("IDENTIFIER")
        self.expect("TERMINATOR")
        # self.expect("ASSIGN")
        # self.expect("INTEGER")
        # while(self.show_next == "ASSIGN")
        ...

    ...

    def parse_expression(self):
        id1 = self.expect("IDENTIFIER")
        if self.show_next().tag == "ASSIGN":
            self.expect("ASSIGN")
            self.expect("ASSIGN")
            int1 = self.expect("INTEGER")
            return ie_Statement(id1, int1)
        if self.show_next().tag == "INFERIOR":
            self.expect("INFERIOR")
            int1 = self.expect("INTEGER")
            return ie_Statement(id1, int1)

    def parse_if_statement(self):
        self.expect("IF")
        self.expect("L_PAREN")
        cond = self.parse_expression()
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        stat1 = self.parse_statement()
        self.expect("R_CURL_BRACKET")
        if self.show_next().tag == "ELSE":
            self.expect("ELSE")
            self.expect("L_CURL_BRACKET")
            stat2 = self.parse_statement()
            self.expect("R_CURL_BRACKET")
            return If_stat(cond, stat1, stat2)
        return If_stat(cond, stat1, None)

    def parse_println2(self):
        self.expect("PRINTLN2")
        self.expect("L_PAREN")
        self.expect("GUILLEMET")
        id2 = self.expect("IDENTIFIER")
        self.expect("GUILLEMET")
        # expr_node = self.parse_expression()
        self.expect("R_PAREN")
        self.expect("TERMINATOR")
        return System_out_println(id2)

    def parse_identifier_statement(self):
        id1 = self.expect("IDENTIFIER")
        self.expect("ASSIGN")
        int1 = self.expect("INTEGER")
        self.expect("TERMINATOR")
        return ie_Statement(id1, int1)

    def parse_statement(self):
        if self.show_next().tag == "IF":
            return self.parse_if_statement()

        if self.show_next().tag == "PRINTLN2":
            return self.parse_println2()

        if self.show_next().tag == "IDENTIFIER":
            return self.parse_identifier_statement()

        if self.show_next().tag == "L_CURL_BRACKET":
            self.expect("L_CURL_BRACKET")
            self.parse_statement()

    def parse_program(self):
        """
        Parses a program which is a succession of assignments:
        Program	::=	MainClass ( ClassDeclaration )* <EOF>
        """
        # BEGINNING OF parse_program
        print('"BEGINNING OF parse_program"')
        self.expect("CLASS")
        self.expect("IDENTIFIER")
        self.expect("L_CURL_BRACKET")
        self.expect("public")
        self.expect("static")
        self.expect("VOID_TYPE")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("String")
        self.expect("KW_ARGS")
        self.expect("CROCHET[")
        self.expect("CROCHET]")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")

        program_node = Program(class1, classDeclaration)
        while self.show_next().tag != "R_CURL_BRACKET":
            if self.show_next().tag in [
                "TYPE_INT",
                "TYPE_CHAR",
                "bool",
                "TYPE_IDENTIFIER",
            ]:
                program_node.ClassDeclaration.append(self.parse_statement())
                # parse_statement()
                print("there is a statement here")
            else:
                print("There is an assignment here")
                program_node.ClassDeclaration.append(self.parse_assignment())
                # self.parse_assignment()

                # program_node.ClassDeclaration.append(parse_assignment())
        # self.expect("IDENTIFIER")
        self.expect("R_CURL_BRACKET")

        "========"
        # End of parse_program
        # Print the node
        print("========")
        print("PRINTING THE NODE")
        print(program_node.ClassDeclaration)
        print(program_node.classes)

        # _________

        main_class_node = self.parse_main_class()
        program_node = Program(main_class=main_class_node)
        while self.show_next().tag == "CLASS":
            class_declaration_node = self.parse_class_declaration()
            program_node.classes.append(class_declaration_node)
        return program_node

    def visit_Program(self, program):
        pass

    def parse_program_2(self):
        """
        Parses a program which is a succession of assignments:
        Program	::=	MainClass ( ClassDeclaration )* <EOF>
        """
        main_class_node = self.parse_main_class()
        class_declarations = []
        # Ca devrait etre un while mais problème de consommation de léxèmes
        if self.show_next() is not None:
            print("show next is not none", self.show_next().tag)

            while self.show_next().tag == "CLASS":
                print("ee", self.show_next().tag)
                class_node = self.parse_class_declaration()
                class_declarations.append(class_node)

                if self.show_next() is None:
                    break
        program_node = Program(main_class=main_class_node, classes=class_declarations)

        return program_node

    def parse_main_class(self):
        """
        MainClass	::=	"class" "Main" "{" "public" "static" "void" "main" "(" "String" "[" "]" "args" ")" "{" Statement "}" "}"
        """
        self.expect("CLASS")
        id = self.expect("IDENTIFIER")
        if id.value != "Main":
            raise ParsingException(
                f"Main class is expected to be named 'Main', is named {id.value}"
            )
        self.expect("L_CURL_BRACKET")
        self.expect("public")
        self.expect("static")
        self.expect("VOID_TYPE")
        self.expect("KW_MAIN")
        self.expect("L_PAREN")
        self.expect("String")
        self.expect("KW_ARGS")
        self.expect("CROCHET[")
        self.expect("CROCHET]")
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        while self.show_next().tag != "R_CURL_BRACKET":
            statement_node = self.parse_statement()

        self.expect("R_CURL_BRACKET")
        self.expect("R_CURL_BRACKET")

        main_class_node = MainClass(statement=statement_node)
        return main_class_node

    def parse_return(self):
        self.expect("RETURN")
        id1 = self.expect("IDENTIFIER")
        self.expect("TERMINATOR")
        return simple_expression(id1)

    def parse_class_declaration(self):
        """
        ClassDeclaration	::=	"class" "IDENTIFIER" "{" ( VarDeclaration )* ( MethodDeclaration )* "}"
        """
        self.expect("CLASS")
        class_name = self.expect("IDENTIFIER")
        self.expect("L_CURL_BRACKET")

        class_node = Class(name=class_name)
        while self.show_next().tag != "public":
            print("self.show_next().tag", self.show_next().tag)
            # print("self.show_next().tag", self.show_next().tag)
            if (
                self.show_next().tag == "TYPE_INT"
                or self.show_next().tag == "TYPE_CHAR"
                or self.show_next().tag == "bool"
                or self.show_next().tag == "TYPE_IDENTIFIER"
            ):
                var_declaration_node = self.parse_var_declaration()

                class_node.var_declarations.append(var_declaration_node)

            if self.show_next().tag == "R_CURL_BRACKET":
                self.expect("R_CURL_BRACKET")
                return class_node

            else:
                print("ERROR", self.show_next().tag)

        if self.show_next().tag == "public":
            # print("There is a public hereDDDDDDDDD")
            method_declaration_node = self.parse_method_declaration()
            class_node.method_declarations.append(method_declaration_node)

        self.expect("R_CURL_BRACKET")

        return class_node

    def parse_method_declaration(self):
        """
        MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"
        """
        # self.expect("PUBLIC")
        self.expect("public")
        method_type = self.parse_type()
        method_name = self.expect("IDENTIFIER")
        self.expect("L_PAREN")
        if self.show_next().tag != "R_PAREN":
            param_type = self.parse_type()
            param_name = self.expect("IDENTIFIER")
            Param1 = Param(param_type, param_name)
            method_params = [Param1]  # Paramètres de la méthode
            while self.show_next().tag == "COMMA":
                self.expect("COMMA")
                param_type = self.parse_type()
                param_name = self.expect("IDENTIFIER")
                method_params.append(Param(type=param_type, identifier=param_name))

            self.expect("R_PAREN")
            self.expect("L_CURL_BRACKET")
            method_node = MethodDeclaration(
                type1=method_type, name=method_name, params=method_params
            )

            while self.show_next().tag != "RETURN":
                if (
                    self.show_next().tag == "TYPE_INT"
                    or self.show_next().tag == "TYPE_CHAR"
                    or self.show_next().tag == "bool"
                    or self.show_next().tag == "TYPE_IDENTIFIER"
                ):
                    var_declaration_node = self.parse_var_declaration()
                    method_node.var_declarations.append(var_declaration_node)

                while self.show_next().tag in [
                    "TYPE_INT",
                    "TYPE_CHAR",
                    "bool",
                    "IDENTIFIER",
                    "TYPE_IDENTIFIER",
                    "KW_THIS",
                    "KW_NEW",
                    "KW_NULL",
                    "L_PAREN",
                    "MINUS",
                    "NOT",
                    "L_CURL_BRACKET",
                    "KW_IF",
                    "KW_WHILE",
                    "KW_SYSTEM",
                    "KW_OUT",
                    "KW_PRINTLN",
                    "KW_READ",
                    "KW_LENGTH",
                    "KW_PARSEINT",
                    "KW_THIS",
                    "KW_NEW",
                    "KW_NULL",
                    "L_PAREN",
                    "MINUS",
                    "NOT",
                    "L_CURL_BRACKET",
                    "IF",
                    "KW_WHILE",
                    "KW_SYSTEM",
                    "KW_OUT",
                    "KW_PRINTLN",
                    "KW_READ",
                    "KW_LENGTH",
                    "KW_PARSEINT",
                ]:
                    method_node.statements.append(self.parse_statement())

            """self.expect("RETURN")
            method_node.return_expression = self.expect("IDENTIFIER")
            self.expect("TERMINATOR")"""

            return1 = self.parse_return()
            method_node.return_expression.append(return1)
            self.expect("R_CURL_BRACKET")

            return method_node

    def parse_var_declaration(self):
        """
        VarDeclaration	::=	Type "IDENTIFIER" ";"
        """

        var_type = self.parse_type()
        var_name = self.expect("IDENTIFIER")
        self.expect("TERMINATOR")
        """print(
            "Var decl has been parsed",
            Vardeclaration(type=var_type, identifier=var_name),
        )"""
        return Vardeclaration(type=var_type, identifier=var_name)
