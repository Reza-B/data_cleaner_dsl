# Generated from C:/Users/Aidin/Desktop/Rep/data_cleaner_dsl/grammar/DataCleaner.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by DataCleanerParser#removeDuplicateStatement.
    def visitRemoveDuplicateStatement(self, ctx:DataCleanerParser.RemoveDuplicateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#dropRowStatement.
    def visitDropRowStatement(self, ctx:DataCleanerParser.DropRowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#dropColumnStatement.
    def visitDropColumnStatement(self, ctx:DataCleanerParser.DropColumnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#integrateInconsistentData.
    def visitIntegrateInconsistentData(self, ctx:DataCleanerParser.IntegrateInconsistentDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#encodingStatement.
    def visitEncodingStatement(self, ctx:DataCleanerParser.EncodingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#handleOutliersStatement.
    def visitHandleOutliersStatement(self, ctx:DataCleanerParser.HandleOutliersStatementContext):
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


    # Visit a parse tree produced by DataCleanerParser#column.
    def visitColumn(self, ctx:DataCleanerParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#option.
    def visitOption(self, ctx:DataCleanerParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#row.
    def visitRow(self, ctx:DataCleanerParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#method.
    def visitMethod(self, ctx:DataCleanerParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#number.
    def visitNumber(self, ctx:DataCleanerParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataCleanerParser#fillMethod.
    def visitFillMethod(self, ctx:DataCleanerParser.FillMethodContext):
        return self.visitChildren(ctx)



del DataCleanerParser