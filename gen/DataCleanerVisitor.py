# Generated from E:/university/Compiler/DataCleaner/grammar/DataCleaner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataCleanerParser import DataCleanerParser
else:
    from DataCleanerParser import DataCleanerParser

# This class defines a complete generic visitor for a parse tree produced by DataCleanerParser.

class DataCleanerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DataCleanerParser#start.
    def visitStart(self, ctx:DataCleanerParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#program.
    def visitProgram(self, ctx:DataCleanerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#statement.
    def visitStatement(self, ctx:DataCleanerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#loadStatement.
    def visitLoadStatement(self, ctx:DataCleanerParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#removeRowsMissingStatement.
    def visitRemoveRowsMissingStatement(self, ctx:DataCleanerParser.RemoveRowsMissingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#fillMissingStatement.
    def visitFillMissingStatement(self, ctx:DataCleanerParser.FillMissingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#normalizeStatement.
    def visitNormalizeStatement(self, ctx:DataCleanerParser.NormalizeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#standardizeStatement.
    def visitStandardizeStatement(self, ctx:DataCleanerParser.StandardizeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#logTransformStatement.
    def visitLogTransformStatement(self, ctx:DataCleanerParser.LogTransformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#autoCategorizeStatement.
    def visitAutoCategorizeStatement(self, ctx:DataCleanerParser.AutoCategorizeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#splitDataStatement.
    def visitSplitDataStatement(self, ctx:DataCleanerParser.SplitDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#path.
    def visitPath(self, ctx:DataCleanerParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#min_val.
    def visitMin_val(self, ctx:DataCleanerParser.Min_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#max_val.
    def visitMax_val(self, ctx:DataCleanerParser.Max_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#number.
    def visitNumber(self, ctx:DataCleanerParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#column.
    def visitColumn(self, ctx:DataCleanerParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#fillMethod.
    def visitFillMethod(self, ctx:DataCleanerParser.FillMethodContext):
        return self.visitChildren(ctx)



del DataCleanerParser