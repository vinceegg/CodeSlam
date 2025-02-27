from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
        self.tokens = []
        self.last_reserved_keyword = None
        self.seclast_reserved_keyword = None
        self.function = None
        self.reserved_keywords = {  
            'Aint': 'Aint',
            'Skrt': 'Skrt',
            'High': 'High',
            'Echos': 'Echos',
            'Tea': 'Tea',
            'Spill': 'Spill',
            'Whatif': 'Whatif',
            'Lesgo': 'Lesgo',
            'Lemme': 'Lemme',
            'Forda': 'Forda',
            'Carps': 'Carps',
            'Bruh': 'Bruh',
            'Gora': 'Gora',
            'Bounce': 'Bounce',
            'Nocap': 'Nocap',
            'Cap': 'Cap',
            'Maine': 'Maine',
            'Pavoid': 'Pavoid',
            'Par': 'Par',
            'Flex': 'Flex',
            'Array': 'Array',
        }

    def _add_tokens(self):
        # Keywords
        reserved_keywords = {
            'Aint': 'Aint',
            'Skrt': 'Skrt',
            'High': 'High',
            'Echos': 'Echos',
            'Tea': 'Tea',
            'Spill': 'Spill',
            'Whatif': 'Whatif',
            'Lesgo': 'Lesgo',
            'Lemme': 'Lemme',
            'Forda': 'Forda',
            'Carps': 'Carps',
            'Bruh': 'Bruh',
            'Gora': 'Gora',
            'Bounce': 'Bounce',
            'Nocap': 'Nocap',
            'Cap': 'Cap',
            'Maine': 'Maine',
            'Pavoid': 'Pavoid',
            'Par': 'Par',
            'Flex': 'Flex',
            'Array': 'Array',
        }
        for keyword, token_name in reserved_keywords.items():
            self.lexer.add(token_name, rf'\b{keyword}\b')

        # Symbols
        symbols = {
            '(': '(',
            ')': ')',
            '[': '[',
            ']': ']',
            '{': '{',
            '}': '}',
            ';': ';',
            '!': '!',
            ',': ',',
            '.': 'DOT',
            '_': '_',
            '~': '~',
            '\\': '\\',
            '\"': '\"',
            '=': '=',
            '+=': '+=',
            '-=': '-=',
            '*=': '*=',
            '/=': '/=',
            '%=': '%=',
            '+': '+',
            '-': '-',
            '*': '*',
            '/': '/',
            '%': '%',
            '<': '<',
            '>': '>',
            '==': '==',
            '!=': '!=',
            '<=': '<=',
            '>=': 'GTE',
            '&&': '&&',
            '??': 'OR',
            '!!': '!!'
        }
        for sym, sym_token in symbols.items():
            self.lexer.add(sym_token, rf'\{sym}')

        # Manually add the OR operator
        self.lexer.add('OR', r'\?\?') 

        # Escape Sequences
        self.lexer.add('TAB', r'\\t')
        self.lexer.add('NEWLINE', r'\\n')

        
        # # Identifier and Literals
        self.lexer.add('NEHLITERAL', r'!\d*\.\d+|!\d+\.\d*')
        self.lexer.add('NEALITERAL', r'!\d+')
        self.lexer.add('identifier', r'[a-z][a-zA-Z0-9_]*')
        self.lexer.add('SKRTLITERAL', r'\"(?:\\.|[^"\\])*\"')
        self.lexer.add('HIGHLITERAL', r'\d*\.\d+|\d+\.\d*')
        self.lexer.add('AINTLITERAL', r'\d+')
        # self.lexer.add('HIGH', r'\d+\.\d*')

        
        # Comments
        self.lexer.ignore(r'\#.*')

        # Ignore spaces
        self.lexer.ignore('\\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    
    def lex(self, s):
        lexer = self.get_lexer()
        for token in lexer.lex(s):
            self.tokens.append(token)  # Store each token in history
            if token.name in self.reserved_keywords.values():
                self.seclast_reserved_keyword = self.last_reserved_keyword
                self.last_reserved_keyword = token  # Update if the token is a reserved keyword
            if token.name in ["Par", "Flex", "Pavoid"]:
                self.function = token
            yield token

    def get_function(self):
        return self.function
    
    def get_last_reserved_keyword(self):
        return self.last_reserved_keyword
    
    def get_seclast_reserved_keyword(self):
        return self.seclast_reserved_keyword
    
    def get_previous_token(self, index=-1):
        # Return the previous token based on the current index
        if len(self.tokens) > abs(index):
            return self.tokens[index-1]
        return None
    
    def get_secprevious_token(self, index=-1):
        # Return the previous token based on the current index
        if len(self.tokens) > abs(index-1):
            return self.tokens[index-2]
        return None    