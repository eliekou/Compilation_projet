# -*- encoding: utf-8 -*-

import sys
from lex_er import Lexer
from p4_rser import Parser

if __name__ == "__main__":
    lexer = Lexer()
    print(lexer.lex_file(sys.argv[1]))
    #parser = Parser(lexer.lex_file(sys.argv[1]))
    #print(parser.parse())
    #
    parser = Parser(lexer.lex_file(sys.argv[1]))
    print(parser.parse()) 
