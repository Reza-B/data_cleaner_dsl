from listener.ast import AST
from listener.make_ast_subtree import make_ast_subtree

from gen.DataCleanerListener import DataCleanerListener


class CustomDataCleanerListener(DataCleanerListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['program', 'loadStatement', 'removeRowsMissingStatement', 'fillMissingStatement',
                                 'normalizeStatement', 'standardizeStatement', 'logTransformStatement',
                                 'autoCategorizeStatement', 'splitDataStatement']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitLoadStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'load', keep_node=True)

    def exitRemoveRowsMissingStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'removeRowsMissing', keep_node=True)

    def exitFillMissingStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'fillMissing', keep_node=True)

    def exitNormalizeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'normalize', keep_node=True)

    def exitStandardizeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'standardize', keep_node=True)

    def exitLogTransformStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'logTransform', keep_node=True)

    def exitAutoCategorizeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'autoCategorize', keep_node=True)

    def exitSplitDataStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, 'splitData', keep_node=True)
