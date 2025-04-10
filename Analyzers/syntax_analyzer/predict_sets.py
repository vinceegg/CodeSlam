
from Analyzers.lexical_analyzer.tokens import TokenType

PREDICT_SETS = {
    # Program -> Team Declaration
    ("program", TokenType.TEAM): 1,
    ("program", TokenType.DUNK): 2,  # Function declaration

    ("function_declaration", TokenType.DUNK): 1,

    # Parameter list productions
    ("parameter_list", TokenType.VAR_INIT): 1,
    
    # Team Declaration
    ("team_declaration", TokenType.TEAM): 1,
    
    # Statement list productions
    ("statement_list", TokenType.FEINT): 1,
    ("statement_list", TokenType.CHANT): 1, 
    ("statement_list", TokenType.FLOATER): 1,
    ("statement_list", TokenType.STAT): 1,
    ("statement_list", TokenType.ANNOUNCE): 1,
    ("statement_list", TokenType.VAR_INIT): 1,
    ("statement_list", TokenType.CODE_BLOCK_RIGHT): 2,  # Empty production
    
    # Statement productions
    ("statement", TokenType.FEINT): 1,  # Variable declaration
    ("statement", TokenType.CHANT): 2,  # Variable declaration
    ("statement", TokenType.FLOATER): 3,  # Variable declaration
    ("statement", TokenType.STAT): 4,  # Variable declaration
    ("statement", TokenType.ANNOUNCE): 5,  # Announce statement
    ("statement", TokenType.VAR_INIT): 6,  # Variable assignment
    ("statement", TokenType.DRIBBLE): 7,  # Conditional statement
    
    # Variable declaration
    ("variable_declaration", TokenType.FEINT): 1,
    ("variable_declaration", TokenType.CHANT): 2,
    ("variable_declaration", TokenType.FLOATER): 3,
    ("variable_declaration", TokenType.STAT): 4,
    
    # Variable assignment
    ("variable_assignment", TokenType.VAR_INIT): 1,
    
    # Announce statement
    ("announce_statement", TokenType.ANNOUNCE): 1,
    
    # Expression productions
    ("expression", TokenType.FEINTLIT): 1,
    ("expression", TokenType.FLOATERLIT): 1,
    ("expression", TokenType.CHANTLIT): 1,
    ("expression", TokenType.LEFT_PAREN): 1,
    ("expression", TokenType.VAR_INIT): 1,
    
    # Term productions
    ("term", TokenType.FEINTLIT): 1,
    ("term", TokenType.FLOATERLIT): 1,
    ("term", TokenType.CHANTLIT): 1,
    ("term", TokenType.LEFT_PAREN): 1,
    ("term", TokenType.VAR_INIT): 1,
    
    # Factor productions
    ("factor", TokenType.FEINTLIT): 1,
    ("factor", TokenType.FLOATERLIT): 2,
    ("factor", TokenType.CHANTLIT): 3,
    ("factor", TokenType.LEFT_PAREN): 4,
    ("factor", TokenType.VAR_INIT): 5,

    # Conditional statement productions
    ("conditional_statement", TokenType.DRIBBLE): 1,
    ("conditional_statement", TokenType.PASS): 2,
    
    # Conditional expression productions
    ("conditional_expression", TokenType.FEINTLIT): 1,
    ("conditional_expression", TokenType.FLOATERLIT): 1,
    ("conditional_expression", TokenType.CHANTLIT): 1,
    ("conditional_expression", TokenType.LEFT_PAREN): 1,
    ("conditional_expression", TokenType.VAR_INIT): 1,
    ("conditional_expression", TokenType.AND_OP): 2,
    ("conditional_expression", TokenType.OR_OP): 3,
    
    # Relational expression productions
    ("relational_expression", TokenType.FEINTLIT): 1,
    ("relational_expression", TokenType.FLOATERLIT): 1,
    ("relational_expression", TokenType.CHANTLIT): 1,
    ("relational_expression", TokenType.LEFT_PAREN): 1,
    ("relational_expression", TokenType.VAR_INIT): 1,

    # Function call productions
    ("function_call", TokenType.LEFT_PAREN): 1,
    
    # Function call statement productions
    ("function_call_statement", TokenType.VAR_INIT): 1,
    
    # Argument list productions
    ("argument_list", TokenType.FEINTLIT): 1,
    ("argument_list", TokenType.FLOATERLIT): 1,
    ("argument_list", TokenType.CHANTLIT): 1,
    ("argument_list", TokenType.LEFT_PAREN): 1,
    ("argument_list", TokenType.VAR_INIT): 1,
}