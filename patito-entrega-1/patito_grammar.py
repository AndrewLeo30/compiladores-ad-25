grammar = r"""
start: programa

programa: "program" ID ";" vars? funcs? "main" body "end"

vars: VARS
funcs: FUNCS
body: BODY

// Terminales
ID: /[a-zA-Z_][a-zA-Z0-9_]*/

VARS: "vars_declaration"
FUNCS: "funcs_declaration"
BODY: "body_declaration"

// Ignored characters
%ignore /[ \t\r\n]+/
"""