from ast_builder import ASTBuilder, NodeType, Team, Statement, Block, VariableDeclaration, Assignment, BinaryOperation, Identifier, Literal, AnnounceStatement
from ast_pretty_printer import ASTPrettyPrinter

def create_sample_ast():
    """
    Create a sample AST for the CodeSlam program:
    
    Team() {
       Feint @x = 5;         
       Feint @y = 10;        
       @result = @x + @y;  
       
       Announce("The result is: " & @result);
    }
    
    Returns:
        A Team node representing the CodeSlam program
    """
    # Create variable declarations
    x_declaration = VariableDeclaration(
        node_type=NodeType.VARIABLE_DECLARATION,
        line_number=2,
        column=1,
        var_type="Feint",
        var_name="@x",
        value=Literal(
            node_type=NodeType.LITERAL,
            line_number=2,
            column=13,
            value=5,
            literal_type="number"
        )
    )
    
    y_declaration = VariableDeclaration(
        node_type=NodeType.VARIABLE_DECLARATION,
        line_number=3,
        column=1,
        var_type="Feint",
        var_name="@y",
        value=Literal(
            node_type=NodeType.LITERAL,
            line_number=3,
            column=13,
            value=10,
            literal_type="number"
        )
    )
    
    # Create the addition expression
    x_var = Identifier(
        node_type=NodeType.IDENTIFIER,
        line_number=4,
        column=12,
        name="@x"
    )
    
    y_var = Identifier(
        node_type=NodeType.IDENTIFIER,
        line_number=4,
        column=16,
        name="@y"
    )
    
    add_expr = BinaryOperation(
        node_type=NodeType.BINARY_OP,
        line_number=4,
        column=14,
        left=x_var,
        operator="+",
        right=y_var
    )
    
    # Create the assignment statement
    result_assignment = Assignment(
        node_type=NodeType.ASSIGNMENT,
        line_number=4,
        column=1,
        var_name="@result",
        value=add_expr
    )
    
    # Create the string concatenation for Announce
    result_var = Identifier(
        node_type=NodeType.IDENTIFIER,
        line_number=6,
        column=31,
        name="@result"
    )
    
    string_literal = Literal(
        node_type=NodeType.LITERAL,
        line_number=6,
        column=10,
        value="The result is: ",
        literal_type="string"
    )
    
    concat_expr = BinaryOperation(
        node_type=NodeType.BINARY_OP,
        line_number=6,
        column=25,
        left=string_literal,
        operator="&",
        right=result_var
    )
    
    # Create the Announce statement (not a function call)
    announce_stmt = AnnounceStatement(
        node_type=NodeType.STATEMENT,
        line_number=6,
        column=1,
        message=concat_expr
    )
    
    # Create the block with all statements
    team_block = Block(
        node_type=NodeType.BLOCK,
        line_number=1,
        column=8,
        statements=[
            x_declaration,
            y_declaration,
            result_assignment,
            announce_stmt
        ]
    )
    
    # Create the Team (main function)
    team = Team(
        node_type=NodeType.TEAM,
        line_number=1,
        column=1,
        body=team_block
    )
    
    return team

def main():
    """Main function to demonstrate the AST builder and pretty printer."""
    # Create a sample AST
    ast = create_sample_ast()
    
    # Create a pretty printer
    printer = ASTPrettyPrinter(indent_size=2)
    
    # Print the AST
    print("Abstract Syntax Tree:")
    print(printer.visit(ast))
    
    # Demonstrate how to use the AST builder with tokens
    # This is just a placeholder since we don't have actual tokens
    builder = ASTBuilder()
    # ast = builder.build(tokens)  # This would be used with actual tokens

if __name__ == "__main__":
    main() 