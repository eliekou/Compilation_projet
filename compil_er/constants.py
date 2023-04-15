LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+",  None),
    (r"^true","TRUE"),
    (r'false','FALSE'),
    (r'boolean','BOOL'),
    (r'System.out.println','PRINTLN2'),
    (r'System','SYSTEM'),
    (r'out','OUT'),
    (r'println','PRINTLN'),
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
    (r'\"','GUILLEMET'),
    (r"return",'RETURN'),
    #STATEMENT
    (r"if",'IF'),
    (r"else",'ELSE'),
    (r"while",'WHILE'),
    #PUNCTUATIONS
    (r'\.','PUNCTUATION'), 
    #LOGICAL OPERATIONS
    (r"\|",'OR'),
    #(r"\!",'NO')
    #RELATIONNAL OPERATIONS
    (r'\>','SUPERIOR'),
    (r'\<','INFERIOR'),
    (r'\[>=]','SUPERIOR OR EQUAL'),
    (r'\[<=]','INFERIOR OR EQUAL'),
    # Keywords
    (r"int", "TYPE_INT"),
    
    (r"args", "KW_ARGS"),
    #SPECIFIC TO A CLASS
    (r"main_class","MAIN_CLASS"),
    (r"main", "KW_MAIN"),
    (r"class","CLASS"),
    (r"static","static"),
    (r"public","public"),
    (r"String","String"),
    (r"private","private"),
    (r"void","VOID_TYPE"),
    (r"\d+", "INTEGER"),
    (r"\w+","IDENTIFIER"),
    
    #(r'[a-z]\w*', 'IDENTIFIER'),
    
]