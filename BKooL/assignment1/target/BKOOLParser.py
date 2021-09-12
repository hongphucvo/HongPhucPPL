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
        buf.write("\u01c1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\5\5p\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\5\6w\n\6\3\7\3\7\3\7\3\7\3\7\5\7~\n\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0088\n\b\3\t\3\t\3\t\5\t\u008d\n")
        buf.write("\t\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\5\f\u009a\n\f\3\f\3\f\5\f\u009e\n\f\3\f\3\f\5\f\u00a2")
        buf.write("\n\f\3\r\3\r\3\r\5\r\u00a7\n\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00b1\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00b7\n\21\3\22\3\22\5\22\u00bb\n\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00c3\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u00cf\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00d7\n\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00dd\n\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u00e6\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\5\33\u00f5\n\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0101\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\5\37\u0108\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \5 \u0113\n \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0126\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u012d\n\"\3#\3#\3#\3#\3#\3#\3#\3#\7#\u0137")
        buf.write("\n#\f#\16#\u013a\13#\3$\3$\3$\5$\u013f\n$\3%\3%\3%\3%")
        buf.write("\5%\u0145\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0150\n&\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\5(\u0159\n(\3(\3(\3(\3(\3(\3)")
        buf.write("\3)\3)\3)\3)\3)\5)\u0166\n)\3*\3*\5*\u016a\n*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\5+\u0177\n+\3,\3,\5,\u017b\n")
        buf.write(",\3,\3,\5,\u017f\n,\3-\3-\3-\5-\u0184\n-\3.\3.\5.\u0188")
        buf.write("\n.\3.\3.\3.\3.\3/\3/\3/\5/\u0191\n/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01a0\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01b4\n\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u01bf\n\62\3\62\2\3D\63\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`b\2\f\3\2\f\r\3\2\f\20\3\28;\3\2-\60\3\2+,\3\2")
        buf.write("\61\62\3\2%&\3\2\'*\3\2\25\26\3\2\30\31\2\u01cc\2d\3\2")
        buf.write("\2\2\4g\3\2\2\2\6i\3\2\2\2\bl\3\2\2\2\ns\3\2\2\2\fx\3")
        buf.write("\2\2\2\16\u0087\3\2\2\2\20\u0089\3\2\2\2\22\u0090\3\2")
        buf.write("\2\2\24\u0092\3\2\2\2\26\u00a1\3\2\2\2\30\u00a6\3\2\2")
        buf.write("\2\32\u00a8\3\2\2\2\34\u00aa\3\2\2\2\36\u00ac\3\2\2\2")
        buf.write(" \u00b2\3\2\2\2\"\u00c2\3\2\2\2$\u00c4\3\2\2\2&\u00ce")
        buf.write("\3\2\2\2(\u00d6\3\2\2\2*\u00d8\3\2\2\2,\u00de\3\2\2\2")
        buf.write(".\u00e1\3\2\2\2\60\u00e7\3\2\2\2\62\u00ec\3\2\2\2\64\u00f0")
        buf.write("\3\2\2\2\66\u00f6\3\2\2\28\u00f8\3\2\2\2:\u0100\3\2\2")
        buf.write("\2<\u0107\3\2\2\2>\u0112\3\2\2\2@\u0125\3\2\2\2B\u012c")
        buf.write("\3\2\2\2D\u012e\3\2\2\2F\u013e\3\2\2\2H\u0144\3\2\2\2")
        buf.write("J\u014f\3\2\2\2L\u0151\3\2\2\2N\u0158\3\2\2\2P\u0165\3")
        buf.write("\2\2\2R\u0169\3\2\2\2T\u0176\3\2\2\2V\u017a\3\2\2\2X\u0180")
        buf.write("\3\2\2\2Z\u0187\3\2\2\2\\\u018d\3\2\2\2^\u01b3\3\2\2\2")
        buf.write("`\u01b5\3\2\2\2b\u01be\3\2\2\2de\5\n\6\2ef\7\2\2\3f\3")
        buf.write("\3\2\2\2gh\t\2\2\2h\5\3\2\2\2ij\5\b\5\2jk\7\37\2\2k\7")
        buf.write("\3\2\2\2lm\7<\2\2mo\7\33\2\2np\5> \2on\3\2\2\2op\3\2\2")
        buf.write("\2pq\3\2\2\2qr\7\34\2\2r\t\3\2\2\2sv\5\f\7\2tw\5\n\6\2")
        buf.write("uw\3\2\2\2vt\3\2\2\2vu\3\2\2\2w\13\3\2\2\2xy\7\6\2\2y")
        buf.write("}\7<\2\2z{\7\7\2\2{~\7<\2\2|~\3\2\2\2}z\3\2\2\2}|\3\2")
        buf.write("\2\2~\177\3\2\2\2\177\u0080\5\16\b\2\u0080\r\3\2\2\2\u0081")
        buf.write("\u0082\7\35\2\2\u0082\u0083\5\20\t\2\u0083\u0084\7\36")
        buf.write("\2\2\u0084\u0088\3\2\2\2\u0085\u0086\7\35\2\2\u0086\u0088")
        buf.write("\7\36\2\2\u0087\u0081\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\17\3\2\2\2\u0089\u008c\5\22\n\2\u008a\u008d\5\20\t\2")
        buf.write("\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3")
        buf.write("\2\2\2\u008d\21\3\2\2\2\u008e\u0091\5\24\13\2\u008f\u0091")
        buf.write("\5\"\22\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\23\3\2\2\2\u0092\u0093\5\26\f\2\u0093\u0094\5\30\r\2")
        buf.write("\u0094\u0095\5\36\20\2\u0095\u0096\7\37\2\2\u0096\25\3")
        buf.write("\2\2\2\u0097\u009a\7\n\2\2\u0098\u009a\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u009e\7\13\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2")
        buf.write("\2\u009d\u009c\3\2\2\2\u009e\u00a2\3\2\2\2\u009f\u00a0")
        buf.write("\7\13\2\2\u00a0\u00a2\7\n\2\2\u00a1\u0099\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a2\27\3\2\2\2\u00a3\u00a7\5\32\16\2")
        buf.write("\u00a4\u00a7\5\60\31\2\u00a5\u00a7\5\34\17\2\u00a6\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\31\3\2\2\2\u00a8\u00a9\t\3\2\2\u00a9\33\3\2\2\2\u00aa")
        buf.write("\u00ab\7<\2\2\u00ab\35\3\2\2\2\u00ac\u00b0\5 \21\2\u00ad")
        buf.write("\u00ae\7!\2\2\u00ae\u00b1\5\36\20\2\u00af\u00b1\3\2\2")
        buf.write("\2\u00b0\u00ad\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\37\3")
        buf.write("\2\2\2\u00b2\u00b6\7<\2\2\u00b3\u00b4\7$\2\2\u00b4\u00b7")
        buf.write("\5> \2\u00b5\u00b7\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7!\3\2\2\2\u00b8\u00bb\7\n\2\2\u00b9\u00bb")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\u00bd\5\30\r\2\u00bd\u00be\7<\2\2")
        buf.write("\u00be\u00bf\5(\25\2\u00bf\u00c0\5&\24\2\u00c0\u00c3\3")
        buf.write("\2\2\2\u00c1\u00c3\5$\23\2\u00c2\u00ba\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3#\3\2\2\2\u00c4\u00c5\7<\2\2\u00c5\u00c6")
        buf.write("\5(\25\2\u00c6\u00c7\5&\24\2\u00c7%\3\2\2\2\u00c8\u00c9")
        buf.write("\7\35\2\2\u00c9\u00ca\5V,\2\u00ca\u00cb\7\36\2\2\u00cb")
        buf.write("\u00cf\3\2\2\2\u00cc\u00cd\7\35\2\2\u00cd\u00cf\7\36\2")
        buf.write("\2\u00ce\u00c8\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\'\3\2")
        buf.write("\2\2\u00d0\u00d1\7\33\2\2\u00d1\u00d2\5*\26\2\u00d2\u00d3")
        buf.write("\7\34\2\2\u00d3\u00d7\3\2\2\2\u00d4\u00d5\7\33\2\2\u00d5")
        buf.write("\u00d7\7\34\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7)\3\2\2\2\u00d8\u00dc\5,\27\2\u00d9\u00da\7\37")
        buf.write("\2\2\u00da\u00dd\5*\26\2\u00db\u00dd\3\2\2\2\u00dc\u00d9")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd+\3\2\2\2\u00de\u00df")
        buf.write("\5\30\r\2\u00df\u00e0\5.\30\2\u00e0-\3\2\2\2\u00e1\u00e5")
        buf.write("\7<\2\2\u00e2\u00e3\7!\2\2\u00e3\u00e6\5.\30\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("/\3\2\2\2\u00e7\u00e8\5\32\16\2\u00e8\u00e9\7\3\2\2\u00e9")
        buf.write("\u00ea\58\35\2\u00ea\u00eb\7\4\2\2\u00eb\61\3\2\2\2\u00ec")
        buf.write("\u00ed\7\35\2\2\u00ed\u00ee\5\64\33\2\u00ee\u00ef\7\36")
        buf.write("\2\2\u00ef\63\3\2\2\2\u00f0\u00f4\5\66\34\2\u00f1\u00f2")
        buf.write("\7!\2\2\u00f2\u00f5\5\64\33\2\u00f3\u00f5\3\2\2\2\u00f4")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\65\3\2\2\2\u00f6")
        buf.write("\u00f7\t\4\2\2\u00f7\67\3\2\2\2\u00f8\u00f9\7:\2\2\u00f9")
        buf.write("9\3\2\2\2\u00fa\u00fb\7\33\2\2\u00fb\u00fc\5<\37\2\u00fc")
        buf.write("\u00fd\7\34\2\2\u00fd\u0101\3\2\2\2\u00fe\u00ff\7\33\2")
        buf.write("\2\u00ff\u0101\7\34\2\2\u0100\u00fa\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101;\3\2\2\2\u0102\u0103\5> \2\u0103\u0104")
        buf.write("\7!\2\2\u0104\u0105\5<\37\2\u0105\u0108\3\2\2\2\u0106")
        buf.write("\u0108\5> \2\u0107\u0102\3\2\2\2\u0107\u0106\3\2\2\2\u0108")
        buf.write("=\3\2\2\2\u0109\u010a\5@!\2\u010a\u010b\t\5\2\2\u010b")
        buf.write("\u010c\5@!\2\u010c\u0113\3\2\2\2\u010d\u010e\5@!\2\u010e")
        buf.write("\u010f\t\6\2\2\u010f\u0110\5@!\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u0113\5@!\2\u0112\u0109\3\2\2\2\u0112\u010d\3\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113?\3\2\2\2\u0114\u0115\5B\"\2\u0115")
        buf.write("\u0116\t\7\2\2\u0116\u0117\5@!\2\u0117\u0126\3\2\2\2\u0118")
        buf.write("\u0119\5B\"\2\u0119\u011a\t\b\2\2\u011a\u011b\5@!\2\u011b")
        buf.write("\u0126\3\2\2\2\u011c\u011d\5B\"\2\u011d\u011e\t\t\2\2")
        buf.write("\u011e\u011f\5@!\2\u011f\u0126\3\2\2\2\u0120\u0121\5B")
        buf.write("\"\2\u0121\u0122\7\64\2\2\u0122\u0123\5@!\2\u0123\u0126")
        buf.write("\3\2\2\2\u0124\u0126\5B\"\2\u0125\u0114\3\2\2\2\u0125")
        buf.write("\u0118\3\2\2\2\u0125\u011c\3\2\2\2\u0125\u0120\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126A\3\2\2\2\u0127\u0128\7\63\2")
        buf.write("\2\u0128\u012d\5B\"\2\u0129\u012a\t\b\2\2\u012a\u012d")
        buf.write("\5B\"\2\u012b\u012d\5D#\2\u012c\u0127\3\2\2\2\u012c\u0129")
        buf.write("\3\2\2\2\u012c\u012b\3\2\2\2\u012dC\3\2\2\2\u012e\u012f")
        buf.write("\b#\1\2\u012f\u0130\5F$\2\u0130\u0138\3\2\2\2\u0131\u0132")
        buf.write("\f\4\2\2\u0132\u0133\7\3\2\2\u0133\u0134\5> \2\u0134\u0135")
        buf.write("\7\4\2\2\u0135\u0137\3\2\2\2\u0136\u0131\3\2\2\2\u0137")
        buf.write("\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139E\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u013f\5N(\2")
        buf.write("\u013c\u013f\5R*\2\u013d\u013f\5H%\2\u013e\u013b\3\2\2")
        buf.write("\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013fG\3\2")
        buf.write("\2\2\u0140\u0141\7\b\2\2\u0141\u0142\7<\2\2\u0142\u0145")
        buf.write("\5:\36\2\u0143\u0145\5J&\2\u0144\u0140\3\2\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145I\3\2\2\2\u0146\u0150\7:\2\2\u0147\u0150")
        buf.write("\78\2\2\u0148\u0150\79\2\2\u0149\u0150\7;\2\2\u014a\u0150")
        buf.write("\5\62\32\2\u014b\u0150\7\t\2\2\u014c\u0150\7\5\2\2\u014d")
        buf.write("\u0150\7<\2\2\u014e\u0150\5L\'\2\u014f\u0146\3\2\2\2\u014f")
        buf.write("\u0147\3\2\2\2\u014f\u0148\3\2\2\2\u014f\u0149\3\2\2\2")
        buf.write("\u014f\u014a\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014c\3")
        buf.write("\2\2\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150K")
        buf.write("\3\2\2\2\u0151\u0152\7\33\2\2\u0152\u0153\5> \2\u0153")
        buf.write("\u0154\7\34\2\2\u0154M\3\2\2\2\u0155\u0159\5R*\2\u0156")
        buf.write("\u0159\5H%\2\u0157\u0159\7<\2\2\u0158\u0155\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a\u015b\7\"\2\2\u015b\u015c\7<\2\2\u015c\u015d\5")
        buf.write(":\36\2\u015d\u015e\5P)\2\u015eO\3\2\2\2\u015f\u0160\7")
        buf.write("\"\2\2\u0160\u0161\7<\2\2\u0161\u0162\5:\36\2\u0162\u0163")
        buf.write("\5P)\2\u0163\u0166\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u015f")
        buf.write("\3\2\2\2\u0165\u0164\3\2\2\2\u0166Q\3\2\2\2\u0167\u016a")
        buf.write("\5H%\2\u0168\u016a\7<\2\2\u0169\u0167\3\2\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\5P)\2\u016c\u016d")
        buf.write("\7\"\2\2\u016d\u016e\7<\2\2\u016e\u016f\5T+\2\u016fS\3")
        buf.write("\2\2\2\u0170\u0171\5P)\2\u0171\u0172\7\"\2\2\u0172\u0173")
        buf.write("\7<\2\2\u0173\u0174\5T+\2\u0174\u0177\3\2\2\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0170\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("U\3\2\2\2\u0178\u017b\5X-\2\u0179\u017b\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2")
        buf.write("\u017c\u017f\5\\/\2\u017d\u017f\3\2\2\2\u017e\u017c\3")
        buf.write("\2\2\2\u017e\u017d\3\2\2\2\u017fW\3\2\2\2\u0180\u0183")
        buf.write("\5Z.\2\u0181\u0184\5X-\2\u0182\u0184\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0183\u0182\3\2\2\2\u0184Y\3\2\2\2\u0185\u0188")
        buf.write("\7\13\2\2\u0186\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\5\30\r")
        buf.write("\2\u018a\u018b\5\36\20\2\u018b\u018c\7\37\2\2\u018c[\3")
        buf.write("\2\2\2\u018d\u0190\5^\60\2\u018e\u0191\5\\/\2\u018f\u0191")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("]\3\2\2\2\u0192\u01b4\5&\24\2\u0193\u0194\5b\62\2\u0194")
        buf.write("\u0195\7#\2\2\u0195\u0196\5> \2\u0196\u0197\7\37\2\2\u0197")
        buf.write("\u01b4\3\2\2\2\u0198\u0199\7\21\2\2\u0199\u019a\5> \2")
        buf.write("\u019a\u019b\7\23\2\2\u019b\u019f\5^\60\2\u019c\u019d")
        buf.write("\7\22\2\2\u019d\u01a0\5^\60\2\u019e\u01a0\3\2\2\2\u019f")
        buf.write("\u019c\3\2\2\2\u019f\u019e\3\2\2\2\u01a0\u01b4\3\2\2\2")
        buf.write("\u01a1\u01a2\7\24\2\2\u01a2\u01a3\5`\61\2\u01a3\u01a4")
        buf.write("\7#\2\2\u01a4\u01a5\5> \2\u01a5\u01a6\t\n\2\2\u01a6\u01a7")
        buf.write("\5> \2\u01a7\u01a8\7\27\2\2\u01a8\u01a9\5^\60\2\u01a9")
        buf.write("\u01b4\3\2\2\2\u01aa\u01ab\t\13\2\2\u01ab\u01b4\7\37\2")
        buf.write("\2\u01ac\u01ad\7\32\2\2\u01ad\u01ae\5> \2\u01ae\u01af")
        buf.write("\7\37\2\2\u01af\u01b4\3\2\2\2\u01b0\u01b1\5N(\2\u01b1")
        buf.write("\u01b2\7\37\2\2\u01b2\u01b4\3\2\2\2\u01b3\u0192\3\2\2")
        buf.write("\2\u01b3\u0193\3\2\2\2\u01b3\u0198\3\2\2\2\u01b3\u01a1")
        buf.write("\3\2\2\2\u01b3\u01aa\3\2\2\2\u01b3\u01ac\3\2\2\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b4_\3\2\2\2\u01b5\u01b6\7<\2\2\u01b6")
        buf.write("a\3\2\2\2\u01b7\u01bf\7<\2\2\u01b8\u01bf\5R*\2\u01b9\u01ba")
        buf.write("\5F$\2\u01ba\u01bb\7\3\2\2\u01bb\u01bc\5> \2\u01bc\u01bd")
        buf.write("\7\4\2\2\u01bd\u01bf\3\2\2\2\u01be\u01b7\3\2\2\2\u01be")
        buf.write("\u01b8\3\2\2\2\u01be\u01b9\3\2\2\2\u01bfc\3\2\2\2*ov}")
        buf.write("\u0087\u008c\u0090\u0099\u009d\u00a1\u00a6\u00b0\u00b6")
        buf.write("\u00ba\u00c2\u00ce\u00d6\u00dc\u00e5\u00f4\u0100\u0107")
        buf.write("\u0112\u0125\u012c\u0138\u013e\u0144\u014f\u0158\u0165")
        buf.write("\u0169\u0176\u017a\u017e\u0183\u0187\u0190\u019f\u01b3")
        buf.write("\u01be")
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
                      "INTLIT", "BOOLLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
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
    RULE_stmBlock = 18
    RULE_paramList = 19
    RULE_paramDeclare = 20
    RULE_param = 21
    RULE_idList = 22
    RULE_arraytype = 23
    RULE_arrayLit = 24
    RULE_elemList = 25
    RULE_elem = 26
    RULE_size = 27
    RULE_explist = 28
    RULE_exps = 29
    RULE_exp = 30
    RULE_exp1 = 31
    RULE_exp2 = 32
    RULE_exp3 = 33
    RULE_exp4 = 34
    RULE_exp5 = 35
    RULE_operand = 36
    RULE_subexp = 37
    RULE_methodInvoke = 38
    RULE_methodRecur = 39
    RULE_attriAccess = 40
    RULE_attriRecur = 41
    RULE_stmList = 42
    RULE_variables = 43
    RULE_variable = 44
    RULE_stms = 45
    RULE_stm = 46
    RULE_scala_var = 47
    RULE_lhs = 48

    ruleNames =  [ "program", "mptype", "body", "funcall", "classdcls", 
                   "classdcl", "memBlock", "memList", "classMember", "attributeDeclare", 
                   "attribute_type", "vartype", "primtype", "classtype", 
                   "attributeList", "attri", "methodDeclare", "constructor", 
                   "stmBlock", "paramList", "paramDeclare", "param", "idList", 
                   "arraytype", "arrayLit", "elemList", "elem", "size", 
                   "explist", "exps", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "operand", "subexp", "methodInvoke", "methodRecur", 
                   "attriAccess", "attriRecur", "stmList", "variables", 
                   "variable", "stms", "stm", "scala_var", "lhs" ]

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
    INTLIT=56
    BOOLLIT=57
    ID=58
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
            self.state = 98
            self.classdcls()
            self.state = 99
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
            self.state = 101
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
            self.state = 103
            self.funcall()
            self.state = 104
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
            self.state = 106
            self.match(BKOOLParser.ID)
            self.state = 107
            self.match(BKOOLParser.LB)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__2) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.SELF) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 108
                self.exp()


            self.state = 111
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
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.classdcl()
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CLASS]:
                self.state = 114
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
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKOOLParser.CLASS)
            self.state = 119
            self.match(BKOOLParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTEND]:
                self.state = 120
                self.match(BKOOLParser.EXTEND)
                self.state = 121
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.memBlock()
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(BKOOLParser.LP)
                self.state = 128
                self.memList()
                self.state = 129
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(BKOOLParser.LP)
                self.state = 132
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
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.classMember()
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC, BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.state = 136
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
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
            self.state = 144
            self.attribute_type()
            self.state = 145
            self.vartype()
            self.state = 146
            self.attributeList()
            self.state = 147
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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 149
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.MUTABLE]:
                    self.state = 153
                    self.match(BKOOLParser.MUTABLE)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(BKOOLParser.MUTABLE)
                self.state = 158
                self.match(BKOOLParser.STATIC)
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
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
            self.state = 166
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
            self.state = 168
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
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.attri()
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 171
                self.match(BKOOLParser.COMMA)
                self.state = 172
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
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BKOOLParser.ID)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ASG]:
                self.state = 177
                self.match(BKOOLParser.ASG)
                self.state = 178
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


    class MethodDeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def stmBlock(self):
            return self.getTypedRuleContext(BKOOLParser.StmBlockContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 182
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 186
                self.vartype()
                self.state = 187
                self.match(BKOOLParser.ID)
                self.state = 188
                self.paramList()
                self.state = 189
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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
            self.state = 194
            self.match(BKOOLParser.ID)
            self.state = 195
            self.paramList()
            self.state = 196
            self.stmBlock()
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
        self.enterRule(localctx, 36, self.RULE_stmBlock)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(BKOOLParser.LP)
                self.state = 199
                self.stmList()
                self.state = 200
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(BKOOLParser.LP)
                self.state = 203
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
        self.enterRule(localctx, 38, self.RULE_paramList)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(BKOOLParser.LB)
                self.state = 207
                self.paramDeclare()
                self.state = 208
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(BKOOLParser.LB)
                self.state = 211
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
        self.enterRule(localctx, 40, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.param()
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.state = 215
                self.match(BKOOLParser.SEMI)
                self.state = 216
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
        self.enterRule(localctx, 42, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.vartype()
            self.state = 221
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
        self.enterRule(localctx, 44, self.RULE_idList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BKOOLParser.ID)
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 224
                self.match(BKOOLParser.COMMA)
                self.state = 225
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
        self.enterRule(localctx, 46, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.primtype()
            self.state = 230
            self.match(BKOOLParser.T__0)
            self.state = 231
            self.size()
            self.state = 232
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
        self.enterRule(localctx, 48, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKOOLParser.LP)
            self.state = 235
            self.elemList()
            self.state = 236
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
        self.enterRule(localctx, 50, self.RULE_elemList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.elem()
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 239
                self.match(BKOOLParser.COMMA)
                self.state = 240
                self.elemList()
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
        self.enterRule(localctx, 52, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
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
        self.enterRule(localctx, 54, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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
        self.enterRule(localctx, 56, self.RULE_explist)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(BKOOLParser.LB)
                self.state = 249
                self.exps()
                self.state = 250
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(BKOOLParser.LB)
                self.state = 253
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
        self.enterRule(localctx, 58, self.RULE_exps)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.exp()
                self.state = 257
                self.match(BKOOLParser.COMMA)
                self.state = 258
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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
        self.enterRule(localctx, 60, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.exp1()
                self.state = 264
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.exp1()
                self.state = 268
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 269
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
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
        self.enterRule(localctx, 62, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.exp2()
                self.state = 275
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 276
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.exp2()
                self.state = 279
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.exp2()
                self.state = 283
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.exp2()
                self.state = 287
                self.match(BKOOLParser.CON)
                self.state = 288
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 290
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
        self.enterRule(localctx, 64, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(BKOOLParser.NOT)
                self.state = 294
                self.exp2()
                pass
            elif token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.exp2()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    self.match(BKOOLParser.T__0)
                    self.state = 305
                    self.exp()
                    self.state = 306
                    self.match(BKOOLParser.T__1) 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_exp4)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
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
        self.enterRule(localctx, 70, self.RULE_exp5)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(BKOOLParser.NEW)
                self.state = 319
                self.match(BKOOLParser.ID)
                self.state = 320
                self.explist()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.SELF, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
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
        self.enterRule(localctx, 72, self.RULE_operand)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 328
                self.arrayLit()
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 329
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 7)
                self.state = 330
                self.match(BKOOLParser.T__2)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 331
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 9)
                self.state = 332
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
        self.enterRule(localctx, 74, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(BKOOLParser.LB)
            self.state = 336
            self.exp()
            self.state = 337
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
        self.enterRule(localctx, 76, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 339
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 340
                self.exp5()
                pass

            elif la_ == 3:
                self.state = 341
                self.match(BKOOLParser.ID)
                pass


            self.state = 344
            self.match(BKOOLParser.DOT)
            self.state = 345
            self.match(BKOOLParser.ID)
            self.state = 346
            self.explist()
            self.state = 347
            self.methodRecur()
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
        self.enterRule(localctx, 78, self.RULE_methodRecur)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(BKOOLParser.DOT)
                self.state = 350
                self.match(BKOOLParser.ID)
                self.state = 351
                self.explist()
                self.state = 352
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
        self.enterRule(localctx, 80, self.RULE_attriAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 357
                self.exp5()
                pass

            elif la_ == 2:
                self.state = 358
                self.match(BKOOLParser.ID)
                pass


            self.state = 361
            self.methodRecur()
            self.state = 362
            self.match(BKOOLParser.DOT)
            self.state = 363
            self.match(BKOOLParser.ID)
            self.state = 364
            self.attriRecur()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttriRecur" ):
                return visitor.visitAttriRecur(self)
            else:
                return visitor.visitChildren(self)




    def attriRecur(self):

        localctx = BKOOLParser.AttriRecurContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_attriRecur)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.methodRecur()
                self.state = 367
                self.match(BKOOLParser.DOT)
                self.state = 368
                self.match(BKOOLParser.ID)
                self.state = 369
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
        self.enterRule(localctx, 84, self.RULE_stmList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 374
                self.variables()
                pass

            elif la_ == 2:
                pass


            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__2, BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 378
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKOOLParser.VariableContext,0)


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
        self.enterRule(localctx, 86, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.variable()
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 383
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

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
        self.enterRule(localctx, 88, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MUTABLE]:
                self.state = 387
                self.match(BKOOLParser.MUTABLE)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 391
            self.vartype()
            self.state = 392
            self.attributeList()
            self.state = 393
            self.match(BKOOLParser.SEMI)
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
        self.enterRule(localctx, 90, self.RULE_stms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.stm()
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__2, BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 396
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 92, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.lhs()
                self.state = 402
                self.match(BKOOLParser.ASGOP)
                self.state = 403
                self.exp()
                self.state = 404
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(BKOOLParser.IF)
                self.state = 407
                self.exp()
                self.state = 408
                self.match(BKOOLParser.THEN)
                self.state = 409
                self.stm()
                self.state = 413
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 410
                    self.match(BKOOLParser.ELSE)
                    self.state = 411
                    self.stm()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.match(BKOOLParser.FOR)
                self.state = 416
                self.scala_var()
                self.state = 417
                self.match(BKOOLParser.ASGOP)
                self.state = 418
                self.exp()
                self.state = 419
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 420
                self.exp()
                self.state = 421
                self.match(BKOOLParser.DO)
                self.state = 422
                self.stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 424
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.BREAK or _la==BKOOLParser.CONT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 425
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 426
                self.match(BKOOLParser.RETURN)
                self.state = 427
                self.exp()
                self.state = 428
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 430
                self.methodInvoke()
                self.state = 431
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
        self.enterRule(localctx, 94, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
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


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_lhs)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.exp4()
                self.state = 440
                self.match(BKOOLParser.T__0)
                self.state = 441
                self.exp()
                self.state = 442
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
        self._predicates[33] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




