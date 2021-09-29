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
        buf.write("\u01a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\5\3a\n\3\3\4\3\4\3\4\3\4\3\4\5\4h\n\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3\6\3\6")
        buf.write("\5\6w\n\6\3\7\3\7\5\7{\n\7\3\b\3\b\5\b\177\n\b\3\b\3\b")
        buf.write("\5\b\u0083\n\b\3\b\3\b\5\b\u0087\n\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\5\t\u0090\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u009a\n\f\3\r\3\r\3\r\3\r\5\r\u00a0\n\r\3\16")
        buf.write("\3\16\5\16\u00a4\n\16\3\16\3\16\5\16\u00a8\n\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b4")
        buf.write("\n\17\3\20\3\20\3\20\3\20\5\20\u00ba\n\20\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\5\22\u00c3\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00cb\n\23\3\24\3\24\5\24\u00cf\n")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00dd\n\26\3\27\3\27\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u00e9\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u00f0\n\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u00fb\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u010e\n\34\3\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u0115\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\7\36\u011f\n\36\f\36\16\36\u0122\13\36\3\37\3\37\3\37")
        buf.write("\5\37\u0127\n\37\3 \3 \3 \3 \5 \u012d\n \3!\3!\3!\3!\3")
        buf.write("!\5!\u0134\n!\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u013d\n#\3#")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\5$\u014a\n$\3%\3%\5%\u014e")
        buf.write("\n%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u015b\n&\3\'\3")
        buf.write("\'\5\'\u015f\n\'\3\'\3\'\5\'\u0163\n\'\3(\3(\3(\5(\u0168")
        buf.write("\n(\3)\3)\5)\u016c\n)\3)\3)\3)\3)\3*\3*\3*\5*\u0175\n")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0184\n+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5")
        buf.write("+\u0198\n+\3,\3,\3-\3-\3-\3-\3-\3-\3-\5-\u01a3\n-\3-\2")
        buf.write("\3:.\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVX\2\13\3\2\f\20\3\28<\3\2-\60")
        buf.write("\3\2+,\3\2\61\62\3\2%&\3\2\'*\3\2\25\26\3\2\30\31\2\u01b1")
        buf.write("\2Z\3\2\2\2\4]\3\2\2\2\6b\3\2\2\2\bq\3\2\2\2\ns\3\2\2")
        buf.write("\2\fz\3\2\2\2\16\u0086\3\2\2\2\20\u008f\3\2\2\2\22\u0091")
        buf.write("\3\2\2\2\24\u0093\3\2\2\2\26\u0095\3\2\2\2\30\u009b\3")
        buf.write("\2\2\2\32\u00a7\3\2\2\2\34\u00b3\3\2\2\2\36\u00b5\3\2")
        buf.write("\2\2 \u00bb\3\2\2\2\"\u00be\3\2\2\2$\u00ca\3\2\2\2&\u00ce")
        buf.write("\3\2\2\2(\u00d4\3\2\2\2*\u00d8\3\2\2\2,\u00de\3\2\2\2")
        buf.write(".\u00e0\3\2\2\2\60\u00e8\3\2\2\2\62\u00ef\3\2\2\2\64\u00fa")
        buf.write("\3\2\2\2\66\u010d\3\2\2\28\u0114\3\2\2\2:\u0116\3\2\2")
        buf.write("\2<\u0126\3\2\2\2>\u012c\3\2\2\2@\u0133\3\2\2\2B\u0135")
        buf.write("\3\2\2\2D\u013c\3\2\2\2F\u0149\3\2\2\2H\u014d\3\2\2\2")
        buf.write("J\u015a\3\2\2\2L\u015e\3\2\2\2N\u0164\3\2\2\2P\u016b\3")
        buf.write("\2\2\2R\u0171\3\2\2\2T\u0197\3\2\2\2V\u0199\3\2\2\2X\u01a2")
        buf.write("\3\2\2\2Z[\5\4\3\2[\\\7\2\2\3\\\3\3\2\2\2]`\5\6\4\2^a")
        buf.write("\5\4\3\2_a\3\2\2\2`^\3\2\2\2`_\3\2\2\2a\5\3\2\2\2bc\7")
        buf.write("\5\2\2cg\7<\2\2de\7\6\2\2eh\7<\2\2fh\3\2\2\2gd\3\2\2\2")
        buf.write("gf\3\2\2\2hi\3\2\2\2ij\5\b\5\2j\7\3\2\2\2kl\7\35\2\2l")
        buf.write("m\5\n\6\2mn\7\36\2\2nr\3\2\2\2op\7\35\2\2pr\7\36\2\2q")
        buf.write("k\3\2\2\2qo\3\2\2\2r\t\3\2\2\2sv\5\f\7\2tw\5\n\6\2uw\3")
        buf.write("\2\2\2vt\3\2\2\2vu\3\2\2\2w\13\3\2\2\2x{\5\16\b\2y{\5")
        buf.write("\32\16\2zx\3\2\2\2zy\3\2\2\2{\r\3\2\2\2|\177\7\n\2\2}")
        buf.write("\177\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080")
        buf.write("\u0083\7\13\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2")
        buf.write("\2\u0082\u0081\3\2\2\2\u0083\u0087\3\2\2\2\u0084\u0085")
        buf.write("\7\13\2\2\u0085\u0087\7\n\2\2\u0086~\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\5\20\t\2\u0089")
        buf.write("\u008a\5\26\f\2\u008a\u008b\7\37\2\2\u008b\17\3\2\2\2")
        buf.write("\u008c\u0090\5\22\n\2\u008d\u0090\5&\24\2\u008e\u0090")
        buf.write("\5\24\13\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\21\3\2\2\2\u0091\u0092\t\2\2\2\u0092")
        buf.write("\23\3\2\2\2\u0093\u0094\7<\2\2\u0094\25\3\2\2\2\u0095")
        buf.write("\u0099\5\30\r\2\u0096\u0097\7!\2\2\u0097\u009a\5\26\f")
        buf.write("\2\u0098\u009a\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0098")
        buf.write("\3\2\2\2\u009a\27\3\2\2\2\u009b\u009f\7<\2\2\u009c\u009d")
        buf.write("\7$\2\2\u009d\u00a0\5\64\33\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u009c\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\31\3\2\2\2\u00a1")
        buf.write("\u00a4\7\n\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a8\5")
        buf.write("\20\t\2\u00a6\u00a8\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\7<\2\2")
        buf.write("\u00aa\u00ab\5\34\17\2\u00ab\u00ac\5$\23\2\u00ac\33\3")
        buf.write("\2\2\2\u00ad\u00ae\7\33\2\2\u00ae\u00af\5\36\20\2\u00af")
        buf.write("\u00b0\7\34\2\2\u00b0\u00b4\3\2\2\2\u00b1\u00b2\7\33\2")
        buf.write("\2\u00b2\u00b4\7\34\2\2\u00b3\u00ad\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\35\3\2\2\2\u00b5\u00b9\5 \21\2\u00b6\u00b7")
        buf.write("\7\37\2\2\u00b7\u00ba\5\36\20\2\u00b8\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b6\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\37\3\2\2\2\u00bb")
        buf.write("\u00bc\5\20\t\2\u00bc\u00bd\5\"\22\2\u00bd!\3\2\2\2\u00be")
        buf.write("\u00c2\7<\2\2\u00bf\u00c0\7!\2\2\u00c0\u00c3\5\"\22\2")
        buf.write("\u00c1\u00c3\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c1\3")
        buf.write("\2\2\2\u00c3#\3\2\2\2\u00c4\u00c5\7\35\2\2\u00c5\u00c6")
        buf.write("\5L\'\2\u00c6\u00c7\7\36\2\2\u00c7\u00cb\3\2\2\2\u00c8")
        buf.write("\u00c9\7\35\2\2\u00c9\u00cb\7\36\2\2\u00ca\u00c4\3\2\2")
        buf.write("\2\u00ca\u00c8\3\2\2\2\u00cb%\3\2\2\2\u00cc\u00cf\5\22")
        buf.write("\n\2\u00cd\u00cf\5\24\13\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\7\3\2\2\u00d1")
        buf.write("\u00d2\5.\30\2\u00d2\u00d3\7\4\2\2\u00d3\'\3\2\2\2\u00d4")
        buf.write("\u00d5\7\35\2\2\u00d5\u00d6\5*\26\2\u00d6\u00d7\7\36\2")
        buf.write("\2\u00d7)\3\2\2\2\u00d8\u00dc\5,\27\2\u00d9\u00da\7!\2")
        buf.write("\2\u00da\u00dd\5*\26\2\u00db\u00dd\3\2\2\2\u00dc\u00d9")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd+\3\2\2\2\u00de\u00df")
        buf.write("\t\3\2\2\u00df-\3\2\2\2\u00e0\u00e1\7:\2\2\u00e1/\3\2")
        buf.write("\2\2\u00e2\u00e3\7\33\2\2\u00e3\u00e4\5\62\32\2\u00e4")
        buf.write("\u00e5\7\34\2\2\u00e5\u00e9\3\2\2\2\u00e6\u00e7\7\33\2")
        buf.write("\2\u00e7\u00e9\7\34\2\2\u00e8\u00e2\3\2\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e9\61\3\2\2\2\u00ea\u00eb\5\64\33\2\u00eb")
        buf.write("\u00ec\7!\2\2\u00ec\u00ed\5\62\32\2\u00ed\u00f0\3\2\2")
        buf.write("\2\u00ee\u00f0\5\64\33\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\63\3\2\2\2\u00f1\u00f2\5\66\34\2\u00f2")
        buf.write("\u00f3\t\4\2\2\u00f3\u00f4\5\66\34\2\u00f4\u00fb\3\2\2")
        buf.write("\2\u00f5\u00f6\5\66\34\2\u00f6\u00f7\t\5\2\2\u00f7\u00f8")
        buf.write("\5\66\34\2\u00f8\u00fb\3\2\2\2\u00f9\u00fb\5\66\34\2\u00fa")
        buf.write("\u00f1\3\2\2\2\u00fa\u00f5\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\65\3\2\2\2\u00fc\u00fd\58\35\2\u00fd\u00fe\t\6")
        buf.write("\2\2\u00fe\u00ff\5\66\34\2\u00ff\u010e\3\2\2\2\u0100\u0101")
        buf.write("\58\35\2\u0101\u0102\t\7\2\2\u0102\u0103\5\66\34\2\u0103")
        buf.write("\u010e\3\2\2\2\u0104\u0105\58\35\2\u0105\u0106\t\b\2\2")
        buf.write("\u0106\u0107\5\66\34\2\u0107\u010e\3\2\2\2\u0108\u0109")
        buf.write("\58\35\2\u0109\u010a\7\64\2\2\u010a\u010b\5\66\34\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010e\58\35\2\u010d\u00fc\3\2\2\2")
        buf.write("\u010d\u0100\3\2\2\2\u010d\u0104\3\2\2\2\u010d\u0108\3")
        buf.write("\2\2\2\u010d\u010c\3\2\2\2\u010e\67\3\2\2\2\u010f\u0110")
        buf.write("\7\63\2\2\u0110\u0115\58\35\2\u0111\u0112\t\7\2\2\u0112")
        buf.write("\u0115\58\35\2\u0113\u0115\5:\36\2\u0114\u010f\3\2\2\2")
        buf.write("\u0114\u0111\3\2\2\2\u0114\u0113\3\2\2\2\u01159\3\2\2")
        buf.write("\2\u0116\u0117\b\36\1\2\u0117\u0118\5<\37\2\u0118\u0120")
        buf.write("\3\2\2\2\u0119\u011a\f\4\2\2\u011a\u011b\7\3\2\2\u011b")
        buf.write("\u011c\5\64\33\2\u011c\u011d\7\4\2\2\u011d\u011f\3\2\2")
        buf.write("\2\u011e\u0119\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121;\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0123\u0127\5D#\2\u0124\u0127\5H%\2\u0125\u0127")
        buf.write("\5> \2\u0126\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127=\3\2\2\2\u0128\u0129\7\7\2\2\u0129\u012a")
        buf.write("\7<\2\2\u012a\u012d\5\60\31\2\u012b\u012d\5@!\2\u012c")
        buf.write("\u0128\3\2\2\2\u012c\u012b\3\2\2\2\u012d?\3\2\2\2\u012e")
        buf.write("\u0134\5(\25\2\u012f\u0134\5,\27\2\u0130\u0134\7\b\2\2")
        buf.write("\u0131\u0134\7\t\2\2\u0132\u0134\5B\"\2\u0133\u012e\3")
        buf.write("\2\2\2\u0133\u012f\3\2\2\2\u0133\u0130\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0132\3\2\2\2\u0134A\3\2\2\2\u0135\u0136")
        buf.write("\7\33\2\2\u0136\u0137\5\64\33\2\u0137\u0138\7\34\2\2\u0138")
        buf.write("C\3\2\2\2\u0139\u013d\5H%\2\u013a\u013d\5> \2\u013b\u013d")
        buf.write("\7<\2\2\u013c\u0139\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7\"\2\2")
        buf.write("\u013f\u0140\7<\2\2\u0140\u0141\5\60\31\2\u0141\u0142")
        buf.write("\5F$\2\u0142E\3\2\2\2\u0143\u0144\7\"\2\2\u0144\u0145")
        buf.write("\7<\2\2\u0145\u0146\5\60\31\2\u0146\u0147\5F$\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u0143\3\2\2\2")
        buf.write("\u0149\u0148\3\2\2\2\u014aG\3\2\2\2\u014b\u014e\5> \2")
        buf.write("\u014c\u014e\7<\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\5F$\2\u0150\u0151")
        buf.write("\7\"\2\2\u0151\u0152\7<\2\2\u0152\u0153\5J&\2\u0153I\3")
        buf.write("\2\2\2\u0154\u0155\5F$\2\u0155\u0156\7\"\2\2\u0156\u0157")
        buf.write("\7<\2\2\u0157\u0158\5J&\2\u0158\u015b\3\2\2\2\u0159\u015b")
        buf.write("\3\2\2\2\u015a\u0154\3\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("K\3\2\2\2\u015c\u015f\5N(\2\u015d\u015f\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2")
        buf.write("\u0160\u0163\5R*\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2")
        buf.write("\2\2\u0162\u0161\3\2\2\2\u0163M\3\2\2\2\u0164\u0167\5")
        buf.write("P)\2\u0165\u0168\5N(\2\u0166\u0168\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168O\3\2\2\2\u0169\u016c")
        buf.write("\7\13\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\5\20\t")
        buf.write("\2\u016e\u016f\5\26\f\2\u016f\u0170\7\37\2\2\u0170Q\3")
        buf.write("\2\2\2\u0171\u0174\5T+\2\u0172\u0175\5R*\2\u0173\u0175")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("S\3\2\2\2\u0176\u0198\5$\23\2\u0177\u0178\5X-\2\u0178")
        buf.write("\u0179\7#\2\2\u0179\u017a\5\64\33\2\u017a\u017b\7\37\2")
        buf.write("\2\u017b\u0198\3\2\2\2\u017c\u017d\7\21\2\2\u017d\u017e")
        buf.write("\5\64\33\2\u017e\u017f\7\23\2\2\u017f\u0183\5T+\2\u0180")
        buf.write("\u0181\7\22\2\2\u0181\u0184\5T+\2\u0182\u0184\3\2\2\2")
        buf.write("\u0183\u0180\3\2\2\2\u0183\u0182\3\2\2\2\u0184\u0198\3")
        buf.write("\2\2\2\u0185\u0186\7\24\2\2\u0186\u0187\5V,\2\u0187\u0188")
        buf.write("\7#\2\2\u0188\u0189\5\64\33\2\u0189\u018a\t\t\2\2\u018a")
        buf.write("\u018b\5\64\33\2\u018b\u018c\7\27\2\2\u018c\u018d\5T+")
        buf.write("\2\u018d\u0198\3\2\2\2\u018e\u018f\t\n\2\2\u018f\u0198")
        buf.write("\7\37\2\2\u0190\u0191\7\32\2\2\u0191\u0192\5\64\33\2\u0192")
        buf.write("\u0193\7\37\2\2\u0193\u0198\3\2\2\2\u0194\u0195\5D#\2")
        buf.write("\u0195\u0196\7\37\2\2\u0196\u0198\3\2\2\2\u0197\u0176")
        buf.write("\3\2\2\2\u0197\u0177\3\2\2\2\u0197\u017c\3\2\2\2\u0197")
        buf.write("\u0185\3\2\2\2\u0197\u018e\3\2\2\2\u0197\u0190\3\2\2\2")
        buf.write("\u0197\u0194\3\2\2\2\u0198U\3\2\2\2\u0199\u019a\7<\2\2")
        buf.write("\u019aW\3\2\2\2\u019b\u01a3\7<\2\2\u019c\u01a3\5H%\2\u019d")
        buf.write("\u019e\5<\37\2\u019e\u019f\7\3\2\2\u019f\u01a0\5\64\33")
        buf.write("\2\u01a0\u01a1\7\4\2\2\u01a1\u01a3\3\2\2\2\u01a2\u019b")
        buf.write("\3\2\2\2\u01a2\u019c\3\2\2\2\u01a2\u019d\3\2\2\2\u01a3")
        buf.write("Y\3\2\2\2*`gqvz~\u0082\u0086\u008f\u0099\u009f\u00a3\u00a7")
        buf.write("\u00b3\u00b9\u00c2\u00ca\u00ce\u00dc\u00e8\u00ef\u00fa")
        buf.write("\u010d\u0114\u0120\u0126\u012c\u0133\u013c\u0149\u014d")
        buf.write("\u015a\u015e\u0162\u0167\u016b\u0174\u0183\u0197\u01a2")
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
                      "NEW", "SELF", "NIL", "STATIC", "MUTABLE", "INTTYPE", 
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
    RULE_methodDeclare = 12
    RULE_paramList = 13
    RULE_paramDeclare = 14
    RULE_param = 15
    RULE_idList = 16
    RULE_stmBlock = 17
    RULE_arraytype = 18
    RULE_arrayLit = 19
    RULE_elemList = 20
    RULE_elem = 21
    RULE_size = 22
    RULE_explist = 23
    RULE_exps = 24
    RULE_exp = 25
    RULE_exp1 = 26
    RULE_exp2 = 27
    RULE_exp3 = 28
    RULE_exp4 = 29
    RULE_exp5 = 30
    RULE_operand = 31
    RULE_subexp = 32
    RULE_methodInvoke = 33
    RULE_methodRecur = 34
    RULE_attriAccess = 35
    RULE_attriRecur = 36
    RULE_stmList = 37
    RULE_variables = 38
    RULE_variable = 39
    RULE_stms = 40
    RULE_stm = 41
    RULE_scala_var = 42
    RULE_lhs = 43

    ruleNames =  [ "program", "classdcls", "classdcl", "memBlock", "memList", 
                   "classMember", "attributeDeclare", "vartype", "primtype", 
                   "classtype", "attributeList", "attri", "methodDeclare", 
                   "paramList", "paramDeclare", "param", "idList", "stmBlock", 
                   "arraytype", "arrayLit", "elemList", "elem", "size", 
                   "explist", "exps", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "operand", "subexp", "methodInvoke", "methodRecur", 
                   "attriAccess", "attriRecur", "stmList", "variables", 
                   "variable", "stms", "stm", "scala_var", "lhs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    CLASS=3
    EXTEND=4
    NEW=5
    SELF=6
    NIL=7
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
            self.state = 88
            self.classdcls()
            self.state = 89
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
            self.state = 91
            self.classdcl()
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CLASS]:
                self.state = 92
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
            self.state = 96
            self.match(BKOOLParser.CLASS)
            self.state = 97
            self.match(BKOOLParser.ID)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTEND]:
                self.state = 98
                self.match(BKOOLParser.EXTEND)
                self.state = 99
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 103
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(BKOOLParser.LP)
                self.state = 106
                self.memList()
                self.state = 107
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(BKOOLParser.LP)
                self.state = 110
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
            self.state = 113
            self.classMember()
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC, BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.state = 114
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
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

        def MUTABLE(self):
            return self.getToken(BKOOLParser.MUTABLE, 0)

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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 124
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 122
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.MUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.MUTABLE]:
                    self.state = 126
                    self.match(BKOOLParser.MUTABLE)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 130
                self.match(BKOOLParser.MUTABLE)
                self.state = 131
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 134
            self.vartype()
            self.state = 135
            self.attributeList()
            self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
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
            self.state = 143
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
            self.state = 145
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
            self.state = 147
            self.attri()
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 148
                self.match(BKOOLParser.COMMA)
                self.state = 149
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
            self.state = 153
            self.match(BKOOLParser.ID)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ASG]:
                self.state = 154
                self.match(BKOOLParser.ASG)
                self.state = 155
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
        self.enterRule(localctx, 24, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 159
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 163
                self.vartype()
                pass

            elif la_ == 2:
                pass


            self.state = 167
            self.match(BKOOLParser.ID)
            self.state = 168
            self.paramList()
            self.state = 169
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
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(BKOOLParser.LB)
                self.state = 172
                self.paramDeclare()
                self.state = 173
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(BKOOLParser.LB)
                self.state = 176
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
        self.enterRule(localctx, 28, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.param()
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.state = 180
                self.match(BKOOLParser.SEMI)
                self.state = 181
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
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.vartype()
            self.state = 186
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
        self.enterRule(localctx, 32, self.RULE_idList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(BKOOLParser.ID)
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 189
                self.match(BKOOLParser.COMMA)
                self.state = 190
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
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(BKOOLParser.LP)
                self.state = 195
                self.stmList()
                self.state = 196
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(BKOOLParser.LP)
                self.state = 199
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
                self.state = 202
                self.primtype()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 203
                self.classtype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 206
            self.match(BKOOLParser.T__0)
            self.state = 207
            self.size()
            self.state = 208
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
        self.enterRule(localctx, 38, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(BKOOLParser.LP)
            self.state = 211
            self.elemList()
            self.state = 212
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
        self.enterRule(localctx, 40, self.RULE_elemList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.elem()
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 215
                self.match(BKOOLParser.COMMA)
                self.state = 216
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = BKOOLParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.ID))) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_size)
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
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
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
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
        self.enterRule(localctx, 50, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
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
                self.state = 244
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
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
        self.enterRule(localctx, 52, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.exp2()
                self.state = 251
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 252
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.exp2()
                self.state = 255
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.exp2()
                self.state = 259
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.exp2()
                self.state = 263
                self.match(BKOOLParser.CON)
                self.state = 264
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
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
        self.enterRule(localctx, 54, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(BKOOLParser.NOT)
                self.state = 270
                self.exp2()
                pass
            elif token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 272
                self.exp2()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
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
                    self.match(BKOOLParser.T__0)
                    self.state = 281
                    self.exp()
                    self.state = 282
                    self.match(BKOOLParser.T__1) 
                self.state = 288
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
        self.enterRule(localctx, 58, self.RULE_exp4)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
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
        self.enterRule(localctx, 60, self.RULE_exp5)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(BKOOLParser.NEW)
                self.state = 295
                self.match(BKOOLParser.ID)
                self.state = 296
                self.explist()
                pass
            elif token in [BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
        self.enterRule(localctx, 62, self.RULE_operand)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.arrayLit()
                pass
            elif token in [BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.elem()
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 303
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 304
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
        self.enterRule(localctx, 64, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(BKOOLParser.LB)
            self.state = 308
            self.exp()
            self.state = 309
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
        self.enterRule(localctx, 66, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 311
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 312
                self.exp5()
                pass

            elif la_ == 3:
                self.state = 313
                self.match(BKOOLParser.ID)
                pass


            self.state = 316
            self.match(BKOOLParser.DOT)
            self.state = 317
            self.match(BKOOLParser.ID)
            self.state = 318
            self.explist()
            self.state = 319
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
        self.enterRule(localctx, 68, self.RULE_methodRecur)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(BKOOLParser.DOT)
                self.state = 322
                self.match(BKOOLParser.ID)
                self.state = 323
                self.explist()
                self.state = 324
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
        self.enterRule(localctx, 70, self.RULE_attriAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 329
                self.exp5()
                pass

            elif la_ == 2:
                self.state = 330
                self.match(BKOOLParser.ID)
                pass


            self.state = 333
            self.methodRecur()
            self.state = 334
            self.match(BKOOLParser.DOT)
            self.state = 335
            self.match(BKOOLParser.ID)
            self.state = 336
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
        self.enterRule(localctx, 72, self.RULE_attriRecur)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.methodRecur()
                self.state = 339
                self.match(BKOOLParser.DOT)
                self.state = 340
                self.match(BKOOLParser.ID)
                self.state = 341
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
        self.enterRule(localctx, 74, self.RULE_stmList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 346
                self.variables()
                pass

            elif la_ == 2:
                pass


            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 350
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
        self.enterRule(localctx, 76, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.variable()
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 355
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
        self.enterRule(localctx, 78, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MUTABLE]:
                self.state = 359
                self.match(BKOOLParser.MUTABLE)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 363
            self.vartype()
            self.state = 364
            self.attributeList()
            self.state = 365
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
        self.enterRule(localctx, 80, self.RULE_stms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.stm()
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 368
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
        self.enterRule(localctx, 82, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.lhs()
                self.state = 374
                self.match(BKOOLParser.ASGOP)
                self.state = 375
                self.exp()
                self.state = 376
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(BKOOLParser.IF)
                self.state = 379
                self.exp()
                self.state = 380
                self.match(BKOOLParser.THEN)
                self.state = 381
                self.stm()
                self.state = 385
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 382
                    self.match(BKOOLParser.ELSE)
                    self.state = 383
                    self.stm()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(BKOOLParser.FOR)
                self.state = 388
                self.scala_var()
                self.state = 389
                self.match(BKOOLParser.ASGOP)
                self.state = 390
                self.exp()
                self.state = 391
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 392
                self.exp()
                self.state = 393
                self.match(BKOOLParser.DO)
                self.state = 394
                self.stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.BREAK or _la==BKOOLParser.CONT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 397
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
                self.match(BKOOLParser.RETURN)
                self.state = 399
                self.exp()
                self.state = 400
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 402
                self.methodInvoke()
                self.state = 403
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
        self.enterRule(localctx, 84, self.RULE_scala_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 86, self.RULE_lhs)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.exp4()
                self.state = 412
                self.match(BKOOLParser.T__0)
                self.state = 413
                self.exp()
                self.state = 414
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
        self._predicates[28] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




