from rply import ParserGenerator
from syntax_analyzer.conversion import conversion_dict
# from ast_1 import *
# Remove " . " from ast_1 kapag sa main.py magrun 
# from ast_1 import *


class Parser:

    expected_tokens = {
        None: ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Flex', 'Pavoid', 'Par'],
        # General expected tokens based solely on the current token type
        'Par': ['Aint'],
        # 'Aint': ['Maine'],
        ('Aint', 'Aint', 'Par'): ['Maine'], # Specific rule when the last reserved word is Par for Aint
        'Maine': ['('],
        # '(': [')'],
        ('(', 'Maine'): [')'], # Specific rule when the last reserved word is Maine for (
        # ')': ['{'],
        (')', 'Maine'): ['{'], # Specific rule when the last reserved word is Maine for )
        '{': ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'], # Maine and Flex
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

        # Declaration Tail
        ',': ['identifier'],
        ('identifier', 'Skrt', ',', 'identifier'): [',', ';'],
        ('identifier', 'Aint', ',', 'identifier'): [',', ';'],
        ('identifier', 'High', ',', 'identifier'): [',', ';'],
        ('identifier', 'Echos', ',', 'identifier'): [',', ';'],

        # Variable Initialization
        ('=', 'Skrt'): ['SKRTLITERAL'],
        ('=', 'Aint'): ['AINTLITERAL', 'NEALITERAL'],
        ('=', 'High'): ['HIGHLITERAL', 'NEHLITERAL'],
        ('=', 'Echos'): ['Nocap', 'Cap'],
        ('=', 'Nocap'): ['Nocap', 'Cap'],
        ('=', 'Cap'): ['Nocap', 'Cap'],
        ('identifier', 'Skrt', ','): ['='],
        ('identifier', 'Aint', ','): ['='],
        ('identifier', 'High', ','): ['='],
        ('identifier', 'Cap', ','): ['='],
        ('identifier', 'Nocap', ','): ['='],
        (',', 'Skrt', 'SKRTLITERAL', '='): ['identifier'],
        (',', 'Aint', 'AINTLITERAL', '='): ['identifier'],
        (',', 'Aint', 'NEALITERAL', '='): ['identifier'],
        (',', 'High', 'HIGHLITERAL', '='): ['identifier'],
        (',', 'High', 'HIGHLITERAL', '='): ['identifier'],
        (',', 'Echos', 'Cap', '='): ['identifier'],
        (',', 'Echos', 'Nocap', '='): ['identifier'],
        
        # identifier<array element>, <expr>, <skrt_concat>, <func_call>, <type_cast>, <esc_Sequence>
        
        # Variable Initialization to Initialize Tail
        ('SKRTLITERAL', 'Skrt'): [',', ';'],
        ('AINTLITERAL', 'Aint'): [',', ';'],
        ('NEALITERAL', 'Aint'): [',', ';'],
        ('HIGHLITERAL', 'High'): [',', ';'],
        ('NEHLITERAL', 'High'): [',', ';'],
        ('Nocap', 'Nocap'): [',', ';'],
        ('Cap', 'Cap'): [',', ';'],
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
        ('Cap', 'Cap', '{'): [','],
        ('Nocap', 'Nocap', '{'): [','],
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
        ('Cap', 'Cap', ','): [',', '}'],
        ('Nocap', 'Nocap', ','): [',', '}'],
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
        ('identifier', 'Skrt', 'Skrt', 'Flex'): [',', ')'],
        ('identifier', 'Aint', 'Aint', 'Flex'): [',', ')'],
        ('identifier', 'High', 'High', 'Flex'): [',', ')'],
        ('identifier', 'Echos', 'Echos', 'Flex'): [',', ')'],
        (',', 'Skrt', 'identifier', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Aint', 'identifier', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'High', 'identifier', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Echos', 'identifier', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos'],
        (')', 'Skrt'): ['{'],
        (')', 'Aint'): ['{'],
        (')', 'High'): ['{'],
        (')', 'Echos'): ['{'],
        ('identifier', 'Skrt', 'Skrt', 'Skrt', 'Flex'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'Aint', 'Flex'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'High', 'Flex'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'Echos', 'Flex'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Skrt', 'Flex'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Aint', 'Flex'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'High', 'Flex'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Echos', 'Flex'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Skrt', 'Flex'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Aint', 'Flex'): [',', ';', '='],
        ('identifier', 'High', 'High', 'High', 'Flex'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Echos', 'Flex'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Skrt', 'Flex'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Aint', 'Flex'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'High', 'Flex'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Echos', 'Flex'): [',', ';', '='],
        (',', 'Skrt', 'identifier', 'Skrt', 'Flex'): ['identifier'],
        (',', 'Skrt', 'identifier', 'Aint', 'Flex'): ['identifier'],
        (',', 'Skrt', 'identifier', 'High', 'Flex'): ['identifier'],
        (',', 'Skrt', 'identifier', 'Echos', 'Flex'): ['identifier'],
        (',', 'Aint', 'identifier', 'Skrt', 'Flex'): ['identifier'],
        (',', 'Aint', 'identifier', 'Aint', 'Flex'): ['identifier'],
        (',', 'Aint', 'identifier', 'High', 'Flex'): ['identifier'],
        (',', 'Aint', 'identifier', 'Echos', 'Flex'): ['identifier'],
        (',', 'High', 'identifier', 'Skrt', 'Flex'): ['identifier'],
        (',', 'High', 'identifier', 'Aint', 'Flex'): ['identifier'],
        (',', 'High', 'identifier', 'High', 'Flex'): ['identifier'],
        (',', 'High', 'identifier', 'Echos', 'Flex'): ['identifier'],
        (',', 'Echos', 'identifier', 'Skrt', 'Flex'): ['identifier'],
        (',', 'Echos', 'identifier', 'Aint', 'Flex'): ['identifier'],
        (',', 'Echos', 'identifier', 'High', 'Flex'): ['identifier'],
        (',', 'Echos', 'identifier', 'Echos', 'Flex'): ['identifier'],
        ('identifier', 'Skrt', 'Skrt', 'Array'): ['['],
        ('identifier', 'Aint', 'Aint', 'Array'): ['['],
        ('identifier', 'High', 'High', 'Array'): ['['],
        ('identifier', 'Echos', 'Echos', 'Array'): ['['],
        (';', 'Skrt', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce', '}'],
        (';', 'Aint', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce', '}'],
        (';', 'High', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce', '}'],
        (';', 'Echos', 'Flex'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce', '}'],
        ('Bounce', 'Bounce'): ['SKRTLITERAL', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL', 'Cap', 'Nocap', 'identifier'],
        # Bounce [expr, skrt_concat, func_call, type_cast, esc_sequence]
        
        ('SKRTLITERAL', 'Bounce'): [';'],
        ('NEALITERAL', 'Bounce'): [';'],
        ('HIGHLITERAL', 'Bounce'): [';'],
        ('NEHLITERAL', 'Bounce'): [';'],
        ('Nocap', 'Nocap', 'Bounce'): [';'],
        ('Cap', 'Cap', 'Bounce'): [';'],
        (';', 'Bounce'): ['}'],
        (';', 'Nocap', 'Flex'): ['}'],
        (';', 'Cap', 'Flex'): ['}'],
        ('}', 'Bounce'): ['Flex', 'Pavoid', 'Par'],

        # Pavoid Function
        'Pavoid': ['identifier'],
        ('identifier', 'Pavoid'): ['('],
        ('identifier', 'Skrt', 'Pavoid'): [',', ')'],
        ('identifier', 'Aint', 'Pavoid'): [',', ')'],
        ('identifier', 'High', 'Pavoid'): [',', ')'],
        ('identifier', 'Echos', 'Pavoid'): [',', ')'],
        (',', 'Skrt', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Aint', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'High', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos'],
        (',', 'Echos', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos'],
        ('{', 'Skrt', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier'],
        ('{', 'Aint', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier'],
        ('{', 'High', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier'],
        ('{', 'Echos', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier'],
        ('identifier', 'Skrt', 'Skrt', 'Skrt', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'Aint', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'High', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Skrt', 'Skrt', 'Echos', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Skrt', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Aint', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'High', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Aint', 'Aint', 'Echos', 'Pavoid'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Skrt', 'Pavoid'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Aint', 'Pavoid'): [',', ';', '='],
        ('identifier', 'High', 'High', 'High', 'Pavoid'): [',', ';', '='],
        ('identifier', 'High', 'High', 'Echos', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Skrt', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Aint', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'High', 'Pavoid'): [',', ';', '='],
        ('identifier', 'Echos', 'Echos', 'Echos', 'Pavoid'): [',', ';', '='],
        (',', 'Skrt', 'identifier', 'Skrt', 'Pavoid'): ['identifier'],
        (',', 'Skrt', 'identifier', 'Aint', 'Pavoid'): ['identifier'],
        (',', 'Skrt', 'identifier', 'High', 'Pavoid'): ['identifier'],
        (',', 'Skrt', 'identifier', 'Echos', 'Pavoid'): ['identifier'],
        (',', 'Aint', 'identifier', 'Skrt', 'Pavoid'): ['identifier'],
        (',', 'Aint', 'identifier', 'Aint', 'Pavoid'): ['identifier'],
        (',', 'Aint', 'identifier', 'High', 'Pavoid'): ['identifier'],
        (',', 'Aint', 'identifier', 'Echos', 'Pavoid'): ['identifier'],
        (',', 'High', 'identifier', 'Skrt', 'Pavoid'): ['identifier'],
        (',', 'High', 'identifier', 'Aint', 'Pavoid'): ['identifier'],
        (',', 'High', 'identifier', 'High', 'Pavoid'): ['identifier'],
        (',', 'High', 'identifier', 'Echos', 'Pavoid'): ['identifier'],
        (',', 'Echos', 'identifier', 'Skrt', 'Pavoid'): ['identifier'],
        (',', 'Echos', 'identifier', 'Aint', 'Pavoid'): ['identifier'],
        (',', 'Echos', 'identifier', 'High', 'Pavoid'): ['identifier'],
        (',', 'Echos', 'identifier', 'Echos', 'Pavoid'): ['identifier'],
        (';', 'Skrt', 'identifier', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],        
        (';', 'Aint', 'identifier', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'High', 'identifier', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Echos', 'identifier', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Skrt', 'SKRTLITERAL', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],        
        (';', 'Aint', 'AINTLITERAL', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Aint', 'NEALITERAL', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'High', 'HIGHLITERAL', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'High', 'NEHLITERAL', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Cap', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Nocap', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 
        (';', 'Skrt', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],
        (';', 'Aint', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],
        (';', 'High', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],
        #(';', 'Skrt', 'Pavoid'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'],
        # (',', 'SKRTLITERAL', '{'): ['sample']
        # ('}', 'Skrt', ';', 'SKRTLITERAL'): ['Flex', 'Pavoid', 'Par..'],
        # closing bracket of void func 


        # Par Aint Maine () {
        (';', 'Skrt', 'Par'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Aint', 'Par'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'High', 'Par'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Cap', 'Par'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Nocap', 'Par'): ['Skrt', 'Aint', 'High', 'Echos', 'Array', 'Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        ('Aint', 'Aint', 'Par'): ['identifier'],


        # Tea Stmt
        'Tea': ['('],
        ('(', 'Tea'): ['identifier'],
        #('identifier', 'Tea', '('): [')'],
        ('identifier', 'Tea'): ['[', ')'],
        ('identifier', 'Tea', '['): [']'],
        ('AINTLITERAL', 'Tea'): [']'],
        (']', 'Tea'): [')'],   
        (')', 'Tea'): [';'],   
        (';', 'Tea'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'], 
        (';', 'Tea', 'Pavoid'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', '}'], 

        # Spill Stmt
        'Spill': ['('],
        ('(', 'Spill'): ['identifier', 'SKRTLITERAL', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL', 'Cap', 'Nocap'],
        ('identifier', 'Spill'): [')', '~'],
        ('SKRTLITERAL', 'Spill'): [')', '~'],
        ('AINTLITERAL', 'Spill'): [')', '~'],
        ('NEALITERAL', 'Spill'): [')', '~'],
        ('HIGHLITERAL', 'Spill'): [')', '~'],
        ('NEHLITERAL', 'Spill'): [')', '~'],
        ('Cap', 'Cap', '('): [')', '~'],
        ('Nocap', 'Nocap', '('): [')', '~'],
        ('~', 'Spill'): ['identifier', 'SKRTLITERAL', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL', 'Cap', 'Nocap'],
        ('~', 'Cap'): ['identifier', 'SKRTLITERAL', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL', 'Cap', 'Nocap'],
        ('~', 'Nocap'): ['identifier', 'SKRTLITERAL', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL', 'Cap', 'Nocap'],
        ('Nocap', 'Nocap', '~'): [')', '~'],
        ('Cap', 'Cap', '~'): [')', '~'],
        (')', 'Spill'): [';'],
        (')', 'Cap'): [';'],
        (')', 'Nocap'): [';'],
        (';', 'Spill'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'], 
        (';', 'Spill', 'Pavoid'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Cap', 'Spill'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Nocap', 'Spill'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Nocap', 'Nocap'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Nocap', 'Cap'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        (';', 'Cap', 'Cap'): ['Whatif', 'Tea', 'Spill', 'Forda', 'Carps', 'identifier', 'Bounce'],
        
        # Forda Stmt
        'Forda': ['('],
        ('(', 'Forda'): ['Aint', 'High'],
        ('identifier', 'Aint', 'Forda'): ['='],
        ('identifier', 'High', 'Forda'): ['='],
        ('AINTLITERAL', 'Aint', 'Forda'): [';'],
        ('NEALITERAL', 'Aint', 'Forda'): [';'],
        ('HIGHLITERAL', 'High', 'Forda'): [';'],
        ('NEHLITERAL', 'High', 'Forda'): [';'],
        (';', 'Aint', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        (';', 'High', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('identifier', 'Aint', ';', 'AINTLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('identifier', 'Aint', ';', 'NEALITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('identifier', 'High', ';', 'HIGHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('identifier', 'High', ';', 'NEHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('AINTLITERAL', 'Aint', ';', 'AINTLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('AINTLITERAL', 'Aint', ';', 'NEALITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('AINTLITERAL', 'High', ';', 'HIGHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('AINTLITERAL', 'High', ';', 'NEHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEALITERAL', 'Aint', ';', 'AINTLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEALITERAL', 'Aint', ';', 'NEALITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEALITERAL', 'High', ';', 'HIGHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEALITERAL', 'High', ';', 'NEHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('HIGHLITERAL', 'Aint', ';', 'AINTLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('HIGHLITERAL', 'Aint', ';', 'NEALITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('HIGHLITERAL', 'High', ';', 'HIGHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('HIGHLITERAL', 'High', ';', 'NEHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEHLITERAL', 'Aint', ';', 'AINTLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEHLITERAL', 'Aint', ';', 'NEALITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEHLITERAL', 'High', ';', 'HIGHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('NEHLITERAL', 'High', ';', 'NEHLITERAL'): ['<', '>', '<=', '>=', '==', '!='],
        ('<', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('<', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('>', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('>', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('<=', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('<=', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('>=', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('>=', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('==', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('==', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('!=', 'Aint'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('!=', 'High'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('identifier', 'Aint', '<'): [';'],
        ('identifier', 'Aint', '>'): [';'],
        ('identifier', 'Aint', '<='): [';'],
        ('identifier', 'Aint', '>='): [';'],
        ('identifier', 'Aint', '=='): [';'],
        ('identifier', 'Aint', '!='): [';'],
        ('identifier', 'High', '<'): [';'],
        ('identifier', 'High', '>'): [';'],
        ('identifier', 'High', '<='): [';'],
        ('identifier', 'High', '>='): [';'],
        ('identifier', 'High', '=='): [';'],
        ('identifier', 'High', '!='): [';'],
        (';', 'Aint', 'identifier', 'Forda', 'Par'): ['identifier'],
        (';', 'High', 'identifier', 'Forda', 'Par'): ['identifier'],
        (';', 'Aint', 'identifier', 'Forda', 'Pavoid'): ['identifier'],
        (';', 'High', 'identifier', 'Forda', 'Pavoid'): ['identifier'],
        (';', 'Aint', 'identifier', 'Forda', 'Flex'): ['identifier'],
        (';', 'High', 'identifier', 'Forda', 'Flex'): ['identifier'],
        ('identifier', 'Aint', ';', 'Forda', 'Par'): ['+=', '-='],
        ('identifier', 'High', ';', 'Forda', 'Par'): ['+=', '-='],
        ('identifier', 'Aint', ';', 'Forda', 'Pavoid'): ['+=', '-='],
        ('identifier', 'High', ';', 'Forda', 'Pavoid'): ['+=', '-='],
        ('identifier', 'Aint', ';', 'Forda', 'Flex'): ['+=', '-='],
        ('identifier', 'High', ';', 'Forda', 'Flex'): ['+=', '-='],
        ('+=', 'Aint', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('-=', 'Aint', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('+=', 'High', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        ('-=', 'High', 'Forda'): ['identifier', 'AINTLITERAL', 'NEALITERAL', 'HIGHLITERAL', 'NEHLITERAL'],
        #('identifier', 'Aint', '+='): ['sss'],

        #...
    }

    def __init__(self, lexer):
        self.lexer = lexer
        self.pg = ParserGenerator(
            ['LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'UNDERSCORE', 'TILDE', 'BACKSLASH',
             'IDENTIFIER', 'AINT', 'SKRT', 'HIGH', 'ECHOS', 'TEA', 'SPILL', 'WHATIF', 'LESGO', 'LEMME', 'FORDA', 'CARPS', 'BRUH',
             'GORA', 'BOUNCE', 'NOCAP', 'CAP', 'PAR', 'ARRAY', 'FLEX', 'MAINE', 'PAVOID', 'SKRTLITERAL', 'AINTLITERAL', 'HIGHLITERAL',
             'NEALITERAL', 'NEHLITERAL', 'ECHOSLITERAL', 'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL',
             'PLUS', 'MINUS', 'STAR', 'SLASH', 'PERCENT', 'LT', 'GT', 'EQ', 'NEQ', 'LTE', 'GTE', 'AND', 'OR', 'NOT', 'TAB', 'NEWLINE', 'DOUBLE_QUOTE']
        )

        self.pg.precedence = [
            ('left', ['OR']),
            ('left', ['AND']),
            ('right', ['NOT']),
            ('left', ['LT', 'LTE', 'GT', 'GTE', 'EQ', 'NEQ']),
            ('left', ['PLUS', 'MINUS']),
            ('left', ['STAR', 'SLASH', 'PERCENT']),
            ('left', ['TILDE']),
            ('right', ['EQUALS', 'PLUSEQUAL', 'MINUSEQUAL', 'STAREQUAL', 'SLASHEQUAL', 'PERCENTEQUAL']),
        ]

        self._add_productions()
        self.parser = self.pg.build()

        # self.parse()

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
        @self.pg.production('program : global_declarations functions PAR AINT MAINE LPAREN RPAREN LBRACE body BOUNCE AINTLITERAL SEMI RBRACE')
        def program(p):
            print("parsing program")

        @self.pg.production('global_declarations : declarations')
        def global_declarations(p):
            print("parsing global_declarations")
            

        @self.pg.production('declarations : declares declarations')
        @self.pg.production('declarations : ')
        def declarations(p):
            print("parsing declarations")
            

        @self.pg.production('declares : variable_decls')
        @self.pg.production('declares : stmt')
        @self.pg.production('declares : array_decl')
        @self.pg.production('declares : array_init')
        @self.pg.production('declares : ')
        def declares(p):
            print("parsing declares")
        

        @self.pg.production('variable_decls : variable_decl')
        @self.pg.production('variable_decls : variable_initialization')
        def variable_decls(p):
            print("parsing variable_decls")
            

        @self.pg.production('variable_decl : data_type IDENTIFIER decl_tail SEMI')
        def variable_decl(p):
            print("parsing variable_decl")


        @self.pg.production('decl_tail : COMMA IDENTIFIER decl_tail')
        @self.pg.production('decl_tail : ')
        def decl_tail(p):
            print("parsing decl_tail")


        @self.pg.production('variable_initialization : data_type IDENTIFIER EQUALS value initialize_tail SEMI')
        def variable_initialization(p):
            print("parsing variable_initialization")


        @self.pg.production('initialize_tail : COMMA IDENTIFIER EQUALS value initialize_tail')
        @self.pg.production('initialize_tail : ')
        def initialize_tail(p):
            print("parsing initialize_tail")

        @self.pg.production('data_type : AINT')
        @self.pg.production('data_type : SKRT') 
        @self.pg.production('data_type : HIGH')
        @self.pg.production('data_type : ECHOS')
        def data_type(p):
            print("parsing data_type")


        @self.pg.production('array_decl : ARRAY data_type IDENTIFIER LBRACKET AINTLITERAL RBRACKET SEMI')
        def array_decl(p):
            print("parsing array_decl")


        @self.pg.production('array_init : ARRAY data_type IDENTIFIER LBRACKET AINTLITERAL RBRACKET EQUALS LBRACE array_elements RBRACE SEMI')
        def array_init(p):
            print("parsing array_init")

        @self.pg.production('array_elements : value COMMA array_elements')
        @self.pg.production('array_elements : value')
        def array_elements(p):
            print("parsing array_elements")

        @self.pg.production('value : identifier LBRACKET expr RBRACKET')
        def value_array_access(p):
            print("parsing value_array_access")


        @self.pg.production('value : identifier')
        @self.pg.production('value : literal')
        @self.pg.production('value : expr')
        # @self.pg.production('value : skrt_concat')
        @self.pg.production('value : func_call')
        @self.pg.production('value : type_cast')
        @self.pg.production('value : esc_sequence')
        @self.pg.production('value : echos_literal')
        def value(p):
            print("parsing value")


        @self.pg.production('type_cast : data_type LPAREN value RPAREN')
        def type_cast(p):
            print("parsing type_cast")


        @self.pg.production('literal : AINTLITERAL')
        @self.pg.production('literal : HIGHLITERAL')
        @self.pg.production('literal : NEALITERAL')
        @self.pg.production('literal : NEHLITERAL')
        @self.pg.production('literal : SKRTLITERAL')
        def literal(p):
            print("parsing literal")


        @self.pg.production('identifier : IDENTIFIER')
        def identifier(p):
            print("parsing identifier")


        @self.pg.production('functions : function_definition functions')
        @self.pg.production('functions : ')
        def functions(p):
            print("parsing functions")


        @self.pg.production('function_definition : FLEX data_type IDENTIFIER LPAREN parameters RPAREN LBRACE flex_body RBRACE')
        @self.pg.production('function_definition : PAVOID IDENTIFIER LPAREN parameters RPAREN LBRACE voidbody RBRACE')
        def function_definition(p):
            print("parsing function_definition")

            
        @self.pg.production('flex_body : declarations stmts BOUNCE value SEMI')
        @self.pg.production('flex_body : declarations BOUNCE value SEMI')
        def flex_body(p):
            print("parsing flex_body")

    
        @self.pg.production('func_call : IDENTIFIER LPAREN args RPAREN')
        def func_call(p):
            print("parsing func_call")

        @self.pg.production('parameters : param parameters_tail')
        @self.pg.production('parameters : ')
        def parameters(p):
            print("parsing parameters")


        @self.pg.production('parameters_tail : COMMA param parameters_tail')
        @self.pg.production('parameters_tail : ')
        def parameters_tail(p):
            print("parsing parameters_tail")


        @self.pg.production('param : data_type IDENTIFIER')
        def param(p):
            pass
    

        @self.pg.production('args : value args_tail')
        @self.pg.production('args : ')
        def args(p):
            print("parsing args")


        @self.pg.production('args_tail : COMMA value args_tail')
        @self.pg.production('args_tail : ')
        def args_tail(p):
            print("parsing args_tail")


        @self.pg.production('body : declarations stmts')
        def body(p):
            print("parsing body")


        @self.pg.production('voidbody : declarations void_stmts')
        def voidbody(p):
            print("parsing voidbody")

        @self.pg.production('void_stmts : void_stmt void_stmts')
        @self.pg.production('void_stmts : ')
        def void_stmts(p):
            print("parsing void_stmts")


        @self.pg.production('void_stmt : tea_stmt SEMI')
        @self.pg.production('void_stmt : spill_stmt SEMI')
        @self.pg.production('void_stmt : void_forda_stmt')
        @self.pg.production('void_stmt : void_carps_stmt')
        @self.pg.production('void_stmt : assignment_stmt SEMI')
        @self.pg.production('void_stmt : func_call SEMI')
        @self.pg.production('void_stmt : break_stmt SEMI')
        @self.pg.production('void_stmt : continue_stmt SEMI')
        def void_stmt(p):
            print("parsing void_stmt")


        @self.pg.production('stmts : stmt stmts')
        @self.pg.production('stmts : ')
        def stmts(p):
            print("parsing stmts")


        @self.pg.production('stmt : tea_stmt SEMI')
        @self.pg.production('stmt : spill_stmt SEMI')
        @self.pg.production('stmt : forda_stmt')
        @self.pg.production('stmt : carps_stmt')
        @self.pg.production('stmt : assignment_stmt SEMI')
        @self.pg.production('stmt : func_call SEMI')
        @self.pg.production('stmt : skrt_concat SEMI')
        @self.pg.production('stmt : echos_expr SEMI')
        @self.pg.production('stmt : whatif_stmt')  # Add this line to allow whatif_stmt as stmt
        @self.pg.production('stmt : break_stmt SEMI')
        @self.pg.production('stmt : continue_stmt SEMI')
        def stmt(p):
            print("parsing stmt")


        @self.pg.production('break_stmt : BRUH')
        def break_stmt(p):
            print("parsing break_stmt")


        @self.pg.production('continue_stmt : GORA')
        def continue_stmt(p):
            print("parsing continue_stmt")


        @self.pg.production('next_stmts : maine_stmt next_stmts')
        @self.pg.production('next_stmts : ')
        def next_stmts(p):
            print("parsing next_stmts")


        @self.pg.production('bounce_stmt : BOUNCE value SEMI')
        def bounce_stmt(p):
            print("parsing bounce_stmt")

        @self.pg.production('maine_stmt : stmt')
        @self.pg.production('maine_stmt : whatif_stmt')
        def maine_stmt(p):
            print("parsing maine_stmt")

        @self.pg.production('tea_stmt : TEA LPAREN IDENTIFIER RPAREN')
        def tea_stmt(p):
            print("parsing tea_stmt")

        @self.pg.production('spill_stmt : SPILL LPAREN skrt_concat RPAREN')
        @self.pg.production('spill_stmt : SPILL LPAREN value RPAREN')
        def spill_stmt(p):
            print("parsing spill_stmt")

        @self.pg.production('forda_stmt : FORDA LPAREN AINT IDENTIFIER EQUALS value SEMI rel_expr SEMI assignment_stmt RPAREN LBRACE stmts RBRACE')
        def forda_stmt(p):
            print("parsing forda_stmt")


        @self.pg.production('carps_stmt : CARPS LPAREN condition RPAREN LBRACE stmts RBRACE')
        def carps_stmt(p):
            print("parsing carps_stmt")


        @self.pg.production('assignment_stmt : IDENTIFIER LBRACKET expr RBRACKET EQUALS value')
        @self.pg.production('assignment_stmt : IDENTIFIER EQUALS value')
        @self.pg.production('assignment_stmt : IDENTIFIER PLUSEQUAL value')
        @self.pg.production('assignment_stmt : IDENTIFIER MINUSEQUAL value')
        @self.pg.production('assignment_stmt : IDENTIFIER STAREQUAL value')
        @self.pg.production('assignment_stmt : IDENTIFIER SLASHEQUAL value')
        @self.pg.production('assignment_stmt : IDENTIFIER PERCENTEQUAL value')
        @self.pg.production('assignment_stmt : IDENTIFIER COMMA identifier_list EQUALS func_call')
        def assignment_stmt(p):
            print("parsing assignment_stmt")

        @self.pg.production('identifier_list : IDENTIFIER COMMA identifier_list')
        @self.pg.production('identifier_list : IDENTIFIER')
        def identifier_list(p):
            pass

        @self.pg.production('expr : echos_expr')
        @self.pg.production('expr : term expr_tail')
        def expr(p):
            print("parsing expr")



        @self.pg.production('expr_tail : PLUS term expr_tail')
        @self.pg.production('expr_tail : MINUS term expr_tail')
        @self.pg.production('expr_tail : ')
        def expr_tail(p):
            print("parsing expr_tail")


        @self.pg.production('term : factor term_tail')
        def term(p):
            print("parsing term")


        @self.pg.production('term_tail : STAR factor term_tail')
        @self.pg.production('term_tail : SLASH factor term_tail')
        @self.pg.production('term_tail : PERCENT factor term_tail')
        @self.pg.production('term_tail : ')
        def term_tail(p):
            print("parsing term_tail")



        @self.pg.production('factor : NOT factor')
        @self.pg.production('factor : IDENTIFIER LBRACKET expr RBRACKET')
        @self.pg.production('factor : IDENTIFIER')
        @self.pg.production('factor : AINTLITERAL')
        @self.pg.production('factor : HIGHLITERAL')
        @self.pg.production('factor : SKRTLITERAL')
        @self.pg.production('factor : echos_literal')
        @self.pg.production('factor : LPAREN expr RPAREN')
        @self.pg.production('factor : data_type LPAREN factor RPAREN')
        def factor(p):
            print("parsing factor")



        @self.pg.production('whatif_stmt : WHATIF LPAREN condition RPAREN LBRACE stmts RBRACE mul_lemme')
        def whatif_stmt(p):
            print("parsing whatif_stmt")

        @self.pg.production('mul_lemme : lemme_stmt mul_lemme')
        @self.pg.production('mul_lemme : lesgo_stmt')
        @self.pg.production('mul_lemme : ')
        def mul_lemme(p):
            print("parsing mul_lemme")


        @self.pg.production('lemme_stmt : LEMME LPAREN condition RPAREN LBRACE stmts RBRACE')
        def lemme_stmt(p):
            print("parsing lemme_stmt")


        @self.pg.production('lesgo_stmt : LESGO LBRACE stmts RBRACE')
        def lesgo_stmt(p):
            print("parsing lesgo_stmt")


        @self.pg.production('condition : expr')
        def condition(p):
            print("parsing condition")


        @self.pg.production('echos_expr : rel_expr')
        @self.pg.production('echos_expr : echos_expr AND echos_expr')
        @self.pg.production('echos_expr : NOT echos_expr')
        @self.pg.production('echos_expr : echos_expr OR echos_expr')
        def echos_expr(p):
            print("parsing echos_expr")



        @self.pg.production('rel_expr : expr rel_op expr')
        def rel_expr(p):
            print("parsing rel_expr")

        # Relational operators
        @self.pg.production('rel_op : LT')
        @self.pg.production('rel_op : GT')
        @self.pg.production('rel_op : LTE')
        @self.pg.production('rel_op : GTE')
        @self.pg.production('rel_op : EQ')
        @self.pg.production('rel_op : NEQ')
        def rel_op(p):
            print("parsing rel_op")


        @self.pg.production('void_forda_stmt : FORDA LPAREN AINT IDENTIFIER EQUALS value SEMI rel_expr SEMI assignment_stmt RPAREN LBRACE void_stmts RBRACE')
        def void_forda_stmt(p):
            print("parsing void_forda_stmt")



        @self.pg.production('void_carps_stmt : CARPS LPAREN rel_expr RPAREN LBRACE void_stmts RBRACE')
        def void_carps_stmt(p):
            print("parsing void_carps_stmt")


        @self.pg.production('skrt_concat : value TILDE skrt_concat')
        @self.pg.production('skrt_concat : value TILDE value')
        def skrt_concat(p):
            print("parsing skrt_concat")


        @self.pg.production('skrt_operand : IDENTIFIER')
        @self.pg.production('skrt_operand : SKRTLITERAL')
        def skrt_operand(p):
            print("parsing skrt_operand")


        @self.pg.production('echos_literal : NOCAP')
        @self.pg.production('echos_literal : CAP')
        def echos_literal(p):
            print("parsing echos_literal")


        @self.pg.production('esc_sequence : TAB')
        @self.pg.production('esc_sequence : NEWLINE')
        @self.pg.production('esc_sequence : BACKSLASH')
        @self.pg.production('esc_sequence : DOUBLE_QUOTE')
        def esc_sequence(p):
            print("parsing esc_sequence")


        
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

                # error_message = f"Function: {function.getstr()}\n2nd prev Token: {secprev_token.getstr()}\nPrev Token: {previous_token.getstr()}\nLast RW: {last_reserved_word.getstr()}\n2nd prev RW: {seclast_reserved_keyword.getstr()}\nUnexpected token: {[token.getstr()]} at line number {token.getsourcepos().lineno}\nExpected Token\s: {expected}\n"
                
                error_message = f"Unexpected token: {[token.getstr()]} at line number {token.getsourcepos().lineno}\nExpected Token\s: {expected}\n"
                raise ValueError(error_message)
        
        # Function to convert tokens
        def convert_token(token_type):
            return conversion_dict.get(token_type, token_type)
        
        def list_expected_tokens(token, last_reserved_word, seclast_reserved_word, secprev_token, function):

            token_type = convert_token(token.gettokentype()) if token else None
            last_reserved_word = convert_token(last_reserved_word.gettokentype()) if last_reserved_word else None
            seclast_reserved_word = convert_token(seclast_reserved_word.gettokentype()) if seclast_reserved_word else None
            secprev_token = convert_token(secprev_token.gettokentype()) if secprev_token else None
            function = convert_token(function.gettokentype()) if function else None

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
from rply import ParserGenerator

    # def get_parser(self):
    #     return self.pg.build()

