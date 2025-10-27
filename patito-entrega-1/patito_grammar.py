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
statement: assign
         | condition
         | cycle
         | f_call
         | print_stmt                -> print_stmt

# ================== STATEMENTS ==================
# -------- ASSIGN --------
assign: ID "=" expr ";"                  -> assign

# -------- CONDITION --------
condition: "if" "(" expr ")" body ("else" body)? ";"   -> condition

# -------- CYCLE (while do) --------
cycle: "while" "(" expr ")" "do" body ";"              -> cycle

# -------- FUNCTION CALL --------
f_call: ID "(" [expr ("," expr)*] ")" ";"             -> f_call

# -------- PRINT --------
print_stmt: "print" "(" expr ("," expr)* ")" ";"              -> print_stmt

# ================== PLACEHOLDERS ==================
?expr: cte | EXPR                                            -> expr_placeholder
EXPR: /<expr>/

# ----- CTE -----
cte: CTE_INT
   | CTE_FLOAT
   | CTE_STRING

# ----- TYPE -----
type: "int" | "float"                 -> type

# ----- LEXER -----
ID: /[a-zA-Z_][a-zA-Z0-9_]*/
CTE_INT: /[0-9]+/
CTE_FLOAT: /[0-9]+\.[0-9]+/

%import common.ESCAPED_STRING -> CTE_STRING
%ignore /[ \t\r\n]+/
"""
