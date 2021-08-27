# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u00ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3\66\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\5\5@\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7M\n\7\3\b\3\b\3\b\3\b\3\b\5\bT\n\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\ff\n\f\3\r\3\r\3\r\3\r\3\r\5\rm\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u0081\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u0088\n\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u0090\n\23\f\23\16\23\u0093\13\23\3\24\3\24")
        buf.write("\5\24\u0097\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u009e\n")
        buf.write("\25\3\26\3\26\3\27\3\27\3\27\5\27\u00a5\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\2\3$\31\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\2\4\3\2\16\17\3\2\3\5\2\u00a3\2\60")
        buf.write("\3\2\2\2\4\65\3\2\2\2\6\67\3\2\2\2\b?\3\2\2\2\nA\3\2\2")
        buf.write("\2\fL\3\2\2\2\16S\3\2\2\2\20U\3\2\2\2\22X\3\2\2\2\24\\")
        buf.write("\3\2\2\2\26e\3\2\2\2\30l\3\2\2\2\32n\3\2\2\2\34r\3\2\2")
        buf.write("\2\36w\3\2\2\2 \u0080\3\2\2\2\"\u0087\3\2\2\2$\u0089\3")
        buf.write("\2\2\2&\u0096\3\2\2\2(\u009d\3\2\2\2*\u009f\3\2\2\2,\u00a4")
        buf.write("\3\2\2\2.\u00a6\3\2\2\2\60\61\5\4\3\2\61\62\7\2\2\3\62")
        buf.write("\3\3\2\2\2\63\66\5\6\4\2\64\66\5\n\6\2\65\63\3\2\2\2\65")
        buf.write("\64\3\2\2\2\66\5\3\2\2\2\678\7\24\2\289\5\b\5\29:\7\20")
        buf.write("\2\2:\7\3\2\2\2;<\7\3\2\2<=\7\13\2\2=@\5\b\5\2>@\7\3\2")
        buf.write("\2?;\3\2\2\2?>\3\2\2\2@\t\3\2\2\2AB\7\24\2\2BC\7\3\2\2")
        buf.write("CD\5\f\7\2DE\5\24\13\2E\13\3\2\2\2FG\7\6\2\2GH\5\16\b")
        buf.write("\2HI\7\7\2\2IM\3\2\2\2JK\7\6\2\2KM\7\7\2\2LF\3\2\2\2L")
        buf.write("J\3\2\2\2M\r\3\2\2\2NO\5\20\t\2OP\7\20\2\2PQ\5\16\b\2")
        buf.write("QT\3\2\2\2RT\5\20\t\2SN\3\2\2\2SR\3\2\2\2T\17\3\2\2\2")
        buf.write("UV\7\24\2\2VW\5\b\5\2W\21\3\2\2\2XY\7\24\2\2YZ\7\3\2\2")
        buf.write("Z[\7\13\2\2[\23\3\2\2\2\\]\7\b\2\2]^\5\26\f\2^_\7\t\2")
        buf.write("\2_\25\3\2\2\2`a\5\30\r\2ab\5\26\f\2bf\3\2\2\2cf\5\30")
        buf.write("\r\2df\3\2\2\2e`\3\2\2\2ec\3\2\2\2ed\3\2\2\2f\27\3\2\2")
        buf.write("\2gm\5\32\16\2hm\5\34\17\2ij\5\36\20\2jk\7\20\2\2km\3")
        buf.write("\2\2\2lg\3\2\2\2lh\3\2\2\2li\3\2\2\2m\31\3\2\2\2no\7\3")
        buf.write("\2\2op\7\n\2\2pq\5 \21\2q\33\3\2\2\2rs\7\3\2\2st\7\6\2")
        buf.write("\2tu\5&\24\2uv\7\7\2\2v\35\3\2\2\2wx\7\23\2\2xy\5 \21")
        buf.write("\2y\37\3\2\2\2z{\5\"\22\2{|\7\f\2\2|}\5 \21\2}\u0081\3")
        buf.write("\2\2\2~\u0081\5\"\22\2\177\u0081\5\"\22\2\u0080z\3\2\2")
        buf.write("\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081!\3\2\2\2\u0082")
        buf.write("\u0083\5$\23\2\u0083\u0084\7\r\2\2\u0084\u0085\5\"\22")
        buf.write("\2\u0085\u0088\3\2\2\2\u0086\u0088\5$\23\2\u0087\u0082")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088#\3\2\2\2\u0089\u008a")
        buf.write("\b\23\1\2\u008a\u008b\5,\27\2\u008b\u0091\3\2\2\2\u008c")
        buf.write("\u008d\f\4\2\2\u008d\u008e\t\2\2\2\u008e\u0090\5,\27\2")
        buf.write("\u008f\u008c\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092%\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0094\u0097\5(\25\2\u0095\u0097\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\'\3\2\2\2\u0098")
        buf.write("\u0099\5*\26\2\u0099\u009a\7\13\2\2\u009a\u009b\5(\25")
        buf.write("\2\u009b\u009e\3\2\2\2\u009c\u009e\5*\26\2\u009d\u0098")
        buf.write("\3\2\2\2\u009d\u009c\3\2\2\2\u009e)\3\2\2\2\u009f\u00a0")
        buf.write("\t\3\2\2\u00a0+\3\2\2\2\u00a1\u00a5\5*\26\2\u00a2\u00a5")
        buf.write("\5\34\17\2\u00a3\u00a5\5.\30\2\u00a4\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5-\3\2\2\2\u00a6")
        buf.write("\u00a7\7\6\2\2\u00a7\u00a8\5 \21\2\u00a8\u00a9\7\7\2\2")
        buf.write("\u00a9/\3\2\2\2\16\65?LSel\u0080\u0087\u0091\u0096\u009d")
        buf.write("\u00a4")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'='", "','", "'+'", "'-'", 
                     "'*'", "'/'", "';'", "':'", "'Var'", "'return'" ]

    symbolicNames = [ "<INVALID>", "ID", "INTVAL", "FLOATVAL", "LB", "RB", 
                      "LCB", "RCB", "ASGOP", "COMMA", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "SEMI", "COLON", "VAR", "RETURN", 
                      "TYPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable = 2
    RULE_idlist = 3
    RULE_function = 4
    RULE_paramdcl = 5
    RULE_paramlist = 6
    RULE_params = 7
    RULE_param = 8
    RULE_body = 9
    RULE_statements = 10
    RULE_statement = 11
    RULE_assignment = 12
    RULE_call = 13
    RULE_returnstate = 14
    RULE_exp = 15
    RULE_exp1 = 16
    RULE_exp2 = 17
    RULE_vallist = 18
    RULE_values = 19
    RULE_val = 20
    RULE_operand = 21
    RULE_subexp = 22

    ruleNames =  [ "program", "declaration", "variable", "idlist", "function", 
                   "paramdcl", "paramlist", "params", "param", "body", "statements", 
                   "statement", "assignment", "call", "returnstate", "exp", 
                   "exp1", "exp2", "vallist", "values", "val", "operand", 
                   "subexp" ]

    EOF = Token.EOF
    ID=1
    INTVAL=2
    FLOATVAL=3
    LB=4
    RB=5
    LCB=6
    RCB=7
    ASGOP=8
    COMMA=9
    ADDOP=10
    SUBOP=11
    MULOP=12
    DIVOP=13
    SEMI=14
    COLON=15
    VAR=16
    RETURN=17
    TYPE=18
    WS=19
    ERROR_CHAR=20
    UNCLOSE_STRING=21
    ILLEGAL_ESCAPE=22
    UNTERMINATED_COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(BKITParser.DeclarationContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.declaration()
            self.state = 47
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def function(self):
            return self.getTypedRuleContext(BKITParser.FunctionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BKITParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKITParser.TYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(BKITParser.TYPE)
            self.state = 54
            self.idlist()
            self.state = 55
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKITParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(BKITParser.ID)
                self.state = 58
                self.match(BKITParser.COMMA)
                self.state = 59
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKITParser.TYPE, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def paramdcl(self):
            return self.getTypedRuleContext(BKITParser.ParamdclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = BKITParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(BKITParser.TYPE)
            self.state = 64
            self.match(BKITParser.ID)
            self.state = 65
            self.paramdcl()
            self.state = 66
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKITParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_paramdcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdcl" ):
                return visitor.visitParamdcl(self)
            else:
                return visitor.visitChildren(self)




    def paramdcl(self):

        localctx = BKITParser.ParamdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramdcl)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(BKITParser.LB)
                self.state = 69
                self.paramlist()
                self.state = 70
                self.match(BKITParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(BKITParser.LB)
                self.state = 73
                self.match(BKITParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(BKITParser.ParamsContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKITParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKITParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.params()
                self.state = 77
                self.match(BKITParser.SEMI)
                self.state = 78
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKITParser.TYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKITParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(BKITParser.TYPE)
            self.state = 84
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKITParser.TYPE, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BKITParser.TYPE)
            self.state = 87
            self.match(BKITParser.ID)
            self.state = 88
            self.match(BKITParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def statements(self):
            return self.getTypedRuleContext(BKITParser.StatementsContext,0)


        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKITParser.LCB)
            self.state = 91
            self.statements()
            self.state = 92
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKITParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(BKITParser.StatementsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BKITParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statements)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.statement()
                self.state = 95
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BKITParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(BKITParser.ReturnstateContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.returnstate()
                self.state = 104
                self.match(BKITParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASGOP(self):
            return self.getToken(BKITParser.ASGOP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BKITParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BKITParser.ID)
            self.state = 109
            self.match(BKITParser.ASGOP)
            self.state = 110
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def vallist(self):
            return self.getTypedRuleContext(BKITParser.VallistContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BKITParser.ID)
            self.state = 113
            self.match(BKITParser.LB)
            self.state = 114
            self.vallist()
            self.state = 115
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstate" ):
                return visitor.visitReturnstate(self)
            else:
                return visitor.visitChildren(self)




    def returnstate(self):

        localctx = BKITParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKITParser.RETURN)
            self.state = 118
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ADDOP(self):
            return self.getToken(BKITParser.ADDOP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.exp1()
                self.state = 121
                self.match(BKITParser.ADDOP)
                self.state = 122
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKITParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp1)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.exp2(0)
                self.state = 129
                self.match(BKITParser.SUBOP)
                self.state = 130
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def MULOP(self):
            return self.getToken(BKITParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(BKITParser.DIVOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 138
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 139
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.MULOP or _la==BKITParser.DIVOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 140
                    self.operand() 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VallistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self):
            return self.getTypedRuleContext(BKITParser.ValuesContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVallist" ):
                return visitor.visitVallist(self)
            else:
                return visitor.visitChildren(self)




    def vallist(self):

        localctx = BKITParser.VallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_vallist)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INTVAL, BKITParser.FLOATVAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.values()
                pass
            elif token in [BKITParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ValuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self):
            return self.getTypedRuleContext(BKITParser.ValContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def values(self):
            return self.getTypedRuleContext(BKITParser.ValuesContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = BKITParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_values)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.val()
                self.state = 151
                self.match(BKITParser.COMMA)
                self.state = 152
                self.values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INTVAL(self):
            return self.getToken(BKITParser.INTVAL, 0)

        def FLOATVAL(self):
            return self.getToken(BKITParser.FLOATVAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)




    def val(self):

        localctx = BKITParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTVAL) | (1 << BKITParser.FLOATVAL))) != 0)):
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


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self):
            return self.getTypedRuleContext(BKITParser.ValContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def subexp(self):
            return self.getTypedRuleContext(BKITParser.SubexpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operand)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.subexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_subexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexp" ):
                return visitor.visitSubexp(self)
            else:
                return visitor.visitChildren(self)




    def subexp(self):

        localctx = BKITParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKITParser.LB)
            self.state = 165
            self.exp()
            self.state = 166
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.exp2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




