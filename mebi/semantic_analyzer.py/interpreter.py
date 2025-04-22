class Environment:
    def __init__(self):
        self.variables = {}

    def set_var(self, name, value):
        self.variables[name] = value

    def get_var(self, name):
        return self.variables.get(name, None)


class Interpreter:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        if node.name == "program":
            for child in node.children:
                self.eval(child)

        elif node.name == "team_block":
            for child in node.children:
                self.eval(child)

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

        elif node.name == "feint_dec":
            var_name = node.children[0].value  # Token for VAR_INIT
            init_value = self.eval(node.children[1])
            self.env.set_var(var_name, init_value)

        elif node.name == "feint_init":
            return int(node.value)

        # Add more as you expand (floater_init, chant_init, expressions...)

        else:
            print(f"[WARN] No evaluation rule for {node.name}")
