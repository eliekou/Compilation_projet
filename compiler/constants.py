LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),
    (r"^true","TRUE"),
    (r'false','FALSE'),
    (r'boolean','BOOL'),
    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r'\;', 'TERMINATOR'),
    (r'\=', 'ASSIGN'),
    (r'\+', 'ADDITION'),
    (r'\-', 'SUBTRACTION'),
    (r'\*', 'MULTIPLICATION'),
    (r'\/', 'DIVISION'),
    (r'\[','CROCHET['),
    (r'\]','CROCHET]'),
    (r'\]','SEMI-COLON'),
    #LOGICAL OPERATIONS
    (r"\&&",'AND'),
    (r"\||",'OR'),
    (r"\!",'NO')
    #RELATIONNAL OPERATIONS
    (r'\>','SUPERIOR'),
     (r'\<','INFERIOR'),
    (r'\[>=]','SUPERIOR OR EQUAL'),
    (r'\[<=]','INFERIOR OR EQUAL'),
    # Keywords
    (r"int", "TYPE_INT"),
    (r"main", "KW_MAIN"),
    (r"\w+","IDENTIFIER"),
    (r"void","VOID_TYPE")
    #SPECIFIC TO A CLAS
    (r"class","CLASS"),
    (r"public","public"),
    (r"private","private"),
]