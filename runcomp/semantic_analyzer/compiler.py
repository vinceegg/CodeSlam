from syntax_analyzer.ast_nodes import ASTNode

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
        self.input_func = None  # Default to None, will use built-in input() if not set

    def get_input(self, prompt):
        """Get user input using either the custom input function or built-in input()"""
        if self.input_func:
            return self.input_func(prompt)
        return input(prompt)

    def eval(self, node):
        # print(f"[DEBUG] Visiting: {node.name if hasattr(node, 'name') else node}")
        
        if node.name == "program":
            for child in node.children:
                self.eval(child)
            
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
            # print(f"[SET] {var_name} = {init_value} (Feint)")

        elif node.name == "feint_dec":
            first_var = node.children[0]  # VAR_INIT
            first_value = None
            additional = []

            if node.children[1].children:
                # more_feint: [feint_init, feint_init_end]
                first_value = self.eval(node.children[1].children[0])  # feint_init
                additional = self.eval(node.children[1].children[1])   # feint_init_end

            self.env.set_var(first_var.value, first_value, "Feint")
            for var_name, value in additional:
                self.env.set_var(var_name, value, "Feint")

        elif node.name == "more_feint":
            if node.children:
                return self.eval(node.children[0]) 
        
        elif node.name == "feint_init":
            if node.value is None:
                return None  # uninitialized
            return int(node.value)
        
        elif node.name == "feint_init_end":
            if not node.children:
                return []

            var_token = node.children[0]  # VAR_INIT
            var_name = var_token.value
            more = node.children[1]       # more_feint

            value = None
            if more.children:
                value = self.eval(more.children[0])  # feint_init
                nested = self.eval(more.children[1])  # feint_init_end
            else:
                nested = []

            return [(var_name, value)] + nested

        elif node.name == "floater_dec":
            first_var = node.children[0]  # VAR_INIT
            init_val = self.eval(node.children[1])  # more_floater

            all_vars = [(first_var.value, init_val)]
            additional = getattr(node.children[1], "additional_vars", [])
            all_vars += additional

            for var_name, val in all_vars:
                self.env.set_var(var_name, val, type_name="Floater")

            
        elif node.name == "more_floater":
            if not node.children:
                return None

            init_val = self.eval(node.children[0])  # floater_init
            rest = self.eval(node.children[1])      # floater_init_end

            # If no trailing variables
            if rest is None:
                return init_val

            node.additional_vars = rest
            return init_val

                    
        elif node.name == "floater_init":
            if node.value is None:
                return None
            try:
                return float(node.value)
            except Exception:
                raise ValueError(f"[TYPE ERROR] Invalid floater value: {node.value}")

        
        elif node.name == "floater_init_end":
            if not node.children:
                return []

            var_token = node.children[0]  # VAR_INIT
            var_name = var_token.value
            more_floater = node.children[1]

            # Evaluate the right-hand side of this variable (if initialized or not)
            val = self.eval(more_floater)
            rest = getattr(more_floater, "additional_vars", [])

            result = [(var_name, val)] + rest
            node.additional_vars = result
            return result

        
        elif node.name == "chant_dec":
            first_var = node.children[0]  # VAR_INIT
            init_val = self.eval(node.children[1])  # more_chant

            all_vars = [(first_var.value, init_val)]
            additional = getattr(node.children[1], "additional_vars", [])
            all_vars += additional

            for var_name, val in all_vars:
                self.env.set_var(var_name, val, type_name="Chant")
        
        elif node.name == "more_chant":
            if not node.children:
                return None

            init_val = self.eval(node.children[0])  # chant_init
            rest = self.eval(node.children[1])      # chant_init_end

            if rest is None:
                return init_val

            node.additional_vars = rest
            return init_val

        elif node.name == "chant_init":
            if node.value is None:
                return None
            return str(node.value).strip('"')

        elif node.name == "chant_init_end":
            if not node.children:
                return []

            var_token = node.children[0]  # VAR_INIT
            var_name = var_token.value
            more_chant = node.children[1]

            val = self.eval(more_chant)
            rest = getattr(more_chant, "additional_vars", [])

            result = [(var_name, val)] + rest
            node.additional_vars = result
            return result
 
        elif node.name == "stat_dec":
            first_var = node.children[0]  # VAR_INIT
            init_val = self.eval(node.children[1])  # more_stat

            all_vars = [(first_var.value, init_val)]
            additional = getattr(node.children[1], "additional_vars", [])
            all_vars += additional

            for var_name, val in all_vars:
                self.env.set_var(var_name, val, type_name="Stat")

        elif node.name == "stat_init":
            return node.value
        
        elif node.name == "more_stat":
            if not node.children:
                return None  # Uninitialized
            init_val = self.eval(node.children[0])  # stat_init
            rest = self.eval(node.children[1])      # stat_init_end

            if rest is None:
                return init_val

            node.additional_vars = rest
            return init_val
        
        elif node.name == "stat_init_end":
            if not node.children:
                return []

            var_token = node.children[0]  # VAR_INIT
            var_name = var_token.value
            more_stat = node.children[1]

            val = self.eval(more_stat)
            rest = getattr(more_stat, "additional_vars", [])

            result = [(var_name, val)] + rest
            node.additional_vars = result
            return result
        
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
            # Print without space in between for formatting consistency
            print("".join(outputs), end="")

        elif node.name == "outputs":
            results = []
            for child in node.children:
                val = self.eval(child)
                results.append(val)
            return results

        elif node.name == "output":
            if node.value:
                # print(f"[OUTPUT] VAR_INIT = {node.value}")
                return str(self.env.get_var(node.value))
            elif node.children:
                val = self.eval(node.children[0])
                # print(f"[OUTPUT] Child node evaluated to: {val}")
                return str(val)
            else:
                return "[EMPTY OUTPUT]"
            
        elif node.name == "statement":
            return self.eval(node.children[0])
                
        elif node.name == "assignment_expression":
            var_token = node.children[0]
            assign_op = node.children[1].value
            rhs = self.eval(node.children[2]) 

            var_name = var_token.value
            var_type = self.env.get_type(var_name)
            self.env.set_var(var_name, rhs, var_type)
            # print(f"[SET] {var_name} = {rhs} ({var_type})")
            return rhs

        elif node.name == "follow_statement":
            pass
        
        elif node.name == "assign_operand":
            # print(f"[DEBUG] Evaluating assign_operand: {node.children[0].name}")
            val = self.eval(node.children[0])
            # print(f"[DEBUG] assign_operand evaluated to: {val}")
            return val

        elif node.name == "expression":
            val = self.eval(node.children[0])
            # print(f"[DEBUG] expression evaluated to: {val}")
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

        elif node.name == "number":
            val = node.value
            if isinstance(val, str) and val.startswith('@'):
                return self.env.get_var(val) 
            elif '.' in str(val):
                # print(f"[DEBUG] Evaluating number: {node.value}")
                return float(val)
            else:
                # print(f"[DEBUG] Evaluating number: {node.value}")
                return int(val)
            
        elif node.name == "relational_expression":
            left = self.eval(node.children[0]) 
            op = node.children[1].value
            right = self.eval(node.children[2])
            # print(f"[RELATIONAL] Evaluating: {left} {op} {right}")
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
    
        elif node.name == "number_rel_operand":
            return self.eval(node.children[0])
        
        elif node.name == "stat_rel_operand" or node.name == "chant_rel_operand":
            if node.value:
                return self.env.get_var(node.value) if node.value.startswith('@') else node.value
            else:
                return self.eval(node.children[0])

        elif node.name == "other_relational_operator":
            return node.value

        elif node.name == "relational_operator":
            # print(f"[DEBUG] Reached relational_operator with value: {node.value}")
            return node.value
        
        elif node.name == "logical_expression":
            return self.eval(node.children[0])

        elif node.name == "not_expr":
            operand = self.eval(node.children[0])
            return "Win" if operand == "Loss" else "Loss"

        elif node.name == "compound_log_expr":
            result = self.eval(node.children[0])
            op = node.children[1].value
            right = self.eval(node.children[2])

            if op == "AND":
                result = "Win" if result == "Win" and right == "Win" else "Loss"
            elif op == "OR":
                result = "Win" if result == "Win" or right == "Win" else "Loss"

            # Handle any additional AND/OR via more_log_term
            i = 3
            while i < len(node.children):
                op = node.children[i].value
                right = self.eval(node.children[i + 1])
                if op == "AND":
                    result = "Win" if result == "Win" and right == "Win" else "Loss"
                elif op == "OR":
                    result = "Win" if result == "Win" or right == "Win" else "Loss"
                i += 2

            return result

        elif node.name == "log_term":
            return self.eval(node.children[0])

        elif node.name == "other_log_term":
            return self.eval(node.children[0])

        elif node.name == "log_operator":
            return node.value

        elif node.name == "inbound_statement":
            prompt = node.children[0].value.strip('"')
            var_token = node.children[1]
            var_name = var_token.value

            expected_type = self.env.get_type(var_name)
            if not expected_type:
                raise ValueError(f"[ERROR] Variable {var_name} not declared before Inbound().")

            user_input = self.get_input(f"{prompt} ")

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
                raise ValueError(f"[TYPE ERROR] {var_name} expects {expected_type} input: {ve}")

            self.env.set_var(var_name, value, expected_type)
            # print(f"[INBOUND] {var_name} = {value} ({expected_type})")
        
        elif node.name == "dribble_statement":
            condition_result = self.eval(node.children[0])  # expression
            # print(f"[DEBUG] Dribble condition evaluated to: {condition_result}")

            if condition_result == "Win" or condition_result == True:
                self.eval(node.children[1])  # loop_statements
            else:
                if len(node.children) > 2:
                    self.eval(node.children[2])  # pass/shoot (add_condition)

        elif node.name == "add_condition":
            i = 0
            while i < len(node.children):
                keyword_node = node.children[i]
                if keyword_node.name == "Pass":
                    condition = self.eval(node.children[i + 1])
                    # print(f"[DEBUG] Pass condition evaluated to: {condition}")
                    if condition == "Win":
                        self.eval(node.children[i + 2])
                        break
                    i += 3
                elif keyword_node.name == "Shoot":
                    # print(f"[DEBUG] Executing Shoot fallback block.")
                    self.eval(node.children[i + 1])
                    break
                else:
                    # print(f"[WARN] Unknown keyword in add_condition: {keyword_node.name}")
                    break
        elif node.name == "Shoot":
            return node 

        elif node.name == "Pass":
            return node 

        elif node.name == "forward_statement":
            loop_var_token = node.children[0]  # VAR_INIT
            loop_var_name = loop_var_token.value

            # Initial value (can be VAR_INIT or literal)
            init_node = node.children[1]
            init_val = self.eval(init_node)
            self.env.set_var(loop_var_name, init_val, "Feint")
            # print(f"[FORWARD] {loop_var_name} initialized to {init_val}")

            # Condition expression
            condition_node = node.children[2]

            # Update components
            update_var_token = node.children[3]
            update_expr = node.children[4]

            # Loop body
            loop_body = node.children[5]

            while True:
                condition_val = self.eval(condition_node)
                # print(f"[FORWARD] Condition evaluated to: {condition_val}")
                if condition_val != "Win":
                    break

                # Execute loop body
                for stmt in loop_body.children:
                    result = self.eval(stmt)
                    if result == "Resume":
                        break

                # Apply update
                current_val = self.env.get_var(loop_var_name)

                if update_expr.name == "forward_inc_dec":
                    update_child = update_expr.children[0]
                    if update_child.name == "increment":
                        new_val = current_val + 1
                    elif update_child.name == "decrement":
                        new_val = current_val - 1
                    elif update_child.name == "forward_assign_operator":
                        op = update_child.value
                        operand_val = self.eval(update_expr.children[1])
                        if op == "+=":
                            new_val = current_val + operand_val
                        elif op == "-=":
                            new_val = current_val - operand_val
                    else:
                        raise RuntimeError("[FORWARD] Unknown increment/decrement operation")

                    self.env.set_var(loop_var_name, new_val, "Feint")
                    # print(f"[FORWARD] {loop_var_name} updated to {new_val}")

        elif node.name == "forward_lit":
            # forward_lit can either be a literal or a variable
            if node.value:
                val = node.value
                if isinstance(val, str) and val.startswith('@'):
                    return self.env.get_var(val)
                elif '.' in str(val):
                    return float(val)
                else:
                    return int(val)
            elif node.children:
                return self.eval(node.children[0])

        elif node.name == "loop_statements":
            for child in node.children:
                result = self.eval(child)
                if result == "Resume":
                    break

        elif node.name == "loop_statement":
            return self.eval(node.children[0])

        elif node.name == "resume_statement":
            # print("[LOOP] Resume triggered.")
            return "Resume"

        elif node.name == "literal":
            # Detect and clean up CHANTLIT values
            if isinstance(node.value, str) and node.value.startswith('"') and node.value.endswith('"'):
                return node.value.strip('"')
            return node.value

        else:
            print(f"[WARN] No eval rule for: {node.name}")
