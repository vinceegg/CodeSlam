class Parser():
    expected_tokens = {
        # General expected tokens based solely on the current token type
        'Par': ['Aint'],
        # 'Aint': ['Maine'],
        ('Aint', 'Aint', 'Par'): ['Maine'], # Specific rule when the last reserved word is Par for Aint
        'Maine': ['('],
        # '(': [')'],
        ('(', 'Maine'): [')'], # Specific rule when the last reserved word is Maine for (
        # ')': ['{'],
        (')', 'Maine'): ['{'], # Specific rule when the last reserved word is Maine for )
        '{': ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Bounce'], # Maine and Flex
        # 'Bounce': ['AINTLITERAL'],
        ('Bounce', 'Maine'): ['AINTLITERAL'], # Specific rule when the for Bounce inside the Maine function to be updated with statements...
        # 'AINTLITERAL': [';'],
        ('AINTLITERAL', 'Bounce'): [';'], # Specific rule when the last reserved word is Bounce for AINTLITERAL

        # Context-specific expected tokens based on the current token and last reserved word
        # Bali yung mga possible terminals na expected based sa last token and reserved word
        # ('{', 'Maine'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Bounce'],  # Specific rule when the last reserved word is 'Maine'

        # Variable Declaration
        'Skrt': ['identifier'],
        'Aint': ['identifier'],
        'High': ['identifier'],
        'Echos': ['identifier'],
        # Variable Declaration to Variable Initialization
        ('identifier', 'Skrt'): [',', ';', '='],
        ('identifier', 'Aint'): [',', ';', '='],
        ('identifier', 'High'): [',', ';', '='],
        ('identifier', 'Echos'): [',', ';', '='],
        (';', 'Skrt'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],
        (';', 'Aint'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],
        (';', 'High'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],
        (';', 'Echos'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],

        # Declaration Tail to Initialization Tail
        ',': ['identifier'],
        ('identifier', 'Skrt', ','): [',', ';'],
        ('identifier', 'Aint', ','): [',', ';'],
        ('identifier', 'High', ','): [',', ';'],
        ('identifier', 'Echos', ','): [',', ';'],

        # Variable Initialization
        ('=', 'Skrt'): ['SKRTLITERAL'],
        ('=', 'Aint'): ['AINTLITERAL', 'NEALITERAL'],
        ('=', 'High'): ['HIGHLITERAL', 'NEHLITERAL'],
        ('=', 'Echos'): ['Nocap', 'Cap'],

        # identifier<array element>, <expr>, <skrt_concat>, <func_call>, <type_cast>, <esc_Sequence>
        
        # Variable Initialization to Initialize Tail
        ('SKRTLITERAL', 'Skrt'): [',', ';'],
        ('AINTLITERAL', 'Aint'): [',', ';'],
        ('NEALITERAL', 'Aint'): [',', ';'],
        ('HIGHLITERAL', 'High'): [',', ';'],
        ('NEHLITERAL', 'High'): [',', ';'],
        ('Nocap', 'Echos'): [',', ';'],
        ('Cap', 'Echos'): [',', ';'],
        (';', 'Cap'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],
        (';', 'Nocap'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],

        # Array Declaration
        'Array': ['Skrt', 'Aint', 'High', 'Echos'],
        ('identifier', 'Skrt', 'Array'): ['['],
        ('identifier', 'Aint', 'Array'): ['['],
        ('identifier', 'High', 'Array'): ['['],
        ('identifier', 'Echos', 'Array'): ['['],
        '[': ['identifier', 'AINTLITERAL'],
        ('identifier', 'Skrt', '['): [']'],
        ('identifier', 'Aint', '['): [']'],
        ('identifier', 'High', '['): [']'],
        ('identifier', 'Echos', '['): [']'],
        ('AINTLITERAL', 'Skrt', '['): [']'],
        ('AINTLITERAL', 'Aint', '['): [']'],
        ('AINTLITERAL', 'High', '['): [']'],
        ('AINTLITERAL', 'Echos', '['): [']'],
        ']': [';', '='],

        # Array Initialization
        ('=', 'Skrt', ']'): ['{'],
        ('=', 'Aint', ']'): ['{'],
        ('=', 'High', ']'): ['{'],
        ('=', 'Echos', ']'): ['{'],
        ('{', 'Skrt', '='): ['SKRTLITERAL'],
        ('{', 'Aint', '='): ['AINTLITERAL', 'NEALITERAL'],
        ('{', 'High', '='): ['HIGHLITERAL', 'NEHLITERAL'],
        ('{', 'Echos', '='): ['ECHOSLITERAL'],
        ('SKRTLITERAL', 'Skrt', '{'): [','],
        ('AINTLITERAL', 'Aint', '{'): [','],
        ('NEALITERAL', 'Aint', '{'): [','],
        ('HIGHLITERAL', 'High', '{'): [','],
        ('NEHLITERAL', 'High', '{'): [','],
        ('Cap', 'Echos', '{'): [','],
        ('Nocap', 'Echos', '{'): [','],
        (',', 'Skrt', 'SKRTLITERAL'): ['SKRTLITERAL'],
        (',', 'Aint', 'AINTLITERAL'): ['AINTLITERAL', 'NEALITERAL'],
        (',', 'Aint', 'NEALITERAL'): ['AINTLITERAL', 'NEALITERAL'],
        (',', 'High', 'HIGHLITERAL'): ['HIGHLITERAL', 'NEHLITERAL'],
        (',', 'High', 'HIGHLITERAL'): ['HIGHLITERAL', 'NEHLITERAL'],
        (',', 'Echos', 'Cap'): ['Cap', 'Nocap'],
        (',', 'Echos', 'Nocap'): ['Cap', 'Nocap'],
        ('SKRTLITERAL', 'Skrt', ','): [',', '}'],
        ('AINTLITERAL', 'Aint', ','): [',', '}'],
        ('NEALITERAL', 'Aint', ','): [',', '}'],
        ('HIGHLITERAL', 'High', ','): [',', '}'],
        ('NEHLITERAL', 'High', ','): [',', '}'],
        ('Cap', 'Echos', ','): [',', '}'],
        ('Nocap', 'Echos', ','): [',', '}'],
        ('}', 'Skrt'): [';'],
        ('}', 'Aint'): [';'],
        ('}', 'High'): [';'],
        ('}', 'Echos'): [';'],
        ('}', 'Cap'): [';'],
        ('}', 'Nocap'): [';'],

        # Function Definition
        'Flex': ['Skrt', 'Aint', 'High', 'Echos'],
        ('identifier', 'Skrt', 'Flex'): ['('],
        ('identifier', 'Aint', 'Flex'): ['('],
        ('identifier', 'High', 'Flex'): ['('],
        ('identifier', 'Echos', 'Flex'): ['('],
        '(': ['Skrt', 'Aint', 'High', 'Echos'],
        ('identifier', 'Skrt', 'Flex'): [',', ')'],
        ('identifier', 'Aint', 'Aint'): [',', ')'],
        ('identifier', 'High', 'High'): [',', ')'],
        ('identifier', 'Echos', 'Echos'): [',', ')'],
        (',', 'Skrt', 'identifier'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Aint', 'identifier'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'High', 'identifier'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Echos', 'identifier'): ['Skrt', 'Aint', 'High', 'Echos'],
        (')', 'Skrt'): ['{'],
        (')', 'Aint'): ['{'],
        (')', 'High'): ['{'],
        (')', 'Echos'): ['{'],
        ('identifier', 'Skrt', '{'): ['Skrt', 'Aint', 'High', 'Echos'],

        (';', 'Skrt', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos', 'Array'],
        

        # ('Bounce', 'Bounce'): ['SKRTLITERAL'],
        # ('Bounce', 'Aint'): ['AINTLITERAL', 'NEALITERAL'],
        # ('Bounce', 'High'): ['HIGHLITERAL', 'NEHLITERAL'],
        # ('Bounce', 'Echos'): ['Nocap', 'Cap'],
        ('SKRTLITERAL', 'Bounce'): [';'],
        ('NEALITERAL', 'Bounce'): [';'],
        ('HIGHLITERAL', 'Bounce'): [';'],
        ('NEHLITERAL', 'Bounce'): [';'],
        # ('Nocap', 'Bounce'): [';'],
        # ('Cap', 'Bounce'): [';'],
        ('}', 'Bounce'): ['Flex', 'Pavoid', 'Par']


    }

    def __init__(self, lexer):
        self.lexer = lexer
        self.pg = CFG(
            # A list of all token names accepted by the parser.
            ['space', '(', ')', '[', ']', '{', '}', ';', '!', ',', '.', '_',
             'tab', 'newline', '\\', 'n', 't', '"', 'identifier', 'comment', 'Aint', 'Skrt',
             'High', 'Echos', 'Tea', 'Spill', 'Whatif', 'Lesgo', 'Lemme', 'Forda',
             'Carps', 'Bruh', 'Gora', 'Bounce', 'Nocap', 'Cap', 'Par', 'Array', 'Flex', 'Maine', 'Pavoid',
             'SKRTLITERAL', 'AINTLITERAL', 'HIGHLITERAL', 'NEALITERAL', 'NEHLITERAL',
             '=', '+=', '-=', '*=', '/=', '%=', '+', '-', '*', '/', '%', '<', '>', '==',
             '!=', '<=', '>=', '&&', '??', '!!', '~']
        )
        
        self._add_productions()
        self.parser = self.pg.build()
    
    def parse(self, text):
        tokens = self.lexer.lex(text)
        try:
            self.parser.parse(tokens)
            print(f"No syntax error/s")
            return (f"No syntax error/s")
        except ValueError as e:
            print(f"Syntax error: {str(e)}")
            return (f"{str(e)}")

    def _add_productions(self):
       # CFG Production 1
        @self.pg.production('program : declarations functions Par Aint Maine ( ) { body Bounce AINTLITERAL ; }')
        def program(p):
            pass

    
        # CFG Production 2 - 3A
        @self.pg.production('declarations : declares declarations')
        @self.pg.production('declarations : ')
        def declarations(p):
            pass
                    
        # CFG Production 4 - 5
        @self.pg.production('declares : variable_decls')
        @self.pg.production('declares : array_decls')
        def declares(p):
            return p[0]

        # CFG Production 6 - 7
        @self.pg.production('functions : function_definition functions')
        @self.pg.production('functions : ')
        def functions(p):
            if p:
                pass
            else:
                return []
            
        @self.pg.production('body : declarations next_stmts')
        def body(p):
            pass

        @self.pg.production('voidbody : declarations void_stmts ')
        @self.pg.production('voidbody : declares void_next_stmts ')
        def voidbody(p):
            pass

        # CFG Production 8 - 11
        @self.pg.production('data_type : Skrt')
        @self.pg.production('data_type : Aint') 
        @self.pg.production('data_type : High')
        @self.pg.production('data_type : Echos')
        def data_type(p):
            pass

        # CFG Production 12 - 13
        @self.pg.production('variable_decls : variable_decl')
        @self.pg.production('variable_decls : variable_initialization')
        def variable_decls(p):
            pass

        # CFG Production 14
        @self.pg.production('variable_decl : data_type identifier decl_tail ;')
        def variable_decl(p):
            pass

        # CFG Production 15 - 16
        @self.pg.production('decl_tail : , identifier decl_tail')
        @self.pg.production('decl_tail : ')
        def decl_tail(p):
            pass

        # CFG Production 17
        @self.pg.production('variable_initialization : data_type identifier = value initialize_tail ;')
        def variable_initialization(p):
            pass

        # CFG Production 18 - 19
        @self.pg.production('initialize_tail : , identifier = value initialize_tail')
        @self.pg.production('initialize_tail : ')
        def initialize_tail(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 20 - 21
        @self.pg.production('array_decls : array_decl')
        @self.pg.production('array_decls : array_initialization')
        def array_decls(p):
            pass

        # CFG Production 22
        @self.pg.production('array_decl : Array data_type identifier [ array_index ] ;')
        def array_decl(p):
            pass

        # CFG Production 23
        @self.pg.production('array_initialization : Array data_type identifier [ array_index ] = { elem , elem  elems } ;')
        def array_initialization(p):
            pass

        # CFG Production 24 - 25
        @self.pg.production('elems : , elem elems')
        @self.pg.production('elems : ')
        def elems(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 26
        @self.pg.production('elem : literal')
        def elem(p):
            pass

        # CFG Production 27 - 28
        @self.pg.production('array_element : [ array_index ]')
        @self.pg.production('array_element : ')
        def array_element(p):
            pass

        # CFG Production 29 - 30
        @self.pg.production('array_index : AINTLITERAL')
        @self.pg.production('array_index : identifier')
        def array_index(p):
            pass

        # CFG Production 31 - 32
        @self.pg.production('parameters : param parameters_tail')
        @self.pg.production('parameters : ')
        def parameters(p):
            if p:
                pass
            else:
                return []

        # CFG Production 33 - 34
        @self.pg.production('parameters_tail : , param parameters_tail')
        @self.pg.production('parameters_tail : ')
        def parameters_tail(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 35
        @self.pg.production('param : data_type identifier')
        def param(p):
            pass

        # CFG Production 36 - 37
        @self.pg.production('function_definition : Flex data_type identifier ( parameters ) { body Bounce value ;  }')
        @self.pg.production('function_definition : Pavoid identifier ( parameters ) { voidbody }')
        def function_definition(p):
            pass

        # # CFG Production 38 - 39
        @self.pg.production('bounce_stmt : Bounce value ;')
        @self.pg.production('bounce_stmt : ')
        def bounce_stmt(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 40 - 41
        @self.pg.production('maine_stmts : stmt next_stmts')
        @self.pg.production('maine_stmts : whatif_stmt next_stmts')
        def maine_stmts(p):
            pass

        # CFG Production 42 - 43
        @self.pg.production('next_stmts : maine_stmts next_stmts')
        @self.pg.production('next_stmts : ')
        def next_stmts(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 44 - 49
        @self.pg.production('stmt : tea_stmt ;')
        @self.pg.production('stmt : spill_stmt ;')
        @self.pg.production('stmt : forda_stmt')
        @self.pg.production('stmt : carps_stmt')
        @self.pg.production('stmt : assignment_stmt')
        @self.pg.production('stmt : func_call ;')
        def stmt(p):
            pass

        # CFG Production 50 - 52
        @self.pg.production('assignment_stmt : identifier array_element ass_op value ;')
        def assignment_stmt(p):
            pass

        # CFG Production 53
        @self.pg.production('tea_stmt : Tea ( input )')
        def tea_stmt(p):
            pass

        # CFG Production 54
        @self.pg.production('input : identifier array_element')
        def input(p):
            pass
        

        # CFG Production 55
        @self.pg.production('spill_stmt : Spill ( outputs )')
        def spill_stmts(p):
            pass
        
        # CFG Production 56
        @self.pg.production('outputs : output output_tail')
        def outputs(p):
            pass

        # CFG Production 57 - 58
        @self.pg.production('output_tail : ~ outputs')
        @self.pg.production('output_tail : ')
        def output_tail(p):
            pass
        
        # CFG Production 59
        @self.pg.production('output : value')
        def output(p):
            pass
        
        # CFG Production 60
        @self.pg.production('skrt_concat : skrt_operand skrt_concat_tail')
        @self.pg.production('skrt_concat : value skrt_concat_tail1')
        def skrt_concat(p):
            pass

        # CFG Production 61 - 64
        @self.pg.production('skrt_operand : SKRTLITERAL')
        @self.pg.production('skrt_operand : identifier array_element')
        @self.pg.production('skrt_operand : func_call')
        @self.pg.production('skrt_operand : Skrt ( skrt_tc )')
        def skrt_operand(p):
            pass

        # CFG Production 65 - 67
        @self.pg.production('skrt_tc : literal')
        @self.pg.production('skrt_tc : identifier array_element')
        @self.pg.production('skrt_tc : expr')
        def skrt_tc(p):
            pass

        # CFG Production 68 - 69
        @self.pg.production('skrt_concat_tail : ~ value concat_tail')
        def skrt_concat_tail(p):
            pass
            
        @self.pg.production('skrt_concat_tail1 : ~ skrt_operand concat_tail')
        def skrt_tail(p):
            pass
            
        # CFG Production 70 - 71
        @self.pg.production('concat_tail : skrt_concat_tail')
        @self.pg.production('concat_tail : ')
        def concat_tail(p):
            if p:
                pass
            else:
                return []
            

        # CFG Production 74 - 80
        @self.pg.production('value : identifier array_element')
        @self.pg.production('value : literal')
        @self.pg.production('value : expr')
        @self.pg.production('value : skrt_concat')
        @self.pg.production('value : func_call')
        @self.pg.production('value : type_cast')
        @self.pg.production('value : esc_sequence')
        def value(p):
            pass

        # CFG Production 81
        @self.pg.production('esc_sequence : " \\ esc_char "')
        def esc_sequence(p):
            pass

        # CFG Production 82 -  85
        @self.pg.production('esc_char : n')
        @self.pg.production('esc_char : t')
        @self.pg.production('esc_char : \\')
        @self.pg.production('esc_char : "')
        def esc_char(p):
            pass

        # CFG Production 86 - 91
        @self.pg.production('literal : AINTLITERAL')
        @self.pg.production('literal : ECHOSLITERAL')
        @self.pg.production('literal : NEALITERAL')
        @self.pg.production('literal : NEHLITERAL')
        @self.pg.production('literal : HIGHLITERAL')
        @self.pg.production('literal : SKRTLITERAL')
        def literal(p):
            pass
        
        # CFG Production 92
        @self.pg.production('type_cast : data_type ( type_cast1 )')
        def type_cast(p):
            pass

        # CFG Production 93 - 94
        @self.pg.production('type_cast1 : literal')
        @self.pg.production('type_cast1 : identifier array_element')
        def type_cast1(p):
            pass

        # CFG Production 95 - 100
        @self.pg.production('ass_op : =')
        @self.pg.production('ass_op : +=')
        @self.pg.production('ass_op : -=')
        @self.pg.production('ass_op : *=')
        @self.pg.production('ass_op : %=')
        @self.pg.production('ass_op : /=')
        def ass_op(p):
            pass

        # CFG Production 101 - 105
        @self.pg.production('arith_op : +')
        @self.pg.production('arith_op : -')
        @self.pg.production('arith_op : *')
        @self.pg.production('arith_op : /')
        @self.pg.production('arith_op : %')
        def arith_op(p):
            return p[0].getstr()

        # CFG Production 106 - 110
        @self.pg.production('rel_op : <')
        @self.pg.production('rel_op : >')
        @self.pg.production('rel_op : <=')
        @self.pg.production('rel_op : >=')
        @self.pg.production('rel_op : rel_equality')
        def rel_op(p):
            print("REL_OP: ", p)
            pass

        # CFG Production 111 - 112
        @self.pg.production('rel_equality : ==')
        @self.pg.production('rel_equality : !=')
        def rel_equality(p):
            print("REL_EQUALITY: ", p)
            pass

        # CFG Production 113 - 114
        @self.pg.production('not_op : !! not_op')
        @self.pg.production('not_op : ')
        def not_op(p):
            print("NOT_OP: ", p)
            if p:
                pass
            else:
                return []
            
        # CFG Production 115 - 116
        @self.pg.production('log_op : &&')
        @self.pg.production('log_op : ??')
        def log_op(p):
            print("LOG_OP: ", p)
            pass



        # CFG Production 117 - 119
        @self.pg.production('expr : arith_expr')
        @self.pg.production('expr : log_expr')
        @self.pg.production('expr : rel_expr')
        def expr(p):
            print("EXPR: ", p)
            return p[0]

        # CFG Production 120
        @self.pg.production('arith_expr : term arithexpr_tail')
        def arith_expr(p):
            print("ARITH_EXPR: ", p)
            # if p[1] == '':  # If the tail is empty
            #     return p[0]
            # else:
            #     result = p[0]
            #     for operator, term in p[1]:
            #         result = BinaryOperationNode(left=result, operator=operator, right=term)
            #     return result
            pass

        # CFG Production 121 - 122
        @self.pg.production('arithexpr_tail : arith_op term arithexpr_tail')
        @self.pg.production('arithexpr_tail : ')
        def arithexpr_tail(p):
            pass
            
        # CFG Production 123 - 127
        @self.pg.production('term : identifier array_element')
        @self.pg.production('term : num_literal')
        @self.pg.production('term : type_cast')
        @self.pg.production('term : func_call')
        @self.pg.production('term : ( arith_expr )')
        def term(p):
            pass


        # CFG Production 128 - 131
        @self.pg.production('num_literal : AINTLITERAL')
        @self.pg.production('num_literal : HIGHLITERAL')
        @self.pg.production('num_literal : NEALITERAL')
        @self.pg.production('num_literal : NEHLITERAL')
        def num_literal(p):
            pass


        # CFG Production 132 - 134
        @self.pg.production('rel_expr : rel_operand rel_op rel_operand rel_tail')
        @self.pg.production('rel_expr : rel_operand_eq rel_equality rel_operand rel_tail_eq')
        @self.pg.production('rel_expr : rel_operand_eq rel_equality rel_operand_eq rel_tail_eq')
        def rel_expr(p):
            pass

        # CFG Production 135 - 136
        @self.pg.production('rel_tail : rel_op rel_operand rel_tail')
        @self.pg.production('rel_tail : ')
        def rel_tail(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 137 -142
        @self.pg.production('rel_operand : arith_expr')
        @self.pg.production('rel_operand : identifier array_element')
        @self.pg.production('rel_operand : func_call')
        @self.pg.production('rel_operand : type_cast')
        @self.pg.production('rel_operand : num_literal')
        @self.pg.production('rel_operand : ( rel_expr )')
        def rel_operand(p):
            pass

        # CFG Production 143 - 147
        @self.pg.production('rel_operand_eq : SKRTLITERAL')
        @self.pg.production('rel_operand_eq : ECHOSLITERAL')
        @self.pg.production('rel_operand_eq : identifier array_element')
        @self.pg.production('rel_operand_eq : log_expr')
        @self.pg.production('rel_operand_eq : ( rel_expr )')
        def rel_operand_eq(p):
            pass        

        # CFG Production 148 - 149
        @self.pg.production('rel_tail_eq : rel_equality rel_operand_eq rel_tail_eq')
        @self.pg.production('rel_tail_eq : ')
        def rel_tail_eq(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 150 - 151
        @self.pg.production('log_expr : not_op log_operand log_tail')
        @self.pg.production('log_expr : log_operand log_tail')
        def log_expr(p):
            pass

        # CFG Production 152 - 153
        @self.pg.production('log_tail : log_op not_op log_operand log_tail')
        @self.pg.production('log_tail : ')
        def log_tail(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 154- 158
        @self.pg.production('log_operand : identifier array_element')
        @self.pg.production('log_operand : ECHOSLITERAL')
        @self.pg.production('log_operand : func_call')
        @self.pg.production('log_operand : type_cast')
        @self.pg.production('log_operand : ( log_expr )')
        @self.pg.production('log_operand : rel_expr')
        @self.pg.production('log_operand : ( rel_expr )')
        def log_operand(p):
            pass
        

        # CFG Production 159
        @self.pg.production('whatif_stmt : Whatif ( condition ) { maine_stmts bounce_stmt } mul_lemme lesgo_part')
        def whatif_stmt(p):
            pass

        # CFG Production 160 - 161
        @self.pg.production('mul_lemme : lemme_part mul_lemme')
        @self.pg.production('mul_lemme : ')
        def mul_lemme(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 162
        @self.pg.production('lemme_part : Lemme ( condition ) { maine_stmts bounce_stmt }')
        def lemme_part(p):
            pass

        # CFG Production 163 - 164
        @self.pg.production('lesgo_part : Lesgo { maine_stmts bounce_stmt }')
        @self.pg.production('lesgo_part : ')
        def lesgo_part(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 165 - 166
        @self.pg.production('condition : rel_expr')
        @self.pg.production('condition : log_expr')
        @self.pg.production('condition : func_call')
        def condition(p):
            pass

        # CFG Production 167
        @self.pg.production('forda_stmt : Forda ( forda_initialization ; forda_condition ; forda_updates ) { loop_stmts next_loopstmts bounce_stmt }')
        def forda_stmt(p):
            pass

        # CFG Production 168
        @self.pg.production('forda_initialization : numdata_type identifier = intial_operand')
        def forda_initialization(p):
            pass

        # CFG Production 169 - 170
        @self.pg.production('numdata_type : Aint')
        @self.pg.production('numdata_type : High')
        def numdata_type(p):
            pass

        # CFG Production 171 - 172
        @self.pg.production('intial_operand : num_literal')
        @self.pg.production('intial_operand : arith_expr')
        def intial_operand(p):
            pass

        # CFG Production 173
        @self.pg.production('forda_condition : forda_operand forda_op forda_operand')
        def forda_condition(p):
            pass

        # CFG Production 174 - 176
        @self.pg.production('forda_operand : identifier')
        @self.pg.production('forda_operand : arith_expr')
        @self.pg.production('forda_operand : num_literal')
        def forda_operand(p):
            pass

        # CFG Production 177
        @self.pg.production('forda_op : rel_op')
        def forda_op(p):
            pass

        # CFG Production 178
        @self.pg.production('forda_updates : identifier forda_unop num_literal')
        def forda_updates(p):
            pass

        # CFG Production 179 - 180
        @self.pg.production('forda_unop : +=')
        @self.pg.production('forda_unop : -=')
        def forda_unop(p):
            pass

        # CFG Production 181 - 185
        @self.pg.production('loop_stmts : stmt')
        @self.pg.production('loop_stmts : loop_whatif')
        @self.pg.production('loop_stmts : Bruh ;')
        @self.pg.production('loop_stmts : Gora ;')
        @self.pg.production('loop_stmts : Bounce value ;')
        def loop_stmts(p):
            pass

        # CFG Production 186
        @self.pg.production('loop_whatif : Whatif ( condition ) { loop_stmts next_loopstmts } loop_lemmes loop_lesgo')
        def loop_whatif(p):
            pass

        # CFG Production 187 - 188
        @self.pg.production('loop_lemmes : loop_lemme loop_lemmes')
        @self.pg.production('loop_lemmes : ')
        def loop_lemmes(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 189
        @self.pg.production('loop_lemme : Lemme ( condition ) { loop_stmts next_loopstmts }')
        def loop_lemme(p):
            pass

        # CFG Production 190 - 191
        @self.pg.production('loop_lesgo : Lesgo { loop_stmts next_loopstmts }')
        @self.pg.production('loop_lesgo : ')
        def loop_lesgo(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 192 - 193
        @self.pg.production('next_loopstmts : loop_stmts next_loopstmts')
        @self.pg.production('next_loopstmts : ')
        def next_loopstmts(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 194
        @self.pg.production('carps_stmt : Carps ( condition ) { loop_stmts next_loopstmts }')
        def carps_stmt(p):
            pass
            
        # CFG Production 195
        @self.pg.production('func_call : identifier ( arguments )')
        def func_call(p):
            pass

        # CFG Production 196 - 197
        @self.pg.production('arguments : arg arguments_tail')
        @self.pg.production('arguments : ')
        def arguments(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 198 - 199
        @self.pg.production('arguments_tail : , arg arguments_tail')
        @self.pg.production('arguments_tail : ')
        def arguments_tail(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 200 -202
        @self.pg.production('arg : identifier array_element')
        @self.pg.production('arg : literal')
        @self.pg.production('arg : type_cast')
        def arg(p):
            pass

        # CFG Production 203 - 204
        @self.pg.production('void_stmts : void_stmt void_next_stmts')
        @self.pg.production('void_stmts : void_whatif_stmt void_next_stmts')
        def void_stmts(p):
            pass

        # CFG Production 205 - 206
        @self.pg.production('void_next_stmts : void_stmts void_next_stmts')
        @self.pg.production('void_next_stmts : ')
        def void_next_stmts(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 207 - 211
        @self.pg.production('void_stmt : tea_stmt ;')
        @self.pg.production('void_stmt : spill_stmt ;')
        @self.pg.production('void_stmt : void_forda_stmt')
        @self.pg.production('void_stmt : void_carps_stmt')
        @self.pg.production('void_stmt : assignment_stmt')
        def void_stmt(p):
            pass

        # CFG Production 212
        @self.pg.production('void_whatif_stmt : Whatif ( condition ) { void_stmts } void_mul_lemme void_lesgo')
        def void_whatif_stmt(p):
            pass

        # CFG Production 213 - 214
        @self.pg.production('void_mul_lemme : void_lemme void_mul_lemme')
        @self.pg.production('void_mul_lemme : ')
        def void_mul_lemme(p):
            if p:
                pass
            else:
                return []

        # CFG Production 215
        @self.pg.production('void_lemme : Lemme ( condition ) { void_stmts }')
        def void_lemme(p):
            pass

        # CFG Production 216 - 217
        @self.pg.production('void_lesgo : Lesgo { void_stmts }')
        @self.pg.production('void_lesgo : ')
        def void_lesgo(p):
            if p:
                pass
            else:
                return []

        # CFG Production 218
        @self.pg.production('void_forda_stmt : Forda ( forda_initialization ; forda_condition ; forda_updates ) { void_loop_stmts }')
        def void_forda_stmt(p):
            pass

        # CFG Production 219 - 222
        @self.pg.production('void_loop_stmts : void_stmt void_next_loop_stmts')
        @self.pg.production('void_loop_stmts : void_loop_whatif void_next_loop_stmts')
        @self.pg.production('void_loop_stmts : Bruh ;')
        @self.pg.production('void_loop_stmts : Gora ;')
        def void_loop_stmts(p):
            pass

        # CFG Production 223 - 224
        @self.pg.production('void_next_loop_stmts : void_loop_stmts void_next_loop_stmts')
        @self.pg.production('void_next_loop_stmts : ')
        def void_next_loop_stmts(p):
            if p:
                pass
            else:
                return []

        # CFG Production 225
        @self.pg.production('void_loop_whatif : Whatif ( condition ) { void_loop_stmts } void_loop_lemmes void_loop_lesgo')
        def void_loop_whatif(p):
            pass

        # CFG Production 226 - 227
        @self.pg.production('void_loop_lemmes : void_loop_lemme void_loop_lemmes')
        @self.pg.production('void_loop_lemmes : ')
        def void_loop_lemmes(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 228
        @self.pg.production('void_loop_lemme : Lemme ( condition ) { void_loop_stmts }')
        def void_loop_lemme(p):
            pass

        # CFG Production 229 - 230
        @self.pg.production('void_loop_lesgo : Lesgo { void_loop_stmts }')
        @self.pg.production('void_loop_lesgo : ')
        def void_loop_lesgo(p):
            if p:
                pass
            else:
                return []
            
        # CFG Production 231
        @self.pg.production('void_carps_stmt : Carps ( condition ) { void_loop_stmts }')
        def void_carps_stmt(p):
            pass
            

        # FOR ECHOSLITERAL
        @self.pg.production('ECHOSLITERAL : Nocap')
        @self.pg.production('ECHOSLITERAL : Cap')
        def ECHOSLITERAL(p):
            pass
        
        @self.pg.error
        def error_handle(token):
            # Use lexer to access the previous token in case of an error
            function = self.lexer.get_function()
            last_reserved_word = self.lexer.get_last_reserved_keyword()
            previous_token = self.lexer.get_previous_token()
            seclast_reserved_keyword = self.lexer.get_seclast_reserved_keyword() # second to the last reserved keyword
            secprev_token = self.lexer.get_secprevious_token() # second to the previous token

            if token.gettokentype() == '$end':
                raise ValueError("Syntax error: Unexpected end of input\n")
            else:            
                expected = list_expected_tokens(previous_token, last_reserved_word, seclast_reserved_keyword, secprev_token, function)

                error_message = f"Function: {function.getstr()}\n2nd prev Token: {secprev_token.getstr()}\nPrev Token: {previous_token.getstr()}\nLast RW: {last_reserved_word.getstr()}\n2nd prev RW: {seclast_reserved_keyword.getstr()}\nUnexpected token: {[token.getstr()]} at line number {token.getsourcepos().lineno}\nExpected Token\s: {expected}\n"
                
                # error_message = f"Unexpected token: {[token.getstr()]} at line number {token.getsourcepos().lineno}\nExpected Token\s: {expected}\n"
                raise ValueError(error_message)
        
        def list_expected_tokens(token, last_reserved_word, seclast_reserved_word, secprev_token, function):
            token_type = token.gettokentype() if token else None
            last_reserved_word = last_reserved_word.gettokentype() if last_reserved_word else None
            seclast_reserved_word = seclast_reserved_word.gettokentype() if seclast_reserved_word else None
            secprev_token = secprev_token.gettokentype() if secprev_token else None
            function = function.gettokentype() if function else None

            # Context Keys
            full_context = (token_type, last_reserved_word, secprev_token, seclast_reserved_word, function)
            four_context = (token_type, last_reserved_word, secprev_token, seclast_reserved_word)
            three_context = (token_type, last_reserved_word, secprev_token)
            three_context_function = (token_type, last_reserved_word, function)
            three_context_alt = (token_type, last_reserved_word, seclast_reserved_word)
            two_context = (token_type, last_reserved_word)

            # context_key = (token_type, last_reserved_word.gettokentype()) if last_reserved_word else token_type

            # Fetch expected tokens based on the token type or the context-specific key
            # return self.expected_tokens.get(context_key, self.expected_tokens.get(token_type, ['unknown']))

            return self.expected_tokens.get(
                full_context,
                self.expected_tokens.get(
                    four_context,
                    self.expected_tokens.get(
                        three_context,
                        self.expected_tokens.get(
                                three_context_function,
                                self.expected_tokens.get(
                                    three_context_alt,
                                    self.expected_tokens.get(
                                        two_context,
                                        self.expected_tokens.get(
                                            token_type,
                                            ['unkown'],
                                    )
                                )
                            )
                        )    
                    )
                )
            )

            
# from lexical_analyzer import tokens
from rply import ParserGenerator as CFG