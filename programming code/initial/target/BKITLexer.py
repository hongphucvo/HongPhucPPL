# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\177\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write("\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\6\2\63\n\2\r\2\16\2\64\3\3\3\3\6\39\n\3\r\3\16\3")
        buf.write(":\3\4\3\4\3\4\6\4@\n\4\r\4\16\4A\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23o\n\23\3\24\6\24r\n\24\r\24\16\24")
        buf.write("s\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\2")
        buf.write("\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\3\2\6\4\2C\\cz\4\2--//\3\2\62;\5\2\13\f\17\17\"\"")
        buf.write("\2\u0083\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\3\62\3\2\2\2\5\66\3\2\2\2\7<\3\2")
        buf.write("\2\2\tC\3\2\2\2\13E\3\2\2\2\rG\3\2\2\2\17I\3\2\2\2\21")
        buf.write("K\3\2\2\2\23M\3\2\2\2\25O\3\2\2\2\27Q\3\2\2\2\31S\3\2")
        buf.write("\2\2\33U\3\2\2\2\35W\3\2\2\2\37Y\3\2\2\2![\3\2\2\2#_\3")
        buf.write("\2\2\2%n\3\2\2\2\'q\3\2\2\2)w\3\2\2\2+y\3\2\2\2-{\3\2")
        buf.write("\2\2/}\3\2\2\2\61\63\t\2\2\2\62\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\62\3\2\2\2\64\65\3\2\2\2\65\4\3\2\2\2\668\t\3\2")
        buf.write("\2\679\t\4\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2")
        buf.write("\2;\6\3\2\2\2<=\t\3\2\2=?\7\60\2\2>@\t\4\2\2?>\3\2\2\2")
        buf.write("@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\b\3\2\2\2CD\7*\2\2D\n")
        buf.write("\3\2\2\2EF\7+\2\2F\f\3\2\2\2GH\7}\2\2H\16\3\2\2\2IJ\7")
        buf.write("\177\2\2J\20\3\2\2\2KL\7?\2\2L\22\3\2\2\2MN\7.\2\2N\24")
        buf.write("\3\2\2\2OP\7-\2\2P\26\3\2\2\2QR\7/\2\2R\30\3\2\2\2ST\7")
        buf.write(",\2\2T\32\3\2\2\2UV\7\61\2\2V\34\3\2\2\2WX\7=\2\2X\36")
        buf.write("\3\2\2\2YZ\7<\2\2Z \3\2\2\2[\\\7X\2\2\\]\7c\2\2]^\7t\2")
        buf.write("\2^\"\3\2\2\2_`\7t\2\2`a\7g\2\2ab\7v\2\2bc\7w\2\2cd\7")
        buf.write("t\2\2de\7p\2\2e$\3\2\2\2fg\7k\2\2gh\7p\2\2ho\7v\2\2ij")
        buf.write("\7h\2\2jk\7n\2\2kl\7q\2\2lm\7c\2\2mo\7v\2\2nf\3\2\2\2")
        buf.write("ni\3\2\2\2o&\3\2\2\2pr\t\5\2\2qp\3\2\2\2rs\3\2\2\2sq\3")
        buf.write("\2\2\2st\3\2\2\2tu\3\2\2\2uv\b\24\2\2v(\3\2\2\2wx\13\2")
        buf.write("\2\2x*\3\2\2\2yz\13\2\2\2z,\3\2\2\2{|\13\2\2\2|.\3\2\2")
        buf.write("\2}~\13\2\2\2~\60\3\2\2\2\b\2\64:Ans\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INTVAL = 2
    FLOATVAL = 3
    LB = 4
    RB = 5
    LCB = 6
    RCB = 7
    ASGOP = 8
    COMMA = 9
    ADDOP = 10
    SUBOP = 11
    MULOP = 12
    DIVOP = 13
    SEMI = 14
    COLON = 15
    VAR = 16
    RETURN = 17
    TYPE = 18
    WS = 19
    ERROR_CHAR = 20
    UNCLOSE_STRING = 21
    ILLEGAL_ESCAPE = 22
    UNTERMINATED_COMMENT = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'='", "','", "'+'", "'-'", "'*'", 
            "'/'", "';'", "':'", "'Var'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTVAL", "FLOATVAL", "LB", "RB", "LCB", "RCB", "ASGOP", 
            "COMMA", "ADDOP", "SUBOP", "MULOP", "DIVOP", "SEMI", "COLON", 
            "VAR", "RETURN", "TYPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "INTVAL", "FLOATVAL", "LB", "RB", "LCB", "RCB", 
                  "ASGOP", "COMMA", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "SEMI", "COLON", "VAR", "RETURN", "TYPE", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


