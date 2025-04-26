from syntax_analyzer.ast_nodes import ASTNode

class Environment:
    def __init__(self):
        self.variables = {}

    def set_var(self, name, value, type_name=None):
        self.variables[name] = {"value": value, "type": type_name}

    def get_var(self, name):
        var = self.variables.get(name)
        if var is None:
            raise ValueError(f"[ERROR] Variable '{name}' not found.")
        return var["value"]

    def get_type(self, name):
        var = self.variables.get(name)
        if var is None:
            raise ValueError(f"[ERROR] Variable '{name}' not found.")
        return var["type"]


class Compiler:
    def __init__(self):
        self.env = Environment()
        self.input_func = None  # Default to None, will use built-in input() if not set

    def get_input(self, prompt):
        """Get user input using either the custom input function or built-in input()"""
        if self.input_func:
            return self.input_func(prompt)
        return input(prompt)
    
    def eval_arithmetic_tail(self, left, tail_node):
        if not tail_node.children:
            return left  # no more operations

        op = tail_node.name
        right = self.eval(tail_node.children[0])  # next term
        next_tail = tail_node.children[1]         # next tail

        if op == "ADD":
            result = left + right
        elif op == "SUB":
            result = left - right
        else:
            raise Exception(f"[EVAL ERROR] Unknown arithmetic tail operation: {op}")

        # continue recursively
        return self.eval_arithmetic_tail(result, next_tail)
    
    def eval_term_tail(self, left, tail_node):
        if not tail_node.children:
            return left  # no more operations

        op = tail_node.name
        right = self.eval(tail_node.children[0])  # next factor
        next_tail = tail_node.children[1]         # next tail

        if op == "MUL":
            result = left * right
        elif op == "DIV":
            result = left / right
        elif op == "MOD":
            result = left % right
        else:
            raise Exception(f"[EVAL ERROR] Unknown term tail operation: {op}")

        # continue recursively
        return self.eval_term_tail(result, next_tail)
    def eval(self, node):
        # --- Top level: PROGRAM node ---
        if node.name == "program":
            for child in node.children:
                self.eval(child)

        # --- GLOBAL_DECL: list of declarations ---
        elif node.name == "global_decl":
            for child in node.children:
                self.eval(child)

        # --- GLOBAL_DECLARATION: either a variable or constant ---
        elif node.name == "global_declaration":
            return self.eval(node.children[0])

        # --- VARIABLE_DEC: list of declarations ---
        elif node.name == "variable_dec":
            return self.eval(node.children[0])

        # --- FEINT_DEC: list of declarations ---
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

        # --- FLOAT_DEC: list of declarations ---
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

        # --- CHANT_DEC: list of declarations ---
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
 
        # --- CHANT_DEC: list of declarations ---
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

        # --- CONSTANT DECLARATION ---
        elif node.name == "const_dec":
            return self.eval(node.children[0])

        # --- FEINT_CONST: list of declarations ---
        elif node.name == "const_feint":
            var_token = node.children[0]   # VAR_INIT
            init_node = node.children[1]   # feint_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            # Set the first variable
            self.env.set_var(var_name, value, type_name="ConstFeint")

            # Set any additional variables
            for name, val in additional_constants:
                self.env.set_var(name, val, type_name="ConstFeint")

        elif node.name == "feint_const_init":
            value = self.eval(node.children[0])  # feint_const
            additional = self.eval(node.children[1])  # feint_const_end
            return value, additional

        elif node.name == "feint_const":
            return int(node.value) # Just return the literal integer

        elif node.name == "feint_const_end":
            if not node.children:
                return []  # No additional variables
            var_token = node.children[0]  # VAR_INIT
            init_node = node.children[1]  # feint_const_init

            var_name = var_token.value
            value, additional = self.eval(init_node)

            return [(var_name, value)] + additional

        # --- FLOATER_CONST: list of declarations ---
        elif node.name == "const_floater":
            var_token = node.children[0]   # VAR_INIT
            init_node = node.children[1]   # floater_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            # Set the first variable
            self.env.set_var(var_name, value, type_name="ConstFloater")

            # Set any additional variables
            for name, val in additional_constants:
                self.env.set_var(name, val, type_name="ConstFloater")
                
        elif node.name == "floater_const_init":
            value = self.eval(node.children[0])  # floater_const
            additional = self.eval(node.children[1])  # floater_const_end
            return value, additional
                        
        elif node.name == "floater_const":
            return float(node.value)  # <-- CAST to float
        
        elif node.name == "floater_const_end":
            if not node.children:
                return []  # No additional variables
            var_token = node.children[0]  # VAR_INIT
            init_node = node.children[1]  # floater_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            return [(var_name, value)] + additional_constants

        # --- CHANT_CONST: list of declarations ---
        elif node.name == "const_chant":
            var_token = node.children[0]   # VAR_INIT
            init_node = node.children[1]   # chant_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            # Set the first variable
            self.env.set_var(var_name, value, type_name="ConstChant")

            # Set any additional variables
            for name, val in additional_constants:
                self.env.set_var(name, val, type_name="ConstChant")
                
        elif node.name == "chant_const_init":
            value = self.eval(node.children[0])  # chant_const
            additional = self.eval(node.children[1])  # chant_const_end
            return value, additional

        elif node.name == "chant_const":
            return str(node.value).strip('"')  # <-- REMOVE surrounding quotes if needed

        elif node.name == "chant_const_end":
            if not node.children:
                return []  # No additional variables
            var_token = node.children[0]  # VAR_INIT
            init_node = node.children[1]  # chant_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            return [(var_name, value)] + additional_constants

        # --- STAT_CONST: list of declarations ---
        elif node.name == "const_stat":
            var_token = node.children[0]   # VAR_INIT
            init_node = node.children[1]   # stat_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            # Set the first variable
            self.env.set_var(var_name, value, type_name="ConstStat")

            # Set any additional variables
            for name, val in additional_constants:
                self.env.set_var(name, val, type_name="ConstStat")
                
        elif node.name == "stat_const_init":
            value = self.eval(node.children[0])  # stat_const
            additional = self.eval(node.children[1])  # stat_const_end
            return value, additional

        elif node.name == "stat_const":
            return self.eval(node.children[0])  # Evaluate the stat_value

        elif node.name == "stat_value":
            if node.value == "Win":
                return True
            elif node.value == "Loss":
                return False
            else:
                raise ValueError(f"[TYPE ERROR] Invalid boolean literal: {node.value}")

        elif node.name == "stat_const_end":
            if not node.children:
                return []  # No additional variables
            var_token = node.children[0]  # VAR_INIT
            init_node = node.children[1]  # stat_const_init

            var_name = var_token.value
            value, additional_constants = self.eval(init_node)

            return [(var_name, value)] + additional_constants

        elif node.name == "array_dec":
            return self.eval(node.children[0]) 

        elif node.name == "feint_array":
            var_token = node.children[0]
            first_dimension = int(node.children[1].value)
            second_dimension_node = node.children[2]
            initializer = node.children[3]

            var_name = var_token.value
            second_dimension = None

            if second_dimension_node.children:
                second_dimension = int(second_dimension_node.children[0].value)

            if initializer.children:
                data = self.eval(initializer)

                if second_dimension is None:
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 1D array initializer.")
                    print(f"[DEBUG] Storing 1D array {var_name}: {data}")
                    self.env.set_var(var_name, data, type_name="FeintArray")
                else:
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 2D array initializer.")
                    
                    total_elements = first_dimension * second_dimension
                    if len(data) != total_elements:
                        raise ValueError(f"[TYPE ERROR] Array initializer size mismatch: expected {total_elements}, got {len(data)}")

                    reshaped = []
                    for i in range(first_dimension):
                        row = data[i * second_dimension : (i + 1) * second_dimension]
                        reshaped.append(row)

                    print(f"[DEBUG] Reshaped 2D array {var_name}: {reshaped}")
                    self.env.set_var(var_name, reshaped, type_name="FeintArray2D")
            else:
                if second_dimension is None:
                    self.env.set_var(var_name, [0]*first_dimension, type_name="FeintArray")
                else:
                    self.env.set_var(var_name, [[0]*second_dimension for _ in range(first_dimension)], type_name="FeintArray2D")

        elif node.name == "2D_array":
            if not node.children:
                return None
            return int(node.children[0].value)  # Make sure it returns int not node


        elif node.name == "feint_array_init":
            if node.children:
                return self.eval(node.children[0])  # eval feint_row
            else:
                return []

        elif node.name == "feint_row":
            values = []
            for child in node.children:
                val = self.eval(child)

                if isinstance(val, list):
                    # If child is already a list (e.g., {1,2,3}), flatten it
                    values.extend(val)
                else:
                    values.append(val)
            return values

        elif node.name == "2D_feint_row":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                if isinstance(val, list):
                    evaluated.extend(val)  # Flatten again
                else:
                    evaluated.append(val)
            return evaluated

        elif node.name == "more_feint_lit":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                evaluated.append(val)
            return evaluated

        elif node.name == "feint_lit":
            return int(node.value)

        elif node.name == "floater_array":
            var_token = node.children[0]   # VAR_INIT
            first_dimension = int(node.children[1].value)  # feint_lit (used as dimension)
            second_dimension_node = node.children[2]       # 2D_array
            initializer = node.children[3]                 # floater_array_init

            var_name = var_token.value
            second_dimension = None

            # Check if second dimension is provided
            if second_dimension_node.children:
                second_dimension = int(second_dimension_node.children[0].value)

            if initializer.children:
                data = self.eval(initializer)  # should return flat list of floaters

                if second_dimension is None:
                    # 1D Floater Array
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 1D floater array initializer.")
                    self.env.set_var(var_name, data, type_name="FloaterArray")
                else:
                    # 2D Floater Array
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 2D floater array initializer.")

                    total_elements = first_dimension * second_dimension
                    if len(data) != total_elements:
                        raise ValueError(f"[TYPE ERROR] Floater array initializer size mismatch: expected {total_elements}, got {len(data)}")

                    reshaped = []
                    for i in range(first_dimension):
                        row = data[i * second_dimension : (i + 1) * second_dimension]
                        reshaped.append(row)

                    self.env.set_var(var_name, reshaped, type_name="FloaterArray2D")
            else:
                # No initializer provided
                if second_dimension is None:
                    self.env.set_var(var_name, [0.0] * first_dimension, type_name="FloaterArray")
                else:
                    self.env.set_var(var_name, [[0.0] * second_dimension for _ in range(first_dimension)], type_name="FloaterArray2D")

        elif node.name == "floater_array_init":
            if node.children:
                return self.eval(node.children[0])  # evaluate floater_row
            else:
                return []

        elif node.name == "floater_row":
            values = []
            for child in node.children:
                val = self.eval(child)

                if isinstance(val, list):
                    values.extend(val)  # flatten nested list
                else:
                    values.append(val)
            return values

        elif node.name == "2D_floater_row":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                if isinstance(val, list):
                    evaluated.extend(val)
                else:
                    evaluated.append(val)
            return evaluated

        elif node.name == "more_floater_lit":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                evaluated.append(val)
            return evaluated

        elif node.name == "floater_lit":
            return float(node.value)

        elif node.name == "chant_array":
            var_token = node.children[0]   # VAR_INIT
            first_dimension = int(node.children[1].value)  # feint_lit (used as dimension)
            second_dimension_node = node.children[2]       # 2D_array
            initializer = node.children[3]                 # chant_array_init

            var_name = var_token.value
            second_dimension = None

            # Check if second dimension is provided
            if second_dimension_node.children:
                second_dimension = int(second_dimension_node.children[0].value)

            if initializer.children:
                data = self.eval(initializer)  # should return flat list of chants (strings)

                if second_dimension is None:
                    # 1D Chant Array
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 1D chant array initializer.")
                    self.env.set_var(var_name, data, type_name="ChantArray")
                else:
                    # 2D Chant Array
                    if not isinstance(data, list):
                        raise ValueError("[TYPE ERROR] Expected list for 2D chant array initializer.")

                    total_elements = first_dimension * second_dimension
                    if len(data) != total_elements:
                        raise ValueError(f"[TYPE ERROR] Chant array initializer size mismatch: expected {total_elements}, got {len(data)}")

                    reshaped = []
                    for i in range(first_dimension):
                        row = data[i * second_dimension : (i + 1) * second_dimension]
                        reshaped.append(row)

                    self.env.set_var(var_name, reshaped, type_name="ChantArray2D")
            else:
                # No initializer provided
                if second_dimension is None:
                    self.env.set_var(var_name, [""] * first_dimension, type_name="ChantArray")
                else:
                    self.env.set_var(var_name, [[""] * second_dimension for _ in range(first_dimension)], type_name="ChantArray2D")

        elif node.name == "chant_array_init":
            if node.children:
                return self.eval(node.children[0])  # evaluate chant_row
            else:
                return []
            
        elif node.name == "chant_row":
            values = []
            for child in node.children:
                val = self.eval(child)

                if isinstance(val, list):
                    values.extend(val)  # flatten nested list
                else:
                    values.append(val)
            return values

        elif node.name == "2D_chant_row":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                if isinstance(val, list):
                    evaluated.extend(val)
                else:
                    evaluated.append(val)
            return evaluated

        elif node.name == "more_chant_lit":
            if not node.children:
                return []
            evaluated = []
            for child in node.children:
                val = self.eval(child)
                evaluated.append(val)
            return evaluated

        elif node.name == "chant_lit":
            val = node.value
            if isinstance(val, str) and val.startswith('"') and val.endswith('"'):
                return val[1:-1]  # Remove the surrounding quotes
            return str(val)

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
            if node.children:
                val = self.eval(node.children[0])
                return str(val)
            elif node.value:
                if isinstance(node.value, str) and node.value.startswith("@"):
                    var_value = self.env.get_var(node.value)
                    var_type = self.env.get_type(node.value)
                    
                    if var_type in ["Stat", "ConstStat"]:
                        return "Win" if var_value else "Loss"
                    else:
                        return str(var_value)
                else:
                    return str(node.value.strip('"'))
            else:
                return "[EMPTY OUTPUT]"

        elif node.name == "statement":
            return self.eval(node.children[0])
                
        elif node.name == "assignment_expression":
            var_token = node.children[0]
            array_access_node = node.children[1]
            assign_op = node.children[2].value 
            rhs = self.eval(node.children[3])

            var_name = var_token.value
            var_type = self.env.get_type(var_name)

            # Define operator behavior
            op_map = {
                '=':  lambda old, new: new,
                '+=': lambda old, new: old + new,
                '-=': lambda old, new: old - new,
                '*=': lambda old, new: old * new,
                '/=': lambda old, new: old / new,
                '%=': lambda old, new: old % new,
            }

            if assign_op not in op_map:
                raise ValueError(f"[EVAL ERROR] Unknown assignment operator: {assign_op}")

            if array_access_node.name == "no_array_access":
                # ---PREVENT CONSTANT REASSIGNMENT ---
                if var_type in ["ConstFeint", "ConstFloater", "ConstChant", "ConstStat"]:
                    raise ValueError(f"[ERROR] Cannot reassign to constant variable '{var_name}' ({var_type}).")

                current_val = self.env.get_var(var_name)
                new_val = op_map[assign_op](current_val, rhs)
                self.env.set_var(var_name, new_val, var_type)

            # 1D Array Assignment
            elif array_access_node.name == "array_access":
                array = self.env.get_var(var_name)
                idx = self.eval(array_access_node.children[0])

                current_val = array[idx]
                new_val = op_map[assign_op](current_val, rhs)
                array[idx] = new_val
                self.env.set_var(var_name, array)

            # 2D Array Assignment
            elif array_access_node.name == "array_access_2d":
                array = self.env.get_var(var_name)
                row_idx = self.eval(array_access_node.children[0])
                col_idx = self.eval(array_access_node.children[1])

                current_val = array[row_idx][col_idx]
                new_val = op_map[assign_op](current_val, rhs)
                array[row_idx][col_idx] = new_val
                self.env.set_var(var_name, array)

            else:
                raise ValueError(f"[EVAL ERROR] Unexpected array access node: {array_access_node.name}")

            return rhs


        elif node.name == "follow_statement":
            pass
        
        elif node.name == "assign_operand":
            # print(f"[DEBUG] Evaluating assign_operand: {node.children[0].name}")
            val = self.eval(node.children[0])
            # print(f"[DEBUG] assign_operand evaluated to: {val}")
            return val

        elif node.name == "expression":
            return self.eval(node.children[0])

        # -- Arithmetic Expressions --
        elif node.name == "arithmetic_expression":
            left = self.eval(node.children[0])  # term
            tail = node.children[1]              # arithmetic_expression_tail
            return self.eval_arithmetic_tail(left, tail)

        elif node.name == "term":
            left = self.eval(node.children[0])  # factor
            tail = node.children[1]             # term_tail
            return self.eval_term_tail(left, tail)

        # -- Relational Expressions --
        elif node.name == "relational_expression":
            left = self.eval(node.children[0])

            # Check if there is a relational_expression_tail
            if len(node.children) == 2:
                op_node = node.children[1]

                # relational_expression_tail might be empty
                if not op_node.children:
                    # No relational operator: pure arithmetic value
                    return left

                operator = op_node.name
                right = self.eval(op_node.children[0])

                if operator == "EQUAL":
                    return left == right
                elif operator == "NOT_EQUAL":
                    return left != right
                elif operator == "LESS_THAN":
                    return left < right
                elif operator == "GREATER_THAN":
                    return left > right
                elif operator == "LESS_EQUAL":
                    return left <= right
                elif operator == "GREATER_EQUAL":
                    return left >= right
                else:
                    raise Exception(f"[EVAL ERROR] Unknown relational operator: {operator}")
            else:
                # No relational tail at all
                return left


        # -- Logical Expressions --
        elif node.name == "logical_expression":
            return self.eval(node.children[0])

        elif node.name == "AND_OP":
            return self.eval(node.children[0]) and self.eval(node.children[1])

        elif node.name == "OR_OP":
            return self.eval(node.children[0]) or self.eval(node.children[1])

        elif node.name == "NOT_OP":
            return not self.eval(node.children[0])

        # -- Terms and Factors --
        elif node.name == "term":
            return self.eval(node.children[0])

        elif node.name == "factor":
            return self.eval(node.children[0])

        # -- Parenthesis (grouped expressions) --
        elif node.name == "grouped_expression":
            return self.eval(node.children[0])

        # -- Variables (@var) --
        elif node.name == "variable":
            return self.env.get_var(node.value)

        elif node.name == "array_access":
            if node.value is None:
                raise ValueError("[EVAL ERROR] array_access node is missing .value (variable name)")
            array = self.env.get_var(node.value)
            idx = self.eval(node.children[0])
            return array[idx]


        elif node.name == "array_access_2d":
            array = self.env.get_var(node.value)
            row_idx = self.eval(node.children[0])  # first element_index
            col_idx = self.eval(node.children[1])  # second element_index
            return array[row_idx][col_idx]

        # -- Tail Empty Nodes (just skip) --
        elif node.name in ["arithmetic_expression_tail", "relational_expression_tail", "logical_expression_tail", "term_tail"]:
            return None

        elif node.name == "element_index":
            val = node.value
            if isinstance(val, str) and val.startswith("@"):
                # If it's a variable (e.g., @i), fetch its value from environment
                return self.env.get_var(val)
            else:
                # Otherwise it's a literal integer (e.g., 3)
                return int(val)
            

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
                    if condition == "Win" or condition == True:
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

            # Initial value
            init_node = node.children[1]
            init_val = self.eval(init_node)
            self.env.set_var(loop_var_name, init_val, "Feint")

            # Condition expression
            condition_node = node.children[2]

            # Update components
            update_var_token = node.children[3]
            update_expr = node.children[4]

            # Loop body
            loop_body = node.children[5]

            while True:
                condition_val = self.eval(condition_node)
                if not condition_val:  # ✅ Directly check if condition fails
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
                            raise RuntimeError("[FORWARD] Unknown assign operator in update.")
                    else:
                        raise RuntimeError("[FORWARD] Unknown increment/decrement operation")

                    self.env.set_var(loop_var_name, new_val, "Feint")

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
            val = node.value

            # Handle string literal (CHANTLIT)
            if isinstance(val, str) and val.startswith('"') and val.endswith('"'):
                return val.strip('"')

            # Handle booleans WIN and LOSS
            if val == "WIN":
                return True
            elif val == "LOSS":
                return False

            # Handle numbers
            try:
                if '.' in str(val):
                    return float(val)
                else:
                    return int(val)
            except (ValueError, TypeError):
                # Fallback (return as-is if cannot parse)
                return val


        else:
            print(f"[WARN] No eval rule for: {node.name}")
