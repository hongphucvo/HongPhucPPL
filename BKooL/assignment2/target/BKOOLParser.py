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
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\5\3m\n\3\3\4\3\4\3\4\3\4\3\4\5\4t\n\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5~\n\5\3\6\3\6\3\6\5")
        buf.write("\6\u0083\n\6\3\7\3\7\5\7\u0087\n\7\3\b\3\b\5\b\u008b\n")
        buf.write("\b\3\b\3\b\5\b\u008f\n\b\3\b\3\b\5\b\u0093\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\5\t\u009c\n\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00a6\n\f\3\r\3\r\3\r\3\r\5\r\u00ac")
        buf.write("\n\r\3\16\3\16\3\16\3\16\5\16\u00b2\n\16\3\17\3\17\5\17")
        buf.write("\u00b6\n\17\3\17\3\17\5\17\u00ba\n\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c6\n\20\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00cc\n\21\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00d7\n\23\3\24\3\24\5\24")
        buf.write("\u00db\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\5\27\u00eb\n\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00f5\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u00fc\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0103\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u010a")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0112\n\35\f")
        buf.write("\35\16\35\u0115\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u011d\n\36\f\36\16\36\u0120\13\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u0128\n\37\f\37\16\37\u012b\13\37\3")
        buf.write(" \3 \3 \3 \3 \3 \7 \u0133\n \f \16 \u0136\13 \3!\3!\3")
        buf.write("!\5!\u013b\n!\3\"\3\"\3\"\5\"\u0140\n\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\7#\u014a\n#\f#\16#\u014d\13#\3$\3$\3$\5$\u0152")
        buf.write("\n$\3%\3%\3%\3%\5%\u0158\n%\3&\3&\3&\3&\3&\3&\5&\u0160")
        buf.write("\n&\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u0169\n(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\5)\u0176\n)\3*\3*\5*\u017a\n*\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3+\3+\3+\5+\u0187\n+\3,\3,\5,\u018b")
        buf.write("\n,\3,\3,\5,\u018f\n,\3-\3-\3-\5-\u0194\n-\3.\3.\5.\u0198")
        buf.write("\n.\3.\3.\3.\3.\3/\3/\3/\5/\u01a1\n/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01b0\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01c2\n\60")
        buf.write("\3\61\3\61\3\61\5\61\u01c7\n\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u01d8\n\63\3\63\2\78:<>D\64\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bd\2\13\3\2\f\20\3\28;\3\2-\60\3\2+,\3\2\61\62")
        buf.write("\3\2%&\3\2\'*\3\2\25\26\3\2\30\31\2\u01e3\2f\3\2\2\2\4")
        buf.write("i\3\2\2\2\6n\3\2\2\2\b}\3\2\2\2\n\177\3\2\2\2\f\u0086")
        buf.write("\3\2\2\2\16\u0092\3\2\2\2\20\u009b\3\2\2\2\22\u009d\3")
        buf.write("\2\2\2\24\u009f\3\2\2\2\26\u00a1\3\2\2\2\30\u00a7\3\2")
        buf.write("\2\2\32\u00ad\3\2\2\2\34\u00b9\3\2\2\2\36\u00c5\3\2\2")
        buf.write("\2 \u00c7\3\2\2\2\"\u00cd\3\2\2\2$\u00d6\3\2\2\2&\u00da")
        buf.write("\3\2\2\2(\u00e0\3\2\2\2*\u00e4\3\2\2\2,\u00e6\3\2\2\2")
        buf.write(".\u00ec\3\2\2\2\60\u00f4\3\2\2\2\62\u00fb\3\2\2\2\64\u0102")
        buf.write("\3\2\2\2\66\u0109\3\2\2\28\u010b\3\2\2\2:\u0116\3\2\2")
        buf.write("\2<\u0121\3\2\2\2>\u012c\3\2\2\2@\u013a\3\2\2\2B\u013f")
        buf.write("\3\2\2\2D\u0141\3\2\2\2F\u0151\3\2\2\2H\u0157\3\2\2\2")
        buf.write("J\u015f\3\2\2\2L\u0161\3\2\2\2N\u0168\3\2\2\2P\u0175\3")
        buf.write("\2\2\2R\u0179\3\2\2\2T\u0186\3\2\2\2V\u018a\3\2\2\2X\u0190")
        buf.write("\3\2\2\2Z\u0197\3\2\2\2\\\u019d\3\2\2\2^\u01c1\3\2\2\2")
        buf.write("`\u01c6\3\2\2\2b\u01ce\3\2\2\2d\u01d7\3\2\2\2fg\5\4\3")
        buf.write("\2gh\7\2\2\3h\3\3\2\2\2il\5\6\4\2jm\5\4\3\2km\3\2\2\2")
        buf.write("lj\3\2\2\2lk\3\2\2\2m\5\3\2\2\2no\7\5\2\2os\7<\2\2pq\7")
        buf.write("\6\2\2qt\7<\2\2rt\3\2\2\2sp\3\2\2\2sr\3\2\2\2tu\3\2\2")
        buf.write("\2uv\5\b\5\2v\7\3\2\2\2wx\7\35\2\2xy\5\n\6\2yz\7\36\2")
        buf.write("\2z~\3\2\2\2{|\7\35\2\2|~\7\36\2\2}w\3\2\2\2}{\3\2\2\2")
        buf.write("~\t\3\2\2\2\177\u0082\5\f\7\2\u0080\u0083\5\n\6\2\u0081")
        buf.write("\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2")
        buf.write("\u0083\13\3\2\2\2\u0084\u0087\5\16\b\2\u0085\u0087\5\34")
        buf.write("\17\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\r")
        buf.write("\3\2\2\2\u0088\u008b\7\n\2\2\u0089\u008b\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2")
        buf.write("\u008c\u008f\7\13\2\2\u008d\u008f\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008d\3\2\2\2\u008f\u0093\3\2\2\2\u0090")
        buf.write("\u0091\7\13\2\2\u0091\u0093\7\n\2\2\u0092\u008a\3\2\2")
        buf.write("\2\u0092\u0090\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\5\20\t\2\u0095\u0096\5\26\f\2\u0096\u0097\7\37\2\2\u0097")
        buf.write("\17\3\2\2\2\u0098\u009c\5\22\n\2\u0099\u009c\5&\24\2\u009a")
        buf.write("\u009c\5\24\13\2\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009c\21\3\2\2\2\u009d\u009e\t")
        buf.write("\2\2\2\u009e\23\3\2\2\2\u009f\u00a0\7<\2\2\u00a0\25\3")
        buf.write("\2\2\2\u00a1\u00a5\5\30\r\2\u00a2\u00a3\7!\2\2\u00a3\u00a6")
        buf.write("\5\26\f\2\u00a4\u00a6\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\27\3\2\2\2\u00a7\u00ab\7<\2\2\u00a8")
        buf.write("\u00a9\7$\2\2\u00a9\u00ac\5\64\33\2\u00aa\u00ac\3\2\2")
        buf.write("\2\u00ab\u00a8\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\31\3")
        buf.write("\2\2\2\u00ad\u00b1\7<\2\2\u00ae\u00af\7!\2\2\u00af\u00b2")
        buf.write("\5\32\16\2\u00b0\u00b2\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b2\33\3\2\2\2\u00b3\u00b6\7\n\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00ba\5\20\t\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\7<\2\2\u00bc\u00bd\5\36\20")
        buf.write("\2\u00bd\u00be\5$\23\2\u00be\35\3\2\2\2\u00bf\u00c0\7")
        buf.write("\33\2\2\u00c0\u00c1\5 \21\2\u00c1\u00c2\7\34\2\2\u00c2")
        buf.write("\u00c6\3\2\2\2\u00c3\u00c4\7\33\2\2\u00c4\u00c6\7\34\2")
        buf.write("\2\u00c5\u00bf\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\37\3")
        buf.write("\2\2\2\u00c7\u00cb\5\"\22\2\u00c8\u00c9\7\37\2\2\u00c9")
        buf.write("\u00cc\5 \21\2\u00ca\u00cc\3\2\2\2\u00cb\u00c8\3\2\2\2")
        buf.write("\u00cb\u00ca\3\2\2\2\u00cc!\3\2\2\2\u00cd\u00ce\5\20\t")
        buf.write("\2\u00ce\u00cf\5\32\16\2\u00cf#\3\2\2\2\u00d0\u00d1\7")
        buf.write("\35\2\2\u00d1\u00d2\5V,\2\u00d2\u00d3\7\36\2\2\u00d3\u00d7")
        buf.write("\3\2\2\2\u00d4\u00d5\7\35\2\2\u00d5\u00d7\7\36\2\2\u00d6")
        buf.write("\u00d0\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7%\3\2\2\2\u00d8")
        buf.write("\u00db\5\22\n\2\u00d9\u00db\5\24\13\2\u00da\u00d8\3\2")
        buf.write("\2\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd")
        buf.write("\7\3\2\2\u00dd\u00de\5*\26\2\u00de\u00df\7\4\2\2\u00df")
        buf.write("\'\3\2\2\2\u00e0\u00e1\7\35\2\2\u00e1\u00e2\5\62\32\2")
        buf.write("\u00e2\u00e3\7\36\2\2\u00e3)\3\2\2\2\u00e4\u00e5\7:\2")
        buf.write("\2\u00e5+\3\2\2\2\u00e6\u00ea\5.\30\2\u00e7\u00e8\7!\2")
        buf.write("\2\u00e8\u00eb\5,\27\2\u00e9\u00eb\3\2\2\2\u00ea\u00e7")
        buf.write("\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb-\3\2\2\2\u00ec\u00ed")
        buf.write("\t\3\2\2\u00ed/\3\2\2\2\u00ee\u00ef\7\33\2\2\u00ef\u00f0")
        buf.write("\5\62\32\2\u00f0\u00f1\7\34\2\2\u00f1\u00f5\3\2\2\2\u00f2")
        buf.write("\u00f3\7\33\2\2\u00f3\u00f5\7\34\2\2\u00f4\u00ee\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f5\61\3\2\2\2\u00f6\u00f7\5")
        buf.write("\64\33\2\u00f7\u00f8\7!\2\2\u00f8\u00f9\5\62\32\2\u00f9")
        buf.write("\u00fc\3\2\2\2\u00fa\u00fc\5\64\33\2\u00fb\u00f6\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc\63\3\2\2\2\u00fd\u00fe\5")
        buf.write("\66\34\2\u00fe\u00ff\t\4\2\2\u00ff\u0100\5\66\34\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u0103\5\66\34\2\u0102\u00fd\3\2\2")
        buf.write("\2\u0102\u0101\3\2\2\2\u0103\65\3\2\2\2\u0104\u0105\5")
        buf.write("8\35\2\u0105\u0106\t\5\2\2\u0106\u0107\58\35\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u010a\58\35\2\u0109\u0104\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\67\3\2\2\2\u010b\u010c\b\35\1\2\u010c")
        buf.write("\u010d\5:\36\2\u010d\u0113\3\2\2\2\u010e\u010f\f\4\2\2")
        buf.write("\u010f\u0110\t\6\2\2\u0110\u0112\5:\36\2\u0111\u010e\3")
        buf.write("\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u01149\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117")
        buf.write("\b\36\1\2\u0117\u0118\5<\37\2\u0118\u011e\3\2\2\2\u0119")
        buf.write("\u011a\f\4\2\2\u011a\u011b\t\7\2\2\u011b\u011d\5<\37\2")
        buf.write("\u011c\u0119\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011e\u011f\3\2\2\2\u011f;\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\u0122\b\37\1\2\u0122\u0123\5> \2\u0123")
        buf.write("\u0129\3\2\2\2\u0124\u0125\f\4\2\2\u0125\u0126\t\b\2\2")
        buf.write("\u0126\u0128\5> \2\u0127\u0124\3\2\2\2\u0128\u012b\3\2")
        buf.write("\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a=\3")
        buf.write("\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\b \1\2\u012d\u012e")
        buf.write("\5@!\2\u012e\u0134\3\2\2\2\u012f\u0130\f\4\2\2\u0130\u0131")
        buf.write("\7\64\2\2\u0131\u0133\5@!\2\u0132\u012f\3\2\2\2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135?\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\7\63\2")
        buf.write("\2\u0138\u013b\5@!\2\u0139\u013b\5B\"\2\u013a\u0137\3")
        buf.write("\2\2\2\u013a\u0139\3\2\2\2\u013bA\3\2\2\2\u013c\u013d")
        buf.write("\t\7\2\2\u013d\u0140\5D#\2\u013e\u0140\5D#\2\u013f\u013c")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140C\3\2\2\2\u0141\u0142")
        buf.write("\b#\1\2\u0142\u0143\5F$\2\u0143\u014b\3\2\2\2\u0144\u0145")
        buf.write("\f\4\2\2\u0145\u0146\7\3\2\2\u0146\u0147\5\64\33\2\u0147")
        buf.write("\u0148\7\4\2\2\u0148\u014a\3\2\2\2\u0149\u0144\3\2\2\2")
        buf.write("\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014cE\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0152")
        buf.write("\5N(\2\u014f\u0152\5R*\2\u0150\u0152\5H%\2\u0151\u014e")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("G\3\2\2\2\u0153\u0154\7\7\2\2\u0154\u0155\7<\2\2\u0155")
        buf.write("\u0158\5\60\31\2\u0156\u0158\5J&\2\u0157\u0153\3\2\2\2")
        buf.write("\u0157\u0156\3\2\2\2\u0158I\3\2\2\2\u0159\u0160\5(\25")
        buf.write("\2\u015a\u0160\5.\30\2\u015b\u0160\7<\2\2\u015c\u0160")
        buf.write("\7\b\2\2\u015d\u0160\7\t\2\2\u015e\u0160\5L\'\2\u015f")
        buf.write("\u0159\3\2\2\2\u015f\u015a\3\2\2\2\u015f\u015b\3\2\2\2")
        buf.write("\u015f\u015c\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3")
        buf.write("\2\2\2\u0160K\3\2\2\2\u0161\u0162\7\33\2\2\u0162\u0163")
        buf.write("\5\64\33\2\u0163\u0164\7\34\2\2\u0164M\3\2\2\2\u0165\u0169")
        buf.write("\5R*\2\u0166\u0169\5H%\2\u0167\u0169\7<\2\2\u0168\u0165")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u016b\7\"\2\2\u016b\u016c\7<\2\2")
        buf.write("\u016c\u016d\5\60\31\2\u016d\u016e\5P)\2\u016eO\3\2\2")
        buf.write("\2\u016f\u0170\7\"\2\2\u0170\u0171\7<\2\2\u0171\u0172")
        buf.write("\5\60\31\2\u0172\u0173\5P)\2\u0173\u0176\3\2\2\2\u0174")
        buf.write("\u0176\3\2\2\2\u0175\u016f\3\2\2\2\u0175\u0174\3\2\2\2")
        buf.write("\u0176Q\3\2\2\2\u0177\u017a\5H%\2\u0178\u017a\7<\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017c\5P)\2\u017c\u017d\7\"\2\2\u017d\u017e\7<")
        buf.write("\2\2\u017e\u017f\5T+\2\u017fS\3\2\2\2\u0180\u0181\5P)")
        buf.write("\2\u0181\u0182\7\"\2\2\u0182\u0183\7<\2\2\u0183\u0184")
        buf.write("\5T+\2\u0184\u0187\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0180")
        buf.write("\3\2\2\2\u0186\u0185\3\2\2\2\u0187U\3\2\2\2\u0188\u018b")
        buf.write("\5X-\2\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018f\5\\/\2\u018d")
        buf.write("\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2")
        buf.write("\u018fW\3\2\2\2\u0190\u0193\5Z.\2\u0191\u0194\5X-\2\u0192")
        buf.write("\u0194\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194Y\3\2\2\2\u0195\u0198\7\13\2\2\u0196\u0198\3\2\2")
        buf.write("\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019a\5\20\t\2\u019a\u019b\5\26\f\2\u019b")
        buf.write("\u019c\7\37\2\2\u019c[\3\2\2\2\u019d\u01a0\5^\60\2\u019e")
        buf.write("\u01a1\5\\/\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a0\u019f\3\2\2\2\u01a1]\3\2\2\2\u01a2\u01c2\5$\23")
        buf.write("\2\u01a3\u01a4\5d\63\2\u01a4\u01a5\7#\2\2\u01a5\u01a6")
        buf.write("\5\64\33\2\u01a6\u01a7\7\37\2\2\u01a7\u01c2\3\2\2\2\u01a8")
        buf.write("\u01a9\7\21\2\2\u01a9\u01aa\5\64\33\2\u01aa\u01ab\7\23")
        buf.write("\2\2\u01ab\u01af\5^\60\2\u01ac\u01ad\7\22\2\2\u01ad\u01b0")
        buf.write("\5^\60\2\u01ae\u01b0\3\2\2\2\u01af\u01ac\3\2\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0\u01c2\3\2\2\2\u01b1\u01b2\7\24\2")
        buf.write("\2\u01b2\u01b3\5b\62\2\u01b3\u01b4\7#\2\2\u01b4\u01b5")
        buf.write("\5\64\33\2\u01b5\u01b6\t\t\2\2\u01b6\u01b7\5\64\33\2\u01b7")
        buf.write("\u01b8\7\27\2\2\u01b8\u01b9\5^\60\2\u01b9\u01c2\3\2\2")
        buf.write("\2\u01ba\u01bb\t\n\2\2\u01bb\u01c2\7\37\2\2\u01bc\u01bd")
        buf.write("\7\32\2\2\u01bd\u01be\5\64\33\2\u01be\u01bf\7\37\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01c2\5`\61\2\u01c1\u01a2\3\2\2\2")
        buf.write("\u01c1\u01a3\3\2\2\2\u01c1\u01a8\3\2\2\2\u01c1\u01b1\3")
        buf.write("\2\2\2\u01c1\u01ba\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2_\3\2\2\2\u01c3\u01c7\5R*\2\u01c4\u01c7")
        buf.write("\5H%\2\u01c5\u01c7\7<\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\7\"\2\2\u01c9\u01ca\7<\2\2\u01ca\u01cb\5\60\31")
        buf.write("\2\u01cb\u01cc\5P)\2\u01cc\u01cd\7\37\2\2\u01cda\3\2\2")
        buf.write("\2\u01ce\u01cf\7<\2\2\u01cfc\3\2\2\2\u01d0\u01d8\7<\2")
        buf.write("\2\u01d1\u01d8\5R*\2\u01d2\u01d3\5F$\2\u01d3\u01d4\7\3")
        buf.write("\2\2\u01d4\u01d5\5\64\33\2\u01d5\u01d6\7\4\2\2\u01d6\u01d8")
        buf.write("\3\2\2\2\u01d7\u01d0\3\2\2\2\u01d7\u01d1\3\2\2\2\u01d7")
        buf.write("\u01d2\3\2\2\2\u01d8e\3\2\2\2\60ls}\u0082\u0086\u008a")
        buf.write("\u008e\u0092\u009b\u00a5\u00ab\u00b1\u00b5\u00b9\u00c5")
        buf.write("\u00cb\u00d6\u00da\u00ea\u00f4\u00fb\u0102\u0109\u0113")
        buf.write("\u011e\u0129\u0134\u013a\u013f\u014b\u0151\u0157\u015f")
        buf.write("\u0168\u0175\u0179\u0186\u018a\u018e\u0193\u0197\u01a0")
        buf.write("\u01af\u01c1\u01c6\u01d7")
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
    RULE_elemList = 21
    RULE_elem = 22
    RULE_explist = 23
    RULE_exps = 24
    RULE_exp = 25
    RULE_exp1 = 26
    RULE_exp2 = 27
    RULE_exp3 = 28
    RULE_exp4 = 29
    RULE_exp5 = 30
    RULE_exp6 = 31
    RULE_exp7 = 32
    RULE_exp8 = 33
    RULE_exp9 = 34
    RULE_exp10 = 35
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
    RULE_methodCall = 47
    RULE_scala_var = 48
    RULE_lhs = 49

    ruleNames =  [ "program", "classdcls", "classdcl", "memBlock", "memList", 
                   "classMember", "attributeDeclare", "vartype", "primtype", 
                   "classtype", "attributeList", "attri", "idList", "methodDeclare", 
                   "paramList", "paramDeclare", "param", "stmBlock", "arraytype", 
                   "arrayLit", "size", "elemList", "elem", "explist", "exps", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "operand", "subexp", 
                   "methodInvoke", "methodRecur", "attriAccess", "attriRecur", 
                   "stmList", "variables", "variable", "stms", "stm", "methodCall", 
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
            self.state = 100
            self.classdcls()
            self.state = 101
            self.match(BKOOLParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_classdcls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.classdcl()
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CLASS]:
                self.state = 104
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
        self.enterRule(localctx, 4, self.RULE_classdcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BKOOLParser.CLASS)
            self.state = 109
            self.match(BKOOLParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTEND]:
                self.state = 110
                self.match(BKOOLParser.EXTEND)
                self.state = 111
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 115
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
        self.enterRule(localctx, 6, self.RULE_memBlock)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(BKOOLParser.LP)
                self.state = 118
                self.memList()
                self.state = 119
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(BKOOLParser.LP)
                self.state = 122
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
        self.enterRule(localctx, 8, self.RULE_memList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.classMember()
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC, BKOOLParser.IMMUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.state = 126
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
        self.enterRule(localctx, 10, self.RULE_classMember)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDeclare" ):
                return visitor.visitAttributeDeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributeDeclare(self):

        localctx = BKOOLParser.AttributeDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 136
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 134
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.IMMUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 140
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.IMMUTABLE]:
                    self.state = 138
                    self.match(BKOOLParser.IMMUTABLE)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 142
                self.match(BKOOLParser.IMMUTABLE)
                self.state = 143
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 146
            self.vartype()
            self.state = 147
            self.attributeList()
            self.state = 148
            self.match(BKOOLParser.SEMI)
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
        self.enterRule(localctx, 14, self.RULE_vartype)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
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
        self.enterRule(localctx, 16, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 18, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
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
        self.enterRule(localctx, 20, self.RULE_attributeList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.attri()
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 160
                self.match(BKOOLParser.COMMA)
                self.state = 161
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
        self.enterRule(localctx, 22, self.RULE_attri)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BKOOLParser.ID)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ASG]:
                self.state = 166
                self.match(BKOOLParser.ASG)
                self.state = 167
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
        self.enterRule(localctx, 24, self.RULE_idList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(BKOOLParser.ID)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 172
                self.match(BKOOLParser.COMMA)
                self.state = 173
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


        def vartype(self):
            return self.getTypedRuleContext(BKOOLParser.VartypeContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclare" ):
                return visitor.visitMethodDeclare(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclare(self):

        localctx = BKOOLParser.MethodDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 177
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 181
                self.vartype()
                pass

            elif la_ == 2:
                pass


            self.state = 185
            self.match(BKOOLParser.ID)
            self.state = 186
            self.paramList()
            self.state = 187
            self.stmBlock()
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
        self.enterRule(localctx, 28, self.RULE_paramList)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(BKOOLParser.LB)
                self.state = 190
                self.paramDeclare()
                self.state = 191
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(BKOOLParser.LB)
                self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.param()
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.state = 198
                self.match(BKOOLParser.SEMI)
                self.state = 199
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
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.vartype()
            self.state = 204
            self.idList()
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
        self.enterRule(localctx, 34, self.RULE_stmBlock)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
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


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
                self.state = 214
                self.primtype()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 215
                self.classtype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 218
            self.match(BKOOLParser.T__0)
            self.state = 219
            self.size()
            self.state = 220
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

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


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
        self.enterRule(localctx, 38, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(BKOOLParser.LP)
            self.state = 223
            self.exps()
            self.state = 224
            self.match(BKOOLParser.RP)
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
        self.enterRule(localctx, 40, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BKOOLParser.INTLIT)
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
        self.enterRule(localctx, 42, self.RULE_elemList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.elem()
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(BKOOLParser.COMMA)
                self.state = 230
                self.elemList()
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
        self.enterRule(localctx, 44, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
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
        self.enterRule(localctx, 46, self.RULE_explist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(BKOOLParser.LB)
                self.state = 237
                self.exps()
                self.state = 238
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(BKOOLParser.LB)
                self.state = 241
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
        self.enterRule(localctx, 48, self.RULE_exps)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.exp()
                self.state = 245
                self.match(BKOOLParser.COMMA)
                self.state = 246
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.exp1()
                self.state = 252
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.exp2(0)
                self.state = 259
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 270
                    self.exp3(0) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 281
                    self.exp4(0) 
                self.state = 286
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 290
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 291
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 292
                    self.exp5(0) 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CON(self):
            return self.getToken(BKOOLParser.CON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 301
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302
                    self.match(BKOOLParser.CON)
                    self.state = 303
                    self.exp6() 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp6)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(BKOOLParser.NOT)
                self.state = 310
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self.exp8(0)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    self.match(BKOOLParser.T__0)
                    self.state = 324
                    self.exp()
                    self.state = 325
                    self.match(BKOOLParser.T__1) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = BKOOLParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp9)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
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
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp10)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BKOOLParser.NEW)
                self.state = 338
                self.match(BKOOLParser.ID)
                self.state = 339
                self.explist()
                pass
            elif token in [BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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

        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def elem(self):
            return self.getTypedRuleContext(BKOOLParser.ElemContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_operand)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.arrayLit()
                pass
            elif token in [BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.elem()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 347
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 348
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
            self.state = 351
            self.match(BKOOLParser.LB)
            self.state = 352
            self.exp()
            self.state = 353
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


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


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
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 355
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 356
                self.exp10()
                pass

            elif la_ == 3:
                self.state = 357
                self.match(BKOOLParser.ID)
                pass


            self.state = 360
            self.match(BKOOLParser.DOT)
            self.state = 361
            self.match(BKOOLParser.ID)
            self.state = 362
            self.explist()
            self.state = 363
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
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(BKOOLParser.DOT)
                self.state = 366
                self.match(BKOOLParser.ID)
                self.state = 367
                self.explist()
                self.state = 368
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


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 373
                self.exp10()
                pass

            elif la_ == 2:
                self.state = 374
                self.match(BKOOLParser.ID)
                pass


            self.state = 377
            self.methodRecur()
            self.state = 378
            self.match(BKOOLParser.DOT)
            self.state = 379
            self.match(BKOOLParser.ID)
            self.state = 380
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
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.methodRecur()
                self.state = 383
                self.match(BKOOLParser.DOT)
                self.state = 384
                self.match(BKOOLParser.ID)
                self.state = 385
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
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 390
                self.variables()
                pass

            elif la_ == 2:
                pass


            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 394
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
            self.state = 398
            self.variable()
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 399
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

        def IMMUTABLE(self):
            return self.getToken(BKOOLParser.IMMUTABLE, 0)

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
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IMMUTABLE]:
                self.state = 403
                self.match(BKOOLParser.IMMUTABLE)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 407
            self.vartype()
            self.state = 408
            self.attributeList()
            self.state = 409
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
            self.state = 411
            self.stm()
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 412
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

        def methodCall(self):
            return self.getTypedRuleContext(BKOOLParser.MethodCallContext,0)


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
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.lhs()
                self.state = 418
                self.match(BKOOLParser.ASGOP)
                self.state = 419
                self.exp()
                self.state = 420
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.match(BKOOLParser.IF)
                self.state = 423
                self.exp()
                self.state = 424
                self.match(BKOOLParser.THEN)
                self.state = 425
                self.stm()
                self.state = 429
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 426
                    self.match(BKOOLParser.ELSE)
                    self.state = 427
                    self.stm()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 431
                self.match(BKOOLParser.FOR)
                self.state = 432
                self.scala_var()
                self.state = 433
                self.match(BKOOLParser.ASGOP)
                self.state = 434
                self.exp()
                self.state = 435
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.exp()
                self.state = 437
                self.match(BKOOLParser.DO)
                self.state = 438
                self.stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 440
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.BREAK or _la==BKOOLParser.CONT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 441
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 442
                self.match(BKOOLParser.RETURN)
                self.state = 443
                self.exp()
                self.state = 444
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 446
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


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = BKOOLParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 449
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 450
                self.exp10()
                pass

            elif la_ == 3:
                self.state = 451
                self.match(BKOOLParser.ID)
                pass


            self.state = 454
            self.match(BKOOLParser.DOT)
            self.state = 455
            self.match(BKOOLParser.ID)
            self.state = 456
            self.explist()
            self.state = 457
            self.methodRecur()
            self.state = 458
            self.match(BKOOLParser.SEMI)
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
        self.enterRule(localctx, 96, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
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


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


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
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.exp9()
                self.state = 465
                self.match(BKOOLParser.T__0)
                self.state = 466
                self.exp()
                self.state = 467
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
        self._predicates[27] = self.exp2_sempred
        self._predicates[28] = self.exp3_sempred
        self._predicates[29] = self.exp4_sempred
        self._predicates[30] = self.exp5_sempred
        self._predicates[33] = self.exp8_sempred
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
         




