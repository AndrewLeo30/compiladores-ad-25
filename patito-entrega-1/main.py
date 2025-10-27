from lark import Lark
from patito_grammar import grammar

def main():
    parser = Lark(grammar, start="start", parser="lalr")
    test_genral = """
    program TestGeneral;
    var x,y:int;
    void util(p:int)[ { print(p); } ];
    main {
        x = 10;
        y = x + 1 - 2 * 3;
        if ( y < 0 ) { print("neg", y); } else { util(y); } ;
        while ( y != 0 ) do { y = y - 1; } ;
        print("done", x, y);
    } end
    """
    tree = parser.parse(test_genral)

    print(tree.pretty())


if __name__ == "__main__":
    main()
