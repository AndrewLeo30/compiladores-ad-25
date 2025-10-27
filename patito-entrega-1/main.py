from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_cycle = """
        program cycle;
        main {
        while ( <expr> ) do {
            if ( 0 ) { print("then"); } else { } ;
            while ( <expr> ) do { print("inner"); } ;
        } ;
        } end
    """
    tree = parser.parse(test_cycle)

    print(tree.pretty())


if __name__ == "__main__":
    main()
