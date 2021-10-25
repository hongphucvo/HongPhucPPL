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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4t\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5|\n\5\3\6\3\6\3\6\3\6\5\6\u0082")
        buf.write("\n\6\3\7\3\7\5\7\u0086\n\7\3\b\3\b\5\b\u008a\n\b\3\b\3")
        buf.write("\b\5\b\u008e\n\b\3\b\3\b\5\b\u0092\n\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\5\t\u0099\n\t\3\t\5\t\u009c\n\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00af\n\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00ba\n\16\3\17\5\17\u00bd\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c8\n\20")
        buf.write("\3\21\3\21\3\21\5\21\u00cd\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00d6\n\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00dc\n\22\f\22\16\22\u00df\13\22\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00e5\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u00ef\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0100\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0111\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u011f\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0145\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u014c\n\37\3 \3 \3 \3 \3 \5 \u0153")
        buf.write("\n \3!\3!\3!\3!\3!\5!\u015a\n!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0162\n\"\f\"\16\"\u0165\13\"\3#\3#\3#\3#\3#\3#\7")
        buf.write("#\u016d\n#\f#\16#\u0170\13#\3$\3$\3$\3$\3$\3$\7$\u0178")
        buf.write("\n$\f$\16$\u017b\13$\3%\3%\3%\3%\3%\3%\7%\u0183\n%\f%")
        buf.write("\16%\u0186\13%\3&\3&\3&\5&\u018b\n&\3\'\3\'\3\'\5\'\u0190")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\5(\u0198\n(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u01ac\n)\f)\16)")
        buf.write("\u01af\13)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01bc\n")
        buf.write("*\3+\3+\3+\3+\3+\3+\5+\u01c4\n+\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\5-\u01cf\n-\3.\3.\3.\3.\5.\u01d5\n.\3/\3/\3/\3/\5")
        buf.write("/\u01db\n/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\2\b\"BD")
        buf.write("FHP\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\t\3\2%&\3\2\62\65")
        buf.write("\3\2\60\61\3\2./\3\2\'(\3\2),\3\2\36\37\2\u01f0\2b\3\2")
        buf.write("\2\2\4i\3\2\2\2\6s\3\2\2\2\b{\3\2\2\2\n\u0081\3\2\2\2")
        buf.write("\f\u0085\3\2\2\2\16\u0091\3\2\2\2\20\u0098\3\2\2\2\22")
        buf.write("\u00a7\3\2\2\2\24\u00ae\3\2\2\2\26\u00b0\3\2\2\2\30\u00b3")
        buf.write("\3\2\2\2\32\u00b9\3\2\2\2\34\u00bc\3\2\2\2\36\u00c7\3")
        buf.write("\2\2\2 \u00c9\3\2\2\2\"\u00d5\3\2\2\2$\u00e4\3\2\2\2&")
        buf.write("\u00ee\3\2\2\2(\u00ff\3\2\2\2*\u0101\3\2\2\2,\u0110\3")
        buf.write("\2\2\2.\u011e\3\2\2\2\60\u0120\3\2\2\2\62\u0125\3\2\2")
        buf.write("\2\64\u012b\3\2\2\2\66\u012e\3\2\2\28\u0131\3\2\2\2:\u0144")
        buf.write("\3\2\2\2<\u014b\3\2\2\2>\u0152\3\2\2\2@\u0159\3\2\2\2")
        buf.write("B\u015b\3\2\2\2D\u0166\3\2\2\2F\u0171\3\2\2\2H\u017c\3")
        buf.write("\2\2\2J\u018a\3\2\2\2L\u018f\3\2\2\2N\u0197\3\2\2\2P\u0199")
        buf.write("\3\2\2\2R\u01bb\3\2\2\2T\u01c3\3\2\2\2V\u01c5\3\2\2\2")
        buf.write("X\u01ce\3\2\2\2Z\u01d4\3\2\2\2\\\u01da\3\2\2\2^\u01dc")
        buf.write("\3\2\2\2`\u01e0\3\2\2\2bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2")
        buf.write("ej\5\6\4\2fg\5\6\4\2gh\5\4\3\2hj\3\2\2\2ie\3\2\2\2if\3")
        buf.write("\2\2\2j\5\3\2\2\2kl\7\21\2\2lm\7=\2\2mn\7\25\2\2no\7=")
        buf.write("\2\2ot\5\b\5\2pq\7\21\2\2qr\7=\2\2rt\5\b\5\2sk\3\2\2\2")
        buf.write("sp\3\2\2\2t\7\3\2\2\2uv\7\3\2\2vw\5\n\6\2wx\7\4\2\2x|")
        buf.write("\3\2\2\2yz\7\3\2\2z|\7\4\2\2{u\3\2\2\2{y\3\2\2\2|\t\3")
        buf.write("\2\2\2}\u0082\5\f\7\2~\177\5\f\7\2\177\u0080\5\n\6\2\u0080")
        buf.write("\u0082\3\2\2\2\u0081}\3\2\2\2\u0081~\3\2\2\2\u0082\13")
        buf.write("\3\2\2\2\u0083\u0086\5\16\b\2\u0084\u0086\5\20\t\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\r\3\2\2\2\u0087")
        buf.write("\u008a\7$\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u008e\7")
        buf.write("#\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\u0092\3\2\2\2\u008f\u0090\7#\2\2\u0090")
        buf.write("\u0092\7$\2\2\u0091\u0089\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\5\"\22\2\u0094\u0095")
        buf.write("\5\36\20\2\u0095\u0096\7\t\2\2\u0096\17\3\2\2\2\u0097")
        buf.write("\u0099\7$\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u009c\5\"\22\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009e\7=\2\2\u009e\u009f\5\22\n\2\u009f\u00a0\5\30\r")
        buf.write("\2\u00a0\21\3\2\2\2\u00a1\u00a2\7\7\2\2\u00a2\u00a3\5")
        buf.write("\24\13\2\u00a3\u00a4\7\b\2\2\u00a4\u00a8\3\2\2\2\u00a5")
        buf.write("\u00a6\7\7\2\2\u00a6\u00a8\7\b\2\2\u00a7\u00a1\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00af\5\26")
        buf.write("\f\2\u00aa\u00ab\5\26\f\2\u00ab\u00ac\7\t\2\2\u00ac\u00ad")
        buf.write("\5\24\13\2\u00ad\u00af\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae")
        buf.write("\u00aa\3\2\2\2\u00af\25\3\2\2\2\u00b0\u00b1\5\"\22\2\u00b1")
        buf.write("\u00b2\5\\/\2\u00b2\27\3\2\2\2\u00b3\u00b4\5(\25\2\u00b4")
        buf.write("\31\3\2\2\2\u00b5\u00ba\5\34\17\2\u00b6\u00b7\5\34\17")
        buf.write("\2\u00b7\u00b8\5\32\16\2\u00b8\u00ba\3\2\2\2\u00b9\u00b5")
        buf.write("\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba\33\3\2\2\2\u00bb\u00bd")
        buf.write("\7#\2\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00bf\5\"\22\2\u00bf\u00c0\5\36\20")
        buf.write("\2\u00c0\u00c1\7\t\2\2\u00c1\35\3\2\2\2\u00c2\u00c8\5")
        buf.write(" \21\2\u00c3\u00c4\5 \21\2\u00c4\u00c5\7\13\2\2\u00c5")
        buf.write("\u00c6\5\36\20\2\u00c6\u00c8\3\2\2\2\u00c7\u00c2\3\2\2")
        buf.write("\2\u00c7\u00c3\3\2\2\2\u00c8\37\3\2\2\2\u00c9\u00cc\7")
        buf.write("=\2\2\u00ca\u00cb\7\16\2\2\u00cb\u00cd\5> \2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd!\3\2\2\2\u00ce\u00cf")
        buf.write("\b\22\1\2\u00cf\u00d6\7\30\2\2\u00d0\u00d6\7\26\2\2\u00d1")
        buf.write("\u00d6\7\17\2\2\u00d2\u00d6\7\32\2\2\u00d3\u00d6\7 \2")
        buf.write("\2\u00d4\u00d6\7=\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00d0")
        buf.write("\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00dd\3\2\2\2")
        buf.write("\u00d7\u00d8\f\t\2\2\u00d8\u00d9\7\5\2\2\u00d9\u00da\7")
        buf.write("\67\2\2\u00da\u00dc\7\6\2\2\u00db\u00d7\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de#\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e5\5&\24")
        buf.write("\2\u00e1\u00e2\5&\24\2\u00e2\u00e3\5$\23\2\u00e3\u00e5")
        buf.write("\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e5")
        buf.write("%\3\2\2\2\u00e6\u00ef\5(\25\2\u00e7\u00ef\5*\26\2\u00e8")
        buf.write("\u00ef\5.\30\2\u00e9\u00ef\5\60\31\2\u00ea\u00ef\5\64")
        buf.write("\33\2\u00eb\u00ef\5\66\34\2\u00ec\u00ef\58\35\2\u00ed")
        buf.write("\u00ef\5:\36\2\u00ee\u00e6\3\2\2\2\u00ee\u00e7\3\2\2\2")
        buf.write("\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea\3")
        buf.write("\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ef\'\3\2\2\2\u00f0\u00f1\7\3\2\2\u00f1\u00f2")
        buf.write("\5\32\16\2\u00f2\u00f3\5$\23\2\u00f3\u00f4\7\4\2\2\u00f4")
        buf.write("\u0100\3\2\2\2\u00f5\u00f6\7\3\2\2\u00f6\u00f7\5\32\16")
        buf.write("\2\u00f7\u00f8\7\4\2\2\u00f8\u0100\3\2\2\2\u00f9\u00fa")
        buf.write("\7\3\2\2\u00fa\u00fb\5$\23\2\u00fb\u00fc\7\4\2\2\u00fc")
        buf.write("\u0100\3\2\2\2\u00fd\u00fe\7\3\2\2\u00fe\u0100\7\4\2\2")
        buf.write("\u00ff\u00f0\3\2\2\2\u00ff\u00f5\3\2\2\2\u00ff\u00f9\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u0100)\3\2\2\2\u0101\u0102")
        buf.write("\5,\27\2\u0102\u0103\7\r\2\2\u0103\u0104\5> \2\u0104\u0105")
        buf.write("\7\t\2\2\u0105+\3\2\2\2\u0106\u0111\7=\2\2\u0107\u0108")
        buf.write("\5P)\2\u0108\u0109\7\f\2\2\u0109\u010a\7=\2\2\u010a\u0111")
        buf.write("\3\2\2\2\u010b\u010c\5P)\2\u010c\u010d\7\5\2\2\u010d\u010e")
        buf.write("\5> \2\u010e\u010f\7\6\2\2\u010f\u0111\3\2\2\2\u0110\u0106")
        buf.write("\3\2\2\2\u0110\u0107\3\2\2\2\u0110\u010b\3\2\2\2\u0111")
        buf.write("-\3\2\2\2\u0112\u0113\7\27\2\2\u0113\u0114\5> \2\u0114")
        buf.write("\u0115\7\33\2\2\u0115\u0116\5&\24\2\u0116\u011f\3\2\2")
        buf.write("\2\u0117\u0118\7\27\2\2\u0118\u0119\5> \2\u0119\u011a")
        buf.write("\7\33\2\2\u011a\u011b\5&\24\2\u011b\u011c\7\24\2\2\u011c")
        buf.write("\u011d\5&\24\2\u011d\u011f\3\2\2\2\u011e\u0112\3\2\2\2")
        buf.write("\u011e\u0117\3\2\2\2\u011f/\3\2\2\2\u0120\u0121\7\34\2")
        buf.write("\2\u0121\u0122\5\62\32\2\u0122\u0123\7\23\2\2\u0123\u0124")
        buf.write("\5&\24\2\u0124\61\3\2\2\2\u0125\u0126\7=\2\2\u0126\u0127")
        buf.write("\7\r\2\2\u0127\u0128\5> \2\u0128\u0129\t\2\2\2\u0129\u012a")
        buf.write("\5> \2\u012a\63\3\2\2\2\u012b\u012c\7\20\2\2\u012c\u012d")
        buf.write("\7\t\2\2\u012d\65\3\2\2\2\u012e\u012f\7\22\2\2\u012f\u0130")
        buf.write("\7\t\2\2\u0130\67\3\2\2\2\u0131\u0132\7\35\2\2\u0132\u0133")
        buf.write("\5> \2\u0133\u0134\7\t\2\2\u01349\3\2\2\2\u0135\u0136")
        buf.write("\5P)\2\u0136\u0137\7\f\2\2\u0137\u0138\7=\2\2\u0138\u0139")
        buf.write("\7\7\2\2\u0139\u013a\5<\37\2\u013a\u013b\7\b\2\2\u013b")
        buf.write("\u013c\7\t\2\2\u013c\u0145\3\2\2\2\u013d\u013e\5P)\2\u013e")
        buf.write("\u013f\7\f\2\2\u013f\u0140\7=\2\2\u0140\u0141\7\7\2\2")
        buf.write("\u0141\u0142\7\b\2\2\u0142\u0143\7\t\2\2\u0143\u0145\3")
        buf.write("\2\2\2\u0144\u0135\3\2\2\2\u0144\u013d\3\2\2\2\u0145;")
        buf.write("\3\2\2\2\u0146\u0147\5> \2\u0147\u0148\7\13\2\2\u0148")
        buf.write("\u0149\5<\37\2\u0149\u014c\3\2\2\2\u014a\u014c\5> \2\u014b")
        buf.write("\u0146\3\2\2\2\u014b\u014a\3\2\2\2\u014c=\3\2\2\2\u014d")
        buf.write("\u014e\5@!\2\u014e\u014f\t\3\2\2\u014f\u0150\5@!\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u0153\5@!\2\u0152\u014d\3\2\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153?\3\2\2\2\u0154\u0155\5B\"\2\u0155")
        buf.write("\u0156\t\4\2\2\u0156\u0157\5B\"\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015a\5B\"\2\u0159\u0154\3\2\2\2\u0159\u0158\3")
        buf.write("\2\2\2\u015aA\3\2\2\2\u015b\u015c\b\"\1\2\u015c\u015d")
        buf.write("\5D#\2\u015d\u0163\3\2\2\2\u015e\u015f\f\4\2\2\u015f\u0160")
        buf.write("\t\5\2\2\u0160\u0162\5D#\2\u0161\u015e\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("C\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b#\1\2\u0167")
        buf.write("\u0168\5F$\2\u0168\u016e\3\2\2\2\u0169\u016a\f\4\2\2\u016a")
        buf.write("\u016b\t\6\2\2\u016b\u016d\5F$\2\u016c\u0169\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016fE\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172\b$\1\2")
        buf.write("\u0172\u0173\5H%\2\u0173\u0179\3\2\2\2\u0174\u0175\f\4")
        buf.write("\2\2\u0175\u0176\t\7\2\2\u0176\u0178\5H%\2\u0177\u0174")
        buf.write("\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017aG\3\2\2\2\u017b\u0179\3\2\2\2\u017c")
        buf.write("\u017d\b%\1\2\u017d\u017e\5J&\2\u017e\u0184\3\2\2\2\u017f")
        buf.write("\u0180\f\4\2\2\u0180\u0181\7\66\2\2\u0181\u0183\5J&\2")
        buf.write("\u0182\u017f\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185I\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0187\u0188\7-\2\2\u0188\u018b\5J&\2\u0189\u018b")
        buf.write("\5L\'\2\u018a\u0187\3\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("K\3\2\2\2\u018c\u018d\t\6\2\2\u018d\u0190\5L\'\2\u018e")
        buf.write("\u0190\5N(\2\u018f\u018c\3\2\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("M\3\2\2\2\u0191\u0192\5P)\2\u0192\u0193\7\5\2\2\u0193")
        buf.write("\u0194\5> \2\u0194\u0195\7\6\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0198\5P)\2\u0197\u0191\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("O\3\2\2\2\u0199\u019a\b)\1\2\u019a\u019b\5R*\2\u019b\u01ad")
        buf.write("\3\2\2\2\u019c\u019d\f\6\2\2\u019d\u019e\7\f\2\2\u019e")
        buf.write("\u019f\7=\2\2\u019f\u01a0\7\7\2\2\u01a0\u01a1\5<\37\2")
        buf.write("\u01a1\u01a2\7\b\2\2\u01a2\u01ac\3\2\2\2\u01a3\u01a4\f")
        buf.write("\5\2\2\u01a4\u01a5\7\f\2\2\u01a5\u01a6\7=\2\2\u01a6\u01a7")
        buf.write("\7\7\2\2\u01a7\u01ac\7\b\2\2\u01a8\u01a9\f\4\2\2\u01a9")
        buf.write("\u01aa\7\f\2\2\u01aa\u01ac\7=\2\2\u01ab\u019c\3\2\2\2")
        buf.write("\u01ab\u01a3\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeQ")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\7\31\2\2\u01b1")
        buf.write("\u01b2\7=\2\2\u01b2\u01b3\7\7\2\2\u01b3\u01b4\5<\37\2")
        buf.write("\u01b4\u01b5\7\b\2\2\u01b5\u01bc\3\2\2\2\u01b6\u01b7\7")
        buf.write("\31\2\2\u01b7\u01b8\7=\2\2\u01b8\u01b9\7\7\2\2\u01b9\u01bc")
        buf.write("\7\b\2\2\u01ba\u01bc\5T+\2\u01bb\u01b0\3\2\2\2\u01bb\u01b6")
        buf.write("\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bcS\3\2\2\2\u01bd\u01c4")
        buf.write("\5Z.\2\u01be\u01c4\5^\60\2\u01bf\u01c4\7\"\2\2\u01c0\u01c4")
        buf.write("\7!\2\2\u01c1\u01c4\7=\2\2\u01c2\u01c4\5V,\2\u01c3\u01bd")
        buf.write("\3\2\2\2\u01c3\u01be\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c3")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4U\3\2\2\2\u01c5\u01c6\7\7\2\2\u01c6\u01c7\5> \2")
        buf.write("\u01c7\u01c8\7\b\2\2\u01c8W\3\2\2\2\u01c9\u01cf\5Z.\2")
        buf.write("\u01ca\u01cb\5Z.\2\u01cb\u01cc\7\13\2\2\u01cc\u01cd\5")
        buf.write("X-\2\u01cd\u01cf\3\2\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca")
        buf.write("\3\2\2\2\u01cfY\3\2\2\2\u01d0\u01d5\7\67\2\2\u01d1\u01d5")
        buf.write("\78\2\2\u01d2\u01d5\5`\61\2\u01d3\u01d5\79\2\2\u01d4\u01d0")
        buf.write("\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5[\3\2\2\2\u01d6\u01db\7=\2\2\u01d7")
        buf.write("\u01d8\7=\2\2\u01d8\u01d9\7\13\2\2\u01d9\u01db\5\\/\2")
        buf.write("\u01da\u01d6\3\2\2\2\u01da\u01d7\3\2\2\2\u01db]\3\2\2")
        buf.write("\2\u01dc\u01dd\7\3\2\2\u01dd\u01de\5<\37\2\u01de\u01df")
        buf.write("\7\4\2\2\u01df_\3\2\2\2\u01e0\u01e1\t\b\2\2\u01e1a\3\2")
        buf.write("\2\2+is{\u0081\u0085\u0089\u008d\u0091\u0098\u009b\u00a7")
        buf.write("\u00ae\u00b9\u00bc\u00c7\u00cc\u00d5\u00dd\u00e4\u00ee")
        buf.write("\u00ff\u0110\u011e\u0144\u014b\u0152\u0159\u0163\u016e")
        buf.write("\u0179\u0184\u018a\u018f\u0197\u01ab\u01ad\u01bb\u01c3")
        buf.write("\u01ce\u01d4\u01da")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "']'", "'('", "')'", 
                     "';'", "':'", "','", "'.'", "':='", "'='", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
                     "'then'", "'for'", "'return'", "'true'", "'false'", 
                     "'void'", "'nil'", "'this'", "'final'", "'static'", 
                     "'to'", "'downto'", "'+'", "'-'", "'*'", "'\\'", "'%'", 
                     "'/'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'^'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "LP", "RP", "LSB", "RSB", "LB", "RB", 
                      "SEMICOLON", "COLON", "COMMA", "DOT", "ASSIGN", "CONST", 
                      "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                      "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                      "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                      "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "I_DIV", "MOD", "F_DIV", "NOT", 
                      "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_EQ", "GREATER_THAN_EQ", "CONCAT", "INTLIT", 
                      "FLOATLIT", "STRINGLIT", "WS", "BLOCK_CMT", "LINE_CMT", 
                      "ID", "UND", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classList = 1
    RULE_classDecl = 2
    RULE_classBody = 3
    RULE_membersList = 4
    RULE_member = 5
    RULE_attributesDecl = 6
    RULE_methodDecl = 7
    RULE_paramMethod = 8
    RULE_paramDeclList = 9
    RULE_paramDecl = 10
    RULE_bodyMethod = 11
    RULE_varDeclMulList = 12
    RULE_varDecls = 13
    RULE_varDeclList = 14
    RULE_varList = 15
    RULE_typeDecl = 16
    RULE_listStatement = 17
    RULE_statements = 18
    RULE_blockStmt = 19
    RULE_assignStmt = 20
    RULE_lhs = 21
    RULE_ifStmt = 22
    RULE_forStmt = 23
    RULE_condition = 24
    RULE_breakStmt = 25
    RULE_continueStmt = 26
    RULE_returnStmt = 27
    RULE_callStmt = 28
    RULE_expList = 29
    RULE_exp = 30
    RULE_exp1 = 31
    RULE_exp2 = 32
    RULE_exp3 = 33
    RULE_exp4 = 34
    RULE_exp5 = 35
    RULE_exp6 = 36
    RULE_exp7 = 37
    RULE_exp8 = 38
    RULE_exp9 = 39
    RULE_exp10 = 40
    RULE_exp11 = 41
    RULE_subexpression = 42
    RULE_literalList = 43
    RULE_literal = 44
    RULE_idList = 45
    RULE_arrayLit = 46
    RULE_booleanlit = 47

    ruleNames =  [ "program", "classList", "classDecl", "classBody", "membersList", 
                   "member", "attributesDecl", "methodDecl", "paramMethod", 
                   "paramDeclList", "paramDecl", "bodyMethod", "varDeclMulList", 
                   "varDecls", "varDeclList", "varList", "typeDecl", "listStatement", 
                   "statements", "blockStmt", "assignStmt", "lhs", "ifStmt", 
                   "forStmt", "condition", "breakStmt", "continueStmt", 
                   "returnStmt", "callStmt", "expList", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "exp11", "subexpression", "literalList", "literal", 
                   "idList", "arrayLit", "booleanlit" ]

    EOF = Token.EOF
    LP=1
    RP=2
    LSB=3
    RSB=4
    LB=5
    RB=6
    SEMICOLON=7
    COLON=8
    COMMA=9
    DOT=10
    ASSIGN=11
    CONST=12
    BOOLEAN=13
    BREAK=14
    CLASS=15
    CONTINUE=16
    DO=17
    ELSE=18
    EXTENDS=19
    FLOAT=20
    IF=21
    INT=22
    NEW=23
    STRING=24
    THEN=25
    FOR=26
    RETURN=27
    TRUE=28
    FALSE=29
    VOID=30
    NIL=31
    THIS=32
    FINAL=33
    STATIC=34
    TO=35
    DOWNTO=36
    ADD=37
    SUB=38
    MUL=39
    I_DIV=40
    MOD=41
    F_DIV=42
    NOT=43
    AND=44
    OR=45
    EQUAL=46
    NOT_EQUAL=47
    LESS_THAN=48
    GREATER_THAN=49
    LESS_THAN_EQ=50
    GREATER_THAN_EQ=51
    CONCAT=52
    INTLIT=53
    FLOATLIT=54
    STRINGLIT=55
    WS=56
    BLOCK_CMT=57
    LINE_CMT=58
    ID=59
    UND=60
    UNCLOSED_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

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

        def classList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassListContext,0)


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
            self.state = 96
            self.classList()
            self.state = 97
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,0)


        def classList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassList" ):
                return visitor.visitClassList(self)
            else:
                return visitor.visitChildren(self)




    def classList(self):

        localctx = BKOOLParser.ClassListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classList)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.classDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.classDecl()
                self.state = 101
                self.classList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
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

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def classBody(self):
            return self.getTypedRuleContext(BKOOLParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(BKOOLParser.CLASS)
                self.state = 106
                self.match(BKOOLParser.ID)
                self.state = 107
                self.match(BKOOLParser.EXTENDS)
                self.state = 108
                self.match(BKOOLParser.ID)
                self.state = 109
                self.classBody()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(BKOOLParser.CLASS)
                self.state = 111
                self.match(BKOOLParser.ID)
                self.state = 112
                self.classBody()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def membersList(self):
            return self.getTypedRuleContext(BKOOLParser.MembersListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = BKOOLParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classBody)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(BKOOLParser.LP)
                self.state = 116
                self.membersList()
                self.state = 117
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(BKOOLParser.LP)
                self.state = 120
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def membersList(self):
            return self.getTypedRuleContext(BKOOLParser.MembersListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_membersList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembersList" ):
                return visitor.visitMembersList(self)
            else:
                return visitor.visitChildren(self)




    def membersList(self):

        localctx = BKOOLParser.MembersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_membersList)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.member()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.member()
                self.state = 125
                self.membersList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributesDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributesDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.attributesDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.TypeDeclContext,0)


        def varDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclListContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributesDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributesDecl" ):
                return visitor.visitAttributesDecl(self)
            else:
                return visitor.visitChildren(self)




    def attributesDecl(self):

        localctx = BKOOLParser.AttributesDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributesDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 133
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.FINAL]:
                    self.state = 137
                    self.match(BKOOLParser.FINAL)
                    pass
                elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 141
                self.match(BKOOLParser.FINAL)
                self.state = 142
                self.match(BKOOLParser.STATIC)
                pass


            self.state = 145
            self.typeDecl(0)
            self.state = 146
            self.varDeclList()
            self.state = 147
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramMethod(self):
            return self.getTypedRuleContext(BKOOLParser.ParamMethodContext,0)


        def bodyMethod(self):
            return self.getTypedRuleContext(BKOOLParser.BodyMethodContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.TypeDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 149
                self.match(BKOOLParser.STATIC)


            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 152
                self.typeDecl(0)


            self.state = 155
            self.match(BKOOLParser.ID)
            self.state = 156
            self.paramMethod()
            self.state = 157
            self.bodyMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamMethod" ):
                return visitor.visitParamMethod(self)
            else:
                return visitor.visitChildren(self)




    def paramMethod(self):

        localctx = BKOOLParser.ParamMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramMethod)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(BKOOLParser.LB)
                self.state = 160
                self.paramDeclList()
                self.state = 161
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BKOOLParser.LB)
                self.state = 164
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclList" ):
                return visitor.visitParamDeclList(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclList(self):

        localctx = BKOOLParser.ParamDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramDeclList)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.paramDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.paramDecl()
                self.state = 169
                self.match(BKOOLParser.SEMICOLON)
                self.state = 170
                self.paramDeclList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.TypeDeclContext,0)


        def idList(self):
            return self.getTypedRuleContext(BKOOLParser.IdListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = BKOOLParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.typeDecl(0)
            self.state = 175
            self.idList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_bodyMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyMethod" ):
                return visitor.visitBodyMethod(self)
            else:
                return visitor.visitChildren(self)




    def bodyMethod(self):

        localctx = BKOOLParser.BodyMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bodyMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclMulListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecls(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclsContext,0)


        def varDeclMulList(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclMulListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDeclMulList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclMulList" ):
                return visitor.visitVarDeclMulList(self)
            else:
                return visitor.visitChildren(self)




    def varDeclMulList(self):

        localctx = BKOOLParser.VarDeclMulListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varDeclMulList)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.varDecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.varDecls()
                self.state = 181
                self.varDeclMulList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.TypeDeclContext,0)


        def varDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclListContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecls" ):
                return visitor.visitVarDecls(self)
            else:
                return visitor.visitChildren(self)




    def varDecls(self):

        localctx = BKOOLParser.VarDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 185
                self.match(BKOOLParser.FINAL)


            self.state = 188
            self.typeDecl(0)
            self.state = 189
            self.varDeclList()
            self.state = 190
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varList(self):
            return self.getTypedRuleContext(BKOOLParser.VarListContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def varDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclList" ):
                return visitor.visitVarDeclList(self)
            else:
                return visitor.visitChildren(self)




    def varDeclList(self):

        localctx = BKOOLParser.VarDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varDeclList)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.varList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.varList()
                self.state = 194
                self.match(BKOOLParser.COMMA)
                self.state = 195
                self.varDeclList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def CONST(self):
            return self.getToken(BKOOLParser.CONST, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarList" ):
                return visitor.visitVarList(self)
            else:
                return visitor.visitChildren(self)




    def varList(self):

        localctx = BKOOLParser.VarListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(BKOOLParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.CONST:
                self.state = 200
                self.match(BKOOLParser.CONST)
                self.state = 201
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.TypeDeclContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)



    def typeDecl(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.TypeDeclContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_typeDecl, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT]:
                self.state = 205
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.state = 206
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.BOOLEAN]:
                self.state = 207
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.STRING]:
                self.state = 208
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.VOID]:
                self.state = 209
                self.match(BKOOLParser.VOID)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 210
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.TypeDeclContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_typeDecl)
                    self.state = 213
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 214
                    self.match(BKOOLParser.LSB)
                    self.state = 215
                    self.match(BKOOLParser.INTLIT)
                    self.state = 216
                    self.match(BKOOLParser.RSB) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(BKOOLParser.StatementsContext,0)


        def listStatement(self):
            return self.getTypedRuleContext(BKOOLParser.ListStatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListStatement" ):
                return visitor.visitListStatement(self)
            else:
                return visitor.visitChildren(self)




    def listStatement(self):

        localctx = BKOOLParser.ListStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_listStatement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.statements()
                self.state = 224
                self.listStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(BKOOLParser.CallStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BKOOLParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statements)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 235
                self.callStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def varDeclMulList(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclMulListContext,0)


        def listStatement(self):
            return self.getTypedRuleContext(BKOOLParser.ListStatementContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_blockStmt)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(BKOOLParser.LP)
                self.state = 239
                self.varDeclMulList()
                self.state = 240
                self.listStatement()
                self.state = 241
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(BKOOLParser.LP)
                self.state = 244
                self.varDeclMulList()
                self.state = 245
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.match(BKOOLParser.LP)
                self.state = 248
                self.listStatement()
                self.state = 249
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(BKOOLParser.LP)
                self.state = 252
                self.match(BKOOLParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.lhs()
            self.state = 256
            self.match(BKOOLParser.ASSIGN)
            self.state = 257
            self.exp()
            self.state = 258
            self.match(BKOOLParser.SEMICOLON)
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

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lhs)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.exp9(0)
                self.state = 262
                self.match(BKOOLParser.DOT)
                self.state = 263
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.exp9(0)
                self.state = 266
                self.match(BKOOLParser.LSB)
                self.state = 267
                self.exp()
                self.state = 268
                self.match(BKOOLParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementsContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifStmt)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(BKOOLParser.IF)
                self.state = 273
                self.exp()
                self.state = 274
                self.match(BKOOLParser.THEN)
                self.state = 275
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(BKOOLParser.IF)
                self.state = 278
                self.exp()
                self.state = 279
                self.match(BKOOLParser.THEN)
                self.state = 280
                self.statements()
                self.state = 281
                self.match(BKOOLParser.ELSE)
                self.state = 282
                self.statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def condition(self):
            return self.getTypedRuleContext(BKOOLParser.ConditionContext,0)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statements(self):
            return self.getTypedRuleContext(BKOOLParser.StatementsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BKOOLParser.FOR)
            self.state = 287
            self.condition()
            self.state = 288
            self.match(BKOOLParser.DO)
            self.state = 289
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = BKOOLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKOOLParser.ID)
            self.state = 292
            self.match(BKOOLParser.ASSIGN)
            self.state = 293
            self.exp()
            self.state = 294
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 295
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKOOLParser.BREAK)
            self.state = 298
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BKOOLParser.CONTINUE)
            self.state = 301
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(BKOOLParser.RETURN)
            self.state = 304
            self.exp()
            self.state = 305
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = BKOOLParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_callStmt)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.exp9(0)
                self.state = 308
                self.match(BKOOLParser.DOT)
                self.state = 309
                self.match(BKOOLParser.ID)
                self.state = 310
                self.match(BKOOLParser.LB)
                self.state = 311
                self.expList()
                self.state = 312
                self.match(BKOOLParser.RB)
                self.state = 313
                self.match(BKOOLParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.exp9(0)
                self.state = 316
                self.match(BKOOLParser.DOT)
                self.state = 317
                self.match(BKOOLParser.ID)
                self.state = 318
                self.match(BKOOLParser.LB)
                self.state = 319
                self.match(BKOOLParser.RB)
                self.state = 320
                self.match(BKOOLParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpList" ):
                return visitor.visitExpList(self)
            else:
                return visitor.visitChildren(self)




    def expList(self):

        localctx = BKOOLParser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expList)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.exp()
                self.state = 325
                self.match(BKOOLParser.COMMA)
                self.state = 326
                self.expList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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


        def LESS_THAN(self):
            return self.getToken(BKOOLParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(BKOOLParser.GREATER_THAN, 0)

        def LESS_THAN_EQ(self):
            return self.getToken(BKOOLParser.LESS_THAN_EQ, 0)

        def GREATER_THAN_EQ(self):
            return self.getToken(BKOOLParser.GREATER_THAN_EQ, 0)

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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.exp1()
                self.state = 332
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS_THAN) | (1 << BKOOLParser.GREATER_THAN) | (1 << BKOOLParser.LESS_THAN_EQ) | (1 << BKOOLParser.GREATER_THAN_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
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


        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

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
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.exp2(0)
                self.state = 339
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.EQUAL or _la==BKOOLParser.NOT_EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 340
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.AND or _la==BKOOLParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 350
                    self.exp3(0) 
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 364
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 359
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 360
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 361
                    self.exp4(0) 
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def I_DIV(self):
            return self.getToken(BKOOLParser.I_DIV, 0)

        def F_DIV(self):
            return self.getToken(BKOOLParser.F_DIV, 0)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 370
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 371
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.MOD) | (1 << BKOOLParser.F_DIV))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 372
                    self.exp5(0) 
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    self.match(BKOOLParser.CONCAT)
                    self.state = 383
                    self.exp6() 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_exp6)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(BKOOLParser.NOT)
                self.state = 390
                self.exp6()
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 395
                self.exp7()
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.exp8()
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


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp8)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.exp9(0)
                self.state = 400
                self.match(BKOOLParser.LSB)
                self.state = 401
                self.exp()
                self.state = 402
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.exp9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 425
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 410
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 411
                        self.match(BKOOLParser.DOT)
                        self.state = 412
                        self.match(BKOOLParser.ID)
                        self.state = 413
                        self.match(BKOOLParser.LB)
                        self.state = 414
                        self.expList()
                        self.state = 415
                        self.match(BKOOLParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 417
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 418
                        self.match(BKOOLParser.DOT)
                        self.state = 419
                        self.match(BKOOLParser.ID)
                        self.state = 420
                        self.match(BKOOLParser.LB)
                        self.state = 421
                        self.match(BKOOLParser.RB)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                        self.state = 422
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 423
                        self.match(BKOOLParser.DOT)
                        self.state = 424
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp10)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(BKOOLParser.NEW)
                self.state = 431
                self.match(BKOOLParser.ID)
                self.state = 432
                self.match(BKOOLParser.LB)
                self.state = 433
                self.expList()
                self.state = 434
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(BKOOLParser.NEW)
                self.state = 437
                self.match(BKOOLParser.ID)
                self.state = 438
                self.match(BKOOLParser.LB)
                self.state = 439
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def subexpression(self):
            return self.getTypedRuleContext(BKOOLParser.SubexpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp11)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.literal()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.arrayLit()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 446
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 447
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 448
                self.subexpression()
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


    class SubexpressionContext(ParserRuleContext):
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
            return BKOOLParser.RULE_subexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpression" ):
                return visitor.visitSubexpression(self)
            else:
                return visitor.visitChildren(self)




    def subexpression(self):

        localctx = BKOOLParser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(BKOOLParser.LB)
            self.state = 452
            self.exp()
            self.state = 453
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def literalList(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literalList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = BKOOLParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literalList)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.literal()
                self.state = 457
                self.match(BKOOLParser.COMMA)
                self.state = 458
                self.literalList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def booleanlit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanlitContext,0)


        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.booleanlit()
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.match(BKOOLParser.STRINGLIT)
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
        self.enterRule(localctx, 90, self.RULE_idList)
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.match(BKOOLParser.ID)
                self.state = 470
                self.match(BKOOLParser.COMMA)
                self.state = 471
                self.idList()
                pass


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

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


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
        self.enterRule(localctx, 92, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(BKOOLParser.LP)
            self.state = 475
            self.expList()
            self.state = 476
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booleanlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanlit" ):
                return visitor.visitBooleanlit(self)
            else:
                return visitor.visitChildren(self)




    def booleanlit(self):

        localctx = BKOOLParser.BooleanlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_booleanlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.typeDecl_sempred
        self._predicates[32] = self.exp2_sempred
        self._predicates[33] = self.exp3_sempred
        self._predicates[34] = self.exp4_sempred
        self._predicates[35] = self.exp5_sempred
        self._predicates[39] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def typeDecl_sempred(self, localctx:TypeDeclContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




