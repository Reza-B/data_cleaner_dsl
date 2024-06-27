# Generated from E:/university/Compiler/DataCleaner/grammar/DataCleaner.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,0,1,1,0,17,19,95,0,34,1,0,0,0,2,37,1,0,0,0,4,51,
        1,0,0,0,6,53,1,0,0,0,8,56,1,0,0,0,10,59,1,0,0,0,12,64,1,0,0,0,14,
        72,1,0,0,0,16,75,1,0,0,0,18,78,1,0,0,0,20,83,1,0,0,0,22,93,1,0,0,
        0,24,95,1,0,0,0,26,97,1,0,0,0,28,99,1,0,0,0,30,101,1,0,0,0,32,103,
        1,0,0,0,34,35,3,2,1,0,35,36,5,0,0,1,36,1,1,0,0,0,37,41,3,6,3,0,38,
        40,3,4,2,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,
        0,42,3,1,0,0,0,43,41,1,0,0,0,44,52,3,8,4,0,45,52,3,10,5,0,46,52,
        3,12,6,0,47,52,3,14,7,0,48,52,3,16,8,0,49,52,3,18,9,0,50,52,3,20,
        10,0,51,44,1,0,0,0,51,45,1,0,0,0,51,46,1,0,0,0,51,47,1,0,0,0,51,
        48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,54,5,1,0,
        0,54,55,3,22,11,0,55,7,1,0,0,0,56,57,5,2,0,0,57,58,3,30,15,0,58,
        9,1,0,0,0,59,60,5,3,0,0,60,61,3,30,15,0,61,62,5,4,0,0,62,63,3,32,
        16,0,63,11,1,0,0,0,64,65,5,5,0,0,65,66,3,30,15,0,66,67,5,6,0,0,67,
        68,3,24,12,0,68,69,5,7,0,0,69,70,3,26,13,0,70,71,5,8,0,0,71,13,1,
        0,0,0,72,73,5,9,0,0,73,74,3,30,15,0,74,15,1,0,0,0,75,76,5,10,0,0,
        76,77,3,30,15,0,77,17,1,0,0,0,78,79,5,11,0,0,79,80,3,30,15,0,80,
        81,5,12,0,0,81,82,3,28,14,0,82,19,1,0,0,0,83,84,5,13,0,0,84,85,5,
        14,0,0,85,86,3,28,14,0,86,87,5,7,0,0,87,88,5,15,0,0,88,89,3,28,14,
        0,89,90,5,7,0,0,90,91,5,16,0,0,91,92,3,28,14,0,92,21,1,0,0,0,93,
        94,5,22,0,0,94,23,1,0,0,0,95,96,5,21,0,0,96,25,1,0,0,0,97,98,5,21,
        0,0,98,27,1,0,0,0,99,100,5,21,0,0,100,29,1,0,0,0,101,102,5,20,0,
        0,102,31,1,0,0,0,103,104,7,0,0,0,104,33,1,0,0,0,2,41,51
    ]

