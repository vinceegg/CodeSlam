from syntax_analyzer.ast_nodes import ASTNode

class Environment:
    def __init__(self):
        self.variables = {}

    def set_var(self, name, value):
        self.variables[name] = value

    def get_var(self, name):
        return self.variables.get(name, f"[ERROR: {name} not found]")


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
            var_token = node.children[0]
            var_name = var_token.value
            more_feint_node = node.children[1]
            init_value = self.eval(more_feint_node) 
            self.env.set_var(var_name, init_value)
            print(f"[SET] {var_name} = {init_value}")

        elif node.name == "more_feint":
            if node.children:
                return self.eval(node.children[0]) 
        
        elif node.name == "feint_init":
            return int(node.value)
        
        #TODO
        elif node.name == "feint_init_end":
            pass

        elif node.name == "floater_dec":
            var_token = node.children[0]
            var_name = var_token.value
            more_floater_node = node.children[1]
            init_value = self.eval(more_floater_node)
            self.env.set_var(var_name, init_value)
            print(f"[SET] {var_name} = {init_value}")
            
        elif node.name == "more_floater":
            if node.children:
                return self.eval(node.children[0])
            
        elif node.name == "floater_init":
            if node.value is not None:
                return float(node.value)
        
        #TODO
        elif node.name == "floater_init_end":
            pass  # Later support @x = 1.5, @y = 2.6;
        
        elif node.name == "chant_dec":
            var_token = node.children[0]  # VAR_INIT
            var_name = var_token.value
            more_chant_node = node.children[1]
            init_value = self.eval(more_chant_node)
            self.env.set_var(var_name, init_value)
            print(f"[SET] {var_name} = {init_value}")
        
        elif node.name == "more_chant":
            if node.children:
                return self.eval(node.children[0])
        
        elif node.name == "chant_init":
            if node.value is not None:
                return str(node.value).strip('"')
            
        elif node.name == "team_statement":
            for stmt in node.children:
                self.eval(stmt)

        elif node.name == "statement":
            return self.eval(node.children[0])

        elif node.name == "announce_statement":
            outputs = self.eval(node.children[0])
            print(*outputs)

        elif node.name == "outputs":
            # Always flatten nested output nodes
            results = []
            for child in node.children:
                val = self.eval(child)
                results.append(val)
            return results

        elif node.name == "output":
            if node.value:
                print(f"[OUTPUT] VAR_INIT = {node.value}")
                return self.env.get_var(node.value)
            elif node.children:
                val = self.eval(node.children[0])
                print(f"[OUTPUT] Child node evaluated to: {val}")
                return val
            else:
                return "[EMPTY OUTPUT]"

        elif node.name == "literal":
            return node.value

        else:
            print(f"[WARN] No eval rule for: {node.name}")
