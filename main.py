from antlr4 import *
import argparse

# Lexer and Parser
from gen.DataCleanerLexer import DataCleanerLexer
from gen.DataCleanerParser import DataCleanerParser

# AST
from listener.ast_to_networkx_graph import show_ast
from listener.post_order_ast_traverser import PostOrderASTTraverser

# Listener
from listener.DataCleanerListener import CustomDataCleanerListener
from listener.DataCleanerCodeGenerator import DataCleanerCodeGenerator


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')

    lexer = DataCleanerLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = DataCleanerParser(token_stream)
    parse_tree = parser.program()

    ast_builder_listener = CustomDataCleanerListener(parser.ruleNames)

    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)
    ast = ast_builder_listener.ast

    show_ast(ast.root)

    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label', 'text', 'number', "children"]
    traversal = post_order_ast_traverser.traverse_ast(ast.root)

    code_generator = DataCleanerCodeGenerator()
    generated_code = code_generator.generate_code(traversal)

    with open(arguments.output, 'w') as output_file:
        output_file.write(generated_code)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'test.datacleaner')
    argparser.add_argument('-o', '--output', help='Output path', default=r'output.py')
    args = argparser.parse_args()
    main(args)
