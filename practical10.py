class Symbol:
    def __init__(self, name, symbol_type, scope_level):
        self._name = name
        self._type = symbol_type
        self._scope_level = scope_level

    def get_name(self):
        return self._name

    def display(self):
        print(f"| Name: {self._name} | Type: {self._type} | Scope: {self._scope_level} |")

class SymbolTable:
    def __init__(self):
        self._table = {}

    def add_symbol(self, sym):
        print(f"Table: Registering symbol '{sym.get_name()}'")
        # Python handles memory management (like unique_ptr in C++) automatically
        self._table[sym.get_name()] = sym

    def get_symbol(self, name):
        # Return the Symbol object if it exists, otherwise None
        return self._table.get(name, None)

class SymbolRegistrar:
    def register_symbol(self, table, name, symbol_type, scope):
        print("Registrar: Preparing to register a new symbol...")
        new_sym = Symbol(name, symbol_type, scope)
        table.add_symbol(new_sym)

if __name__ == "__main__":
    global_scope_table = SymbolTable()
    registrar = SymbolRegistrar()

    registrar.register_symbol(global_scope_table, "myVariable", "int", 1)
    registrar.register_symbol(global_scope_table, "calculate", "function", 1)

    print("\nRetrieving a symbol from the table:")
    s = global_scope_table.get_symbol("myVariable")
    if s:
        s.display()
