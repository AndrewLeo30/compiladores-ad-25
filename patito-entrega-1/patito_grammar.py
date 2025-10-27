grammar = r"""
start: programa

programa: "program" ID ";" vars? funcs? "main" body "end"

# ----- VARS -----
vars: var_decl+                       -> vars_block
var_decl: "var" id_list ":" type ";"  -> var_decl
id_list: ID ("," ID)*                 -> id_list

# ----- FUNCS -----
funcs: func_decl+                     -> funcs_block
func_decl: "void" ID "(" [param ("," param)*] ")" "[" vars? body "]" ";"  -> func_decl
param: ID ":" type                    -> param

# ----- BODY -----
body: "{" statement* "}"              -> body
statement: STATEMENT                  -> stmt_placeholder

# ----- TYPE -----
type: "int" | "float"                 -> type

# ----- LEXER -----
ID: /[a-zA-Z_][a-zA-Z0-9_]*/
STATEMENT: /<stmt>/                 #placeholder para tests

%ignore /[ \t\r\n]+/
"""
