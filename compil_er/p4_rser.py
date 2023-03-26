# -*- encoding: utf-8 -*-

import logging
from ast import Program

logger = logging.getLogger(__name__)


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
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        print(tag)
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
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
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
        
        program_node = Program()
        while (self.show_next().tag != "R_CURL_BRACKET"):

            if (self.show_next().tag in ["TYPE_INT","TYPE_CHAR","bool","TYPE_IDENTIFIER"]):
                program_node.ClassDeclaration.append(parse_statement())
            else:
                self.parse_assignment()
                program_node.ClassDeclaration.append(parse_assignments())
        # self.expect("IDENTIFIER")
        self.expect("R_CURL_BRACKET")


        
        # Your code here!
        #self.expect("R_CURL_BRACKET")

    def parse_assignment(self):
        """self.expect("IDENTIFIER")
        self.expect("L_PARENT")
        self.expect("L_CURL_BRACKET")
        self.expect("R_CURL_BRACKET")
        self.expect("R_PARENT")
"""
        """
        identifier ('[' expression ']')? '=' expression ';' """
        self.expect("SYSTEM")
        self.expect("PUNCTUATION")
        self.expect("OUT")
        self.expect("PUNCTUATION")
        self.expect("PRINTLN")
        #self.expect("PUNCTUATION")
        self.expect("L_PAREN")
        self.expect("GUILLEMET")
        while (self.show_next().tag != "GUILLEMET"):

            self.expect("IDENTIFIER")
        self.expect("GUILLEMET")
        self.expect("R_PAREN")
        """if self.show_next().tag == "L_SQ_BRACKET":
                self.expect("L_SQ_BRACKET")
                self.parse_expression()
                self.expect("R_SQ_BRACKET")"""
        #self.expect("ASSIGN")
        #self.parse_expression()
        self.expect("TERMINATOR")
        

    def parse_Vardeclaration(self):

        self.expect("TYPE_INT")
        self.expect("TYPE_IDENTIFIER")
        self.expect("ASSIGN")
        self.expect("INTEGER")
        #while(self.show_next == "ASSIGN")
        ...

    ...
    def parse_statement(self):
        self.expect("TYPE_INT")
        self.expect("TYPE_IDENTIFIER")
        self.expect("TYPE_IDENTIFIER")