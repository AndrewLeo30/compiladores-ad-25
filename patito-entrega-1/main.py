from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_condition = """
        program demoCond;
        main {
        if ( <expr> ) {
            if ( 0 ) { };
        } else {
        
        };
        } end
    """
    tree = parser.parse(test_condition)

    print(tree.pretty())


if __name__ == "__main__":
    main()
