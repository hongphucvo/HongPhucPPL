# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\67\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\27\n\2\r\2\16\2\30")
        buf.write("\3\2\7\2\34\n\2\f\2\16\2\37\13\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\6\6*\n\6\r\6\16\6+\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\3\2\5\3\2cz\4\2\62;cz\5\2\13\f\17\17\"\"")
        buf.write("\29\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\3\26\3\2\2\2\5 \3\2\2\2\7\"\3\2\2\2\t$\3\2\2")
        buf.write("\2\13)\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63\3\2\2\2")
        buf.write("\23\65\3\2\2\2\25\27\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\26\3\2\2\2\30\31\3\2\2\2\31\35\3\2\2\2\32\34\t\3")
        buf.write("\2\2\33\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3")
        buf.write("\2\2\2\36\4\3\2\2\2\37\35\3\2\2\2 !\7=\2\2!\6\3\2\2\2")
        buf.write("\"#\7<\2\2#\b\3\2\2\2$%\7X\2\2%&\7c\2\2&\'\7t\2\2\'\n")
        buf.write("\3\2\2\2(*\t\4\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,-\3\2\2\2-.\b\6\2\2.\f\3\2\2\2/\60\13\2\2\2\60\16")
        buf.write("\3\2\2\2\61\62\13\2\2\2\62\20\3\2\2\2\63\64\13\2\2\2\64")
        buf.write("\22\3\2\2\2\65\66\13\2\2\2\66\24\3\2\2\2\6\2\30\35+\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8
    UNTERMINATED_COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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


