# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u008a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\5\4E\n\4\3\5\3\5\7\5I\n\5\f\5\16")
        buf.write("\5L\13\5\3\6\5\6O\n\6\3\6\6\6R\n\6\r\6\16\6S\3\7\5\7W")
        buf.write("\n\7\3\7\6\7Z\n\7\r\7\16\7[\3\7\3\7\6\7`\n\7\r\7\16\7")
        buf.write("a\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\6\24}\n\24\r\24\16\24~\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\2\2\31\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3\2\7\3\2c|\4")
        buf.write("\2\62;c|\4\2--//\3\2\62;\5\2\13\f\17\17\"\"\2\u0091\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\3\61\3\2\2\2\5\65\3\2\2\2\7D\3\2\2\2\tF\3")
        buf.write("\2\2\2\13N\3\2\2\2\rV\3\2\2\2\17c\3\2\2\2\21e\3\2\2\2")
        buf.write("\23g\3\2\2\2\25i\3\2\2\2\27k\3\2\2\2\31m\3\2\2\2\33o\3")
        buf.write("\2\2\2\35q\3\2\2\2\37s\3\2\2\2!u\3\2\2\2#w\3\2\2\2%y\3")
        buf.write("\2\2\2\'|\3\2\2\2)\u0082\3\2\2\2+\u0084\3\2\2\2-\u0086")
        buf.write("\3\2\2\2/\u0088\3\2\2\2\61\62\7X\2\2\62\63\7c\2\2\63\64")
        buf.write("\7t\2\2\64\4\3\2\2\2\65\66\7t\2\2\66\67\7g\2\2\678\7v")
        buf.write("\2\289\7w\2\29:\7t\2\2:;\7p\2\2;\6\3\2\2\2<=\7k\2\2=>")
        buf.write("\7p\2\2>E\7v\2\2?@\7h\2\2@A\7n\2\2AB\7q\2\2BC\7c\2\2C")
        buf.write("E\7v\2\2D<\3\2\2\2D?\3\2\2\2E\b\3\2\2\2FJ\t\2\2\2GI\t")
        buf.write("\3\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\n\3\2")
        buf.write("\2\2LJ\3\2\2\2MO\t\4\2\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2")
        buf.write("PR\t\5\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\f")
        buf.write("\3\2\2\2UW\t\4\2\2VU\3\2\2\2VW\3\2\2\2WY\3\2\2\2XZ\t\5")
        buf.write("\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2")
        buf.write("\2]_\7\60\2\2^`\t\5\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2")
        buf.write("ab\3\2\2\2b\16\3\2\2\2cd\7*\2\2d\20\3\2\2\2ef\7+\2\2f")
        buf.write("\22\3\2\2\2gh\7}\2\2h\24\3\2\2\2ij\7\177\2\2j\26\3\2\2")
        buf.write("\2kl\7?\2\2l\30\3\2\2\2mn\7.\2\2n\32\3\2\2\2op\7-\2\2")
        buf.write("p\34\3\2\2\2qr\7/\2\2r\36\3\2\2\2st\7,\2\2t \3\2\2\2u")
        buf.write("v\7\61\2\2v\"\3\2\2\2wx\7=\2\2x$\3\2\2\2yz\7<\2\2z&\3")
        buf.write("\2\2\2{}\t\6\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0080\3\2\2\2\u0080\u0081\b\24\2\2\u0081(\3")
        buf.write("\2\2\2\u0082\u0083\13\2\2\2\u0083*\3\2\2\2\u0084\u0085")
        buf.write("\13\2\2\2\u0085,\3\2\2\2\u0086\u0087\13\2\2\2\u0087.\3")
        buf.write("\2\2\2\u0088\u0089\13\2\2\2\u0089\60\3\2\2\2\13\2DJNS")
        buf.write("V[a~\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    RETURNKEY = 2
    TYPE = 3
    ID = 4
    INTVAL = 5
    FLOATVAL = 6
    LB = 7
    RB = 8
    LCB = 9
    RCB = 10
    ASGOP = 11
    COMMA = 12
    ADDOP = 13
    SUBOP = 14
    MULOP = 15
    DIVOP = 16
    SEMI = 17
    COLON = 18
    WS = 19
    ERROR_CHAR = 20
    UNCLOSE_STRING = 21
    ILLEGAL_ESCAPE = 22
    UNTERMINATED_COMMENT = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'return'", "'('", "')'", "'{'", "'}'", "'='", "','", 
            "'+'", "'-'", "'*'", "'/'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "RETURNKEY", "TYPE", "ID", "INTVAL", "FLOATVAL", "LB", 
            "RB", "LCB", "RCB", "ASGOP", "COMMA", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "SEMI", "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "VAR", "RETURNKEY", "TYPE", "ID", "INTVAL", "FLOATVAL", 
                  "LB", "RB", "LCB", "RCB", "ASGOP", "COMMA", "ADDOP", "SUBOP", 
                  "MULOP", "DIVOP", "SEMI", "COLON", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


