from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_funcs = """
        program demo2;
        void foo(x:int, y:float)[ { <stmt> } ];
        main { } end
    """
    tree = parser.parse(test_funcs)

    print(tree.pretty())


if __name__ == "__main__":
    main()
