# -*- encoding: utf-8 -*-

import sys
from lex_er import Lexer
from p4_rser import Parser
from visiter import *

if __name__ == "__main__":
    lexer = Lexer()

    parser = Parser(lexer.lex_file(sys.argv[1]))

    # Pretty Printer
    test1 = PrettyPrinter()
    test1.visit_program(parser.parse())

    # 1er analyseur sémantique
    test2 = SemanticAnalyzer()
    """test2.visit_program(parser.parse())"""

    # 2ème analyseur sémantique
    test3 = SemanticAnalyser2()
    """test3.visit_program(parser.parse())"""
