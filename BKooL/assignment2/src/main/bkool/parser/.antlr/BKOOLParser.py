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
        buf.write("\u01c1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\3\3\3\3\3\5\3e\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4l\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5v\n\5")
        buf.write("\3\6\3\6\3\6\5\6{\n\6\3\7\3\7\5\7\177\n\7\3\b\3\b\3\b")
        buf.write("\5\b\u0084\n\b\3\b\3\b\5\b\u0088\n\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u0090\n\b\3\b\3\b\3\b\3\b\5\b\u0096\n\b\3\t")
        buf.write("\3\t\3\t\5\t\u009b\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00a5\n\f\3\r\3\r\3\r\3\r\5\r\u00ab\n\r\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00b1\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00b9\n\17\3\20\3\20\5\20\u00bd\n\20\3\20\3")
        buf.write("\20\5\20\u00c1\n\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00cd\n\21\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00d3\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00de\n\24\3\25\3\25\5\25\u00e2\n\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00f0\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\5\32\u00fc\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0103\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u010e\n\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0121\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0128\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0132")
        buf.write("\n\37\f\37\16\37\u0135\13\37\3 \3 \3 \5 \u013a\n \3!\3")
        buf.write("!\3!\3!\5!\u0140\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0147\n\"")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\5$\u0150\n$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u015d\n%\3&\3&\5&\u0161\n&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u016e\n\'\3(\3(\5(\u0172")
        buf.write("\n(\3(\3(\5(\u0176\n(\3)\3)\3)\5)\u017b\n)\3*\3*\5*\u017f")
        buf.write("\n*\3*\3*\3*\3*\3+\3+\3+\5+\u0188\n+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u0197\n,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01a9\n,\3-\3-\3-\5-\u01ae")
        buf.write("\n-\3-\3-\3-\3-\3-\3-\3.\3.\3/\3/\3/\3/\3/\3/\3/\5/\u01bf")
        buf.write("\n/\3/\2\3<\60\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\\2\13\3\2\f\20")
        buf.write("\3\28<\3\2-\60\3\2+,\3\2\61\62\3\2%&\3\2\'*\3\2\25\26")
        buf.write("\3\2\30\31\2\u01cf\2^\3\2\2\2\4a\3\2\2\2\6f\3\2\2\2\b")
        buf.write("u\3\2\2\2\nw\3\2\2\2\f~\3\2\2\2\16\u0095\3\2\2\2\20\u009a")
        buf.write("\3\2\2\2\22\u009c\3\2\2\2\24\u009e\3\2\2\2\26\u00a0\3")
        buf.write("\2\2\2\30\u00a6\3\2\2\2\32\u00ac\3\2\2\2\34\u00b2\3\2")
        buf.write("\2\2\36\u00c0\3\2\2\2 \u00cc\3\2\2\2\"\u00ce\3\2\2\2$")
        buf.write("\u00d4\3\2\2\2&\u00dd\3\2\2\2(\u00e1\3\2\2\2*\u00e7\3")
        buf.write("\2\2\2,\u00eb\3\2\2\2.\u00f1\3\2\2\2\60\u00f3\3\2\2\2")
        buf.write("\62\u00fb\3\2\2\2\64\u0102\3\2\2\2\66\u010d\3\2\2\28\u0120")
        buf.write("\3\2\2\2:\u0127\3\2\2\2<\u0129\3\2\2\2>\u0139\3\2\2\2")
        buf.write("@\u013f\3\2\2\2B\u0146\3\2\2\2D\u0148\3\2\2\2F\u014f\3")
        buf.write("\2\2\2H\u015c\3\2\2\2J\u0160\3\2\2\2L\u016d\3\2\2\2N\u0171")
        buf.write("\3\2\2\2P\u0177\3\2\2\2R\u017e\3\2\2\2T\u0184\3\2\2\2")
        buf.write("V\u01a8\3\2\2\2X\u01ad\3\2\2\2Z\u01b5\3\2\2\2\\\u01be")
        buf.write("\3\2\2\2^_\5\4\3\2_`\7\2\2\3`\3\3\2\2\2ad\5\6\4\2be\5")
        buf.write("\4\3\2ce\3\2\2\2db\3\2\2\2dc\3\2\2\2e\5\3\2\2\2fg\7\5")
        buf.write("\2\2gk\7<\2\2hi\7\6\2\2il\7<\2\2jl\3\2\2\2kh\3\2\2\2k")
        buf.write("j\3\2\2\2lm\3\2\2\2mn\5\b\5\2n\7\3\2\2\2op\7\35\2\2pq")
        buf.write("\5\n\6\2qr\7\36\2\2rv\3\2\2\2st\7\35\2\2tv\7\36\2\2uo")
        buf.write("\3\2\2\2us\3\2\2\2v\t\3\2\2\2wz\5\f\7\2x{\5\n\6\2y{\3")
        buf.write("\2\2\2zx\3\2\2\2zy\3\2\2\2{\13\3\2\2\2|\177\5\16\b\2}")
        buf.write("\177\5\36\20\2~|\3\2\2\2~}\3\2\2\2\177\r\3\2\2\2\u0080")
        buf.write("\u0083\7\13\2\2\u0081\u0084\7\n\2\2\u0082\u0084\3\2\2")
        buf.write("\2\u0083\u0081\3\2\2\2\u0083\u0082\3\2\2\2\u0084\u0088")
        buf.write("\3\2\2\2\u0085\u0086\7\n\2\2\u0086\u0088\7\13\2\2\u0087")
        buf.write("\u0080\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008a\5\20\t\2\u008a\u008b\5\34\17\2\u008b\u008c")
        buf.write("\7\37\2\2\u008c\u0096\3\2\2\2\u008d\u0090\7\n\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\5\20\t\2\u0092\u0093")
        buf.write("\5\26\f\2\u0093\u0094\7\37\2\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u0087\3\2\2\2\u0095\u008f\3\2\2\2\u0096\17\3\2\2\2\u0097")
        buf.write("\u009b\5\22\n\2\u0098\u009b\5(\25\2\u0099\u009b\5\24\13")
        buf.write("\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\21\3\2\2\2\u009c\u009d\t\2\2\2\u009d\23")
        buf.write("\3\2\2\2\u009e\u009f\7<\2\2\u009f\25\3\2\2\2\u00a0\u00a4")
        buf.write("\5\30\r\2\u00a1\u00a2\7!\2\2\u00a2\u00a5\5\26\f\2\u00a3")
        buf.write("\u00a5\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a3\3\2\2\2")
        buf.write("\u00a5\27\3\2\2\2\u00a6\u00aa\7<\2\2\u00a7\u00a8\7$\2")
        buf.write("\2\u00a8\u00ab\5\66\34\2\u00a9\u00ab\3\2\2\2\u00aa\u00a7")
        buf.write("\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\31\3\2\2\2\u00ac\u00b0")
        buf.write("\7<\2\2\u00ad\u00ae\7!\2\2\u00ae\u00b1\5\32\16\2\u00af")
        buf.write("\u00b1\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b0\u00af\3\2\2\2")
        buf.write("\u00b1\33\3\2\2\2\u00b2\u00b3\7<\2\2\u00b3\u00b4\7$\2")
        buf.write("\2\u00b4\u00b8\5\66\34\2\u00b5\u00b6\7!\2\2\u00b6\u00b9")
        buf.write("\5\34\17\2\u00b7\u00b9\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00bd\7\n\2\2\u00bb")
        buf.write("\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00c1\5\20\t\2\u00bf\u00c1")
        buf.write("\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c3\7<\2\2\u00c3\u00c4\5 \21\2")
        buf.write("\u00c4\u00c5\5&\24\2\u00c5\37\3\2\2\2\u00c6\u00c7\7\33")
        buf.write("\2\2\u00c7\u00c8\5\"\22\2\u00c8\u00c9\7\34\2\2\u00c9\u00cd")
        buf.write("\3\2\2\2\u00ca\u00cb\7\33\2\2\u00cb\u00cd\7\34\2\2\u00cc")
        buf.write("\u00c6\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd!\3\2\2\2\u00ce")
        buf.write("\u00d2\5$\23\2\u00cf\u00d0\7\37\2\2\u00d0\u00d3\5\"\22")
        buf.write("\2\u00d1\u00d3\3\2\2\2\u00d2\u00cf\3\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3#\3\2\2\2\u00d4\u00d5\5\20\t\2\u00d5\u00d6")
        buf.write("\5\32\16\2\u00d6%\3\2\2\2\u00d7\u00d8\7\35\2\2\u00d8\u00d9")
        buf.write("\5N(\2\u00d9\u00da\7\36\2\2\u00da\u00de\3\2\2\2\u00db")
        buf.write("\u00dc\7\35\2\2\u00dc\u00de\7\36\2\2\u00dd\u00d7\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00de\'\3\2\2\2\u00df\u00e2\5\22")
        buf.write("\n\2\u00e0\u00e2\5\24\13\2\u00e1\u00df\3\2\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7\3\2\2\u00e4")
        buf.write("\u00e5\5\60\31\2\u00e5\u00e6\7\4\2\2\u00e6)\3\2\2\2\u00e7")
        buf.write("\u00e8\7\35\2\2\u00e8\u00e9\5,\27\2\u00e9\u00ea\7\36\2")
        buf.write("\2\u00ea+\3\2\2\2\u00eb\u00ef\5.\30\2\u00ec\u00ed\7!\2")
        buf.write("\2\u00ed\u00f0\5,\27\2\u00ee\u00f0\3\2\2\2\u00ef\u00ec")
        buf.write("\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0-\3\2\2\2\u00f1\u00f2")
        buf.write("\t\3\2\2\u00f2/\3\2\2\2\u00f3\u00f4\7:\2\2\u00f4\61\3")
        buf.write("\2\2\2\u00f5\u00f6\7\33\2\2\u00f6\u00f7\5\64\33\2\u00f7")
        buf.write("\u00f8\7\34\2\2\u00f8\u00fc\3\2\2\2\u00f9\u00fa\7\33\2")
        buf.write("\2\u00fa\u00fc\7\34\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\63\3\2\2\2\u00fd\u00fe\5\66\34\2\u00fe")
        buf.write("\u00ff\7!\2\2\u00ff\u0100\5\64\33\2\u0100\u0103\3\2\2")
        buf.write("\2\u0101\u0103\5\66\34\2\u0102\u00fd\3\2\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0103\65\3\2\2\2\u0104\u0105\58\35\2\u0105\u0106")
        buf.write("\t\4\2\2\u0106\u0107\58\35\2\u0107\u010e\3\2\2\2\u0108")
        buf.write("\u0109\58\35\2\u0109\u010a\t\5\2\2\u010a\u010b\58\35\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010e\58\35\2\u010d\u0104\3")
        buf.write("\2\2\2\u010d\u0108\3\2\2\2\u010d\u010c\3\2\2\2\u010e\67")
        buf.write("\3\2\2\2\u010f\u0110\5:\36\2\u0110\u0111\t\6\2\2\u0111")
        buf.write("\u0112\58\35\2\u0112\u0121\3\2\2\2\u0113\u0114\5:\36\2")
        buf.write("\u0114\u0115\t\7\2\2\u0115\u0116\58\35\2\u0116\u0121\3")
        buf.write("\2\2\2\u0117\u0118\5:\36\2\u0118\u0119\t\b\2\2\u0119\u011a")
        buf.write("\58\35\2\u011a\u0121\3\2\2\2\u011b\u011c\5:\36\2\u011c")
        buf.write("\u011d\7\64\2\2\u011d\u011e\58\35\2\u011e\u0121\3\2\2")
        buf.write("\2\u011f\u0121\5:\36\2\u0120\u010f\3\2\2\2\u0120\u0113")
        buf.write("\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u011b\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u01219\3\2\2\2\u0122\u0123\7\63\2\2\u0123")
        buf.write("\u0128\5:\36\2\u0124\u0125\t\7\2\2\u0125\u0128\5:\36\2")
        buf.write("\u0126\u0128\5<\37\2\u0127\u0122\3\2\2\2\u0127\u0124\3")
        buf.write("\2\2\2\u0127\u0126\3\2\2\2\u0128;\3\2\2\2\u0129\u012a")
        buf.write("\b\37\1\2\u012a\u012b\5> \2\u012b\u0133\3\2\2\2\u012c")
        buf.write("\u012d\f\4\2\2\u012d\u012e\7\3\2\2\u012e\u012f\5\66\34")
        buf.write("\2\u012f\u0130\7\4\2\2\u0130\u0132\3\2\2\2\u0131\u012c")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134=\3\2\2\2\u0135\u0133\3\2\2\2\u0136")
        buf.write("\u013a\5F$\2\u0137\u013a\5J&\2\u0138\u013a\5@!\2\u0139")
        buf.write("\u0136\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2")
        buf.write("\u013a?\3\2\2\2\u013b\u013c\7\7\2\2\u013c\u013d\7<\2\2")
        buf.write("\u013d\u0140\5\62\32\2\u013e\u0140\5B\"\2\u013f\u013b")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140A\3\2\2\2\u0141\u0147")
        buf.write("\5*\26\2\u0142\u0147\5.\30\2\u0143\u0147\7\b\2\2\u0144")
        buf.write("\u0147\7\t\2\2\u0145\u0147\5D#\2\u0146\u0141\3\2\2\2\u0146")
        buf.write("\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0145\3\2\2\2\u0147C\3\2\2\2\u0148\u0149\7\33\2")
        buf.write("\2\u0149\u014a\5\66\34\2\u014a\u014b\7\34\2\2\u014bE\3")
        buf.write("\2\2\2\u014c\u0150\5J&\2\u014d\u0150\5@!\2\u014e\u0150")
        buf.write("\7<\2\2\u014f\u014c\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\7\"\2\2")
        buf.write("\u0152\u0153\7<\2\2\u0153\u0154\5\62\32\2\u0154\u0155")
        buf.write("\5H%\2\u0155G\3\2\2\2\u0156\u0157\7\"\2\2\u0157\u0158")
        buf.write("\7<\2\2\u0158\u0159\5\62\32\2\u0159\u015a\5H%\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u0156\3\2\2\2")
        buf.write("\u015c\u015b\3\2\2\2\u015dI\3\2\2\2\u015e\u0161\5@!\2")
        buf.write("\u015f\u0161\7<\2\2\u0160\u015e\3\2\2\2\u0160\u015f\3")
        buf.write("\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\5H%\2\u0163\u0164")
        buf.write("\7\"\2\2\u0164\u0165\7<\2\2\u0165\u0166\5L\'\2\u0166K")
        buf.write("\3\2\2\2\u0167\u0168\5H%\2\u0168\u0169\7\"\2\2\u0169\u016a")
        buf.write("\7<\2\2\u016a\u016b\5L\'\2\u016b\u016e\3\2\2\2\u016c\u016e")
        buf.write("\3\2\2\2\u016d\u0167\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("M\3\2\2\2\u016f\u0172\5P)\2\u0170\u0172\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0176\5T+\2\u0174\u0176\3\2\2\2\u0175\u0173\3\2")
        buf.write("\2\2\u0175\u0174\3\2\2\2\u0176O\3\2\2\2\u0177\u017a\5")
        buf.write("R*\2\u0178\u017b\5P)\2\u0179\u017b\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u0179\3\2\2\2\u017bQ\3\2\2\2\u017c\u017f")
        buf.write("\7\13\2\2\u017d\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\5\20\t")
        buf.write("\2\u0181\u0182\5\26\f\2\u0182\u0183\7\37\2\2\u0183S\3")
        buf.write("\2\2\2\u0184\u0187\5V,\2\u0185\u0188\5T+\2\u0186\u0188")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("U\3\2\2\2\u0189\u01a9\5&\24\2\u018a\u018b\5\\/\2\u018b")
        buf.write("\u018c\7#\2\2\u018c\u018d\5\66\34\2\u018d\u018e\7\37\2")
        buf.write("\2\u018e\u01a9\3\2\2\2\u018f\u0190\7\21\2\2\u0190\u0191")
        buf.write("\5\66\34\2\u0191\u0192\7\23\2\2\u0192\u0196\5V,\2\u0193")
        buf.write("\u0194\7\22\2\2\u0194\u0197\5V,\2\u0195\u0197\3\2\2\2")
        buf.write("\u0196\u0193\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u01a9\3")
        buf.write("\2\2\2\u0198\u0199\7\24\2\2\u0199\u019a\5Z.\2\u019a\u019b")
        buf.write("\7#\2\2\u019b\u019c\5\66\34\2\u019c\u019d\t\t\2\2\u019d")
        buf.write("\u019e\5\66\34\2\u019e\u019f\7\27\2\2\u019f\u01a0\5V,")
        buf.write("\2\u01a0\u01a9\3\2\2\2\u01a1\u01a2\t\n\2\2\u01a2\u01a9")
        buf.write("\7\37\2\2\u01a3\u01a4\7\32\2\2\u01a4\u01a5\5\66\34\2\u01a5")
        buf.write("\u01a6\7\37\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a9\5X-\2")
        buf.write("\u01a8\u0189\3\2\2\2\u01a8\u018a\3\2\2\2\u01a8\u018f\3")
        buf.write("\2\2\2\u01a8\u0198\3\2\2\2\u01a8\u01a1\3\2\2\2\u01a8\u01a3")
        buf.write("\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9W\3\2\2\2\u01aa\u01ae")
        buf.write("\5J&\2\u01ab\u01ae\5@!\2\u01ac\u01ae\7<\2\2\u01ad\u01aa")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\7\"\2\2\u01b0\u01b1\7<\2\2")
        buf.write("\u01b1\u01b2\5\62\32\2\u01b2\u01b3\5H%\2\u01b3\u01b4\7")
        buf.write("\37\2\2\u01b4Y\3\2\2\2\u01b5\u01b6\7<\2\2\u01b6[\3\2\2")
        buf.write("\2\u01b7\u01bf\7<\2\2\u01b8\u01bf\5J&\2\u01b9\u01ba\5")
        buf.write("> \2\u01ba\u01bb\7\3\2\2\u01bb\u01bc\5\66\34\2\u01bc\u01bd")
        buf.write("\7\4\2\2\u01bd\u01bf\3\2\2\2\u01be\u01b7\3\2\2\2\u01be")
        buf.write("\u01b8\3\2\2\2\u01be\u01b9\3\2\2\2\u01bf]\3\2\2\2-dku")
        buf.write("z~\u0083\u0087\u008f\u0095\u009a\u00a4\u00aa\u00b0\u00b8")
        buf.write("\u00bc\u00c0\u00cc\u00d2\u00dd\u00e1\u00ef\u00fb\u0102")
        buf.write("\u010d\u0120\u0127\u0133\u0139\u013f\u0146\u014f\u015c")
        buf.write("\u0160\u016d\u0171\u0175\u017a\u017e\u0187\u0196\u01a8")
        buf.write("\u01ad\u01be")
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
    RULE_assignList = 13
    RULE_methodDeclare = 14
    RULE_paramList = 15
    RULE_paramDeclare = 16
    RULE_param = 17
    RULE_stmBlock = 18
    RULE_arraytype = 19
    RULE_arrayLit = 20
    RULE_elemList = 21
    RULE_elem = 22
    RULE_size = 23
    RULE_explist = 24
    RULE_exps = 25
    RULE_exp = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_operand = 32
    RULE_subexp = 33
    RULE_methodInvoke = 34
    RULE_methodRecur = 35
    RULE_attriAccess = 36
    RULE_attriRecur = 37
    RULE_stmList = 38
    RULE_variables = 39
    RULE_variable = 40
    RULE_stms = 41
    RULE_stm = 42
    RULE_methodCall = 43
    RULE_scala_var = 44
    RULE_lhs = 45

    ruleNames =  [ "program", "classdcls", "classdcl", "memBlock", "memList", 
                   "classMember", "attributeDeclare", "vartype", "primtype", 
                   "classtype", "attributeList", "attri", "idList", "assignList", 
                   "methodDeclare", "paramList", "paramDeclare", "param", 
                   "stmBlock", "arraytype", "arrayLit", "elemList", "elem", 
                   "size", "explist", "exps", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "operand", "subexp", "methodInvoke", 
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
            self.state = 92
            self.classdcls()
            self.state = 93
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
            self.state = 95
            self.classdcl()
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CLASS]:
                self.state = 96
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
            self.state = 100
            self.match(BKOOLParser.CLASS)
            self.state = 101
            self.match(BKOOLParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTEND]:
                self.state = 102
                self.match(BKOOLParser.EXTEND)
                self.state = 103
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 107
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(BKOOLParser.LP)
                self.state = 110
                self.memList()
                self.state = 111
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(BKOOLParser.LP)
                self.state = 114
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
            self.state = 117
            self.classMember()
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC, BKOOLParser.IMMUTABLE, BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                self.state = 118
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
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.attributeDeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
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


        def assignList(self):
            return self.getTypedRuleContext(BKOOLParser.AssignListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def IMMUTABLE(self):
            return self.getToken(BKOOLParser.IMMUTABLE, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def attributeList(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDeclare




    def attributeDeclare(self):

        localctx = BKOOLParser.AttributeDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributeDeclare)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.IMMUTABLE]:
                    self.state = 126
                    self.match(BKOOLParser.IMMUTABLE)
                    self.state = 129
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKOOLParser.STATIC]:
                        self.state = 127
                        self.match(BKOOLParser.STATIC)
                        pass
                    elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass
                elif token in [BKOOLParser.STATIC]:
                    self.state = 131
                    self.match(BKOOLParser.STATIC)
                    self.state = 132
                    self.match(BKOOLParser.IMMUTABLE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 135
                self.vartype()
                self.state = 136
                self.assignList()
                self.state = 137
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 139
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
                self.vartype()
                self.state = 144
                self.attributeList()
                self.state = 145
                self.match(BKOOLParser.SEMI)
                pass


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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.arraytype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
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
            self.state = 154
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
            self.state = 156
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
            self.state = 158
            self.attri()
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 159
                self.match(BKOOLParser.COMMA)
                self.state = 160
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
            self.state = 164
            self.match(BKOOLParser.ID)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ASG]:
                self.state = 165
                self.match(BKOOLParser.ASG)
                self.state = 166
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
            self.state = 170
            self.match(BKOOLParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 171
                self.match(BKOOLParser.COMMA)
                self.state = 172
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


    class AssignListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASG(self):
            return self.getToken(BKOOLParser.ASG, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def assignList(self):
            return self.getTypedRuleContext(BKOOLParser.AssignListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignList




    def assignList(self):

        localctx = BKOOLParser.AssignListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BKOOLParser.ID)
            self.state = 177
            self.match(BKOOLParser.ASG)
            self.state = 178
            self.exp()
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 179
                self.match(BKOOLParser.COMMA)
                self.state = 180
                self.assignList()
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
        self.enterRule(localctx, 28, self.RULE_methodDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 186
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.STATIC]:
                    self.state = 184
                    self.match(BKOOLParser.STATIC)
                    pass
                elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 188
                self.vartype()
                pass

            elif la_ == 2:
                pass


            self.state = 192
            self.match(BKOOLParser.ID)
            self.state = 193
            self.paramList()
            self.state = 194
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
        self.enterRule(localctx, 30, self.RULE_paramList)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(BKOOLParser.LB)
                self.state = 197
                self.paramDeclare()
                self.state = 198
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(BKOOLParser.LB)
                self.state = 201
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
        self.enterRule(localctx, 32, self.RULE_paramDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.param()
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.state = 205
                self.match(BKOOLParser.SEMI)
                self.state = 206
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
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.vartype()
            self.state = 211
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
        self.enterRule(localctx, 36, self.RULE_stmBlock)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(BKOOLParser.LP)
                self.state = 214
                self.stmList()
                self.state = 215
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(BKOOLParser.LP)
                self.state = 218
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
        self.enterRule(localctx, 38, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE]:
                self.state = 221
                self.primtype()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 222
                self.classtype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 225
            self.match(BKOOLParser.T__0)
            self.state = 226
            self.size()
            self.state = 227
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

        def elemList(self):
            return self.getTypedRuleContext(BKOOLParser.ElemListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BKOOLParser.LP)
            self.state = 230
            self.elemList()
            self.state = 231
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemListContext(ParserRuleContext):

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




    def elemList(self):

        localctx = BKOOLParser.ElemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elemList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.elem()
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 234
                self.match(BKOOLParser.COMMA)
                self.state = 235
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




    def elem(self):

        localctx = BKOOLParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_size




    def size(self):

        localctx = BKOOLParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
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
        self.enterRule(localctx, 48, self.RULE_explist)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(BKOOLParser.LB)
                self.state = 244
                self.exps()
                self.state = 245
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(BKOOLParser.LB)
                self.state = 248
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
        self.enterRule(localctx, 50, self.RULE_exps)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.exp()
                self.state = 252
                self.match(BKOOLParser.COMMA)
                self.state = 253
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.exp1()
                self.state = 259
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LEQ) | (1 << BKOOLParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.exp1()
                self.state = 263
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 264
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
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




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.exp2()
                self.state = 270
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.exp2()
                self.state = 274
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.exp2()
                self.state = 278
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOATDIV) | (1 << BKOOLParser.INTDIV) | (1 << BKOOLParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.exp2()
                self.state = 282
                self.match(BKOOLParser.CON)
                self.state = 283
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
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




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(BKOOLParser.NOT)
                self.state = 289
                self.exp2()
                pass
            elif token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.exp2()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 298
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 299
                    self.match(BKOOLParser.T__0)
                    self.state = 300
                    self.exp()
                    self.state = 301
                    self.match(BKOOLParser.T__1) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def attriAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttriAccessContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4




    def exp4(self):

        localctx = BKOOLParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp4)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.methodInvoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.attriAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
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




    def exp5(self):

        localctx = BKOOLParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp5)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(BKOOLParser.NEW)
                self.state = 314
                self.match(BKOOLParser.ID)
                self.state = 315
                self.explist()
                pass
            elif token in [BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operand)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.arrayLit()
                pass
            elif token in [BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.elem()
                pass
            elif token in [BKOOLParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(BKOOLParser.SELF)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
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
        self.enterRule(localctx, 66, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(BKOOLParser.LB)
            self.state = 327
            self.exp()
            self.state = 328
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


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvoke




    def methodInvoke(self):

        localctx = BKOOLParser.MethodInvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 330
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 331
                self.exp5()
                pass

            elif la_ == 3:
                self.state = 332
                self.match(BKOOLParser.ID)
                pass


            self.state = 335
            self.match(BKOOLParser.DOT)
            self.state = 336
            self.match(BKOOLParser.ID)
            self.state = 337
            self.explist()
            self.state = 338
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
        self.enterRule(localctx, 70, self.RULE_methodRecur)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(BKOOLParser.DOT)
                self.state = 341
                self.match(BKOOLParser.ID)
                self.state = 342
                self.explist()
                self.state = 343
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


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attriAccess




    def attriAccess(self):

        localctx = BKOOLParser.AttriAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attriAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 348
                self.exp5()
                pass

            elif la_ == 2:
                self.state = 349
                self.match(BKOOLParser.ID)
                pass


            self.state = 352
            self.methodRecur()
            self.state = 353
            self.match(BKOOLParser.DOT)
            self.state = 354
            self.match(BKOOLParser.ID)
            self.state = 355
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
        self.enterRule(localctx, 74, self.RULE_attriRecur)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.methodRecur()
                self.state = 358
                self.match(BKOOLParser.DOT)
                self.state = 359
                self.match(BKOOLParser.ID)
                self.state = 360
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
        self.enterRule(localctx, 76, self.RULE_stmList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 365
                self.variables()
                pass

            elif la_ == 2:
                pass


            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 369
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
        self.enterRule(localctx, 78, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.variable()
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 374
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
        self.enterRule(localctx, 80, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IMMUTABLE]:
                self.state = 378
                self.match(BKOOLParser.IMMUTABLE)
                pass
            elif token in [BKOOLParser.INTTYPE, BKOOLParser.VOIDTYPE, BKOOLParser.FLOATTYPE, BKOOLParser.BOOLTYPE, BKOOLParser.STRINGTYPE, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 382
            self.vartype()
            self.state = 383
            self.attributeList()
            self.state = 384
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
        self.enterRule(localctx, 82, self.RULE_stms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.stm()
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.SELF, BKOOLParser.NIL, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONT, BKOOLParser.RETURN, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.BOOLLIT, BKOOLParser.ID]:
                self.state = 387
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
        self.enterRule(localctx, 84, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.stmBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.lhs()
                self.state = 393
                self.match(BKOOLParser.ASGOP)
                self.state = 394
                self.exp()
                self.state = 395
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(BKOOLParser.IF)
                self.state = 398
                self.exp()
                self.state = 399
                self.match(BKOOLParser.THEN)
                self.state = 400
                self.stm()
                self.state = 404
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 401
                    self.match(BKOOLParser.ELSE)
                    self.state = 402
                    self.stm()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.match(BKOOLParser.FOR)
                self.state = 407
                self.scala_var()
                self.state = 408
                self.match(BKOOLParser.ASGOP)
                self.state = 409
                self.exp()
                self.state = 410
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.exp()
                self.state = 412
                self.match(BKOOLParser.DO)
                self.state = 413
                self.stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 415
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.BREAK or _la==BKOOLParser.CONT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 416
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 417
                self.match(BKOOLParser.RETURN)
                self.state = 418
                self.exp()
                self.state = 419
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 421
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


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodCall




    def methodCall(self):

        localctx = BKOOLParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 424
                self.attriAccess()
                pass

            elif la_ == 2:
                self.state = 425
                self.exp5()
                pass

            elif la_ == 3:
                self.state = 426
                self.match(BKOOLParser.ID)
                pass


            self.state = 429
            self.match(BKOOLParser.DOT)
            self.state = 430
            self.match(BKOOLParser.ID)
            self.state = 431
            self.explist()
            self.state = 432
            self.methodRecur()
            self.state = 433
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
        self.enterRule(localctx, 88, self.RULE_scala_var)
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




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lhs)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
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
        self._predicates[29] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




