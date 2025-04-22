from syntax_analyzer.ast_nodes import ASTNode

class Environment:
    def __init__(self):
        self.variables = {}

    def set_var(self, name, value):
        self.variables[name] = value

    def get_var(self, name):
        return self.variables.get(name, None)


class Compiler:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        if node.name == "program":
            for child in node.children:
                self.eval(child)
        elif node.name == "global_decl":
            for child in node.children:
                self.eval(child)

        elif node.name == "function_def":
            for child in node.children:
                self.eval(child)
                
        elif node.name == "team_block":
            for child in node.children:
                self.eval(child)

        elif node.name == "local_decl":
            for child in node.children:
                self.eval(child)

        elif node.name == "local_declaration":
            return self.eval(node.children[0])

        elif node.name == "variable_dec":
            return self.eval(node.children[0])

        elif node.name == "feint_dec":
            var_token = node.children[0]  # Token('VAR_INIT', '@score')
            var_name = var_token.value
            init_node = node.children[1]
            init_value = self.eval(init_node)
            self.env.set_var(var_name, init_value)

        elif node.name == "feint_init":
            return int(node.value)

        elif node.name == "team_statement":
            for stmt in node.children:
                self.eval(stmt)

        elif node.name == "statement":
            return self.eval(node.children[0])

        elif node.name == "announce_statement":
            outputs = self.eval(node.children[0])
            print(*outputs)

        elif node.name == "outputs":
            return [self.eval(child) for child in node.children]

        elif node.name == "output":
            return self.eval(node.children[0])

        elif node.name == "literal":
            return node.value

        else:
            print(f"[WARN] No eval rule for: {node.name}")
