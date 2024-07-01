# Generated from D:/University/Semester-8/Compiler/Final_Project/data_cleaner_dsl/grammar/DataCleaner.g4 by ANTLR 4.13.1
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
        4,1,36,210,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,1,1,1,5,1,60,8,1,10,1,12,1,63,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,3,1,3,1,3,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,5,12,124,8,12,10,12,12,
        12,127,9,12,1,12,1,12,1,12,1,12,1,12,1,12,4,12,135,8,12,11,12,12,
        12,136,3,12,139,8,12,3,12,141,8,12,1,13,1,13,4,13,145,8,13,11,13,
        12,13,146,1,14,1,14,4,14,151,8,14,11,14,12,14,152,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,4,15,162,8,15,11,15,12,15,163,1,15,1,15,3,15,
        168,8,15,1,15,1,15,1,15,1,16,1,16,4,16,175,8,16,11,16,12,16,176,
        1,16,1,16,3,16,181,8,16,1,16,1,16,1,16,1,17,1,17,4,17,188,8,17,11,
        17,12,17,189,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,
        23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,1,
        1,0,28,30,208,0,54,1,0,0,0,2,57,1,0,0,0,4,77,1,0,0,0,6,79,1,0,0,
        0,8,82,1,0,0,0,10,85,1,0,0,0,12,90,1,0,0,0,14,98,1,0,0,0,16,101,
        1,0,0,0,18,104,1,0,0,0,20,109,1,0,0,0,22,119,1,0,0,0,24,140,1,0,
        0,0,26,142,1,0,0,0,28,148,1,0,0,0,30,159,1,0,0,0,32,172,1,0,0,0,
        34,185,1,0,0,0,36,191,1,0,0,0,38,193,1,0,0,0,40,195,1,0,0,0,42,197,
        1,0,0,0,44,199,1,0,0,0,46,201,1,0,0,0,48,203,1,0,0,0,50,205,1,0,
        0,0,52,207,1,0,0,0,54,55,3,2,1,0,55,56,5,0,0,1,56,1,1,0,0,0,57,61,
        3,6,3,0,58,60,3,4,2,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,
        61,62,1,0,0,0,62,3,1,0,0,0,63,61,1,0,0,0,64,78,3,8,4,0,65,78,3,10,
        5,0,66,78,3,12,6,0,67,78,3,14,7,0,68,78,3,16,8,0,69,78,3,18,9,0,
        70,78,3,20,10,0,71,78,3,22,11,0,72,78,3,24,12,0,73,78,3,26,13,0,
        74,78,3,28,14,0,75,78,3,30,15,0,76,78,3,32,16,0,77,64,1,0,0,0,77,
        65,1,0,0,0,77,66,1,0,0,0,77,67,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,
        0,77,70,1,0,0,0,77,71,1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,
        1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,5,1,0,0,0,79,80,5,1,0,0,80,
        81,3,36,18,0,81,7,1,0,0,0,82,83,5,2,0,0,83,84,3,42,21,0,84,9,1,0,
        0,0,85,86,5,3,0,0,86,87,3,42,21,0,87,88,5,4,0,0,88,89,3,52,26,0,
        89,11,1,0,0,0,90,91,5,5,0,0,91,92,3,42,21,0,92,93,5,6,0,0,93,94,
        3,38,19,0,94,95,5,7,0,0,95,96,3,40,20,0,96,97,5,8,0,0,97,13,1,0,
        0,0,98,99,5,9,0,0,99,100,3,42,21,0,100,15,1,0,0,0,101,102,5,10,0,
        0,102,103,3,42,21,0,103,17,1,0,0,0,104,105,5,11,0,0,105,106,3,42,
        21,0,106,107,5,12,0,0,107,108,3,50,25,0,108,19,1,0,0,0,109,110,5,
        13,0,0,110,111,5,14,0,0,111,112,3,50,25,0,112,113,5,7,0,0,113,114,
        5,15,0,0,114,115,3,50,25,0,115,116,5,7,0,0,116,117,5,16,0,0,117,
        118,3,50,25,0,118,21,1,0,0,0,119,120,5,17,0,0,120,23,1,0,0,0,121,
        125,5,18,0,0,122,124,3,46,23,0,123,122,1,0,0,0,124,127,1,0,0,0,125,
        123,1,0,0,0,125,126,1,0,0,0,126,141,1,0,0,0,127,125,1,0,0,0,128,
        129,5,19,0,0,129,130,3,46,23,0,130,131,5,20,0,0,131,138,3,46,23,
        0,132,134,5,21,0,0,133,135,3,46,23,0,134,133,1,0,0,0,135,136,1,0,
        0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,132,1,0,
        0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,121,1,0,0,0,140,128,1,0,
        0,0,141,25,1,0,0,0,142,144,5,22,0,0,143,145,3,42,21,0,144,143,1,
        0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,27,1,0,
        0,0,148,150,5,23,0,0,149,151,3,44,22,0,150,149,1,0,0,0,151,152,1,
        0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,5,
        20,0,0,155,156,3,44,22,0,156,157,5,24,0,0,157,158,3,42,21,0,158,
        29,1,0,0,0,159,167,5,25,0,0,160,162,3,42,21,0,161,160,1,0,0,0,162,
        163,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,168,1,0,0,0,165,
        168,5,26,0,0,166,168,3,34,17,0,167,161,1,0,0,0,167,165,1,0,0,0,167,
        166,1,0,0,0,168,169,1,0,0,0,169,170,5,4,0,0,170,171,3,48,24,0,171,
        31,1,0,0,0,172,180,5,27,0,0,173,175,3,42,21,0,174,173,1,0,0,0,175,
        176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,181,1,0,0,0,178,
        181,5,26,0,0,179,181,3,34,17,0,180,174,1,0,0,0,180,178,1,0,0,0,180,
        179,1,0,0,0,181,182,1,0,0,0,182,183,5,4,0,0,183,184,3,48,24,0,184,
        33,1,0,0,0,185,187,5,21,0,0,186,188,3,42,21,0,187,186,1,0,0,0,188,
        189,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,35,1,0,0,0,191,192,
        5,33,0,0,192,37,1,0,0,0,193,194,5,32,0,0,194,39,1,0,0,0,195,196,
        5,32,0,0,196,41,1,0,0,0,197,198,5,31,0,0,198,43,1,0,0,0,199,200,
        5,31,0,0,200,45,1,0,0,0,201,202,5,32,0,0,202,47,1,0,0,0,203,204,
        5,31,0,0,204,49,1,0,0,0,205,206,5,32,0,0,206,51,1,0,0,0,207,208,
        7,0,0,0,208,53,1,0,0,0,13,61,77,125,136,138,140,146,152,163,167,
        176,180,189
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
                     "'test='", "'remove_duplicates'", "'drop_row'", "'from'", 
                     "'to'", "'exclude'", "'drop_column'", "'integrate'", 
                     "'in'", "'encode'", "'all'", "'delete_outliers'", "'mean'", 
                     "'median'", "'mode'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "STRING", "WS", "NEWLINE", "COMMENT" ]

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
    RULE_removeDuplicateStatement = 11
    RULE_dropRowStatement = 12
    RULE_dropColumnStatement = 13
    RULE_integrateInconsistentData = 14
    RULE_encodingStatement = 15
    RULE_handleOutliersStatement = 16
    RULE_excludeColumnsStatement = 17
    RULE_path = 18
    RULE_min_val = 19
    RULE_max_val = 20
    RULE_column = 21
    RULE_option = 22
    RULE_row = 23
    RULE_method = 24
    RULE_number = 25
    RULE_fillMethod = 26

    ruleNames =  [ "start", "program", "statement", "loadStatement", "removeRowsMissingStatement", 
                   "fillMissingStatement", "normalizeStatement", "standardizeStatement", 
                   "logTransformStatement", "autoCategorizeStatement", "splitDataStatement", 
                   "removeDuplicateStatement", "dropRowStatement", "dropColumnStatement", 
                   "integrateInconsistentData", "encodingStatement", "handleOutliersStatement", 
                   "excludeColumnsStatement", "path", "min_val", "max_val", 
                   "column", "option", "row", "method", "number", "fillMethod" ]

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
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    ID=31
    NUMBER=32
    STRING=33
    WS=34
    NEWLINE=35
    COMMENT=36

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
            self.state = 54
            self.program()
            self.state = 55
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
            self.state = 57
            self.loadStatement()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 181284396) != 0):
                self.state = 58
                self.statement()
                self.state = 63
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


        def removeDuplicateStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.RemoveDuplicateStatementContext,0)


        def dropRowStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.DropRowStatementContext,0)


        def dropColumnStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.DropColumnStatementContext,0)


        def integrateInconsistentData(self):
            return self.getTypedRuleContext(DataCleanerParser.IntegrateInconsistentDataContext,0)


        def encodingStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.EncodingStatementContext,0)


        def handleOutliersStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.HandleOutliersStatementContext,0)


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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.removeRowsMissingStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.fillMissingStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.normalizeStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.standardizeStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.logTransformStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.autoCategorizeStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.splitDataStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.removeDuplicateStatement()
                pass
            elif token in [18, 19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.dropRowStatement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 73
                self.dropColumnStatement()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 11)
                self.state = 74
                self.integrateInconsistentData()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 12)
                self.state = 75
                self.encodingStatement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 13)
                self.state = 76
                self.handleOutliersStatement()
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
            self.state = 79
            self.match(DataCleanerParser.T__0)
            self.state = 80
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
            self.state = 82
            self.match(DataCleanerParser.T__1)
            self.state = 83
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
            self.state = 85
            self.match(DataCleanerParser.T__2)
            self.state = 86
            self.column()
            self.state = 87
            self.match(DataCleanerParser.T__3)
            self.state = 88
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
            self.state = 90
            self.match(DataCleanerParser.T__4)
            self.state = 91
            self.column()
            self.state = 92
            self.match(DataCleanerParser.T__5)
            self.state = 93
            self.min_val()
            self.state = 94
            self.match(DataCleanerParser.T__6)
            self.state = 95
            self.max_val()
            self.state = 96
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
            self.state = 98
            self.match(DataCleanerParser.T__8)
            self.state = 99
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
            self.state = 101
            self.match(DataCleanerParser.T__9)
            self.state = 102
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
            self.state = 104
            self.match(DataCleanerParser.T__10)
            self.state = 105
            self.column()
            self.state = 106
            self.match(DataCleanerParser.T__11)
            self.state = 107
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
            self.state = 109
            self.match(DataCleanerParser.T__12)
            self.state = 110
            self.match(DataCleanerParser.T__13)
            self.state = 111
            self.number()
            self.state = 112
            self.match(DataCleanerParser.T__6)
            self.state = 113
            self.match(DataCleanerParser.T__14)
            self.state = 114
            self.number()
            self.state = 115
            self.match(DataCleanerParser.T__6)
            self.state = 116
            self.match(DataCleanerParser.T__15)
            self.state = 117
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveDuplicateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataCleanerParser.RULE_removeDuplicateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemoveDuplicateStatement" ):
                listener.enterRemoveDuplicateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemoveDuplicateStatement" ):
                listener.exitRemoveDuplicateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveDuplicateStatement" ):
                return visitor.visitRemoveDuplicateStatement(self)
            else:
                return visitor.visitChildren(self)




    def removeDuplicateStatement(self):

        localctx = DataCleanerParser.RemoveDuplicateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_removeDuplicateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(DataCleanerParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropRowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.RowContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.RowContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_dropRowStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropRowStatement" ):
                listener.enterDropRowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropRowStatement" ):
                listener.exitDropRowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropRowStatement" ):
                return visitor.visitDropRowStatement(self)
            else:
                return visitor.visitChildren(self)




    def dropRowStatement(self):

        localctx = DataCleanerParser.DropRowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dropRowStatement)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(DataCleanerParser.T__17)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 122
                    self.row()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(DataCleanerParser.T__18)
                self.state = 129
                self.row()
                self.state = 130
                self.match(DataCleanerParser.T__19)
                self.state = 131
                self.row()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 132
                    self.match(DataCleanerParser.T__20)
                    self.state = 134 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 133
                        self.row()
                        self.state = 136 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==32):
                            break



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


    class DropColumnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.ColumnContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_dropColumnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropColumnStatement" ):
                listener.enterDropColumnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropColumnStatement" ):
                listener.exitDropColumnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropColumnStatement" ):
                return visitor.visitDropColumnStatement(self)
            else:
                return visitor.visitChildren(self)




    def dropColumnStatement(self):

        localctx = DataCleanerParser.DropColumnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dropColumnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(DataCleanerParser.T__21)
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.column()
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegrateInconsistentDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.OptionContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.OptionContext,i)


        def column(self):
            return self.getTypedRuleContext(DataCleanerParser.ColumnContext,0)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_integrateInconsistentData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegrateInconsistentData" ):
                listener.enterIntegrateInconsistentData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegrateInconsistentData" ):
                listener.exitIntegrateInconsistentData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegrateInconsistentData" ):
                return visitor.visitIntegrateInconsistentData(self)
            else:
                return visitor.visitChildren(self)




    def integrateInconsistentData(self):

        localctx = DataCleanerParser.IntegrateInconsistentDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_integrateInconsistentData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(DataCleanerParser.T__22)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.option()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

            self.state = 154
            self.match(DataCleanerParser.T__19)
            self.state = 155
            self.option()
            self.state = 156
            self.match(DataCleanerParser.T__23)
            self.state = 157
            self.column()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EncodingStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(DataCleanerParser.MethodContext,0)


        def excludeColumnsStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.ExcludeColumnsStatementContext,0)


        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.ColumnContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_encodingStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEncodingStatement" ):
                listener.enterEncodingStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEncodingStatement" ):
                listener.exitEncodingStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEncodingStatement" ):
                return visitor.visitEncodingStatement(self)
            else:
                return visitor.visitChildren(self)




    def encodingStatement(self):

        localctx = DataCleanerParser.EncodingStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_encodingStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(DataCleanerParser.T__24)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 160
                    self.column()
                    self.state = 163 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                pass
            elif token in [26]:
                self.state = 165
                self.match(DataCleanerParser.T__25)
                pass
            elif token in [21]:
                self.state = 166
                self.excludeColumnsStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 169
            self.match(DataCleanerParser.T__3)
            self.state = 170
            self.method()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HandleOutliersStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(DataCleanerParser.MethodContext,0)


        def excludeColumnsStatement(self):
            return self.getTypedRuleContext(DataCleanerParser.ExcludeColumnsStatementContext,0)


        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.ColumnContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_handleOutliersStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHandleOutliersStatement" ):
                listener.enterHandleOutliersStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHandleOutliersStatement" ):
                listener.exitHandleOutliersStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHandleOutliersStatement" ):
                return visitor.visitHandleOutliersStatement(self)
            else:
                return visitor.visitChildren(self)




    def handleOutliersStatement(self):

        localctx = DataCleanerParser.HandleOutliersStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_handleOutliersStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(DataCleanerParser.T__26)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 173
                    self.column()
                    self.state = 176 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                pass
            elif token in [26]:
                self.state = 178
                self.match(DataCleanerParser.T__25)
                pass
            elif token in [21]:
                self.state = 179
                self.excludeColumnsStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 182
            self.match(DataCleanerParser.T__3)
            self.state = 183
            self.method()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExcludeColumnsStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataCleanerParser.ColumnContext)
            else:
                return self.getTypedRuleContext(DataCleanerParser.ColumnContext,i)


        def getRuleIndex(self):
            return DataCleanerParser.RULE_excludeColumnsStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcludeColumnsStatement" ):
                listener.enterExcludeColumnsStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcludeColumnsStatement" ):
                listener.exitExcludeColumnsStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExcludeColumnsStatement" ):
                return visitor.visitExcludeColumnsStatement(self)
            else:
                return visitor.visitChildren(self)




    def excludeColumnsStatement(self):

        localctx = DataCleanerParser.ExcludeColumnsStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_excludeColumnsStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(DataCleanerParser.T__20)
            self.state = 187 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 186
                self.column()
                self.state = 189 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

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
            self.rule_type = "str()"

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
        self.enterRule(localctx, 36, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
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
            self.rule_type = "id()"

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
        self.enterRule(localctx, 38, self.RULE_min_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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
            self.rule_type = "id()"

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
        self.enterRule(localctx, 40, self.RULE_max_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
            self.rule_type = "id()"

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
        self.enterRule(localctx, 42, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(DataCleanerParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = "id()"

        def ID(self):
            return self.getToken(DataCleanerParser.ID, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption" ):
                listener.enterOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption" ):
                listener.exitOption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = DataCleanerParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(DataCleanerParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = "int()"

        def NUMBER(self):
            return self.getToken(DataCleanerParser.NUMBER, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = DataCleanerParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_row)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(DataCleanerParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = "id()"

        def ID(self):
            return self.getToken(DataCleanerParser.ID, 0)

        def getRuleIndex(self):
            return DataCleanerParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = DataCleanerParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(DataCleanerParser.ID)
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
            self.rule_type = "int()"

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
        self.enterRule(localctx, 50, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(DataCleanerParser.NUMBER)
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
            self.rule_type = "str()"


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
        self.enterRule(localctx, 52, self.RULE_fillMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
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





