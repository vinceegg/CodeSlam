class ASTNode:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children if children is not None else []
        self.value = value

    def __repr__(self):
        return self.pretty()

    def pretty(self, indent=0):
        pad = '  ' * indent
        val_str = f": {self.value}" if self.value is not None else ""
        result = f"{pad}{self.name}{val_str}\n"
        for child in self.children:
            if isinstance(child, ASTNode):
                result += child.pretty(indent + 1)
            else:
                result += f"{'  ' * (indent + 1)}{repr(child)}\n"
        return result
