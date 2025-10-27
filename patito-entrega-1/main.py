from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_vars = """
        program demo1;
        var a,intro:int;
        var c:float;
        main { <stmt> } end
        """.replace("intro", "b")
    tree = parser.parse(test_vars)

    print(tree.pretty())


if __name__ == "__main__":
    main()
