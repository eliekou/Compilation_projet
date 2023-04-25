# -*- encoding: utf-8 -*-

import sys
from lex_er import Lexer
from p4_rser import Parser
from visiter import *

if __name__ == "__main__":
    lexer = Lexer()

    parser = Parser(lexer.lex_file(sys.argv[1]))

    test1 = PrettyPrinter()
    test1.visit_program(parser.parse())
