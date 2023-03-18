# -*- encoding: utf-8 -*-

import sys

from compiler.lexer import Lexer
from compiler.p4rser import Parser

if __name__ == "__main__":
    lexer = Lexer()
    print(lexer.lex_file(sys.argv[1]))
    parser = Parser(lexer.lex_file(sys.argv[1]))
    print(parser.parse())