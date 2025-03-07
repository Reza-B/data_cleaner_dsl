# Generated from /home/h00man/University/Compiler/project/data_cleaner_dsl/grammar/DataCleaner.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DataCleanerParser import DataCleanerParser
else:
    from DataCleanerParser import DataCleanerParser

# This class defines a complete listener for a parse tree produced by DataCleanerParser.
class DataCleanerListener(ParseTreeListener):

    # Enter a parse tree produced by DataCleanerParser#start.
    def enterStart(self, ctx:DataCleanerParser.StartContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#start.
    def exitStart(self, ctx:DataCleanerParser.StartContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#program.
    def enterProgram(self, ctx:DataCleanerParser.ProgramContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#program.
    def exitProgram(self, ctx:DataCleanerParser.ProgramContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#statement.
    def enterStatement(self, ctx:DataCleanerParser.StatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#statement.
    def exitStatement(self, ctx:DataCleanerParser.StatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#loadStatement.
    def enterLoadStatement(self, ctx:DataCleanerParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#loadStatement.
    def exitLoadStatement(self, ctx:DataCleanerParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#removeRowsMissingStatement.
    def enterRemoveRowsMissingStatement(self, ctx:DataCleanerParser.RemoveRowsMissingStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#removeRowsMissingStatement.
    def exitRemoveRowsMissingStatement(self, ctx:DataCleanerParser.RemoveRowsMissingStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#fillMissingStatement.
    def enterFillMissingStatement(self, ctx:DataCleanerParser.FillMissingStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#fillMissingStatement.
    def exitFillMissingStatement(self, ctx:DataCleanerParser.FillMissingStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#normalizeStatement.
    def enterNormalizeStatement(self, ctx:DataCleanerParser.NormalizeStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#normalizeStatement.
    def exitNormalizeStatement(self, ctx:DataCleanerParser.NormalizeStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#standardizeStatement.
    def enterStandardizeStatement(self, ctx:DataCleanerParser.StandardizeStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#standardizeStatement.
    def exitStandardizeStatement(self, ctx:DataCleanerParser.StandardizeStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#logTransformStatement.
    def enterLogTransformStatement(self, ctx:DataCleanerParser.LogTransformStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#logTransformStatement.
    def exitLogTransformStatement(self, ctx:DataCleanerParser.LogTransformStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#autoCategorizeStatement.
    def enterAutoCategorizeStatement(self, ctx:DataCleanerParser.AutoCategorizeStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#autoCategorizeStatement.
    def exitAutoCategorizeStatement(self, ctx:DataCleanerParser.AutoCategorizeStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#splitDataStatement.
    def enterSplitDataStatement(self, ctx:DataCleanerParser.SplitDataStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#splitDataStatement.
    def exitSplitDataStatement(self, ctx:DataCleanerParser.SplitDataStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#removeDuplicateStatement.
    def enterRemoveDuplicateStatement(self, ctx:DataCleanerParser.RemoveDuplicateStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#removeDuplicateStatement.
    def exitRemoveDuplicateStatement(self, ctx:DataCleanerParser.RemoveDuplicateStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#dropRowStatement.
    def enterDropRowStatement(self, ctx:DataCleanerParser.DropRowStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#dropRowStatement.
    def exitDropRowStatement(self, ctx:DataCleanerParser.DropRowStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#dropColumnStatement.
    def enterDropColumnStatement(self, ctx:DataCleanerParser.DropColumnStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#dropColumnStatement.
    def exitDropColumnStatement(self, ctx:DataCleanerParser.DropColumnStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#integrateInconsistentData.
    def enterIntegrateInconsistentData(self, ctx:DataCleanerParser.IntegrateInconsistentDataContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#integrateInconsistentData.
    def exitIntegrateInconsistentData(self, ctx:DataCleanerParser.IntegrateInconsistentDataContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#encodingStatement.
    def enterEncodingStatement(self, ctx:DataCleanerParser.EncodingStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#encodingStatement.
    def exitEncodingStatement(self, ctx:DataCleanerParser.EncodingStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#handleOutliersStatement.
    def enterHandleOutliersStatement(self, ctx:DataCleanerParser.HandleOutliersStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#handleOutliersStatement.
    def exitHandleOutliersStatement(self, ctx:DataCleanerParser.HandleOutliersStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#excludeColumnsStatement.
    def enterExcludeColumnsStatement(self, ctx:DataCleanerParser.ExcludeColumnsStatementContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#excludeColumnsStatement.
    def exitExcludeColumnsStatement(self, ctx:DataCleanerParser.ExcludeColumnsStatementContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#path.
    def enterPath(self, ctx:DataCleanerParser.PathContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#path.
    def exitPath(self, ctx:DataCleanerParser.PathContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#min_val.
    def enterMin_val(self, ctx:DataCleanerParser.Min_valContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#min_val.
    def exitMin_val(self, ctx:DataCleanerParser.Min_valContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#max_val.
    def enterMax_val(self, ctx:DataCleanerParser.Max_valContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#max_val.
    def exitMax_val(self, ctx:DataCleanerParser.Max_valContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#column.
    def enterColumn(self, ctx:DataCleanerParser.ColumnContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#column.
    def exitColumn(self, ctx:DataCleanerParser.ColumnContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#option.
    def enterOption(self, ctx:DataCleanerParser.OptionContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#option.
    def exitOption(self, ctx:DataCleanerParser.OptionContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#row.
    def enterRow(self, ctx:DataCleanerParser.RowContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#row.
    def exitRow(self, ctx:DataCleanerParser.RowContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#method.
    def enterMethod(self, ctx:DataCleanerParser.MethodContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#method.
    def exitMethod(self, ctx:DataCleanerParser.MethodContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#number.
    def enterNumber(self, ctx:DataCleanerParser.NumberContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#number.
    def exitNumber(self, ctx:DataCleanerParser.NumberContext):
        pass


    # Enter a parse tree produced by DataCleanerParser#fillMethod.
    def enterFillMethod(self, ctx:DataCleanerParser.FillMethodContext):
        pass

    # Exit a parse tree produced by DataCleanerParser#fillMethod.
    def exitFillMethod(self, ctx:DataCleanerParser.FillMethodContext):
        pass



del DataCleanerParser