# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\5\5t\n\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\5\6|\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u008e\n\b\3\t\3\t\3\t\3\t\5\t\u0094\n\t\3\n\3\n\5\n\u0098")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00a6\n\f\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00b6\n\20\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00bc\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00c5\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\24\3\24\5\24\u00cd\n\24\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00d7\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u00df\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u00e6")
        buf.write("\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u00ef\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u00ff\n\35\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \5 \u010b\n \3!\3!\3!\3!\3!\5!\u0112")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u011d\n\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u0130\n#\3$\3$\3$\3$\3$\5$\u0137\n$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\7%\u0141\n%\f%\16%\u0144\13%\3&\3&\3&\5&\u0149")
        buf.write("\n&\3\'\3\'\3\'\3\'\5\'\u014f\n\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\5(\u015a\n(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u0168\n*\3*\3*\3*\3*\3*\5*\u016f\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\5+\u0177\n+\3,\3,\5,\u017b\n,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u0187\n,\3,\3,\3,\5,\u018c\n,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u019a\n-\3.\3.\3.\3.\3.\3")
        buf.write(".\5.\u01a2\n.\3/\3/\3/\3/\3/\3/\3/\5/\u01ab\n/\3\60\5")
        buf.write("\60\u01ae\n\60\3\60\3\60\3\60\3\60\5\60\u01b4\n\60\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u01ba\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01d6\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u01e3\n\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\5\64\u01ee\n\64\3\64\2\3H\65")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\13\3\2\f\r\3\2\f\20")
        buf.write("\4\289;<\3\2-\60\3\2+,\3\2\61\62\3\2%&\3\2\'*\3\2\25\26")
        buf.write("\2\u0200\2h\3\2\2\2\4k\3\2\2\2\6m\3\2\2\2\bp\3\2\2\2\n")
        buf.write("{\3\2\2\2\f\u0085\3\2\2\2\16\u008d\3\2\2\2\20\u0093\3")
        buf.write("\2\2\2\22\u0097\3\2\2\2\24\u0099\3\2\2\2\26\u00a5\3\2")
        buf.write("\2\2\30\u00aa\3\2\2\2\32\u00ac\3\2\2\2\34\u00ae\3\2\2")
        buf.write("\2\36\u00b5\3\2\2\2 \u00bb\3\2\2\2\"\u00c4\3\2\2\2$\u00c6")
        buf.write("\3\2\2\2&\u00cc\3\2\2\2(\u00ce\3\2\2\2*\u00d6\3\2\2\2")
        buf.write(",\u00de\3\2\2\2.\u00e5\3\2\2\2\60\u00e7\3\2\2\2\62\u00ee")
        buf.write("\3\2\2\2\64\u00f0\3\2\2\2\66\u00f5\3\2\2\28\u00fe\3\2")
        buf.write("\2\2:\u0100\3\2\2\2<\u0102\3\2\2\2>\u010a\3\2\2\2@\u0111")
        buf.write("\3\2\2\2B\u011c\3\2\2\2D\u012f\3\2\2\2F\u0136\3\2\2\2")
        buf.write("H\u0138\3\2\2\2J\u0148\3\2\2\2L\u014e\3\2\2\2N\u0159\3")
        buf.write("\2\2\2P\u015b\3\2\2\2R\u016e\3\2\2\2T\u0176\3\2\2\2V\u018b")
        buf.write("\3\2\2\2X\u0199\3\2\2\2Z\u01a1\3\2\2\2\\\u01aa\3\2\2\2")
        buf.write("^\u01b3\3\2\2\2`\u01b9\3\2\2\2b\u01e2\3\2\2\2d\u01e4\3")
        buf.write("\2\2\2f\u01ed\3\2\2\2hi\5\n\6\2ij\7\2\2\3j\3\3\2\2\2k")
        buf.write("l\t\2\2\2l\5\3\2\2\2mn\5\b\5\2no\7\37\2\2o\7\3\2\2\2p")
        buf.write("q\7:\2\2qs\7\33\2\2rt\5B\"\2sr\3\2\2\2st\3\2\2\2tu\3\2")
        buf.write("\2\2uv\7\34\2\2v\t\3\2\2\2wx\5\f\7\2xy\5\n\6\2y|\3\2\2")
        buf.write("\2z|\5\f\7\2{w\3\2\2\2{z\3\2\2\2|\13\3\2\2\2}~\7\6\2\2")
        buf.write("~\177\7:\2\2\177\u0086\5\16\b\2\u0080\u0081\7\6\2\2\u0081")
        buf.write("\u0082\7:\2\2\u0082\u0083\7\7\2\2\u0083\u0084\7:\2\2\u0084")
        buf.write("\u0086\5\16\b\2\u0085}\3\2\2\2\u0085\u0080\3\2\2\2\u0086")
        buf.write("\r\3\2\2\2\u0087\u0088\7\35\2\2\u0088\u0089\5\20\t\2\u0089")
        buf.write("\u008a\7\36\2\2\u008a\u008e\3\2\2\2\u008b\u008c\7\35\2")
        buf.write("\2\u008c\u008e\7\36\2\2\u008d\u0087\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008e\17\3\2\2\2\u008f\u0090\5\22\n\2\u0090\u0091")
        buf.write("\5\20\t\2\u0091\u0094\3\2\2\2\u0092\u0094\5\22\n\2\u0093")
        buf.write("\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094\21\3\2\2\2\u0095")
        buf.write("\u0098\5\24\13\2\u0096\u0098\5\"\22\2\u0097\u0095\3\2")
        buf.write("\2\2\u0097\u0096\3\2\2\2\u0098\23\3\2\2\2\u0099\u009a")
        buf.write("\5\26\f\2\u009a\u009b\5\30\r\2\u009b\u009c\5\36\20\2\u009c")
        buf.write("\u009d\7\37\2\2\u009d\25\3\2\2\2\u009e\u009f\7\n\2\2\u009f")
        buf.write("\u00a6\7\13\2\2\u00a0\u00a1\7\13\2\2\u00a1\u00a6\7\n\2")
        buf.write("\2\u00a2\u00a6\7\n\2\2\u00a3\u00a6\7\13\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u009e\3\2\2\2\u00a5\u00a0\3\2\2\2\u00a5")
        buf.write("\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a6\27\3\2\2\2\u00a7\u00ab\5\32\16\2\u00a8\u00ab\5")
        buf.write("\64\33\2\u00a9\u00ab\5\34\17\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac")
        buf.write("\u00ad\t\3\2\2\u00ad\33\3\2\2\2\u00ae\u00af\7:\2\2\u00af")
        buf.write("\35\3\2\2\2\u00b0\u00b1\5 \21\2\u00b1\u00b2\7!\2\2\u00b2")
        buf.write("\u00b3\5\36\20\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6\5 \21")
        buf.write("\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\37\3")
        buf.write("\2\2\2\u00b7\u00b8\7:\2\2\u00b8\u00b9\7$\2\2\u00b9\u00bc")
        buf.write("\5B\"\2\u00ba\u00bc\7:\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc!\3\2\2\2\u00bd\u00be\5&\24\2\u00be\u00bf")
        buf.write("\5(\25\2\u00bf\u00c0\7:\2\2\u00c0\u00c1\5,\27\2\u00c1")
        buf.write("\u00c2\5*\26\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5$\23\2")
        buf.write("\u00c4\u00bd\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5#\3\2\2")
        buf.write("\2\u00c6\u00c7\7:\2\2\u00c7\u00c8\5,\27\2\u00c8\u00c9")
        buf.write("\5*\26\2\u00c9%\3\2\2\2\u00ca\u00cd\7\n\2\2\u00cb\u00cd")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\'\3\2\2\2\u00ce\u00cf\5\30\r\2\u00cf)\3\2\2\2\u00d0\u00d1")
        buf.write("\7\35\2\2\u00d1\u00d2\5Z.\2\u00d2\u00d3\7\36\2\2\u00d3")
        buf.write("\u00d7\3\2\2\2\u00d4\u00d5\7\35\2\2\u00d5\u00d7\7\36\2")
        buf.write("\2\u00d6\u00d0\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7+\3\2")
        buf.write("\2\2\u00d8\u00d9\7\33\2\2\u00d9\u00da\5.\30\2\u00da\u00db")
        buf.write("\7\34\2\2\u00db\u00df\3\2\2\2\u00dc\u00dd\7\33\2\2\u00dd")
        buf.write("\u00df\7\34\2\2\u00de\u00d8\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write("\2\u00df-\3\2\2\2\u00e0\u00e1\5\60\31\2\u00e1\u00e2\7")
        buf.write("\37\2\2\u00e2\u00e3\5.\30\2\u00e3\u00e6\3\2\2\2\u00e4")
        buf.write("\u00e6\5\60\31\2\u00e5\u00e0\3\2\2\2\u00e5\u00e4\3\2\2")
        buf.write("\2\u00e6/\3\2\2\2\u00e7\u00e8\5\30\r\2\u00e8\u00e9\5\62")
        buf.write("\32\2\u00e9\61\3\2\2\2\u00ea\u00eb\7:\2\2\u00eb\u00ec")
        buf.write("\7!\2\2\u00ec\u00ef\5\62\32\2\u00ed\u00ef\7:\2\2\u00ee")
        buf.write("\u00ea\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\63\3\2\2\2\u00f0")
        buf.write("\u00f1\5\32\16\2\u00f1\u00f2\7\3\2\2\u00f2\u00f3\5<\37")
        buf.write("\2\u00f3\u00f4\7\4\2\2\u00f4\65\3\2\2\2\u00f5\u00f6\7")
        buf.write("\35\2\2\u00f6\u00f7\58\35\2\u00f7\u00f8\7\36\2\2\u00f8")
        buf.write("\67\3\2\2\2\u00f9\u00fa\5:\36\2\u00fa\u00fb\7!\2\2\u00fb")
        buf.write("\u00fc\58\35\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff\5:\36\2")
        buf.write("\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff9\3\2\2")
        buf.write("\2\u0100\u0101\t\4\2\2\u0101;\3\2\2\2\u0102\u0103\7;\2")
        buf.write("\2\u0103=\3\2\2\2\u0104\u0105\7\33\2\2\u0105\u0106\5@")
        buf.write("!\2\u0106\u0107\7\34\2\2\u0107\u010b\3\2\2\2\u0108\u0109")
        buf.write("\7\33\2\2\u0109\u010b\7\34\2\2\u010a\u0104\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b?\3\2\2\2\u010c\u010d\5B\"\2\u010d")
        buf.write("\u010e\7!\2\2\u010e\u010f\5@!\2\u010f\u0112\3\2\2\2\u0110")
        buf.write("\u0112\5B\"\2\u0111\u010c\3\2\2\2\u0111\u0110\3\2\2\2")
        buf.write("\u0112A\3\2\2\2\u0113\u0114\5D#\2\u0114\u0115\t\5\2\2")
        buf.write("\u0115\u0116\5D#\2\u0116\u011d\3\2\2\2\u0117\u0118\5D")
        buf.write("#\2\u0118\u0119\t\6\2\2\u0119\u011a\5D#\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u011d\5D#\2\u011c\u0113\3\2\2\2\u011c\u0117")
        buf.write("\3\2\2\2\u011c\u011b\3\2\2\2\u011dC\3\2\2\2\u011e\u011f")
        buf.write("\5F$\2\u011f\u0120\t\7\2\2\u0120\u0121\5D#\2\u0121\u0130")
        buf.write("\3\2\2\2\u0122\u0123\5F$\2\u0123\u0124\t\b\2\2\u0124\u0125")
        buf.write("\5D#\2\u0125\u0130\3\2\2\2\u0126\u0127\5F$\2\u0127\u0128")
        buf.write("\t\t\2\2\u0128\u0129\5D#\2\u0129\u0130\3\2\2\2\u012a\u012b")
        buf.write("\5F$\2\u012b\u012c\7\64\2\2\u012c\u012d\5D#\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u0130\5F$\2\u012f\u011e\3\2\2\2\u012f\u0122")
        buf.write("\3\2\2\2\u012f\u0126\3\2\2\2\u012f\u012a\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130E\3\2\2\2\u0131\u0132\7\63\2\2\u0132")
        buf.write("\u0137\5F$\2\u0133\u0134\t\b\2\2\u0134\u0137\5F$\2\u0135")
        buf.write("\u0137\5H%\2\u0136\u0131\3\2\2\2\u0136\u0133\3\2\2\2\u0136")
        buf.write("\u0135\3\2\2\2\u0137G\3\2\2\2\u0138\u0139\b%\1\2\u0139")
        buf.write("\u013a\5J&\2\u013a\u0142\3\2\2\2\u013b\u013c\f\4\2\2\u013c")
        buf.write("\u013d\7\3\2\2\u013d\u013e\5B\"\2\u013e\u013f\7\4\2\2")
        buf.write("\u013f\u0141\3\2\2\2\u0140\u013b\3\2\2\2\u0141\u0144\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143I")
        buf.write("\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0149\5R*\2\u0146\u0149")
        buf.write("\5V,\2\u0147\u0149\5L\'\2\u0148\u0145\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0148\u0147\3\2\2\2\u0149K\3\2\2\2\u014a\u014b")
        buf.write("\7\b\2\2\u014b\u014c\7:\2\2\u014c\u014f\5> \2\u014d\u014f")
        buf.write("\5N(\2\u014e\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014fM")
        buf.write("\3\2\2\2\u0150\u015a\7;\2\2\u0151\u015a\78\2\2\u0152\u015a")
        buf.write("\79\2\2\u0153\u015a\7<\2\2\u0154\u015a\5\66\34\2\u0155")
        buf.write("\u015a\7\t\2\2\u0156\u015a\7\5\2\2\u0157\u015a\7:\2\2")
        buf.write("\u0158\u015a\5P)\2\u0159\u0150\3\2\2\2\u0159\u0151\3\2")
        buf.write("\2\2\u0159\u0152\3\2\2\2\u0159\u0153\3\2\2\2\u0159\u0154")
        buf.write("\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0156\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015aO\3\2\2\2\u015b")
        buf.write("\u015c\7\33\2\2\u015c\u015d\5B\"\2\u015d\u015e\7\34\2")
        buf.write("\2\u015eQ\3\2\2\2\u015f\u0160\5V,\2\u0160\u0161\7\"\2")
        buf.write("\2\u0161\u0162\7:\2\2\u0162\u0163\5> \2\u0163\u0164\5")
        buf.write("T+\2\u0164\u016f\3\2\2\2\u0165\u0168\5L\'\2\u0166\u0168")
        buf.write("\7:\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\7\"\2\2\u016a\u016b\7:\2\2")
        buf.write("\u016b\u016c\5> \2\u016c\u016d\5T+\2\u016d\u016f\3\2\2")
        buf.write("\2\u016e\u015f\3\2\2\2\u016e\u0167\3\2\2\2\u016fS\3\2")
        buf.write("\2\2\u0170\u0171\7\"\2\2\u0171\u0172\7:\2\2\u0172\u0173")
        buf.write("\5> \2\u0173\u0174\5T+\2\u0174\u0177\3\2\2\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0170\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("U\3\2\2\2\u0178\u017b\5L\'\2\u0179\u017b\7:\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017d\7\"\2\2\u017d\u017e\7:\2\2\u017e\u017f\5")
        buf.write("> \2\u017f\u0180\5T+\2\u0180\u0181\7\"\2\2\u0181\u0182")
        buf.write("\7:\2\2\u0182\u0183\5X-\2\u0183\u018c\3\2\2\2\u0184\u0187")
        buf.write("\5L\'\2\u0185\u0187\7:\2\2\u0186\u0184\3\2\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7\"\2\2\u0189")
        buf.write("\u018a\7:\2\2\u018a\u018c\5X-\2\u018b\u017a\3\2\2\2\u018b")
        buf.write("\u0186\3\2\2\2\u018cW\3\2\2\2\u018d\u018e\7\"\2\2\u018e")
        buf.write("\u018f\7:\2\2\u018f\u019a\5X-\2\u0190\u0191\7\"\2\2\u0191")
        buf.write("\u0192\7:\2\2\u0192\u0193\5> \2\u0193\u0194\5T+\2\u0194")
        buf.write("\u0195\7\"\2\2\u0195\u0196\7:\2\2\u0196\u0197\5X-\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u018d\3\2\2\2")
        buf.write("\u0199\u0190\3\2\2\2\u0199\u0198\3\2\2\2\u019aY\3\2\2")
        buf.write("\2\u019b\u019c\5\\/\2\u019c\u019d\5`\61\2\u019d\u01a2")
        buf.write("\3\2\2\2\u019e\u01a2\5\\/\2\u019f\u01a2\5`\61\2\u01a0")
        buf.write("\u01a2\3\2\2\2\u01a1\u019b\3\2\2\2\u01a1\u019e\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2[\3\2\2")
        buf.write("\2\u01a3\u01a4\5^\60\2\u01a4\u01a5\7\37\2\2\u01a5\u01a6")
        buf.write("\5\\/\2\u01a6\u01ab\3\2\2\2\u01a7\u01a8\5^\60\2\u01a8")
        buf.write("\u01a9\7\37\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a3\3\2\2")
        buf.write("\2\u01aa\u01a7\3\2\2\2\u01ab]\3\2\2\2\u01ac\u01ae\7\13")
        buf.write("\2\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b0\5\30\r\2\u01b0\u01b1\5\62\32\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01ad\3\2\2\2")
        buf.write("\u01b3\u01b2\3\2\2\2\u01b4_\3\2\2\2\u01b5\u01b6\5b\62")
        buf.write("\2\u01b6\u01b7\5`\61\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba")
        buf.write("\5b\62\2\u01b9\u01b5\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("a\3\2\2\2\u01bb\u01bc\5f\64\2\u01bc\u01bd\7#\2\2\u01bd")
        buf.write("\u01be\5B\"\2\u01be\u01bf\7\37\2\2\u01bf\u01e3\3\2\2\2")
        buf.write("\u01c0\u01c1\7\21\2\2\u01c1\u01c2\5B\"\2\u01c2\u01c3\7")
        buf.write("\23\2\2\u01c3\u01c4\5b\62\2\u01c4\u01e3\3\2\2\2\u01c5")
        buf.write("\u01c6\7\21\2\2\u01c6\u01c7\5B\"\2\u01c7\u01c8\7\23\2")
        buf.write("\2\u01c8\u01c9\5b\62\2\u01c9\u01ca\7\22\2\2\u01ca\u01cb")
        buf.write("\5b\62\2\u01cb\u01e3\3\2\2\2\u01cc\u01cd\7\24\2\2\u01cd")
        buf.write("\u01ce\5d\63\2\u01ce\u01cf\7#\2\2\u01cf\u01d0\5D#\2\u01d0")
        buf.write("\u01d1\t\n\2\2\u01d1\u01d2\5F$\2\u01d2\u01d5\7\27\2\2")
        buf.write("\u01d3\u01d6\5*\26\2\u01d4\u01d6\5b\62\2\u01d5\u01d3\3")
        buf.write("\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01e3\3\2\2\2\u01d7\u01d8")
        buf.write("\7\30\2\2\u01d8\u01e3\7\37\2\2\u01d9\u01da\7\31\2\2\u01da")
        buf.write("\u01e3\7\37\2\2\u01db\u01dc\7\32\2\2\u01dc\u01dd\5B\"")
        buf.write("\2\u01dd\u01de\7\37\2\2\u01de\u01e3\3\2\2\2\u01df\u01e0")
        buf.write("\5R*\2\u01e0\u01e1\7\37\2\2\u01e1\u01e3\3\2\2\2\u01e2")
        buf.write("\u01bb\3\2\2\2\u01e2\u01c0\3\2\2\2\u01e2\u01c5\3\2\2\2")
        buf.write("\u01e2\u01cc\3\2\2\2\u01e2\u01d7\3\2\2\2\u01e2\u01d9\3")
        buf.write("\2\2\2\u01e2\u01db\3\2\2\2\u01e2\u01df\3\2\2\2\u01e3c")
        buf.write("\3\2\2\2\u01e4\u01e5\7:\2\2\u01e5e\3\2\2\2\u01e6\u01ee")
        buf.write("\7:\2\2\u01e7\u01ee\5V,\2\u01e8\u01e9\5B\"\2\u01e9\u01ea")
        buf.write("\7\3\2\2\u01ea\u01eb\5B\"\2\u01eb\u01ec\7\4\2\2\u01ec")
        buf.write("\u01ee\3\2\2\2\u01ed\u01e6\3\2\2\2\u01ed\u01e7\3\2\2\2")
        buf.write("\u01ed\u01e8\3\2\2\2\u01eeg\3\2\2\2+s{\u0085\u008d\u0093")
        buf.write("\u0097\u00a5\u00aa\u00b5\u00bb\u00c4\u00cc\u00d6\u00de")
        buf.write("\u00e5\u00ee\u00fe\u010a\u0111\u011c\u012f\u0136\u0142")
        buf.write("\u0148\u014e\u0159\u0167\u016e\u0176\u017a\u0186\u018b")
        buf.write("\u0199\u01a1\u01aa\u01ad\u01b3\u01b9\u01d5\u01e2\u01ed")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'nil'", "'class'", "'extends'", 
                     "'new'", "'this'", "'static'", "'final'", "'int'", 
                     "'void'", "'float'", "'boolean'", "'string'", "'if'", 
                     "'else'", "'then'", "'for'", "'to'", "'downto'", "'do'", 
                     "'break'", "'continue'", "'return'", "'('", "')'", 
                     "'{'", "'}'", "';'", "':'", "','", "'.'", "':='", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CLASS", "EXTEND", "NEW", "SELF", "STATIC", "MUTABLE", 
                      "INTTYPE", "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", 
                      "IF", "ELSE", "THEN", "FOR", "TO", "DOWNTO", "DO", 
                      "BREAK", "CONT", "RETURN", "LB", "RB", "LP", "RP", 
                      "SEMI", "COLON", "COMMA", "DOT", "ASGOP", "ASG", "ADD", 
                      "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", 
                      "EQ", "LT", "GT", "LEQ", "GEQ", "OR", "AND", "NOT", 
                      "CON", "LINECMT", "BLOCKCMT", "WS", "FLOATLIT", "STRINGLIT", 
                      "ID", "INTLIT", "BOOLLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_funcall = 3
    RULE_classdcls = 4
    RULE_classdcl = 5
    RULE_memBlock = 6
    RULE_memList = 7
    RULE_classMember = 8
    RULE_attributeDeclare = 9
    RULE_attribute_type = 10
    RULE_vartype = 11
    RULE_primtype = 12
    RULE_classtype = 13
    RULE_attributeList = 14
    RULE_attri = 15
    RULE_methodDeclare = 16
    RULE_constructor = 17
    RULE_methodType = 18
    RULE_returnType = 19
    RULE_stmBlock = 20
    RULE_paramList = 21
    RULE_paramDeclare = 22
    RULE_param = 23
    RULE_idList = 24
    RULE_arraytype = 25
    RULE_arrayLit = 26
    RULE_elemList = 27
    RULE_elem = 28
    RULE_size = 29
    RULE_explist = 30
    RULE_exps = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_operand = 38
    RULE_subexp = 39
    RULE_methodInvoke = 40
    RULE_methodRecur = 41
    RULE_attriAccess = 42
    RULE_attriRecur = 43
    RULE_stmList = 44
    RULE_variables = 45
    RULE_variable = 46
    RULE_stms = 47
    RULE_stm = 48
    RULE_scala_var = 49
    RULE_lhs = 50

    ruleNames =  [ "program", "mptype", "body", "funcall", "classdcls", 
                   "classdcl", "memBlock", "memList", "classMember", "attributeDeclare", 
                   "attribute_type", "vartype", "primtype", "classtype", 
                   "attributeList", "attri", "methodDeclare", "constructor", 
                   "methodType", "returnType", "stmBlock", "paramList", 
                   "paramDeclare", "param", "idList", "arraytype", "arrayLit", 
                   "elemList", "elem", "size", "explist", "exps", "exp", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "operand", "subexp", 
                   "methodInvoke", "methodRecur", "attriAccess", "attriRecur", 
                   "stmList", "variables", "variable", "stms", "stm", "scala_var", 
                   "lhs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    CLASS=4
    EXTEND=5
    NEW=6
    SELF=7
    STATIC=8
    MUTABLE=9
    INTTYPE=10
    VOIDTYPE=11
    FLOATTYPE=12
    BOOLTYPE=13
    STRINGTYPE=14
    IF=15
    ELSE=16
    THEN=17
    FOR=18
    TO=19
    DOWNTO=20
    DO=21
    BREAK=22
    CONT=23
    RETURN=24
    LB=25
    RB=26
    LP=27
    RP=28
    SEMI=29
    COLON=30
    COMMA=31
    DOT=32
    ASGOP=33
    ASG=34
    ADD=35
    SUB=36
    MUL=37
    FLOATDIV=38
    INTDIV=39
    MOD=40
    NEQ=41
    EQ=42
    LT=43
    GT=44
    LEQ=45
    GEQ=46
    OR=47
    AND=48
    NOT=49
    CON=50
    LINECMT=51
    BLOCKCMT=52
    WS=53
    FLOATLIT=54
    STRINGLIT=55
    ID=56
    INTLIT=57
    BOOLLIT=58
    ILLEGAL_ESCAPE=59
    UNCLOSE_STRING=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdcls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.classdcls()
            self.state = 103
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = BKOOLParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.VOIDTYPE):
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(BKOOLParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.funcall()
            self.state = 108
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = BKOOLParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BKOOLParser.ID)
            self.state = 111
            self.match(BKOOLParser.LB)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__2) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.SELF) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT))) != 0):
                self.state = 112
                self.exp()


            self.state = 115
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdcl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclContext,0)


        def classdcls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classdcls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdcls" ):
                return visitor.visitClassdcls(self)
            else:
                return visitor.visitChildren(self)




    def classdcls(self):

        localctx = BKOOLParser.ClassdclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classdcls)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.classdcl()
                self.state = 118
                self.classdcls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.classdcl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def memBlock(self):
            return self.getTypedRuleContext(BKOOLParser.MemBlockContext,0)


        def EXTEND(self):
            return self.getToken(BKOOLParser.EXTEND, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classdcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdcl" ):
                return visitor.visitClassdcl(self)
            else:
                return visitor.visitChildren(self)




    def classdcl(self):

        localctx = BKOOLParser.ClassdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classdcl)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(BKOOLParser.CLASS)
                self.state = 124
                self.match(BKOOLParser.ID)
                self.state = 125
                self.memBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(BKOOLParser.CLASS)
                self.state = 127
                self.match(BKOOLParser.ID)
                self.state = 128
                self.match(BKOOLParser.EXTEND)
                self.state = 129
                self.match(BKOOLParser.ID)
                self.state = 130
                self.memBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def memList(self):
            return self.getTypedRuleContext(BKOOLParser.MemListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_memBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemBlock" ):
                return visitor.visitMemBlock(self)
            else:
                return visitor.visitChildren(self)




    def memBlock(self):

        localctx = BKOOLParser.MemBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_memBlock)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BKOOLParser.LP)
                self.state = 134
                self.memList()
                self.state = 135
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(BKOOLParser.LP)
                self.state = 138
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMember(self):
            return self.getTypedRuleContext(BKOOLParser.ClassMemberContext,0)


        def memList(self):
            return self.getTypedRuleContext(BKOOLParser.MemListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemList" ):
                return visitor.visitMemList(self)
            else:
                return visitor.visitChildren(self)




    def memList(self):

        localctx = BKOOLParser.MemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_memList)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.classMember()
                self.state = 142
                self.memList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.classMember()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclareContext,0)


        def methodDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)




    def classMember(self):

        localctx = BKOOLParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classMember)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.methodDeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_typeContext,0)


        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclare" ):
                return visitor.visitAttributeDeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributeDeclare(self):

        localctx = BKOOLParser.AttributeDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributeDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.attribute_type()
            self.state = 152
            self.vartype()
            self.state = 153
            self.attributeList()
            self.state = 154
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def MUTABLE(self):
            return self.getToken(BKOOLParser.MUTABLE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_type" ):
                return visitor.visitAttribute_type(self)
            else:
                return visitor.visitChildren(self)




    def attribute_type(self):

        localctx = BKOOLParser.Attribute_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_type)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(BKOOLParser.STATIC)
                self.state = 157
                self.match(BKOOLParser.MUTABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(BKOOLParser.MUTABLE)
                self.state = 159
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(BKOOLParser.MUTABLE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(BKOOLParser.PrimtypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def classtype(self):
            return self.getTypedRuleContext(BKOOLParser.ClasstypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = BKOOLParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vartype)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.classtype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKOOLParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(BKOOLParser.STRINGTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(BKOOLParser.BOOLTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimtype" ):
                return visitor.visitPrimtype(self)
            else:
                return visitor.visitChildren(self)




    def primtype(self):

        localctx = BKOOLParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.VOIDTYPE) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.BOOLTYPE) | (1 << BKOOLParser.STRINGTYPE))) != 0)):
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


    class ClasstypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstype" ):
                return visitor.visitClasstype(self)
            else:
                return visitor.visitChildren(self)




    def classtype(self):

        localctx = BKOOLParser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attri(self):
            return self.getTypedRuleContext(BKOOLParser.AttriContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeList" ):
                return visitor.visitAttributeList(self)
            else:
                return visitor.visitChildren(self)




    def attributeList(self):

        localctx = BKOOLParser.AttributeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attributeList)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.attri()
                self.state = 175
                self.match(BKOOLParser.COMMA)
                self.state = 176
                self.attributeList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.attri()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttriContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASG(self):
            return self.getToken(BKOOLParser.ASG, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attri

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttri" ):
                return visitor.visitAttri(self)
            else:
                return visitor.visitChildren(self)




    def attri(self):

        localctx = BKOOLParser.AttriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attri)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(BKOOLParser.ID)
                self.state = 182
                self.match(BKOOLParser.ASG)
                self.state = 183
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodType(self):
            return self.getTypedRuleContext(BKOOLParser.MethodTypeContext,0)


        def returnType(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclare" ):
                return visitor.visitMethodDeclare(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclare(self):

        localctx = BKOOLParser.MethodDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodDeclare)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.methodType()
                self.state = 188
                self.returnType()
                self.state = 189
                self.match(BKOOLParser.ID)
                self.state = 190
                self.paramList()
                self.state = 191
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BKOOLParser.ID)
            self.state = 197
            self.paramList()
            self.state = 198
            self.stmBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodType" ):
                return visitor.visitMethodType(self)
            else:
                return visitor.visitChildren(self)




    def methodType(self):

        localctx = BKOOLParser.MethodTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_methodType)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
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


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = BKOOLParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def stmList(self):
            return self.getTypedRuleContext(BKOOLParser.StmListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_stmBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmBlock" ):
                return visitor.visitStmBlock(self)
            else:
                return visitor.visitChildren(self)




    def stmBlock(self):

        localctx = BKOOLParser.StmBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmBlock)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(BKOOLParser.LP)
                self.state = 207
                self.stmList()
                self.state = 208
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(BKOOLParser.LP)
                self.state = 211
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclareContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paramList)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(BKOOLParser.LB)
                self.state = 215
                self.paramDeclare()
                self.state = 216
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(BKOOLParser.LB)
                self.state = 219
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclare" ):
                return visitor.visitParamDeclare(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclare(self):

        localctx = BKOOLParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramDeclare)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.param()
                self.state = 223
                self.match(BKOOLParser.SEMI)
                self.state = 224
                self.paramDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.vartype()
            self.state = 230
            self.idList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = BKOOLParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_idList)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(BKOOLParser.ID)
                self.state = 233
                self.match(BKOOLParser.COMMA)
                self.state = 234
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(BKOOLParser.PrimtypeContext,0)


        def size(self):
            return self.getTypedRuleContext(BKOOLParser.SizeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.primtype()
            self.state = 239
            self.match(BKOOLParser.T__0)
            self.state = 240
            self.size()
            self.state = 241
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def elemList(self):
            return self.getTypedRuleContext(BKOOLParser.ElemListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(BKOOLParser.LP)
            self.state = 244
            self.elemList()
            self.state = 245
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem(self):
            return self.getTypedRuleContext(BKOOLParser.ElemContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def elemList(self):
            return self.getTypedRuleContext(BKOOLParser.ElemListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_elemList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemList" ):
                return visitor.visitElemList(self)
            else:
                return visitor.visitChildren(self)




    def elemList(self):

        localctx = BKOOLParser.ElemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elemList)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.elem()
                self.state = 248
                self.match(BKOOLParser.COMMA)
                self.state = 249
                self.elemList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.elem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = BKOOLParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT))) != 0)):
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


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = BKOOLParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(BKOOLParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = BKOOLParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_explist)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(BKOOLParser.LB)
                self.state = 259
                self.exps()
                self.state = 260
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(BKOOLParser.LB)
                self.state = 263
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exps

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExps" ):
                return visitor.visitExps(self)
            else:
                return visitor.visitChildren(self)




    def exps(self):

        localctx = BKOOLParser.ExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exps)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.exp()
                self.state = 267
                self.match(BKOOLParser.COMMA)
                self.state = 268
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def LEQ(self):
            return self.getToken(BKOOLParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(BKOOLParser.GEQ, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.exp1()
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.exp1()
                self.state = 278
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKOOLParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FLOATDIV(self):
            return self.getToken(BKOOLParser.FLOATDIV, 0)

        def INTDIV(self):
            return self.getToken(BKOOLParser.INTDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def CON(self):
            return self.getToken(BKOOLParser.CON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.exp2()
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 286
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.exp2()
                self.state = 289
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 290
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.exp2()
                self.state = 293
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 294
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.exp2()
                self.state = 297
                self.match(BKOOLParser.CON)
                self.state = 298
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(BKOOLParser.NOT)
                self.state = 304
                self.exp2()
                pass
            elif token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 306
                self.exp2()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.exp3(0)
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


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 314
                    self.match(BKOOLParser.T__0)
                    self.state = 315
                    self.exp()
                    self.state = 316
                    self.match(BKOOLParser.T__1) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKOOLParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.exp5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def operand(self):
            return self.getTypedRuleContext(BKOOLParser.OperandContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKOOLParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(BKOOLParser.NEW)
                self.state = 329
                self.match(BKOOLParser.ID)
                self.state = 330
                self.explist()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.SELF, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.operand()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def SELF(self):
            return self.getToken(BKOOLParser.SELF, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def subexp(self):
            return self.getTypedRuleContext(BKOOLParser.SubexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operand)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.arrayLit()
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                self.match(BKOOLParser.T__2)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 341
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 342
                self.subexp()
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


    class SubexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexp" ):
                return visitor.visitSubexp(self)
            else:
                return visitor.visitChildren(self)




    def subexp(self):

        localctx = BKOOLParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BKOOLParser.LB)
            self.state = 346
            self.exp()
            self.state = 347
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvoke

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvoke" ):
                return visitor.visitMethodInvoke(self)
            else:
                return visitor.visitChildren(self)




    def methodInvoke(self):

        localctx = BKOOLParser.MethodInvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_methodInvoke)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.attriAccess()
                self.state = 350
                self.match(BKOOLParser.DOT)
                self.state = 351
                self.match(BKOOLParser.ID)
                self.state = 352
                self.explist()
                self.state = 353
                self.methodRecur()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 355
                    self.exp5()
                    pass

                elif la_ == 2:
                    self.state = 356
                    self.match(BKOOLParser.ID)
                    pass


                self.state = 359
                self.match(BKOOLParser.DOT)
                self.state = 360
                self.match(BKOOLParser.ID)
                self.state = 361
                self.explist()
                self.state = 362
                self.methodRecur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodRecurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodRecur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodRecur" ):
                return visitor.visitMethodRecur(self)
            else:
                return visitor.visitChildren(self)




    def methodRecur(self):

        localctx = BKOOLParser.MethodRecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_methodRecur)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(BKOOLParser.DOT)
                self.state = 367
                self.match(BKOOLParser.ID)
                self.state = 368
                self.explist()
                self.state = 369
                self.methodRecur()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttriAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def attriRecur(self):
            return self.getTypedRuleContext(BKOOLParser.AttriRecurContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attriAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttriAccess" ):
                return visitor.visitAttriAccess(self)
            else:
                return visitor.visitChildren(self)




    def attriAccess(self):

        localctx = BKOOLParser.AttriAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_attriAccess)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 374
                    self.exp5()
                    pass

                elif la_ == 2:
                    self.state = 375
                    self.match(BKOOLParser.ID)
                    pass


                self.state = 378
                self.match(BKOOLParser.DOT)
                self.state = 379
                self.match(BKOOLParser.ID)
                self.state = 380
                self.explist()
                self.state = 381
                self.methodRecur()
                self.state = 382
                self.match(BKOOLParser.DOT)
                self.state = 383
                self.match(BKOOLParser.ID)
                self.state = 384
                self.attriRecur()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 386
                    self.exp5()
                    pass

                elif la_ == 2:
                    self.state = 387
                    self.match(BKOOLParser.ID)
                    pass


                self.state = 390
                self.match(BKOOLParser.DOT)
                self.state = 391
                self.match(BKOOLParser.ID)
                self.state = 392
                self.attriRecur()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttriRecurContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def attriRecur(self):
            return self.getTypedRuleContext(BKOOLParser.AttriRecurContext,0)


        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attriRecur

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttriRecur" ):
                return visitor.visitAttriRecur(self)
            else:
                return visitor.visitChildren(self)




    def attriRecur(self):

        localctx = BKOOLParser.AttriRecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_attriRecur)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(BKOOLParser.DOT)
                self.state = 396
                self.match(BKOOLParser.ID)
                self.state = 397
                self.attriRecur()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(BKOOLParser.DOT)
                self.state = 399
                self.match(BKOOLParser.ID)
                self.state = 400
                self.explist()
                self.state = 401
                self.methodRecur()
                self.state = 402
                self.match(BKOOLParser.DOT)
                self.state = 403
                self.match(BKOOLParser.ID)
                self.state = 404
                self.attriRecur()
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


    class StmListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(BKOOLParser.VariablesContext,0)


        def stms(self):
            return self.getTypedRuleContext(BKOOLParser.StmsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmList" ):
                return visitor.visitStmList(self)
            else:
                return visitor.visitChildren(self)




    def stmList(self):

        localctx = BKOOLParser.StmListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmList)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.variables()
                self.state = 410
                self.stms()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.variables()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.stms()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKOOLParser.VariableContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def variables(self):
            return self.getTypedRuleContext(BKOOLParser.VariablesContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = BKOOLParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_variables)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.variable()
                self.state = 418
                self.match(BKOOLParser.SEMI)
                self.state = 419
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.variable()
                self.state = 422
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def MUTABLE(self):
            return self.getToken(BKOOLParser.MUTABLE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKOOLParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.MUTABLE:
                    self.state = 426
                    self.match(BKOOLParser.MUTABLE)


                self.state = 429
                self.vartype()
                self.state = 430
                self.idList()
                pass
            elif token in [BKOOLParser.SEMI]:
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


    class StmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(BKOOLParser.StmContext,0)


        def stms(self):
            return self.getTypedRuleContext(BKOOLParser.StmsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStms" ):
                return visitor.visitStms(self)
            else:
                return visitor.visitChildren(self)




    def stms(self):

        localctx = BKOOLParser.StmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stms)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.stm()
                self.state = 436
                self.stms()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASGOP(self):
            return self.getToken(BKOOLParser.ASGOP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scala_var(self):
            return self.getTypedRuleContext(BKOOLParser.Scala_varContext,0)


        def exp1(self):
            return self.getTypedRuleContext(BKOOLParser.Exp1Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def CONT(self):
            return self.getToken(BKOOLParser.CONT, 0)

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = BKOOLParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.lhs()
                self.state = 442
                self.match(BKOOLParser.ASGOP)
                self.state = 443
                self.exp()
                self.state = 444
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(BKOOLParser.IF)
                self.state = 447
                self.exp()
                self.state = 448
                self.match(BKOOLParser.THEN)
                self.state = 449
                self.stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(BKOOLParser.IF)
                self.state = 452
                self.exp()
                self.state = 453
                self.match(BKOOLParser.THEN)
                self.state = 454
                self.stm()
                self.state = 455
                self.match(BKOOLParser.ELSE)
                self.state = 456
                self.stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(BKOOLParser.FOR)
                self.state = 459
                self.scala_var()
                self.state = 460
                self.match(BKOOLParser.ASGOP)
                self.state = 461
                self.exp1()
                self.state = 462
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 463
                self.exp2()
                self.state = 464
                self.match(BKOOLParser.DO)
                self.state = 467
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.stmBlock()
                    pass

                elif la_ == 2:
                    self.state = 466
                    self.stm()
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.match(BKOOLParser.BREAK)
                self.state = 470
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.match(BKOOLParser.CONT)
                self.state = 472
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 473
                self.match(BKOOLParser.RETURN)
                self.state = 474
                self.exp()
                self.state = 475
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 477
                self.methodInvoke()
                self.state = 478
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scala_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scala_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScala_var" ):
                return visitor.visitScala_var(self)
            else:
                return visitor.visitChildren(self)




    def scala_var(self):

        localctx = BKOOLParser.Scala_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lhs)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.exp()
                self.state = 487
                self.match(BKOOLParser.T__0)
                self.state = 488
                self.exp()
                self.state = 489
                self.match(BKOOLParser.T__1)
                pass


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
        self._predicates[35] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




