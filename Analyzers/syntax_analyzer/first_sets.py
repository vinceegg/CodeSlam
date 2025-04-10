from Analyzers.lexical_analyzer.tokens import TokenType

FIRST_SETS = {
    "program": {
        TokenType.TEAM, TokenType.DUNK
    },
    "team_declaration": {
        TokenType.TEAM
    },
    "statement_list": {
        TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT,
        TokenType.ANNOUNCE, TokenType.VAR_INIT,
        # Empty production also possible - would include CODE_BLOCK_RIGHT
    },
    "statement": {
        TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT,
        TokenType.ANNOUNCE, TokenType.VAR_INIT, TokenType.PASS
    },
    "variable_declaration": {
        TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT, TokenType.COMMA
    },
    "variable_assignment": {
        TokenType.VAR_INIT
    },
    "announce_statement": {
        TokenType.ANNOUNCE
    },
    "expression": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT
    },
    "term": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT
    },
    "factor": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT
    },
    "conditional_statement": {
        TokenType.DRIBBLE
    },
    "conditional_expression": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT, TokenType.AND_OP, TokenType.OR_OP
    },
    "relational_expression": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT
    },
    "logical_expression": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT, TokenType.AND_OP, TokenType.OR_OP
    },
    "parameter_list": {
        TokenType.VAR_INIT
    },
    "function_declaration": {
        TokenType.DUNK
    },
    "function_call": {
        TokenType.LEFT_PAREN
    },
    "function_call_statement": {
        TokenType.VAR_INIT
    },
    "argument_list": {
        TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
        TokenType.LEFT_PAREN, TokenType.VAR_INIT
    }
}