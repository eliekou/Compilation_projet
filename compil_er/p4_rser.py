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
            pass
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

    ...

    def parse_expression(self):
        """La fonction parse_expression doit, pour respecter la grammaire, prendre en compte toutes les différentes
        expressions y compris toutes les opérations logiques entre expressions. On fait donc plusieurs fois appel à la
        fonction parse_expression dans la fonction parse_expression."""

        if self.show_next().tag == "TRUE":
            self.expect("TRUE")
            return bool_expression(True)
        if self.show_next().tag == "FALSE":
            self.expect("FALSE")
            return bool_expression(False)
        if self.show_next().tag == "NO":
            self.expect("NO")
            expr2 = self.parse_expression()
            return bool_expression(expr2)

        if self.show_next().tag == "AND":
            self.expect("AND")
            expr2 = self.parse_expression()

        if self.show_next().tag == "OR":
            self.expect("OR")
            expr2 = self.parse_expression()
        if self.show_next().tag == "INTEGER":
            int1 = self.expect("INTEGER")

            return int_expression(int1)

        if self.show_next().tag == "IDENTIFIER":
            id1 = self.expect("IDENTIFIER")

            if self.show_next().tag == "ASSIGN":
                self.expect("ASSIGN")

                id2 = self.parse_expression()

                return ie_Statement(id1, id2)
            if self.show_next().tag == "INFERIOR":
                self.expect("INFERIOR")

                id2 = self.parse_expression()

                return ie_Statement(id1, id2)
            if self.show_next().tag == "AND":
                self.expect("AND")

                id2 = self.parse_expression()

                return ie_Statement(id1, id2)
            else:
                return Identifier(id1)

    def parse_if_statement(self):
        """Va parser les statement avec if et else"""
        self.expect("IF")
        self.expect("L_PAREN")
        cond = self.parse_expression()

        if_stat = If_stat(cond)
        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        while self.show_next().tag != "R_CURL_BRACKET":
            stat1 = self.parse_statement()
            if_stat.body.append(stat1)

        self.expect("R_CURL_BRACKET")
        if self.show_next().tag == "ELSE":
            self.expect("ELSE")
            self.expect("L_CURL_BRACKET")
            while self.show_next().tag != "R_CURL_BRACKET":
                stat2 = self.parse_statement()
                if_stat.else_body.append(stat2)

            self.expect("R_CURL_BRACKET")
            return if_stat

        return if_stat

    def parse_while_statement(self):
        """Va parser les statement avec while"""

        self.expect("WHILE")
        self.expect("L_PAREN")
        cond = self.parse_expression()

        while_stat = While_stat(cond)

        self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")
        while self.show_next().tag != "R_CURL_BRACKET":
            stat1 = self.parse_statement()
            print
            while_stat.body.append(stat1)

        self.expect("R_CURL_BRACKET")

        return while_stat

    def parse_println2(self):
        """Va parser les statement d'affichage"""

        self.expect("PRINTLN2")
        self.expect("L_PAREN")
        self.expect("GUILLEMET")
        id2 = self.expect("IDENTIFIER")
        self.expect("GUILLEMET")

        self.expect("R_PAREN")
        self.expect("TERMINATOR")
        return System_out_println(id2)

    def parse_statement(self):
        """La fonction parse_statement qui en fonction des cas va renvoyer sur toutes les autres fonctions
        pour parser les diffférents types de statements"""

        if self.show_next().tag == "IF":
            return self.parse_if_statement()

        if self.show_next().tag == "WHILE":
            return self.parse_while_statement()

        if self.show_next().tag == "PRINTLN2":
            return self.parse_println2()

        if self.show_next().tag == "L_CURL_BRACKET":
            self.expect("L_CURL_BRACKET")
            self.parse_statement()
        if self.show_next().tag == "IDENTIFIER":
            id1 = self.expect("IDENTIFIER")
            if self.show_next().tag == "ASSIGN":
                self.expect("ASSIGN")
                expr = self.parse_expression()

                self.expect("TERMINATOR")
                return ie_Statement(id1, expr)

    def parse_program_2(self):
        """
        Parses a program which is a succession of assignments:
        Program	::=	MainClass ( ClassDeclaration )* <EOF>
        """
        main_class_node = self.parse_main_class()
        class_declarations = []

        if self.show_next() is not None:
            while self.show_next().tag == "CLASS":
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
        """Toutes les classes principales doivent s'appeler Main, cf Grammaire"""
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
        """Va parser les return des méthodes"""

        self.expect("RETURN")
        id1 = self.expect("IDENTIFIER")
        self.expect("TERMINATOR")
        return simple_expression(id1)

    def parse_class_declaration(self):
        """
        ClassDeclaration	::=	"class" "IDENTIFIER"(extends Identifier) "{" ( VarDeclaration )* ( MethodDeclaration )* "}"
        """
        parent_class_name = None
        self.expect("CLASS")
        class_name = self.expect("IDENTIFIER")

        if self.show_next().tag == "L_PAREN":
            self.expect("L_PAREN")
            self.expect("EXTENDS")
            parent_class_name = self.expect("IDENTIFIER")
            self.expect("R_PAREN")
        self.expect("L_CURL_BRACKET")

        class_node = Class(name=class_name, parent=parent_class_name)
        while self.show_next().tag != "public":
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

            """else:
                print("ERROR", self.show_next().tag)"""

        if self.show_next().tag == "public":
            method_declaration_node = self.parse_method_declaration()
            class_node.method_declarations.append(method_declaration_node)

        self.expect("R_CURL_BRACKET")

        return class_node

    def parse_method_declaration(self):
        """
        MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"
        """

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
                    "WHILE",
                    "KW_WHILE",
                    "KW_SYSTEM",
                    "KW_OUT",
                    "KW_PRINTLN",
                    "KW_READ",
                    "KW_LENGTH",
                    "KW_PARSEINT",
                ]:
                    method_node.statements.append(self.parse_statement())

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

        return Vardeclaration(type=var_type, identifier=var_name)
