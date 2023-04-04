# -*- encoding: utf-8 -*-

import logging
from ast import Program
from ast import *
import ast

logger = logging.getLogger(__name__)
class1 =[]
classDeclaration =[]

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
            self.parse_program_2()
        except ParsingException as err:
            logger.exception(err)
            raise



        
        # Your code here!
        #self.expect("R_CURL_BRACKET")

    def parse_assignment(self):
       
        self.expect("SYSTEM")
        self.expect("PUNCTUATION")
        self.expect("OUT")
        self.expect("PUNCTUATION")
        self.expect("PRINTLN")
        #self.expect("PUNCTUATION")
        self.expect("L_PAREN")
        self.expect("GUILLEMET")
        while (self.show_next().tag != "GUILLEMET"):
            #program_node.ClassDeclaration.Vardeclaration .append.()
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
        #Prise en compte des statements
        #self.expect("TYPE_INT")
        """self.expect("TYPE_IDENTIFIER")
        self.expect("TYPE_IDENTIFIER")"""
       #self.expect("")
        if self.show_next().tag == "if":
                self.expect("if")
        if self.show_next().tag == "PRINTLN2":
            self.expect("PRINTLN2")
            self.expect("L_PAREN")
            self.expect("GUILLEMET")
            self.expect("IDENTIFIER")
            self.expect("GUILLEMET")
            self.expect("R_PAREN")
            self.expect("TERMINATOR")
            print("Le print est \n)",System_out_println("identifier"))
            return System_out_println("identifier")


    def parse_program(self):
        """
        Parses a program which is a succession of assignments:
        Program	::=	MainClass ( ClassDeclaration )* <EOF>
        """
        #BEGINNING OF parse_program
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
        
        program_node = Program(class1,classDeclaration)
        while (self.show_next().tag != "R_CURL_BRACKET"):

            if (self.show_next().tag in ["TYPE_INT","TYPE_CHAR","bool","TYPE_IDENTIFIER"]):
                program_node.ClassDeclaration.append(self.parse_statement())
                #parse_statement()
                print("there is a statement here")
            else:
                print("There is an assignment here")
                program_node.ClassDeclaration.append(self.parse_assignment())
                #self.parse_assignment()

                #program_node.ClassDeclaration.append(parse_assignment())
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

    def parse_program_2(self):

        main_class_node = self.parse_main_class()
        #self.parse_main_class()
        print(main_class_node)


    def parse_main_class(self):
        '''
        MainClass	::=	"class" "MainClass" "{" "public" "static" "void" "main" "(" "String" "[" "]" "args" ")" "{" Statement "}" "}"
        '''


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
        
        self.parse_statement()

        self.expect("R_CURL_BRACKET")
        self.expect("R_CURL_BRACKET")
        #return MainClass()

