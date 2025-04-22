from syntax_analyzer.ast_nodes import ASTNode
from rply.token import BaseBox

class Environment:
    def __init__(self):
        self.variables = {}

    def set_var(self, name, value, type_name=None):
        self.variables[name] = {"value": value, "type": type_name}

    def get_var(self, name):
        var = self.variables.get(name)
        return var["value"] if var else f"[ERROR: {name} not found]"

    def get_type(self, name):
        var = self.variables.get(name)
        return var["type"] if var else None


class Compiler:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        print(f"[DEBUG] Visiting: {node.name if hasattr(node, 'name') else node}")
        # If node is a Token (like Token('VAR_INIT', '@passed')), extract its value
        if hasattr(node, "gettokentype") and node.gettokentype() == "VAR_INIT":
            return self.env.get_var(node.value)
        
        if node.name == "program":
            for child in node.children:
                self.eval(child)
        
        elif node.name == "number_rel_operand":
            return self.eval(node.children[0])
        
        elif node.name == "number":
            val = node.value
            if isinstance(val, str) and val.startswith('@'):
                return self.env.get_var(val) 
            elif '.' in str(val):
                print(f"[DEBUG] Evaluating number: {node.value}")
                return float(val)
            else:
                print(f"[DEBUG] Evaluating number: {node.value}")
                return int(val)
            
        elif node.name == "global_decl":
            for child in node.children:
                self.eval(child)

        elif node.name == "variable_dec":
            return self.eval(node.children[0])

        elif node.name == "feint_dec":
            var_token = node.children[0]
            var_name = var_token.value
            init_value = self.eval(node.children[1])
            self.env.set_var(var_name, init_value, type_name="Feint")
            print(f"[SET] {var_name} = {init_value} (Feint)")

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
            init_value = self.eval(node.children[1])
            self.env.set_var(var_name, init_value, type_name="Floater")
            print(f"[SET] {var_name} = {init_value} (Floater)")
            
        elif node.name == "more_floater":
            if node.children:
                return self.eval(node.children[0])
            
        elif node.name == "floater_init":
            if node.value is not None:
                return float(node.value)
        
        #TODO
        elif node.name == "floater_init_end":
            pass
        
        elif node.name == "chant_dec":
            var_token = node.children[0]
            var_name = var_token.value
            more_chant_node = node.children[1]
            init_value = self.eval(node.children[1])
            self.env.set_var(var_name, init_value, type_name="Chant")
            print(f"[SET] {var_name} = {init_value} (Chant)")
        
        elif node.name == "more_chant":
            if node.children:
                return self.eval(node.children[0])
        
        elif node.name == "chant_init":
            if node.value is not None:
                return str(node.value).strip('"')

        elif node.name == "stat_dec":
            var_token = node.children[0]
            var_name = var_token.value
            more_stat_node = node.children[1]
            init_value = self.eval(node.children[1])
            self.env.set_var(var_name, init_value, type_name="Stat")
            print(f"[SET] {var_name} = {init_value} (Stat)")
        
        elif node.name == "stat_init":
            return node.value
        
        elif node.name == "more_stat":
            if node.children:
                return self.eval(node.children[0])
        
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
        
        elif node.name == "team_statement":
            for stmt in node.children:
                self.eval(stmt)

        elif node.name == "statement":
            return self.eval(node.children[0])

        # Double check formatting of the print statement: spaces
        elif node.name == "announce_statement":
            outputs = self.eval(node.children[0])
            print(*outputs)

        elif node.name == "outputs":
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
            
        elif node.name == "statement":
            return self.eval(node.children[0])
                
        elif node.name == "assignment_expression":
            var_token = node.children[0]  # VAR_INIT
            assign_op = node.children[1].value  # assign_operator
            rhs = self.eval(node.children[2])  # assign_operand

            var_name = var_token.value
            var_type = self.env.get_type(var_name)
            self.env.set_var(var_name, rhs, var_type)
            print(f"[SET] {var_name} = {rhs} ({var_type})")
            return rhs

        elif node.name == "follow_statement":
            print("[DEBUG] Entered follow_statement")
            var_token = node._parent.children[0]  # VAR_INIT token
            var_name = var_token.value
            value = self.eval(node.children[0])  # assignment_expression
            var_type = self.env.get_type(var_name)
            self.env.set_var(var_name, value, var_type)
            print(f"[SET] {var_name} = {value} ({var_type})")
            return value
        
        elif node.name == "assign_operand":
            print(f"[DEBUG] Evaluating assign_operand: {node.children[0].name}")
            val = self.eval(node.children[0])
            print(f"[DEBUG] assign_operand evaluated to: {val}")
            return val

        elif node.name == "expression":
            val = self.eval(node.children[0])
            print(f"[DEBUG] expression evaluated to: {val}")
            return val

        elif node.name == "arithmetic_expression":
            return self.eval(node.children[0])

        elif node.name == "ADD":
            return self.eval(node.children[0]) + self.eval(node.children[1])
        elif node.name == "SUB":
            return self.eval(node.children[0]) - self.eval(node.children[1])
        elif node.name == "MUL":
            return self.eval(node.children[0]) * self.eval(node.children[1])
        elif node.name == "DIV":
            return self.eval(node.children[0]) / self.eval(node.children[1])
        elif node.name == "MOD":
            return self.eval(node.children[0]) % self.eval(node.children[1])  

        elif node.name == "relational_expression":
            left = self.eval(node.children[0]) 
            op = node.children[1].value
            right = self.eval(node.children[2])
            print(f"[RELATIONAL] Evaluating: {left} {op} {right}")
            if op == "<":
                return "Win" if left < right else "Loss"
            elif op == ">":
                return "Win" if left > right else "Loss"
            elif op == "==":
                return "Win" if left == right else "Loss"
            elif op == "<=":
                return "Win" if left <= right else "Loss"
            elif op == ">=":
                return "Win" if left >= right else "Loss"
            elif op == "!=":
                return "Win" if left != right else "Loss"

            
        elif node.name == "stat_rel_operand" or node.name == "chant_rel_operand":
            if node.value:
                return self.env.get_var(node.value) if node.value.startswith('@') else node.value
            else:
                return self.eval(node.children[0])

        elif node.name == "other_relational_operator":
            return node.value

        elif node.name == "relational_operator":
            print(f"[DEBUG] Reached relational_operator with value: {node.value}")
            return node.value  # already returning e.g. '<', '=='
        
        elif node.name == "inbound_statement":
            prompt = node.children[0].value.strip('"')
            var_token = node.children[1]
            var_name = var_token.value

            expected_type = self.env.get_type(var_name)
            if not expected_type:
                raise ValueError(f"[ERROR] Variable {var_name} not declared before Inbound().")

            user_input = input(f"{prompt} ")

            # Type-check based on expected type
            try:
                if expected_type == "Feint":
                    value = int(user_input)
                elif expected_type == "Floater":
                    value = float(user_input)
                elif expected_type == "Stat":
                    if user_input == "Win":
                        value = "Win"
                    elif user_input == "Loss":
                        value = "Loss"
                    else:
                        raise ValueError("Expected 'Win' or 'Loss'")
                elif expected_type == "Chant":
                    value = user_input
                else:
                    raise ValueError(f"[ERROR] Unsupported type '{expected_type}'")
            except ValueError as ve:
                raise ValueError(f"[TYPE ERROR] {var_name} expects {expected_type} input: {ve}") # Double check error messages

            self.env.set_var(var_name, value, expected_type)
            print(f"[INBOUND] {var_name} = {value} ({expected_type})")

        elif node.name == "literal":
            # Detect and clean up CHANTLIT values
            if isinstance(node.value, str) and node.value.startswith('"') and node.value.endswith('"'):
                return node.value.strip('"')
            return node.value

        else:
            print(f"[WARN] No eval rule for: {node.name}")
