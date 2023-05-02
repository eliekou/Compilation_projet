# -*- encoding: utf-8 -*-

import sys
from lex_er import Lexer
from p4_rser import Parser
from visiter import *

if __name__ == "__main__":
    lexer = Lexer()

    parser = Parser(lexer.lex_file(sys.argv[1]))

    test1 = PrettyPrinter()
    """test2 = Visitor()
    test2.visit_program(parser.parse())"""
    test1.visit_program(parser.parse())

    """test3 = SemanticAnalyser()
    test3.visit_program(parser.parse())"""

    """test4 = SemanticAnalyzer2()
    test4.visit_program(parser.parse())"""

    # print(test3)