class DataCleanerParser ( Parser ):

    grammarFileName = "DataCleaner.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'remove_rows_missing'", "'fill_missing'", 
                     "'with'", "'normalize'", "'to_range('", "','", "')'", 
                     "'standardize'", "'log_transform'", "'auto_categorize'", 
                     "'n_clusters='", "'split_data'", "'train='", "'validate='", 
                     "'test='", "'mean'", "'median'", "'mode'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "STRING", "WS", "NEWLINE", "COMMENT" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_loadStatement = 3
    RULE_removeRowsMissingStatement = 4
    RULE_fillMissingStatement = 5
    RULE_normalizeStatement = 6
    RULE_standardizeStatement = 7
    RULE_logTransformStatement = 8
    RULE_autoCategorizeStatement = 9
    RULE_splitDataStatement = 10
    RULE_path = 11
    RULE_min_val = 12
    RULE_max_val = 13
    RULE_number = 14
    RULE_column = 15
    RULE_fillMethod = 16

    ruleNames =  [ "start", "program", "statement", "loadStatement", "removeRowsMissingStatement", 
                   "fillMissingStatement", "normalizeStatement", "standardizeStatement", 
                   "logTransformStatement", "autoCategorizeStatement", "splitDataStatement", 
                   "path", "min_val", "max_val", "number", "column", "fillMethod" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    NUMBER=21
    STRING=22
    WS=23
    NEWLINE=24
    COMMENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(DataCleanerParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(DataCleanerParser.EOF, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = DataCleanerParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.program()
            self.state = 35
            self.match(DataCleanerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.LoadStatementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.StatementContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.StatementContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DataCleanerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.loadStatement()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11820) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def removeRowsMissingStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.RemoveRowsMissingStatementContext,0)


        def fillMissingStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.FillMissingStatementContext,0)


        def normalizeStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.NormalizeStatementContext,0)


        def standardizeStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.StandardizeStatementContext,0)


        def logTransformStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.LogTransformStatementContext,0)


        def autoCategorizeStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.AutoCategorizeStatementContext,0)


        def splitDataStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.SplitDataStatementContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DataCleanerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.removeRowsMissingStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.fillMissingStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.normalizeStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.standardizeStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.logTransformStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.autoCategorizeStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.splitDataStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(DataCleanerParser.PathContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_loadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStatement" ):
                listener.enterLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStatement" ):
                listener.exitLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def loadStatement(self):

        localctx = DataCleanerParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(DataCleanerParser.T__0)
            self.state = 54
            self.path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveRowsMissingStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_removeRowsMissingStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemoveRowsMissingStatement" ):
                listener.enterRemoveRowsMissingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemoveRowsMissingStatement" ):
                listener.exitRemoveRowsMissingStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveRowsMissingStatement" ):
                return visitor.visitRemoveRowsMissingStatement(self)
            else:
                return visitor.visitChildren(self)




    def removeRowsMissingStatement(self):

        localctx = DataCleanerParser.RemoveRowsMissingStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_removeRowsMissingStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(DataCleanerParser.T__1)
            self.state = 57
            self.column()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FillMissingStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def fillMethod(self):
            return self.getTypedRuleContext(DataCleanerParser.FillMethodContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_fillMissingStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFillMissingStatement" ):
                listener.enterFillMissingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFillMissingStatement" ):
                listener.exitFillMissingStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFillMissingStatement" ):
                return visitor.visitFillMissingStatement(self)
            else:
                return visitor.visitChildren(self)




    def fillMissingStatement(self):

        localctx = DataCleanerParser.FillMissingStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fillMissingStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DataCleanerParser.T__2)
            self.state = 60
            self.column()
            self.state = 61
            self.match(DataCleanerParser.T__3)
            self.state = 62
            self.fillMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalizeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def min_val(self):
            return self.getTypedRuleContext(DataCleanerParser.Min_valContext,0)


        def max_val(self):
            return self.getTypedRuleContext(DataCleanerParser.Max_valContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_normalizeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalizeStatement" ):
                listener.enterNormalizeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalizeStatement" ):
                listener.exitNormalizeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalizeStatement" ):
                return visitor.visitNormalizeStatement(self)
            else:
                return visitor.visitChildren(self)




    def normalizeStatement(self):

        localctx = DataCleanerParser.NormalizeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_normalizeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(DataCleanerParser.T__4)
            self.state = 65
            self.column()
            self.state = 66
            self.match(DataCleanerParser.T__5)
            self.state = 67
            self.min_val()
            self.state = 68
            self.match(DataCleanerParser.T__6)
            self.state = 69
            self.max_val()
            self.state = 70
            self.match(DataCleanerParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StandardizeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_standardizeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandardizeStatement" ):
                listener.enterStandardizeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandardizeStatement" ):
                listener.exitStandardizeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandardizeStatement" ):
                return visitor.visitStandardizeStatement(self)
            else:
                return visitor.visitChildren(self)




    def standardizeStatement(self):

        localctx = DataCleanerParser.StandardizeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_standardizeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(DataCleanerParser.T__8)
            self.state = 73
            self.column()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogTransformStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_logTransformStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogTransformStatement" ):
                listener.enterLogTransformStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogTransformStatement" ):
                listener.exitLogTransformStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogTransformStatement" ):
                return visitor.visitLogTransformStatement(self)
            else:
                return visitor.visitChildren(self)




    def logTransformStatement(self):

        localctx = DataCleanerParser.LogTransformStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logTransformStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DataCleanerParser.T__9)
            self.state = 76
            self.column()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutoCategorizeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def number(self):
            return self.getTypedRuleContext(DataCleanerParser.NumberContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_autoCategorizeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutoCategorizeStatement" ):
                listener.enterAutoCategorizeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutoCategorizeStatement" ):
                listener.exitAutoCategorizeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAutoCategorizeStatement" ):
                return visitor.visitAutoCategorizeStatement(self)
            else:
                return visitor.visitChildren(self)




    def autoCategorizeStatement(self):

        localctx = DataCleanerParser.AutoCategorizeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_autoCategorizeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(DataCleanerParser.T__10)
            self.state = 79
            self.column()
            self.state = 80
            self.match(DataCleanerParser.T__11)
            self.state = 81
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitDataStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.NumberContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.NumberContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_splitDataStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplitDataStatement" ):
                listener.enterSplitDataStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplitDataStatement" ):
                listener.exitSplitDataStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplitDataStatement" ):
                return visitor.visitSplitDataStatement(self)
            else:
                return visitor.visitChildren(self)




    def splitDataStatement(self):

        localctx = DataCleanerParser.SplitDataStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_splitDataStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(DataCleanerParser.T__12)
            self.state = 84
            self.match(DataCleanerParser.T__13)
            self.state = 85
            self.number()
            self.state = 86
            self.match(DataCleanerParser.T__6)
            self.state = 87
            self.match(DataCleanerParser.T__14)
            self.state = 88
            self.number()
            self.state = 89
            self.match(DataCleanerParser.T__6)
            self.state = 90
            self.match(DataCleanerParser.T__15)
            self.state = 91
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataCleanerParser.STRING, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = DataCleanerParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(DataCleanerParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Min_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DataCleanerParser.NUMBER, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_min_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin_val" ):
                listener.enterMin_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin_val" ):
                listener.exitMin_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMin_val" ):
                return visitor.visitMin_val(self)
            else:
                return visitor.visitChildren(self)




    def min_val(self):

        localctx = DataCleanerParser.Min_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_min_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(DataCleanerParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Max_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DataCleanerParser.NUMBER, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_max_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMax_val" ):
                listener.enterMax_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMax_val" ):
                listener.exitMax_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMax_val" ):
                return visitor.visitMax_val(self)
            else:
                return visitor.visitChildren(self)




    def max_val(self):

        localctx = DataCleanerParser.Max_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_max_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DataCleanerParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DataCleanerParser.NUMBER, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = DataCleanerParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(DataCleanerParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DataCleanerParser.ID, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = DataCleanerParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(DataCleanerParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FillMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataCleanerParser.RULE_fillMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFillMethod" ):
                listener.enterFillMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFillMethod" ):
                listener.exitFillMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFillMethod" ):
                return visitor.visitFillMethod(self)
            else:
                return visitor.visitChildren(self)




    def fillMethod(self):

        localctx = DataCleanerParser.FillMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fillMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





