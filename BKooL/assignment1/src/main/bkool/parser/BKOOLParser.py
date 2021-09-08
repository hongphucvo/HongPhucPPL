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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01bc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\5\5l\n\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6t\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7~\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3\t\5\t\u008c\n\t\3\n\3")
        buf.write("\n\5\n\u0090\n\n\3\13\3\13\3\13\3\13\5\13\u0096\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a3\n")
        buf.write("\r\3\16\3\16\3\16\5\16\u00a8\n\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00b3\n\21\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00b9\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00c2\n\23\3\24\3\24\3\24\3\24\3\25\3\25\5")
        buf.write("\25\u00ca\n\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00d4\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00dc")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00e3\n\31\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\5\33\u00ec\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u00fc\n\36\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u0108\n!\3\"\3\"\3\"\3\"\3\"\5\"\u010f\n\"\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\5#\u011a\n#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u012d\n$\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u0135\n%\3&\3&\3&\3&\3&\3&\5&\u013d\n&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\5\'\u0150\n\'\3(\3(\3(\3(\5(\u0156\n(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\5)\u0160\n)\3*\3*\3*\3*\5*\u0166\n")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\5+\u016f\n+\3,\5,\u0172\n,\3,\3")
        buf.write(",\3,\3,\5,\u0178\n,\3-\3-\3-\3-\3-\3-\3-\5-\u0181\n-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u019f\n.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u01a9\n.\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01ba\n")
        buf.write("\60\3\60\2\2\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\f\3\2\22")
        buf.write("\23\3\2\20\21\3\2\22\26\3\2\b\13\3\2\62\65\3\2\60\61\3")
        buf.write("\2\66\67\3\2*+\3\2,/\3\2\33\34\2\u01c9\2`\3\2\2\2\4c\3")
        buf.write("\2\2\2\6e\3\2\2\2\bh\3\2\2\2\ns\3\2\2\2\f}\3\2\2\2\16")
        buf.write("\u0085\3\2\2\2\20\u008b\3\2\2\2\22\u008f\3\2\2\2\24\u0095")
        buf.write("\3\2\2\2\26\u0097\3\2\2\2\30\u00a2\3\2\2\2\32\u00a7\3")
        buf.write("\2\2\2\34\u00a9\3\2\2\2\36\u00ab\3\2\2\2 \u00b2\3\2\2")
        buf.write("\2\"\u00b8\3\2\2\2$\u00c1\3\2\2\2&\u00c3\3\2\2\2(\u00c9")
        buf.write("\3\2\2\2*\u00cb\3\2\2\2,\u00d3\3\2\2\2.\u00db\3\2\2\2")
        buf.write("\60\u00e2\3\2\2\2\62\u00e4\3\2\2\2\64\u00eb\3\2\2\2\66")
        buf.write("\u00ed\3\2\2\28\u00f2\3\2\2\2:\u00fb\3\2\2\2<\u00fd\3")
        buf.write("\2\2\2>\u00ff\3\2\2\2@\u0107\3\2\2\2B\u010e\3\2\2\2D\u0119")
        buf.write("\3\2\2\2F\u012c\3\2\2\2H\u0134\3\2\2\2J\u013c\3\2\2\2")
        buf.write("L\u014f\3\2\2\2N\u0155\3\2\2\2P\u015f\3\2\2\2R\u0165\3")
        buf.write("\2\2\2T\u016e\3\2\2\2V\u0177\3\2\2\2X\u0180\3\2\2\2Z\u01a8")
        buf.write("\3\2\2\2\\\u01aa\3\2\2\2^\u01b9\3\2\2\2`a\5\n\6\2ab\7")
        buf.write("\2\2\3b\3\3\2\2\2cd\t\2\2\2d\5\3\2\2\2ef\5\b\5\2fg\7%")
        buf.write("\2\2g\7\3\2\2\2hi\7\7\2\2ik\7!\2\2jl\5D#\2kj\3\2\2\2k")
        buf.write("l\3\2\2\2lm\3\2\2\2mn\7\"\2\2n\t\3\2\2\2op\5\f\7\2pq\5")
        buf.write("\n\6\2qt\3\2\2\2rt\5\f\7\2so\3\2\2\2sr\3\2\2\2t\13\3\2")
        buf.write("\2\2uv\7\f\2\2vw\7\7\2\2w~\5\16\b\2xy\7\f\2\2yz\7\7\2")
        buf.write("\2z{\7\r\2\2{|\7\7\2\2|~\5\16\b\2}u\3\2\2\2}x\3\2\2\2")
        buf.write("~\r\3\2\2\2\177\u0080\7#\2\2\u0080\u0081\5\20\t\2\u0081")
        buf.write("\u0082\7$\2\2\u0082\u0086\3\2\2\2\u0083\u0084\7#\2\2\u0084")
        buf.write("\u0086\7$\2\2\u0085\177\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write("\17\3\2\2\2\u0087\u0088\5\22\n\2\u0088\u0089\5\20\t\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u008c\5\22\n\2\u008b\u0087")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008c\21\3\2\2\2\u008d\u0090")
        buf.write("\5\26\f\2\u008e\u0090\5$\23\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\23\3\2\2\2\u0091\u0092\5\26\f\2\u0092")
        buf.write("\u0093\5\24\13\2\u0093\u0096\3\2\2\2\u0094\u0096\3\2\2")
        buf.write("\2\u0095\u0091\3\2\2\2\u0095\u0094\3\2\2\2\u0096\25\3")
        buf.write("\2\2\2\u0097\u0098\5\30\r\2\u0098\u0099\5\32\16\2\u0099")
        buf.write("\u009a\5 \21\2\u009a\u009b\7%\2\2\u009b\27\3\2\2\2\u009c")
        buf.write("\u009d\7\20\2\2\u009d\u00a3\7\21\2\2\u009e\u009f\7\21")
        buf.write("\2\2\u009f\u00a3\7\20\2\2\u00a0\u00a3\t\3\2\2\u00a1\u00a3")
        buf.write("\3\2\2\2\u00a2\u009c\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\31\3\2\2\2\u00a4")
        buf.write("\u00a8\5\34\17\2\u00a5\u00a8\5\66\34\2\u00a6\u00a8\5\36")
        buf.write("\20\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\33\3\2\2\2\u00a9\u00aa\t\4\2\2\u00aa\35")
        buf.write("\3\2\2\2\u00ab\u00ac\7\7\2\2\u00ac\37\3\2\2\2\u00ad\u00ae")
        buf.write("\5\"\22\2\u00ae\u00af\7\'\2\2\u00af\u00b0\5 \21\2\u00b0")
        buf.write("\u00b3\3\2\2\2\u00b1\u00b3\5\"\22\2\u00b2\u00ad\3\2\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3!\3\2\2\2\u00b4\u00b5\7\7")
        buf.write("\2\2\u00b5\u00b6\7)\2\2\u00b6\u00b9\5D#\2\u00b7\u00b9")
        buf.write("\7\7\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("#\3\2\2\2\u00ba\u00bb\5(\25\2\u00bb\u00bc\5*\26\2\u00bc")
        buf.write("\u00bd\7\7\2\2\u00bd\u00be\5.\30\2\u00be\u00bf\5,\27\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00c2\5&\24\2\u00c1\u00ba\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2%\3\2\2\2\u00c3\u00c4")
        buf.write("\7\7\2\2\u00c4\u00c5\5\60\31\2\u00c5\u00c6\5,\27\2\u00c6")
        buf.write("\'\3\2\2\2\u00c7\u00ca\7\20\2\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca)\3\2\2\2\u00cb")
        buf.write("\u00cc\5\32\16\2\u00cc+\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce")
        buf.write("\u00cf\5R*\2\u00cf\u00d0\7$\2\2\u00d0\u00d4\3\2\2\2\u00d1")
        buf.write("\u00d2\7#\2\2\u00d2\u00d4\7$\2\2\u00d3\u00cd\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4-\3\2\2\2\u00d5\u00d6\7!\2\2\u00d6")
        buf.write("\u00d7\5\60\31\2\u00d7\u00d8\7\"\2\2\u00d8\u00dc\3\2\2")
        buf.write("\2\u00d9\u00da\7!\2\2\u00da\u00dc\7\"\2\2\u00db\u00d5")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc/\3\2\2\2\u00dd\u00de")
        buf.write("\5\62\32\2\u00de\u00df\7%\2\2\u00df\u00e0\5\60\31\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00e3\5\62\32\2\u00e2\u00dd\3\2\2")
        buf.write("\2\u00e2\u00e1\3\2\2\2\u00e3\61\3\2\2\2\u00e4\u00e5\5")
        buf.write("\32\16\2\u00e5\u00e6\5\64\33\2\u00e6\63\3\2\2\2\u00e7")
        buf.write("\u00e8\7\7\2\2\u00e8\u00e9\7\'\2\2\u00e9\u00ec\5\64\33")
        buf.write("\2\u00ea\u00ec\7\7\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\65\3\2\2\2\u00ed\u00ee\5\34\17\2\u00ee")
        buf.write("\u00ef\7\3\2\2\u00ef\u00f0\5> \2\u00f0\u00f1\7\4\2\2\u00f1")
        buf.write("\67\3\2\2\2\u00f2\u00f3\7#\2\2\u00f3\u00f4\5:\36\2\u00f4")
        buf.write("\u00f5\7$\2\2\u00f59\3\2\2\2\u00f6\u00f7\5<\37\2\u00f7")
        buf.write("\u00f8\7\'\2\2\u00f8\u00f9\5:\36\2\u00f9\u00fc\3\2\2\2")
        buf.write("\u00fa\u00fc\5<\37\2\u00fb\u00f6\3\2\2\2\u00fb\u00fa\3")
        buf.write("\2\2\2\u00fc;\3\2\2\2\u00fd\u00fe\t\5\2\2\u00fe=\3\2\2")
        buf.write("\2\u00ff\u0100\7\b\2\2\u0100?\3\2\2\2\u0101\u0102\7!\2")
        buf.write("\2\u0102\u0103\5B\"\2\u0103\u0104\7\"\2\2\u0104\u0108")
        buf.write("\3\2\2\2\u0105\u0106\7!\2\2\u0106\u0108\7\"\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0107\u0105\3\2\2\2\u0108A\3\2\2\2\u0109")
        buf.write("\u010a\5D#\2\u010a\u010b\7\'\2\2\u010b\u010c\5B\"\2\u010c")
        buf.write("\u010f\3\2\2\2\u010d\u010f\5D#\2\u010e\u0109\3\2\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010fC\3\2\2\2\u0110\u0111\5F$\2\u0111")
        buf.write("\u0112\t\6\2\2\u0112\u0113\5F$\2\u0113\u011a\3\2\2\2\u0114")
        buf.write("\u0115\5F$\2\u0115\u0116\t\7\2\2\u0116\u0117\5F$\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u011a\5F$\2\u0119\u0110\3\2\2\2\u0119")
        buf.write("\u0114\3\2\2\2\u0119\u0118\3\2\2\2\u011aE\3\2\2\2\u011b")
        buf.write("\u011c\5H%\2\u011c\u011d\t\b\2\2\u011d\u011e\5F$\2\u011e")
        buf.write("\u012d\3\2\2\2\u011f\u0120\5H%\2\u0120\u0121\t\t\2\2\u0121")
        buf.write("\u0122\5F$\2\u0122\u012d\3\2\2\2\u0123\u0124\5H%\2\u0124")
        buf.write("\u0125\t\n\2\2\u0125\u0126\5F$\2\u0126\u012d\3\2\2\2\u0127")
        buf.write("\u0128\5H%\2\u0128\u0129\79\2\2\u0129\u012a\5F$\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u012d\5H%\2\u012c\u011b\3\2\2\2\u012c")
        buf.write("\u011f\3\2\2\2\u012c\u0123\3\2\2\2\u012c\u0127\3\2\2\2")
        buf.write("\u012c\u012b\3\2\2\2\u012dG\3\2\2\2\u012e\u012f\78\2\2")
        buf.write("\u012f\u0135\5J&\2\u0130\u0135\7*\2\2\u0131\u0132\7+\2")
        buf.write("\2\u0132\u0135\5J&\2\u0133\u0135\5J&\2\u0134\u012e\3\2")
        buf.write("\2\2\u0134\u0130\3\2\2\2\u0134\u0131\3\2\2\2\u0134\u0133")
        buf.write("\3\2\2\2\u0135I\3\2\2\2\u0136\u0137\5L\'\2\u0137\u0138")
        buf.write("\7\3\2\2\u0138\u0139\5B\"\2\u0139\u013a\7\4\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u013d\5L\'\2\u013c\u0136\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013dK\3\2\2\2\u013e\u013f\5N(\2")
        buf.write("\u013f\u0140\7(\2\2\u0140\u0141\7\7\2\2\u0141\u0150\3")
        buf.write("\2\2\2\u0142\u0143\7\7\2\2\u0143\u0144\7(\2\2\u0144\u0150")
        buf.write("\7\7\2\2\u0145\u0146\5N(\2\u0146\u0147\7(\2\2\u0147\u0148")
        buf.write("\7\7\2\2\u0148\u0149\5@!\2\u0149\u0150\3\2\2\2\u014a\u014b")
        buf.write("\7\7\2\2\u014b\u014c\7(\2\2\u014c\u014d\7\7\2\2\u014d")
        buf.write("\u0150\5@!\2\u014e\u0150\5N(\2\u014f\u013e\3\2\2\2\u014f")
        buf.write("\u0142\3\2\2\2\u014f\u0145\3\2\2\2\u014f\u014a\3\2\2\2")
        buf.write("\u014f\u014e\3\2\2\2\u0150M\3\2\2\2\u0151\u0152\7\16\2")
        buf.write("\2\u0152\u0153\7\7\2\2\u0153\u0156\5@!\2\u0154\u0156\5")
        buf.write("P)\2\u0155\u0151\3\2\2\2\u0155\u0154\3\2\2\2\u0156O\3")
        buf.write("\2\2\2\u0157\u0160\7\b\2\2\u0158\u0160\7\n\2\2\u0159\u0160")
        buf.write("\7\13\2\2\u015a\u0160\7\t\2\2\u015b\u0160\58\35\2\u015c")
        buf.write("\u0160\7\17\2\2\u015d\u0160\7\5\2\2\u015e\u0160\7\7\2")
        buf.write("\2\u015f\u0157\3\2\2\2\u015f\u0158\3\2\2\2\u015f\u0159")
        buf.write("\3\2\2\2\u015f\u015a\3\2\2\2\u015f\u015b\3\2\2\2\u015f")
        buf.write("\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160Q\3\2\2\2\u0161\u0162\5T+\2\u0162\u0163\5X-\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0166\5X-\2\u0165\u0161\3\2\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166S\3\2\2\2\u0167\u0168\5V,\2\u0168")
        buf.write("\u0169\7%\2\2\u0169\u016a\5T+\2\u016a\u016f\3\2\2\2\u016b")
        buf.write("\u016c\5V,\2\u016c\u016d\7%\2\2\u016d\u016f\3\2\2\2\u016e")
        buf.write("\u0167\3\2\2\2\u016e\u016b\3\2\2\2\u016fU\3\2\2\2\u0170")
        buf.write("\u0172\7\21\2\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2")
        buf.write("\2\u0172\u0173\3\2\2\2\u0173\u0174\5\32\16\2\u0174\u0175")
        buf.write("\5\64\33\2\u0175\u0178\3\2\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0171\3\2\2\2\u0177\u0176\3\2\2\2\u0178W\3\2\2\2\u0179")
        buf.write("\u017a\5Z.\2\u017a\u017b\7%\2\2\u017b\u017c\5X-\2\u017c")
        buf.write("\u0181\3\2\2\2\u017d\u017e\5Z.\2\u017e\u017f\7%\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u0179\3\2\2\2\u0180\u017d\3\2\2\2")
        buf.write("\u0181Y\3\2\2\2\u0182\u0183\5^\60\2\u0183\u0184\7\6\2")
        buf.write("\2\u0184\u0185\5D#\2\u0185\u01a9\3\2\2\2\u0186\u0187\7")
        buf.write("\27\2\2\u0187\u0188\5D#\2\u0188\u0189\7\31\2\2\u0189\u018a")
        buf.write("\5Z.\2\u018a\u01a9\3\2\2\2\u018b\u018c\7\27\2\2\u018c")
        buf.write("\u018d\5D#\2\u018d\u018e\7\31\2\2\u018e\u018f\5Z.\2\u018f")
        buf.write("\u0190\7%\2\2\u0190\u0191\7\30\2\2\u0191\u0192\5Z.\2\u0192")
        buf.write("\u01a9\3\2\2\2\u0193\u0194\7\32\2\2\u0194\u0195\5\\/\2")
        buf.write("\u0195\u0196\7\6\2\2\u0196\u0197\5F$\2\u0197\u0198\t\13")
        buf.write("\2\2\u0198\u0199\5H%\2\u0199\u019e\7\35\2\2\u019a\u019f")
        buf.write("\5,\27\2\u019b\u019c\5Z.\2\u019c\u019d\7%\2\2\u019d\u019f")
        buf.write("\3\2\2\2\u019e\u019a\3\2\2\2\u019e\u019b\3\2\2\2\u019f")
        buf.write("\u01a9\3\2\2\2\u01a0\u01a9\7\36\2\2\u01a1\u01a9\7\37\2")
        buf.write("\2\u01a2\u01a3\7 \2\2\u01a3\u01a9\5D#\2\u01a4\u01a5\7")
        buf.write("\7\2\2\u01a5\u01a6\7(\2\2\u01a6\u01a7\7\7\2\2\u01a7\u01a9")
        buf.write("\5@!\2\u01a8\u0182\3\2\2\2\u01a8\u0186\3\2\2\2\u01a8\u018b")
        buf.write("\3\2\2\2\u01a8\u0193\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8")
        buf.write("\u01a1\3\2\2\2\u01a8\u01a2\3\2\2\2\u01a8\u01a4\3\2\2\2")
        buf.write("\u01a9[\3\2\2\2\u01aa\u01ab\7\7\2\2\u01ab]\3\2\2\2\u01ac")
        buf.write("\u01ba\7\7\2\2\u01ad\u01ae\7\7\2\2\u01ae\u01af\7(\2\2")
        buf.write("\u01af\u01ba\7\7\2\2\u01b0\u01b1\5D#\2\u01b1\u01b2\7(")
        buf.write("\2\2\u01b2\u01b3\7\7\2\2\u01b3\u01ba\3\2\2\2\u01b4\u01b5")
        buf.write("\5D#\2\u01b5\u01b6\7\3\2\2\u01b6\u01b7\5D#\2\u01b7\u01b8")
        buf.write("\7\4\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01ac\3\2\2\2\u01b9")
        buf.write("\u01ad\3\2\2\2\u01b9\u01b0\3\2\2\2\u01b9\u01b4\3\2\2\2")
        buf.write("\u01ba_\3\2\2\2%ks}\u0085\u008b\u008f\u0095\u00a2\u00a7")
        buf.write("\u00b2\u00b8\u00c1\u00c9\u00d3\u00db\u00e2\u00eb\u00fb")
        buf.write("\u0107\u010e\u0119\u012c\u0134\u013c\u014f\u0155\u015f")
        buf.write("\u0165\u016e\u0171\u0177\u0180\u019e\u01a8\u01b9")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'nil'", "':='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'class'", "'extends'", "'new'", "'this'", "'static'", 
                     "'final'", "'int'", "'void'", "'float'", "'boolean'", 
                     "'string'", "'if'", "'else'", "'then'", "'for'", "'to'", 
                     "'downto'", "'do'", "'break'", "'continue'", "'return'", 
                     "'('", "')'", "'{'", "'}'", "';'", "':'", "','", "'.'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INTLIT", "BOOLLIT", "FLOATLIT", 
                      "STRINGLIT", "CLASS", "EXTEND", "NEW", "SELF", "STATIC", 
                      "MUTABLE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", 
                      "STRINGTYPE", "IF", "ELSE", "THEN", "FOR", "TO", "DOWNTO", 
                      "DO", "BREAK", "CONT", "RETURN", "LB", "RB", "LP", 
                      "RP", "SEMI", "COLON", "COMMA", "DOT", "ASG", "ADD", 
                      "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", 
                      "EQ", "LT", "GT", "LEQ", "GEQ", "OR", "AND", "NOT", 
                      "CON", "LINECMT", "BLOCKCMT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_funcall = 3
    RULE_classdcls = 4
    RULE_classdcl = 5
    RULE_memBlock = 6
    RULE_memList = 7
    RULE_classMember = 8
    RULE_attributes = 9
    RULE_attributeDeclare = 10
    RULE_attribute_type = 11
    RULE_vartype = 12
    RULE_primtype = 13
    RULE_classtype = 14
    RULE_attributeList = 15
    RULE_attri = 16
    RULE_methodDeclare = 17
    RULE_constructor = 18
    RULE_methodType = 19
    RULE_returnType = 20
    RULE_stmBlock = 21
    RULE_paramList = 22
    RULE_paramDeclare = 23
    RULE_param = 24
    RULE_idList = 25
    RULE_arraytype = 26
    RULE_arrayLit = 27
    RULE_elemList = 28
    RULE_elem = 29
    RULE_size = 30
    RULE_explist = 31
    RULE_exps = 32
    RULE_exp = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_operand = 39
    RULE_stmList = 40
    RULE_variables = 41
    RULE_variable = 42
    RULE_stms = 43
    RULE_stm = 44
    RULE_scala_var = 45
    RULE_lhs = 46

    ruleNames =  [ "program", "mptype", "body", "funcall", "classdcls", 
                   "classdcl", "memBlock", "memList", "classMember", "attributes", 
                   "attributeDeclare", "attribute_type", "vartype", "primtype", 
                   "classtype", "attributeList", "attri", "methodDeclare", 
                   "constructor", "methodType", "returnType", "stmBlock", 
                   "paramList", "paramDeclare", "param", "idList", "arraytype", 
                   "arrayLit", "elemList", "elem", "size", "explist", "exps", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "operand", 
                   "stmList", "variables", "variable", "stms", "stm", "scala_var", 
                   "lhs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    INTLIT=6
    BOOLLIT=7
    FLOATLIT=8
    STRINGLIT=9
    CLASS=10
    EXTEND=11
    NEW=12
    SELF=13
    STATIC=14
    MUTABLE=15
    INTTYPE=16
    VOIDTYPE=17
    FLOATTYPE=18
    BOOLTYPE=19
    STRINGTYPE=20
    IF=21
    ELSE=22
    THEN=23
    FOR=24
    TO=25
    DOWNTO=26
    DO=27
    BREAK=28
    CONT=29
    RETURN=30
    LB=31
    RB=32
    LP=33
    RP=34
    SEMI=35
    COLON=36
    COMMA=37
    DOT=38
    ASG=39
    ADD=40
    SUB=41
    MUL=42
    FLOATDIV=43
    INTDIV=44
    MOD=45
    NEQ=46
    EQ=47
    LT=48
    GT=49
    LEQ=50
    GEQ=51
    OR=52
    AND=53
    NOT=54
    CON=55
    LINECMT=56
    BLOCKCMT=57
    WS=58
    ILLEGAL_ESCAPE=59
    UNCLOSE_STRING=60
    ERROR_CHAR=61
    UNTERMINATED_COMMENT=62

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
            self.state = 94
            self.classdcls()
            self.state = 95
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
            self.state = 97
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
            self.state = 99
            self.funcall()
            self.state = 100
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
            self.state = 102
            self.match(BKOOLParser.ID)
            self.state = 103
            self.match(BKOOLParser.LB)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__2) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.SELF) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT))) != 0):
                self.state = 104
                self.exp()


            self.state = 107
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.classdcl()
                self.state = 110
                self.classdcls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(BKOOLParser.CLASS)
                self.state = 116
                self.match(BKOOLParser.ID)
                self.state = 117
                self.memBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(BKOOLParser.CLASS)
                self.state = 119
                self.match(BKOOLParser.ID)
                self.state = 120
                self.match(BKOOLParser.EXTEND)
                self.state = 121
                self.match(BKOOLParser.ID)
                self.state = 122
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(BKOOLParser.LP)
                self.state = 126
                self.memList()
                self.state = 127
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(BKOOLParser.LP)
                self.state = 130
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.classMember()
                self.state = 134
                self.memList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.methodDeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclareContext,0)


        def attributes(self):
            return self.getTypedRuleContext(BKOOLParser.AttributesContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = BKOOLParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributes)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.attributeDeclare()
                self.state = 144
                self.attributes()
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
        self.enterRule(localctx, 20, self.RULE_attributeDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.attribute_type()
            self.state = 150
            self.vartype()
            self.state = 151
            self.attributeList()
            self.state = 152
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
        self.enterRule(localctx, 22, self.RULE_attribute_type)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(BKOOLParser.STATIC)
                self.state = 155
                self.match(BKOOLParser.MUTABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(BKOOLParser.MUTABLE)
                self.state = 157
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.STATIC or _la==BKOOLParser.MUTABLE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 24, self.RULE_vartype)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
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
        self.enterRule(localctx, 26, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 28, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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
        self.enterRule(localctx, 30, self.RULE_attributeList)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.attri()
                self.state = 172
                self.match(BKOOLParser.COMMA)
                self.state = 173
                self.attributeList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
        self.enterRule(localctx, 32, self.RULE_attri)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(BKOOLParser.ID)
                self.state = 179
                self.match(BKOOLParser.ASG)
                self.state = 180
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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
        self.enterRule(localctx, 34, self.RULE_methodDeclare)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.methodType()
                self.state = 185
                self.returnType()
                self.state = 186
                self.match(BKOOLParser.ID)
                self.state = 187
                self.paramList()
                self.state = 188
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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

        def paramDeclare(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclareContext,0)


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
        self.enterRule(localctx, 36, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(BKOOLParser.ID)
            self.state = 194
            self.paramDeclare()
            self.state = 195
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
        self.enterRule(localctx, 38, self.RULE_methodType)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.ID, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
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
        self.enterRule(localctx, 40, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 42, self.RULE_stmBlock)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(BKOOLParser.LP)
                self.state = 204
                self.stmList()
                self.state = 205
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(BKOOLParser.LP)
                self.state = 208
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
        self.enterRule(localctx, 44, self.RULE_paramList)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(BKOOLParser.LB)
                self.state = 212
                self.paramDeclare()
                self.state = 213
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(BKOOLParser.LB)
                self.state = 216
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
        self.enterRule(localctx, 46, self.RULE_paramDeclare)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.param()
                self.state = 220
                self.match(BKOOLParser.SEMI)
                self.state = 221
                self.paramDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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
        self.enterRule(localctx, 48, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.vartype()
            self.state = 227
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
        self.enterRule(localctx, 50, self.RULE_idList)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(BKOOLParser.ID)
                self.state = 230
                self.match(BKOOLParser.COMMA)
                self.state = 231
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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
        self.enterRule(localctx, 52, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.primtype()
            self.state = 236
            self.match(BKOOLParser.T__0)
            self.state = 237
            self.size()
            self.state = 238
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
        self.enterRule(localctx, 54, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BKOOLParser.LP)
            self.state = 241
            self.elemList()
            self.state = 242
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
        self.enterRule(localctx, 56, self.RULE_elemList)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.elem()
                self.state = 245
                self.match(BKOOLParser.COMMA)
                self.state = 246
                self.elemList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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
        self.enterRule(localctx, 58, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT))) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        self.enterRule(localctx, 62, self.RULE_explist)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(BKOOLParser.LB)
                self.state = 256
                self.exps()
                self.state = 257
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(BKOOLParser.LB)
                self.state = 260
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
        self.enterRule(localctx, 64, self.RULE_exps)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.exp()
                self.state = 264
                self.match(BKOOLParser.COMMA)
                self.state = 265
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        self.enterRule(localctx, 66, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.exp1()
                self.state = 271
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.exp1()
                self.state = 275
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 276
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
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
        self.enterRule(localctx, 68, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.exp2()
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.exp2()
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.exp2()
                self.state = 290
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.exp2()
                self.state = 294
                self.match(BKOOLParser.CON)
                self.state = 295
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
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

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp2)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(BKOOLParser.NOT)
                self.state = 301
                self.exp3()
                pass
            elif token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(BKOOLParser.ADD)
                pass
            elif token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(BKOOLParser.SUB)
                self.state = 304
                self.exp3()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 305
                self.exp3()
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


        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKOOLParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp3)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.exp4()
                self.state = 309
                self.match(BKOOLParser.T__0)
                self.state = 310
                self.exps()
                self.state = 311
                self.match(BKOOLParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKOOLParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp4)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.exp5()
                self.state = 317
                self.match(BKOOLParser.DOT)
                self.state = 318
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(BKOOLParser.ID)
                self.state = 321
                self.match(BKOOLParser.DOT)
                self.state = 322
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.exp5()
                self.state = 324
                self.match(BKOOLParser.DOT)
                self.state = 325
                self.match(BKOOLParser.ID)
                self.state = 326
                self.explist()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.match(BKOOLParser.ID)
                self.state = 329
                self.match(BKOOLParser.DOT)
                self.state = 330
                self.match(BKOOLParser.ID)
                self.state = 331
                self.explist()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
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
        self.enterRule(localctx, 76, self.RULE_exp5)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(BKOOLParser.NEW)
                self.state = 336
                self.match(BKOOLParser.ID)
                self.state = 337
                self.explist()
                pass
            elif token in [BKOOLParser.T__2, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.SELF, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_operand)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                self.arrayLit()
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 346
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 7)
                self.state = 347
                self.match(BKOOLParser.T__2)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 348
                self.match(BKOOLParser.ID)
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
        self.enterRule(localctx, 80, self.RULE_stmList)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.variables()
                self.state = 352
                self.stms()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.stms()
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
        self.enterRule(localctx, 82, self.RULE_variables)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.variable()
                self.state = 358
                self.match(BKOOLParser.SEMI)
                self.state = 359
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.variable()
                self.state = 362
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
        self.enterRule(localctx, 84, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID, BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.MUTABLE:
                    self.state = 366
                    self.match(BKOOLParser.MUTABLE)


                self.state = 369
                self.vartype()
                self.state = 370
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


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

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
        self.enterRule(localctx, 86, self.RULE_stms)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.stm()
                self.state = 376
                self.match(BKOOLParser.SEMI)
                self.state = 377
                self.stms()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.stm()
                self.state = 380
                self.match(BKOOLParser.SEMI)
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


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = BKOOLParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.lhs()
                self.state = 385
                self.match(BKOOLParser.T__3)
                self.state = 386
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(BKOOLParser.IF)
                self.state = 389
                self.exp()
                self.state = 390
                self.match(BKOOLParser.THEN)
                self.state = 391
                self.stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.match(BKOOLParser.IF)
                self.state = 394
                self.exp()
                self.state = 395
                self.match(BKOOLParser.THEN)
                self.state = 396
                self.stm()
                self.state = 397
                self.match(BKOOLParser.SEMI)
                self.state = 398
                self.match(BKOOLParser.ELSE)
                self.state = 399
                self.stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 401
                self.match(BKOOLParser.FOR)
                self.state = 402
                self.scala_var()
                self.state = 403
                self.match(BKOOLParser.T__3)
                self.state = 404
                self.exp1()
                self.state = 405
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 406
                self.exp2()
                self.state = 407
                self.match(BKOOLParser.DO)
                self.state = 412
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 408
                    self.stmBlock()
                    pass

                elif la_ == 2:
                    self.state = 409
                    self.stm()
                    self.state = 410
                    self.match(BKOOLParser.SEMI)
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 414
                self.match(BKOOLParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 415
                self.match(BKOOLParser.CONT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 416
                self.match(BKOOLParser.RETURN)
                self.state = 417
                self.exp()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 418
                self.match(BKOOLParser.ID)
                self.state = 419
                self.match(BKOOLParser.DOT)
                self.state = 420
                self.match(BKOOLParser.ID)
                self.state = 421
                self.explist()
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
        self.enterRule(localctx, 90, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

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
        self.enterRule(localctx, 92, self.RULE_lhs)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(BKOOLParser.ID)
                self.state = 428
                self.match(BKOOLParser.DOT)
                self.state = 429
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                self.exp()
                self.state = 431
                self.match(BKOOLParser.DOT)
                self.state = 432
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 434
                self.exp()
                self.state = 435
                self.match(BKOOLParser.T__0)
                self.state = 436
                self.exp()
                self.state = 437
                self.match(BKOOLParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





