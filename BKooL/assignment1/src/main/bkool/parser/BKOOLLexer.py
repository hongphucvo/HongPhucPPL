# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01bc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\7\64\u0143\n\64\f\64\16\64\u0146\13\64\3\64\5\64\u0149")
        buf.write("\n\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0151\n\65\f")
        buf.write("\65\16\65\u0154\13\65\3\65\3\65\3\65\3\65\3\65\3\66\6")
        buf.write("\66\u015c\n\66\r\66\16\66\u015d\3\66\3\66\3\67\6\67\u0163")
        buf.write("\n\67\r\67\16\67\u0164\38\38\78\u0169\n8\f8\168\u016c")
        buf.write("\138\39\39\59\u0170\n9\39\69\u0173\n9\r9\169\u0174\3:")
        buf.write("\3:\5:\u0179\n:\3;\3;\3;\3<\3<\3<\5<\u0181\n<\3<\5<\u0184")
        buf.write("\n<\3=\3=\7=\u0188\n=\f=\16=\u018b\13=\3=\3=\3>\3>\3?")
        buf.write("\3?\3?\3?\3?\3?\3?\3?\3?\5?\u019a\n?\3@\3@\7@\u019e\n")
        buf.write("@\f@\16@\u01a1\13@\3A\3A\7A\u01a5\nA\fA\16A\u01a8\13A")
        buf.write("\3A\3A\3A\3A\3B\3B\7B\u01b0\nB\fB\16B\u01b3\13B\3B\5B")
        buf.write("\u01b6\nB\3B\3B\3C\3C\3C\5\u0144\u0152\u0189\2D\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2")
        buf.write("w8y9{:};\177<\u0081=\u0083>\u0085?\3\2\f\3\3\f\f\5\2\13")
        buf.write("\f\16\17\"\"\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^")
        buf.write("^\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\3\f\f")
        buf.write("\17\17\2\u01c5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2")
        buf.write("\2\5\u0089\3\2\2\2\7\u008b\3\2\2\2\t\u008f\3\2\2\2\13")
        buf.write("\u0095\3\2\2\2\r\u009d\3\2\2\2\17\u00a1\3\2\2\2\21\u00a6")
        buf.write("\3\2\2\2\23\u00ad\3\2\2\2\25\u00b3\3\2\2\2\27\u00b7\3")
        buf.write("\2\2\2\31\u00bc\3\2\2\2\33\u00c2\3\2\2\2\35\u00ca\3\2")
        buf.write("\2\2\37\u00d1\3\2\2\2!\u00d4\3\2\2\2#\u00d9\3\2\2\2%\u00de")
        buf.write("\3\2\2\2\'\u00e2\3\2\2\2)\u00e5\3\2\2\2+\u00ec\3\2\2\2")
        buf.write("-\u00ef\3\2\2\2/\u00f5\3\2\2\2\61\u00fe\3\2\2\2\63\u0105")
        buf.write("\3\2\2\2\65\u0107\3\2\2\2\67\u0109\3\2\2\29\u010b\3\2")
        buf.write("\2\2;\u010d\3\2\2\2=\u010f\3\2\2\2?\u0111\3\2\2\2A\u0113")
        buf.write("\3\2\2\2C\u0115\3\2\2\2E\u0118\3\2\2\2G\u011a\3\2\2\2")
        buf.write("I\u011c\3\2\2\2K\u011e\3\2\2\2M\u0120\3\2\2\2O\u0122\3")
        buf.write("\2\2\2Q\u0124\3\2\2\2S\u0126\3\2\2\2U\u0129\3\2\2\2W\u012c")
        buf.write("\3\2\2\2Y\u012e\3\2\2\2[\u0130\3\2\2\2]\u0133\3\2\2\2")
        buf.write("_\u0136\3\2\2\2a\u0139\3\2\2\2c\u013c\3\2\2\2e\u013e\3")
        buf.write("\2\2\2g\u0140\3\2\2\2i\u014c\3\2\2\2k\u015b\3\2\2\2m\u0162")
        buf.write("\3\2\2\2o\u0166\3\2\2\2q\u016d\3\2\2\2s\u0178\3\2\2\2")
        buf.write("u\u017a\3\2\2\2w\u017d\3\2\2\2y\u0185\3\2\2\2{\u018e\3")
        buf.write("\2\2\2}\u0199\3\2\2\2\177\u019b\3\2\2\2\u0081\u01a2\3")
        buf.write("\2\2\2\u0083\u01ad\3\2\2\2\u0085\u01b9\3\2\2\2\u0087\u0088")
        buf.write("\7]\2\2\u0088\4\3\2\2\2\u0089\u008a\7_\2\2\u008a\6\3\2")
        buf.write("\2\2\u008b\u008c\7p\2\2\u008c\u008d\7k\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\b\3\2\2\2\u008f\u0090\7e\2\2\u0090\u0091")
        buf.write("\7n\2\2\u0091\u0092\7c\2\2\u0092\u0093\7u\2\2\u0093\u0094")
        buf.write("\7u\2\2\u0094\n\3\2\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7z\2\2\u0097\u0098\7v\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7f\2\2\u009b\u009c\7u\2\2\u009c\f")
        buf.write("\3\2\2\2\u009d\u009e\7p\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7y\2\2\u00a0\16\3\2\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7j\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7u\2\2\u00a5\20")
        buf.write("\3\2\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\24\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\26\3\2\2\2\u00b7\u00b8")
        buf.write("\7x\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7f\2\2\u00bb\30\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\32\3\2\2\2\u00c2\u00c3\7d\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7p\2\2\u00c9\34")
        buf.write("\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7i\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7h\2\2\u00d3 \3\2\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7n\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7g\2\2\u00d8\"")
        buf.write("\3\2\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7j\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7p\2\2\u00dd$\3\2\2\2\u00de\u00df")
        buf.write("\7h\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7t\2\2\u00e1&\3")
        buf.write("\2\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7q\2\2\u00e4(\3")
        buf.write("\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7y\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb*\3\2\2\2\u00ec\u00ed\7f\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee,\3\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7m\2\2\u00f4.\3\2\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\60\3\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7v\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7p\2\2\u0104\62\3\2\2\2\u0105\u0106")
        buf.write("\7*\2\2\u0106\64\3\2\2\2\u0107\u0108\7+\2\2\u0108\66\3")
        buf.write("\2\2\2\u0109\u010a\7}\2\2\u010a8\3\2\2\2\u010b\u010c\7")
        buf.write("\177\2\2\u010c:\3\2\2\2\u010d\u010e\7=\2\2\u010e<\3\2")
        buf.write("\2\2\u010f\u0110\7<\2\2\u0110>\3\2\2\2\u0111\u0112\7.")
        buf.write("\2\2\u0112@\3\2\2\2\u0113\u0114\7\60\2\2\u0114B\3\2\2")
        buf.write("\2\u0115\u0116\7<\2\2\u0116\u0117\7?\2\2\u0117D\3\2\2")
        buf.write("\2\u0118\u0119\7?\2\2\u0119F\3\2\2\2\u011a\u011b\7-\2")
        buf.write("\2\u011bH\3\2\2\2\u011c\u011d\7/\2\2\u011dJ\3\2\2\2\u011e")
        buf.write("\u011f\7,\2\2\u011fL\3\2\2\2\u0120\u0121\7\61\2\2\u0121")
        buf.write("N\3\2\2\2\u0122\u0123\7^\2\2\u0123P\3\2\2\2\u0124\u0125")
        buf.write("\7\'\2\2\u0125R\3\2\2\2\u0126\u0127\7#\2\2\u0127\u0128")
        buf.write("\7?\2\2\u0128T\3\2\2\2\u0129\u012a\7?\2\2\u012a\u012b")
        buf.write("\7?\2\2\u012bV\3\2\2\2\u012c\u012d\7>\2\2\u012dX\3\2\2")
        buf.write("\2\u012e\u012f\7@\2\2\u012fZ\3\2\2\2\u0130\u0131\7>\2")
        buf.write("\2\u0131\u0132\7?\2\2\u0132\\\3\2\2\2\u0133\u0134\7@\2")
        buf.write("\2\u0134\u0135\7?\2\2\u0135^\3\2\2\2\u0136\u0137\7~\2")
        buf.write("\2\u0137\u0138\7~\2\2\u0138`\3\2\2\2\u0139\u013a\7(\2")
        buf.write("\2\u013a\u013b\7(\2\2\u013bb\3\2\2\2\u013c\u013d\7#\2")
        buf.write("\2\u013dd\3\2\2\2\u013e\u013f\7`\2\2\u013ff\3\2\2\2\u0140")
        buf.write("\u0144\7%\2\2\u0141\u0143\13\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\u0146\3\2\2\2\u0144\u0145\3\2\2\2\u0144\u0142\3")
        buf.write("\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0149")
        buf.write("\t\2\2\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\b\64\2\2\u014bh\3\2\2\2\u014c\u014d\7\61\2\2\u014d")
        buf.write("\u014e\7,\2\2\u014e\u0152\3\2\2\2\u014f\u0151\13\2\2\2")
        buf.write("\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0153\3")
        buf.write("\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0155\u0156\7,\2\2\u0156\u0157\7\61\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\b\65\2\2\u0159j\3\2\2\2\u015a")
        buf.write("\u015c\t\3\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0160\b\66\2\2\u0160l\3\2\2\2\u0161\u0163")
        buf.write("\t\4\2\2\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165n\3\2\2\2\u0166")
        buf.write("\u016a\7\60\2\2\u0167\u0169\t\4\2\2\u0168\u0167\3\2\2")
        buf.write("\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016bp\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016f")
        buf.write("\t\5\2\2\u016e\u0170\t\6\2\2\u016f\u016e\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u0173\t\4\2\2")
        buf.write("\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0172\3")
        buf.write("\2\2\2\u0174\u0175\3\2\2\2\u0175r\3\2\2\2\u0176\u0179")
        buf.write("\n\7\2\2\u0177\u0179\5u;\2\u0178\u0176\3\2\2\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179t\3\2\2\2\u017a\u017b\7^\2\2\u017b\u017c")
        buf.write("\t\b\2\2\u017cv\3\2\2\2\u017d\u0183\5m\67\2\u017e\u0184")
        buf.write("\5o8\2\u017f\u0181\5o8\2\u0180\u017f\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\5q9\2\u0183\u017e")
        buf.write("\3\2\2\2\u0183\u0180\3\2\2\2\u0184x\3\2\2\2\u0185\u0189")
        buf.write("\7$\2\2\u0186\u0188\5s:\2\u0187\u0186\3\2\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7$\2\2")
        buf.write("\u018dz\3\2\2\2\u018e\u018f\5m\67\2\u018f|\3\2\2\2\u0190")
        buf.write("\u0191\7v\2\2\u0191\u0192\7t\2\2\u0192\u0193\7w\2\2\u0193")
        buf.write("\u019a\7g\2\2\u0194\u0195\7h\2\2\u0195\u0196\7c\2\2\u0196")
        buf.write("\u0197\7n\2\2\u0197\u0198\7u\2\2\u0198\u019a\7g\2\2\u0199")
        buf.write("\u0190\3\2\2\2\u0199\u0194\3\2\2\2\u019a~\3\2\2\2\u019b")
        buf.write("\u019f\t\t\2\2\u019c\u019e\t\n\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u0080\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a6")
        buf.write("\7$\2\2\u01a3\u01a5\5s:\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01aa\7^\2\2")
        buf.write("\u01aa\u01ab\n\b\2\2\u01ab\u01ac\bA\3\2\u01ac\u0082\3")
        buf.write("\2\2\2\u01ad\u01b1\7$\2\2\u01ae\u01b0\5s:\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b6\t\13\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b8\bB\4\2\u01b8\u0084\3\2\2\2\u01b9")
        buf.write("\u01ba\13\2\2\2\u01ba\u01bb\bC\5\2\u01bb\u0086\3\2\2\2")
        buf.write("\24\2\u0144\u0148\u0152\u015d\u0164\u016a\u016f\u0174")
        buf.write("\u0178\u0180\u0183\u0189\u0199\u019f\u01a6\u01b1\u01b5")
        buf.write("\6\b\2\2\3A\2\3B\3\3C\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    CLASS = 4
    EXTEND = 5
    NEW = 6
    SELF = 7
    STATIC = 8
    MUTABLE = 9
    INTTYPE = 10
    VOIDTYPE = 11
    FLOATTYPE = 12
    BOOLTYPE = 13
    STRINGTYPE = 14
    IF = 15
    ELSE = 16
    THEN = 17
    FOR = 18
    TO = 19
    DOWNTO = 20
    DO = 21
    BREAK = 22
    CONT = 23
    RETURN = 24
    LB = 25
    RB = 26
    LP = 27
    RP = 28
    SEMI = 29
    COLON = 30
    COMMA = 31
    DOT = 32
    ASGOP = 33
    ASG = 34
    ADD = 35
    SUB = 36
    MUL = 37
    FLOATDIV = 38
    INTDIV = 39
    MOD = 40
    NEQ = 41
    EQ = 42
    LT = 43
    GT = 44
    LEQ = 45
    GEQ = 46
    OR = 47
    AND = 48
    NOT = 49
    CON = 50
    LINECMT = 51
    BLOCKCMT = 52
    WS = 53
    FLOATLIT = 54
    STRINGLIT = 55
    INTLIT = 56
    BOOLLIT = 57
    ID = 58
    ILLEGAL_ESCAPE = 59
    UNCLOSE_STRING = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'nil'", "'class'", "'extends'", "'new'", "'this'", 
            "'static'", "'final'", "'int'", "'void'", "'float'", "'boolean'", 
            "'string'", "'if'", "'else'", "'then'", "'for'", "'to'", "'downto'", 
            "'do'", "'break'", "'continue'", "'return'", "'('", "')'", "'{'", 
            "'}'", "';'", "':'", "','", "'.'", "':='", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", 
            "'>='", "'||'", "'&&'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "EXTEND", "NEW", "SELF", "STATIC", "MUTABLE", "INTTYPE", 
            "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "IF", "ELSE", 
            "THEN", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONT", "RETURN", 
            "LB", "RB", "LP", "RP", "SEMI", "COLON", "COMMA", "DOT", "ASGOP", 
            "ASG", "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", 
            "EQ", "LT", "GT", "LEQ", "GEQ", "OR", "AND", "NOT", "CON", "LINECMT", 
            "BLOCKCMT", "WS", "FLOATLIT", "STRINGLIT", "INTLIT", "BOOLLIT", 
            "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "CLASS", "EXTEND", "NEW", "SELF", 
                  "STATIC", "MUTABLE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", 
                  "BOOLTYPE", "STRINGTYPE", "IF", "ELSE", "THEN", "FOR", 
                  "TO", "DOWNTO", "DO", "BREAK", "CONT", "RETURN", "LB", 
                  "RB", "LP", "RP", "SEMI", "COLON", "COMMA", "DOT", "ASGOP", 
                  "ASG", "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", 
                  "NEQ", "EQ", "LT", "GT", "LEQ", "GEQ", "OR", "AND", "NOT", 
                  "CON", "LINECMT", "BLOCKCMT", "WS", "IntegerPart", "DecimalPart", 
                  "ExponentPart", "Char", "EscapeStr", "FLOATLIT", "STRINGLIT", 
                  "INTLIT", "BOOLLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text[0:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                if self.text[-1] in ["\n","\r"] :
                                    raise UncloseString(self.text[0:-1])
                                else: raise UncloseString(self.text[0:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


