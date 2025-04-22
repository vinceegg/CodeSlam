import unittest
from .ast_builder import ASTBuilder, NodeType
from ..lexical_analyzer.tokens import Token, TokenType

class TestASTBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = ASTBuilder()

    def test_variable_declaration(self):
        # Test parsing a variable declaration: Feint score = 10
        tokens = [
            Token(TokenType.FEINT, "Feint"),
            Token(TokenType.VAR_INIT, "score"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.FEINTLIT, "10"),
            Token(TokenType.SEMICOLON, ";")
        ]
        
        ast = self.builder.build(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.statements), 1)
        self.assertEqual(ast.statements[0].node_type, NodeType.VARIABLE_DECLARATION)
        self.assertEqual(ast.statements[0].variable_name, "score")
        self.assertEqual(ast.statements[0].variable_type, "FEINT")
        self.assertEqual(ast.statements[0].initial_value.value, 10)

    def test_if_statement(self):
        # Test parsing an if statement: DRIBBLE (score > 0) { ... }
        tokens = [
            Token(TokenType.DRIBBLE, "DRIBBLE"),
            Token(TokenType.LEFT_PAREN, "("),
            Token(TokenType.VAR_INIT, "score"),
            Token(TokenType.GREATER_THAN, ">"),
            Token(TokenType.FEINTLIT, "0"),
            Token(TokenType.RIGHT_PAREN, ")"),
            Token(TokenType.CODE_BLOCK_LEFT, "{"),
            Token(TokenType.CODE_BLOCK_RIGHT, "}")
        ]
        
        ast = self.builder.build(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.statements), 1)
        self.assertEqual(ast.statements[0].node_type, NodeType.IF_STATEMENT)
        self.assertIsNotNone(ast.statements[0].condition)
        self.assertEqual(ast.statements[0].condition.node_type, NodeType.BINARY_OP)
        self.assertEqual(ast.statements[0].condition.operator, ">")

    def test_function_declaration(self):
        # Test parsing a function declaration: WILT calculateScore() DUNK { ... }
        tokens = [
            Token(TokenType.WILT, "WILT"),
            Token(TokenType.VAR_INIT, "calculateScore"),
            Token(TokenType.LEFT_PAREN, "("),
            Token(TokenType.RIGHT_PAREN, ")"),
            Token(TokenType.DUNK, "DUNK"),
            Token(TokenType.CODE_BLOCK_LEFT, "{"),
            Token(TokenType.CODE_BLOCK_RIGHT, "}")
        ]
        
        ast = self.builder.build(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.statements), 1)
        self.assertEqual(ast.statements[0].node_type, NodeType.FUNCTION_DECLARATION)
        self.assertEqual(ast.statements[0].function_name, "calculateScore")
        self.assertEqual(ast.statements[0].return_type, "DUNK")

    def test_array_declaration(self):
        # Test parsing an array declaration: ZONE scores[5] FEINT
        tokens = [
            Token(TokenType.ZONE, "ZONE"),
            Token(TokenType.VAR_INIT, "scores"),
            Token(TokenType.ARRAY_INDEX_LEFT, "["),
            Token(TokenType.FEINTLIT, "5"),
            Token(TokenType.ARRAY_INDEX_RIGHT, "]"),
            Token(TokenType.FEINT, "Feint"),
            Token(TokenType.SEMICOLON, ";")
        ]
        
        ast = self.builder.build(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.statements), 1)
        self.assertEqual(ast.statements[0].node_type, NodeType.ARRAY_DECLARATION)
        self.assertEqual(ast.statements[0].array_name, "scores")
        self.assertEqual(ast.statements[0].element_type, "FEINT")
        self.assertEqual(ast.statements[0].size.value, 5)

if __name__ == '__main__':
    unittest.main() 