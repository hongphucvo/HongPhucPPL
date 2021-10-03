# Generated from e:\hongphuc\PPL\BKooL\assignment2\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
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
        buf.write("\u01d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\5\3i")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\5\4p\n\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5z\n\5\3\6\3\6\3\6\5\6\177\n\6\3\7\3\7")
        buf.write("\5\7\u0083\n\7\3\b\3\b\5\b\u0087\n\b\3\b\3\b\5\b\u008b")
        buf.write("\n\b\3\b\3\b\5\b\u008f\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\5\t\u0098\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00a2")
        buf.write("\n\f\3\r\3\r\3\r\3\r\5\r\u00a8\n\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00ae\n\16\3\17\3\17\5\17\u00b2\n\17\3\17\3\17\5")
        buf.write("\17\u00b6\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00c2\n\20\3\21\3\21\3\21\3\21\5\21\u00c8")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00d3\n\23\3\24\3\24\5\24\u00d7\n\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u00e9\n\27\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u00f0\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00f7\n\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u00fe\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\7\33\u0106\n\33\f\33\16\33\u0109\13")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0111\n\34\f\34")
        buf.write("\16\34\u0114\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u011c\n\35\f\35\16\35\u011f\13\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u0127\n\36\f\36\16\36\u012a\13\36\3\37")
        buf.write("\3\37\3\37\5\37\u012f\n\37\3 \3 \3 \5 \u0134\n \3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\7!\u013e\n!\f!\16!\u0141\13!\3\"\3")
        buf.write("\"\3\"\5\"\u0146\n\"\3#\3#\3#\3#\5#\u014c\n#\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\5$\u0157\n$\3%\3%\3%\3%\3&\3&\3&\5")
        buf.write("&\u0160\n&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u016d\n\'\3(\3(\5(\u0171\n(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\5)\u017e\n)\3*\3*\5*\u0182\n*\3*\3*\5*\u0186\n")
        buf.write("*\3+\3+\3+\5+\u018b\n+\3,\3,\5,\u018f\n,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\5-\u0198\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01a7\n.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01b9\n.\3/\3/\3/\5/\u01be\n/\3/\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u01cf\n\61\3\61\2\7\64\668:@\62\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`\2\n\3\2\f\20\3\2-\60\3\2+,\3\2\61\62\3\2\'")
        buf.write("*\3\2%&\3\2\25\26\3\2\30\31\2\u01de\2b\3\2\2\2\4e\3\2")
        buf.write("\2\2\6j\3\2\2\2\by\3\2\2\2\n{\3\2\2\2\f\u0082\3\2\2\2")
        buf.write("\16\u008e\3\2\2\2\20\u0097\3\2\2\2\22\u0099\3\2\2\2\24")
        buf.write("\u009b\3\2\2\2\26\u009d\3\2\2\2\30\u00a3\3\2\2\2\32\u00a9")
        buf.write("\3\2\2\2\34\u00b5\3\2\2\2\36\u00c1\3\2\2\2 \u00c3\3\2")
        buf.write("\2\2\"\u00c9\3\2\2\2$\u00d2\3\2\2\2&\u00d6\3\2\2\2(\u00dc")
        buf.write("\3\2\2\2*\u00e0\3\2\2\2,\u00e8\3\2\2\2.\u00ef\3\2\2\2")
        buf.write("\60\u00f6\3\2\2\2\62\u00fd\3\2\2\2\64\u00ff\3\2\2\2\66")
        buf.write("\u010a\3\2\2\28\u0115\3\2\2\2:\u0120\3\2\2\2<\u012e\3")
        buf.write("\2\2\2>\u0133\3\2\2\2@\u0135\3\2\2\2B\u0145\3\2\2\2D\u014b")
        buf.write("\3\2\2\2F\u0156\3\2\2\2H\u0158\3\2\2\2J\u015f\3\2\2\2")
        buf.write("L\u016c\3\2\2\2N\u0170\3\2\2\2P\u017d\3\2\2\2R\u0181\3")
        buf.write("\2\2\2T\u0187\3\2\2\2V\u018e\3\2\2\2X\u0194\3\2\2\2Z\u01b8")
        buf.write("\3\2\2\2\\\u01bd\3\2\2\2^\u01c5\3\2\2\2`\u01ce\3\2\2\2")
        buf.write("bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2eh\5\6\4\2fi\5\4\3\2gi")
        buf.write("\3\2\2\2hf\3\2\2\2hg\3\2\2\2i\5\3\2\2\2jk\7\5\2\2ko\7")
        buf.write("<\2\2lm\7\6\2\2mp\7<\2\2np\3\2\2\2ol\3\2\2\2on\3\2\2\2")
        buf.write("pq\3\2\2\2qr\5\b\5\2r\7\3\2\2\2st\7\35\2\2tu\5\n\6\2u")
        buf.write("v\7\36\2\2vz\3\2\2\2wx\7\35\2\2xz\7\36\2\2ys\3\2\2\2y")
        buf.write("w\3\2\2\2z\t\3\2\2\2{~\5\f\7\2|\177\5\n\6\2}\177\3\2\2")
        buf.write("\2~|\3\2\2\2~}\3\2\2\2\177\13\3\2\2\2\u0080\u0083\5\16")
        buf.write("\b\2\u0081\u0083\5\34\17\2\u0082\u0080\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\r\3\2\2\2\u0084\u0087\7\n\2\2\u0085\u0087")
        buf.write("\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u008b\7\13\2\2\u0089\u008b\3\2\2")
        buf.write("\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u008f")
        buf.write("\3\2\2\2\u008c\u008d\7\13\2\2\u008d\u008f\7\n\2\2\u008e")
        buf.write("\u0086\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\5\20\t\2\u0091\u0092\5\26\f\2\u0092\u0093")
        buf.write("\7\37\2\2\u0093\17\3\2\2\2\u0094\u0098\5\22\n\2\u0095")
        buf.write("\u0098\5&\24\2\u0096\u0098\5\24\13\2\u0097\u0094\3\2\2")
        buf.write("\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\21\3")
        buf.write("\2\2\2\u0099\u009a\t\2\2\2\u009a\23\3\2\2\2\u009b\u009c")
        buf.write("\7<\2\2\u009c\25\3\2\2\2\u009d\u00a1\5\30\r\2\u009e\u009f")
        buf.write("\7!\2\2\u009f\u00a2\5\26\f\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\27\3\2\2\2\u00a3")
        buf.write("\u00a7\7<\2\2\u00a4\u00a5\7$\2\2\u00a5\u00a8\5\60\31\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a6\3")
        buf.write("\2\2\2\u00a8\31\3\2\2\2\u00a9\u00ad\7<\2\2\u00aa\u00ab")
        buf.write("\7!\2\2\u00ab\u00ae\5\32\16\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00aa\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\33\3\2\2\2\u00af")
        buf.write("\u00b2\7\n\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\5")
        buf.write("\20\t\2\u00b4\u00b6\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7<\2\2")
        buf.write("\u00b8\u00b9\5\36\20\2\u00b9\u00ba\5$\23\2\u00ba\35\3")
        buf.write("\2\2\2\u00bb\u00bc\7\33\2\2\u00bc\u00bd\5 \21\2\u00bd")
        buf.write("\u00be\7\34\2\2\u00be\u00c2\3\2\2\2\u00bf\u00c0\7\33\2")
        buf.write("\2\u00c0\u00c2\7\34\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\37\3\2\2\2\u00c3\u00c7\5\"\22\2\u00c4\u00c5")
        buf.write("\7\37\2\2\u00c5\u00c8\5 \21\2\u00c6\u00c8\3\2\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8!\3\2\2\2\u00c9")
        buf.write("\u00ca\5\20\t\2\u00ca\u00cb\5\32\16\2\u00cb#\3\2\2\2\u00cc")
        buf.write("\u00cd\7\35\2\2\u00cd\u00ce\5R*\2\u00ce\u00cf\7\36\2\2")
        buf.write("\u00cf\u00d3\3\2\2\2\u00d0\u00d1\7\35\2\2\u00d1\u00d3")
        buf.write("\7\36\2\2\u00d2\u00cc\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3")
        buf.write("%\3\2\2\2\u00d4\u00d7\5\22\n\2\u00d5\u00d7\5\24\13\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00d9\7\3\2\2\u00d9\u00da\5*\26\2\u00da\u00db\7")
        buf.write("\4\2\2\u00db\'\3\2\2\2\u00dc\u00dd\7\35\2\2\u00dd\u00de")
        buf.write("\5.\30\2\u00de\u00df\7\36\2\2\u00df)\3\2\2\2\u00e0\u00e1")
        buf.write("\7:\2\2\u00e1+\3\2\2\2\u00e2\u00e3\7\33\2\2\u00e3\u00e4")
        buf.write("\5.\30\2\u00e4\u00e5\7\34\2\2\u00e5\u00e9\3\2\2\2\u00e6")
        buf.write("\u00e7\7\33\2\2\u00e7\u00e9\7\34\2\2\u00e8\u00e2\3\2\2")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e9-\3\2\2\2\u00ea\u00eb\5\60")
        buf.write("\31\2\u00eb\u00ec\7!\2\2\u00ec\u00ed\5.\30\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00f0\5\60\31\2\u00ef\u00ea\3\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0/\3\2\2\2\u00f1\u00f2\5\62\32\2\u00f2")
        buf.write("\u00f3\t\3\2\2\u00f3\u00f4\5\62\32\2\u00f4\u00f7\3\2\2")
        buf.write("\2\u00f5\u00f7\5\62\32\2\u00f6\u00f1\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\61\3\2\2\2\u00f8\u00f9\5\64\33\2\u00f9")
        buf.write("\u00fa\t\4\2\2\u00fa\u00fb\5\64\33\2\u00fb\u00fe\3\2\2")
        buf.write("\2\u00fc\u00fe\5\64\33\2\u00fd\u00f8\3\2\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe\63\3\2\2\2\u00ff\u0100\b\33\1\2\u0100\u0101")
        buf.write("\5\66\34\2\u0101\u0107\3\2\2\2\u0102\u0103\f\4\2\2\u0103")
        buf.write("\u0104\t\5\2\2\u0104\u0106\5\66\34\2\u0105\u0102\3\2\2")
        buf.write("\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\65\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b")
        buf.write("\b\34\1\2\u010b\u010c\58\35\2\u010c\u0112\3\2\2\2\u010d")
        buf.write("\u010e\f\4\2\2\u010e\u010f\7\64\2\2\u010f\u0111\58\35")
        buf.write("\2\u0110\u010d\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\67\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0116\b\35\1\2\u0116\u0117\5:\36\2\u0117")
        buf.write("\u011d\3\2\2\2\u0118\u0119\f\4\2\2\u0119\u011a\t\6\2\2")
        buf.write("\u011a\u011c\5:\36\2\u011b\u0118\3\2\2\2\u011c\u011f\3")
        buf.write("\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e9")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\b\36\1\2\u0121")
        buf.write("\u0122\5<\37\2\u0122\u0128\3\2\2\2\u0123\u0124\f\4\2\2")
        buf.write("\u0124\u0125\t\7\2\2\u0125\u0127\5<\37\2\u0126\u0123\3")
        buf.write("\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129;\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c")
        buf.write("\7\63\2\2\u012c\u012f\5> \2\u012d\u012f\5> \2\u012e\u012b")
        buf.write("\3\2\2\2\u012e\u012d\3\2\2\2\u012f=\3\2\2\2\u0130\u0131")
        buf.write("\t\7\2\2\u0131\u0134\5@!\2\u0132\u0134\5@!\2\u0133\u0130")
        buf.write("\3\2\2\2\u0133\u0132\3\2\2\2\u0134?\3\2\2\2\u0135\u0136")
        buf.write("\b!\1\2\u0136\u0137\5B\"\2\u0137\u013f\3\2\2\2\u0138\u0139")
        buf.write("\f\4\2\2\u0139\u013a\7\3\2\2\u013a\u013b\5\60\31\2\u013b")
        buf.write("\u013c\7\4\2\2\u013c\u013e\3\2\2\2\u013d\u0138\3\2\2\2")
        buf.write("\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140A\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0146")
        buf.write("\5J&\2\u0143\u0146\5N(\2\u0144\u0146\5D#\2\u0145\u0142")
        buf.write("\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("C\3\2\2\2\u0147\u0148\7\7\2\2\u0148\u0149\7<\2\2\u0149")
        buf.write("\u014c\5,\27\2\u014a\u014c\5F$\2\u014b\u0147\3\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014cE\3\2\2\2\u014d\u0157\5(\25\2\u014e")
        buf.write("\u0157\7:\2\2\u014f\u0157\78\2\2\u0150\u0157\7;\2\2\u0151")
        buf.write("\u0157\79\2\2\u0152\u0157\7<\2\2\u0153\u0157\7\b\2\2\u0154")
        buf.write("\u0157\7\t\2\2\u0155\u0157\5H%\2\u0156\u014d\3\2\2\2\u0156")
        buf.write("\u014e\3\2\2\2\u0156\u014f\3\2\2\2\u0156\u0150\3\2\2\2")
        buf.write("\u0156\u0151\3\2\2\2\u0156\u0152\3\2\2\2\u0156\u0153\3")
        buf.write("\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157G")
        buf.write("\3\2\2\2\u0158\u0159\7\33\2\2\u0159\u015a\5\60\31\2\u015a")
        buf.write("\u015b\7\34\2\2\u015bI\3\2\2\2\u015c\u0160\5N(\2\u015d")
        buf.write("\u0160\5D#\2\u015e\u0160\7<\2\2\u015f\u015c\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0162\7\"\2\2\u0162\u0163\7<\2\2\u0163\u0164\5")
        buf.write(",\27\2\u0164\u0165\5L\'\2\u0165K\3\2\2\2\u0166\u0167\7")
        buf.write("\"\2\2\u0167\u0168\7<\2\2\u0168\u0169\5,\27\2\u0169\u016a")
        buf.write("\5L\'\2\u016a\u016d\3\2\2\2\u016b\u016d\3\2\2\2\u016c")
        buf.write("\u0166\3\2\2\2\u016c\u016b\3\2\2\2\u016dM\3\2\2\2\u016e")
        buf.write("\u0171\5D#\2\u016f\u0171\7<\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\5L\'\2")
        buf.write("\u0173\u0174\7\"\2\2\u0174\u0175\7<\2\2\u0175\u0176\5")
        buf.write("P)\2\u0176O\3\2\2\2\u0177\u0178\5L\'\2\u0178\u0179\7\"")
        buf.write("\2\2\u0179\u017a\7<\2\2\u017a\u017b\5P)\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u0177\3\2\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017eQ\3\2\2\2\u017f\u0182\5T+\2\u0180")
        buf.write("\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0185\3\2\2\2\u0183\u0186\5X-\2\u0184\u0186\3\2")
        buf.write("\2\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186S\3")
        buf.write("\2\2\2\u0187\u018a\5V,\2\u0188\u018b\5T+\2\u0189\u018b")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("U\3\2\2\2\u018c\u018f\7\13\2\2\u018d\u018f\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u0191\5\20\t\2\u0191\u0192\5\26\f\2\u0192\u0193")
        buf.write("\7\37\2\2\u0193W\3\2\2\2\u0194\u0197\5Z.\2\u0195\u0198")
        buf.write("\5X-\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198Y\3\2\2\2\u0199\u01b9\5$\23\2\u019a\u019b")
        buf.write("\5`\61\2\u019b\u019c\7#\2\2\u019c\u019d\5\60\31\2\u019d")
        buf.write("\u019e\7\37\2\2\u019e\u01b9\3\2\2\2\u019f\u01a0\7\21\2")
        buf.write("\2\u01a0\u01a1\5\60\31\2\u01a1\u01a2\7\23\2\2\u01a2\u01a6")
        buf.write("\5Z.\2\u01a3\u01a4\7\22\2\2\u01a4\u01a7\5Z.\2\u01a5\u01a7")
        buf.write("\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01b9\3\2\2\2\u01a8\u01a9\7\24\2\2\u01a9\u01aa\5^\60")
        buf.write("\2\u01aa\u01ab\7#\2\2\u01ab\u01ac\5\60\31\2\u01ac\u01ad")
        buf.write("\t\b\2\2\u01ad\u01ae\5\60\31\2\u01ae\u01af\7\27\2\2\u01af")
        buf.write("\u01b0\5Z.\2\u01b0\u01b9\3\2\2\2\u01b1\u01b2\t\t\2\2\u01b2")
        buf.write("\u01b9\7\37\2\2\u01b3\u01b4\7\32\2\2\u01b4\u01b5\5\60")
        buf.write("\31\2\u01b5\u01b6\7\37\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b9")
        buf.write("\5\\/\2\u01b8\u0199\3\2\2\2\u01b8\u019a\3\2\2\2\u01b8")
        buf.write("\u019f\3\2\2\2\u01b8\u01a8\3\2\2\2\u01b8\u01b1\3\2\2\2")
        buf.write("\u01b8\u01b3\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9[\3\2\2")
        buf.write("\2\u01ba\u01be\5N(\2\u01bb\u01be\5D#\2\u01bc\u01be\7<")
        buf.write("\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\7\"\2\2\u01c0")
        buf.write("\u01c1\7<\2\2\u01c1\u01c2\5,\27\2\u01c2\u01c3\5L\'\2\u01c3")
        buf.write("\u01c4\7\37\2\2\u01c4]\3\2\2\2\u01c5\u01c6\7<\2\2\u01c6")
        buf.write("_\3\2\2\2\u01c7\u01cf\7<\2\2\u01c8\u01cf\5N(\2\u01c9\u01ca")
        buf.write("\5B\"\2\u01ca\u01cb\7\3\2\2\u01cb\u01cc\5\60\31\2\u01cc")
        buf.write("\u01cd\7\4\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01c7\3\2\2\2")
        buf.write("\u01ce\u01c8\3\2\2\2\u01ce\u01c9\3\2\2\2\u01cfa\3\2\2")
        buf.write("\2/hoy~\u0082\u0086\u008a\u008e\u0097\u00a1\u00a7\u00ad")
        buf.write("\u00b1\u00b5\u00c1\u00c7\u00d2\u00d6\u00e8\u00ef\u00f6")
        buf.write("\u00fd\u0107\u0112\u011d\u0128\u012e\u0133\u013f\u0145")
        buf.write("\u014b\u0156\u015f\u016c\u0170\u017d\u0181\u0185\u018a")
        buf.write("\u018e\u0197\u01a6\u01b8\u01bd\u01ce")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'class'", "'extends'", 
                     "'new'", "'this'", "'nil'", "'static'", "'final'", 
                     "'int'", "'void'", "'float'", "'boolean'", "'string'", 
                     "'if'", "'else'", "'then'", "'for'", "'to'", "'downto'", 
                     "'do'", "'break'", "'continue'", "'return'", "'('", 
                     "')'", "'{'", "'}'", "';'", "':'", "','", "'.'", "':='", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "CLASS", "EXTEND", 
                      "NEW", "SELF", "NIL", "STATIC", "IMMUTABLE", "INTTYPE", 
                      "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", 
                      "IF", "ELSE", "THEN", "FOR", "TO", "DOWNTO", "DO", 
                      "BREAK", "CONT", "RETURN", "LB", "RB", "LP", "RP", 
                      "SEMI", "COLON", "COMMA", "DOT", "ASGOP", "ASG", "ADD", 
                      "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", 
                      "EQ", "LT", "GT", "LEQ", "GEQ", "OR", "AND", "NOT", 
                      "CON", "LINECMT", "BLOCKCMT", "WS", "FLOATLIT", "STRINGLIT", 
                      "INTLIT", "BOOLLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdcls = 1
    RULE_classdcl = 2
    RULE_memBlock = 3
    RULE_memList = 4
    RULE_classMember = 5
    RULE_attributeDeclare = 6
    RULE_vartype = 7
    RULE_primtype = 8
    RULE_classtype = 9
    RULE_attributeList = 10
    RULE_attri = 11
    RULE_idList = 12
    RULE_methodDeclare = 13
    RULE_paramList = 14
    RULE_paramDeclare = 15
    RULE_param = 16
    RULE_stmBlock = 17
    RULE_arraytype = 18
    RULE_arrayLit = 19
    RULE_size = 20
    RULE_explist = 21
    RULE_exps = 22
    RULE_exp = 23
    RULE_exp1 = 24
    RULE_exp2 = 25
    RULE_exp3 = 26
    RULE_exp4 = 27
    RULE_exp5 = 28
    RULE_exp6 = 29
    RULE_exp7 = 30
    RULE_exp8 = 31
    RULE_exp9 = 32
    RULE_exp10 = 33
    RULE_operand = 34
    RULE_subexp = 35
    RULE_methodInvoke = 36
    RULE_methodRecur = 37
    RULE_attriAccess = 38
    RULE_attriRecur = 39
    RULE_stmList = 40
    RULE_variables = 41
    RULE_variable = 42
    RULE_stms = 43
    RULE_stm = 44
    RULE_methodCall = 45
    RULE_scala_var = 46
    RULE_lhs = 47

    ruleNames =  [ "program", "classdcls", "classdcl", "memBlock", "memList", 
                   "classMember", "attributeDeclare", "vartype", "primtype", 
                   "classtype", "attributeList", "attri", "idList", "methodDeclare", 
                   "paramList", "paramDeclare", "param", "stmBlock", "arraytype", 
                   "arrayLit", "size", "explist", "exps", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "operand", "subexp", "methodInvoke", 
                   "methodRecur", "attriAccess", "attriRecur", "stmList", 
                   "variables", "variable", "stms", "stm", "methodCall", 
                   "scala_var", "lhs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    CLASS=3
    EXTEND=4
    NEW=5
    SELF=6
    NIL=7
    STATIC=8
    IMMUTABLE=9
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
    INTLIT=56
    BOOLLIT=57
    ID=58
    ILLEGAL_ESCAPE=59
    UNCLOSE_STRING=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdcls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.classdcls()
            self.state = 97
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdcl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclContext,0)


        def classdcls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassdclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classdcls




    def classdcls(self):

        localctx = BKOOLParser.ClassdclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdcls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.classdcl()
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CLASS]:
                self.state = 100
                self.classdcls()
                pass
            elif token in [BKOOLParser.EOF]:
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


    class ClassdclContext(ParserRuleContext):

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




    def classdcl(self):

        localctx = BKOOLParser.ClassdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BKOOLParser.CLASS)
            self.state = 105
            self.match(BKOOLParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTEND]:
                self.state = 106
                self.match(BKOOLParser.EXTEND)
                self.state = 107
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 111
            self.memBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemBlockContext(ParserRuleContext):

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




    def memBlock(self):

        localctx = BKOOLParser.MemBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memBlock)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(BKOOLParser.LP)
                self.state = 114
                self.memList()
                self.state = 115
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(BKOOLParser.LP)
                self.state = 118
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMember(self):
            return self.getTypedRuleContext(BKOOLParser.ClassMemberContext,0)


        def memList(self):
            return self.getTypedRuleContext(BKOOLParser.MemListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memList




    def memList(self):

        localctx = BKOOLParser.MemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.classMember()
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC, BKOOLParser.IMMUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.state = 122
                self.memList()
                pass
            elif token in [BKOOLParser.RP]:
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


    class ClassMemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclareContext,0)


        def methodDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMember




    def classMember(self):

        localctx = BKOOLParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classMember)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def IMMUTABLE(self):
            return self.getToken(BKOOLParser.IMMUTABLE, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDeclare




    def attributeDeclare(self):

        localctx = BKOOLParser.AttributeDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 132
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 130
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.IMMUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 136
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.IMMUTABLE]:
                    self.state = 134
                    self.match(BKOOLParser.IMMUTABLE)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 138
                self.match(BKOOLParser.IMMUTABLE)
                self.state = 139
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 142
            self.vartype()
            self.state = 143
            self.attributeList()
            self.state = 144
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):

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




    def vartype(self):

        localctx = BKOOLParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vartype)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
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




    def primtype(self):

        localctx = BKOOLParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classtype




    def classtype(self):

        localctx = BKOOLParser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeListContext(ParserRuleContext):

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




    def attributeList(self):

        localctx = BKOOLParser.AttributeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attributeList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.attri()
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 156
                self.match(BKOOLParser.COMMA)
                self.state = 157
                self.attributeList()
                pass
            elif token in [BKOOLParser.SEMI]:
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


    class AttriContext(ParserRuleContext):

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




    def attri(self):

        localctx = BKOOLParser.AttriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attri)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(BKOOLParser.ID)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ASG]:
                self.state = 162
                self.match(BKOOLParser.ASG)
                self.state = 163
                self.exp()
                pass
            elif token in [BKOOLParser.SEMI, BKOOLParser.COMMA]:
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


    class IdListContext(ParserRuleContext):

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




    def idList(self):

        localctx = BKOOLParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_idList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKOOLParser.ID)
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 168
                self.match(BKOOLParser.COMMA)
                self.state = 169
                self.idList()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.SEMI]:
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


    class MethodDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDeclare




    def methodDeclare(self):

        localctx = BKOOLParser.MethodDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 175
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 173
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 177
                self.vartype()
                pass

            elif la_ == 2:
                pass


            self.state = 181
            self.match(BKOOLParser.ID)
            self.state = 182
            self.paramList()
            self.state = 183
            self.stmBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):

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




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(BKOOLParser.LB)
                self.state = 186
                self.paramDeclare()
                self.state = 187
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(BKOOLParser.LB)
                self.state = 190
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




    def paramDeclare(self):

        localctx = BKOOLParser.ParamDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.param()
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.state = 194
                self.match(BKOOLParser.SEMI)
                self.state = 195
                self.paramDeclare()
                pass
            elif token in [BKOOLParser.RB]:
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


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.vartype()
            self.state = 200
            self.idList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmBlockContext(ParserRuleContext):

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




    def stmBlock(self):

        localctx = BKOOLParser.StmBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmBlock)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(BKOOLParser.LP)
                self.state = 203
                self.stmList()
                self.state = 204
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(BKOOLParser.LP)
                self.state = 207
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def size(self):
            return self.getTypedRuleContext(BKOOLParser.SizeContext,0)


        def primtype(self):
            return self.getTypedRuleContext(BKOOLParser.PrimtypeContext,0)


        def classtype(self):
            return self.getTypedRuleContext(BKOOLParser.ClasstypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
                self.state = 210
                self.primtype()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 211
                self.classtype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 214
            self.match(BKOOLParser.T__0)
            self.state = 215
            self.size()
            self.state = 216
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BKOOLParser.LP)
            self.state = 219
            self.exps()
            self.state = 220
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_size




    def size(self):

        localctx = BKOOLParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(BKOOLParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

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




    def explist(self):

        localctx = BKOOLParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_explist)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(BKOOLParser.LB)
                self.state = 225
                self.exps()
                self.state = 226
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(BKOOLParser.LB)
                self.state = 229
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




    def exps(self):

        localctx = BKOOLParser.ExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exps)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exp()
                self.state = 233
                self.match(BKOOLParser.COMMA)
                self.state = 234
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.exp1()
                self.state = 240
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.exp2(0)
                self.state = 247
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.exp3(0) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def CON(self):
            return self.getToken(BKOOLParser.CON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    self.match(BKOOLParser.CON)
                    self.state = 269
                    self.exp4(0) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FLOATDIV(self):
            return self.getToken(BKOOLParser.FLOATDIV, 0)

        def INTDIV(self):
            return self.getToken(BKOOLParser.INTDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.exp5(0) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 291
                    self.exp6() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp6)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(BKOOLParser.NOT)
                self.state = 298
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.exp7()
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


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.exp8(0)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.exp8(0)
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    self.match(BKOOLParser.T__0)
                    self.state = 312
                    self.exp()
                    self.state = 313
                    self.match(BKOOLParser.T__1) 
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9




    def exp9(self):

        localctx = BKOOLParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp9)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):

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
            return BKOOLParser.RULE_exp10




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp10)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(BKOOLParser.NEW)
                self.state = 326
                self.match(BKOOLParser.ID)
                self.state = 327
                self.explist()
                pass
            elif token in [BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def SELF(self):
            return self.getToken(BKOOLParser.SELF, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def subexp(self):
            return self.getTypedRuleContext(BKOOLParser.SubexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operand




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.arrayLit()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 335
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 336
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 7)
                self.state = 337
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 338
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 339
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




    def subexp(self):

        localctx = BKOOLParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.LB)
            self.state = 343
            self.exp()
            self.state = 344
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvokeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvoke




    def methodInvoke(self):

        localctx = BKOOLParser.MethodInvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 346
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 347
                self.exp10()
                pass

            elif la_ == 3:
                self.state = 348
                self.match(BKOOLParser.ID)
                pass


            self.state = 351
            self.match(BKOOLParser.DOT)
            self.state = 352
            self.match(BKOOLParser.ID)
            self.state = 353
            self.explist()
            self.state = 354
            self.methodRecur()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodRecurContext(ParserRuleContext):

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




    def methodRecur(self):

        localctx = BKOOLParser.MethodRecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_methodRecur)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(BKOOLParser.DOT)
                self.state = 357
                self.match(BKOOLParser.ID)
                self.state = 358
                self.explist()
                self.state = 359
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def attriRecur(self):
            return self.getTypedRuleContext(BKOOLParser.AttriRecurContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attriAccess




    def attriAccess(self):

        localctx = BKOOLParser.AttriAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_attriAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 364
                self.exp10()
                pass

            elif la_ == 2:
                self.state = 365
                self.match(BKOOLParser.ID)
                pass


            self.state = 368
            self.methodRecur()
            self.state = 369
            self.match(BKOOLParser.DOT)
            self.state = 370
            self.match(BKOOLParser.ID)
            self.state = 371
            self.attriRecur()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttriRecurContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodRecur(self):
            return self.getTypedRuleContext(BKOOLParser.MethodRecurContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def attriRecur(self):
            return self.getTypedRuleContext(BKOOLParser.AttriRecurContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attriRecur




    def attriRecur(self):

        localctx = BKOOLParser.AttriRecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_attriRecur)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.methodRecur()
                self.state = 374
                self.match(BKOOLParser.DOT)
                self.state = 375
                self.match(BKOOLParser.ID)
                self.state = 376
                self.attriRecur()
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


    class StmListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(BKOOLParser.VariablesContext,0)


        def stms(self):
            return self.getTypedRuleContext(BKOOLParser.StmsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmList




    def stmList(self):

        localctx = BKOOLParser.StmListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 381
                self.variables()
                pass

            elif la_ == 2:
                pass


            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 385
                self.stms()
                pass
            elif token in [BKOOLParser.RP]:
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


    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKOOLParser.VariableContext,0)


        def variables(self):
            return self.getTypedRuleContext(BKOOLParser.VariablesContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variables




    def variables(self):

        localctx = BKOOLParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.variable()
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 390
                self.variables()
                pass

            elif la_ == 2:
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

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def IMMUTABLE(self):
            return self.getToken(BKOOLParser.IMMUTABLE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable




    def variable(self):

        localctx = BKOOLParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IMMUTABLE]:
                self.state = 394
                self.match(BKOOLParser.IMMUTABLE)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 398
            self.vartype()
            self.state = 399
            self.attributeList()
            self.state = 400
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(BKOOLParser.StmContext,0)


        def stms(self):
            return self.getTypedRuleContext(BKOOLParser.StmsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stms




    def stms(self):

        localctx = BKOOLParser.StmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.stm()
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 403
                self.stms()
                pass
            elif token in [BKOOLParser.RP]:
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


    class StmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASGOP(self):
            return self.getToken(BKOOLParser.ASGOP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


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


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def CONT(self):
            return self.getToken(BKOOLParser.CONT, 0)

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def methodCall(self):
            return self.getTypedRuleContext(BKOOLParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stm




    def stm(self):

        localctx = BKOOLParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.lhs()
                self.state = 409
                self.match(BKOOLParser.ASGOP)
                self.state = 410
                self.exp()
                self.state = 411
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.match(BKOOLParser.IF)
                self.state = 414
                self.exp()
                self.state = 415
                self.match(BKOOLParser.THEN)
                self.state = 416
                self.stm()
                self.state = 420
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 417
                    self.match(BKOOLParser.ELSE)
                    self.state = 418
                    self.stm()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 422
                self.match(BKOOLParser.FOR)
                self.state = 423
                self.scala_var()
                self.state = 424
                self.match(BKOOLParser.ASGOP)
                self.state = 425
                self.exp()
                self.state = 426
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 427
                self.exp()
                self.state = 428
                self.match(BKOOLParser.DO)
                self.state = 429
                self.stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.BREAK or _la==BKOOLParser.CONT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 432
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 433
                self.match(BKOOLParser.RETURN)
                self.state = 434
                self.exp()
                self.state = 435
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 437
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodCall




    def methodCall(self):

        localctx = BKOOLParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 440
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 441
                self.exp10()
                pass

            elif la_ == 3:
                self.state = 442
                self.match(BKOOLParser.ID)
                pass


            self.state = 445
            self.match(BKOOLParser.DOT)
            self.state = 446
            self.match(BKOOLParser.ID)
            self.state = 447
            self.explist()
            self.state = 448
            self.methodRecur()
            self.state = 449
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scala_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scala_var




    def scala_var(self):

        localctx = BKOOLParser.Scala_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_lhs)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.exp9()
                self.state = 456
                self.match(BKOOLParser.T__0)
                self.state = 457
                self.exp()
                self.state = 458
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
        self._predicates[25] = self.exp2_sempred
        self._predicates[26] = self.exp3_sempred
        self._predicates[27] = self.exp4_sempred
        self._predicates[28] = self.exp5_sempred
        self._predicates[31] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




