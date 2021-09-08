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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\7\6\u0099\n\6\f\6\16\6\u009c\13\6\3\7\6\7")
        buf.write("\u009f\n\7\r\7\16\7\u00a0\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00ac\n\b\3\t\3\t\3\t\5\t\u00b1\n\t\3\t\5")
        buf.write("\t\u00b4\n\t\3\n\6\n\u00b7\n\n\r\n\16\n\u00b8\3\13\3\13")
        buf.write("\7\13\u00bd\n\13\f\13\16\13\u00c0\13\13\3\f\3\f\5\f\u00c4")
        buf.write("\n\f\3\f\6\f\u00c7\n\f\r\f\16\f\u00c8\3\r\3\r\7\r\u00cd")
        buf.write("\n\r\f\r\16\r\u00d0\13\r\3\r\3\r\3\16\3\16\5\16\u00d6")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00e0")
        buf.write("\n\20\f\20\16\20\u00e3\13\20\3\20\3\20\5\20\u00e7\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3;")
        buf.write("\3<\3<\3<\3=\3=\3>\3>\3?\3?\7?\u0199\n?\f?\16?\u019c\13")
        buf.write("?\3?\5?\u019f\n?\3?\3?\3@\3@\3@\3@\7@\u01a7\n@\f@\16@")
        buf.write("\u01aa\13@\3@\3@\3@\3@\3@\3A\6A\u01b2\nA\rA\16A\u01b3")
        buf.write("\3A\3A\3B\3B\7B\u01ba\nB\fB\16B\u01bd\13B\3B\3B\3B\3B")
        buf.write("\3C\3C\7C\u01c5\nC\fC\16C\u01c8\13C\3C\3C\3D\3D\3D\3E")
        buf.write("\3E\3E\3E\7E\u01d3\nE\fE\16E\u01d6\13E\3E\3E\3E\7\u00ce")
        buf.write("\u00e1\u019a\u01a8\u01d4\2F\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\2\25\2\27\2\31\13\33\2\35\2\37\2!\f#\r%\16")
        buf.write("\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31")
        buf.write("=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c")
        buf.write("-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081")
        buf.write("<\u0083=\u0085>\u0087?\u0089@\3\2\f\6\2C\\aac|~~\7\2\62")
        buf.write(";C\\aac|~~\3\2\62;\4\2GGgg\4\2--//\6\2\13\f\16\17$$^^")
        buf.write("\b\2^^ddhhppttvv\3\3\f\f\5\2\13\f\17\17\"\"\t\2$$^^dd")
        buf.write("hhppttvv\2\u01e6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\3\u008b\3\2\2\2\5\u008d\3\2\2\2\7\u008f\3\2\2\2\t\u0093")
        buf.write("\3\2\2\2\13\u0096\3\2\2\2\r\u009e\3\2\2\2\17\u00ab\3\2")
        buf.write("\2\2\21\u00ad\3\2\2\2\23\u00b6\3\2\2\2\25\u00ba\3\2\2")
        buf.write("\2\27\u00c1\3\2\2\2\31\u00ca\3\2\2\2\33\u00d5\3\2\2\2")
        buf.write("\35\u00d7\3\2\2\2\37\u00e6\3\2\2\2!\u00e8\3\2\2\2#\u00ee")
        buf.write("\3\2\2\2%\u00f6\3\2\2\2\'\u00fa\3\2\2\2)\u00ff\3\2\2\2")
        buf.write("+\u0106\3\2\2\2-\u010c\3\2\2\2/\u0110\3\2\2\2\61\u0115")
        buf.write("\3\2\2\2\63\u011b\3\2\2\2\65\u0123\3\2\2\2\67\u012a\3")
        buf.write("\2\2\29\u012d\3\2\2\2;\u0132\3\2\2\2=\u0137\3\2\2\2?\u013b")
        buf.write("\3\2\2\2A\u013e\3\2\2\2C\u0145\3\2\2\2E\u0148\3\2\2\2")
        buf.write("G\u014e\3\2\2\2I\u0157\3\2\2\2K\u015e\3\2\2\2M\u0160\3")
        buf.write("\2\2\2O\u0162\3\2\2\2Q\u0164\3\2\2\2S\u0166\3\2\2\2U\u0168")
        buf.write("\3\2\2\2W\u016a\3\2\2\2Y\u016c\3\2\2\2[\u016e\3\2\2\2")
        buf.write("]\u0170\3\2\2\2_\u0172\3\2\2\2a\u0174\3\2\2\2c\u0176\3")
        buf.write("\2\2\2e\u0178\3\2\2\2g\u017a\3\2\2\2i\u017c\3\2\2\2k\u017f")
        buf.write("\3\2\2\2m\u0182\3\2\2\2o\u0184\3\2\2\2q\u0186\3\2\2\2")
        buf.write("s\u0189\3\2\2\2u\u018c\3\2\2\2w\u018f\3\2\2\2y\u0192\3")
        buf.write("\2\2\2{\u0194\3\2\2\2}\u0196\3\2\2\2\177\u01a2\3\2\2\2")
        buf.write("\u0081\u01b1\3\2\2\2\u0083\u01b7\3\2\2\2\u0085\u01c2\3")
        buf.write("\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01ce\3\2\2\2\u008b\u008c")
        buf.write("\7]\2\2\u008c\4\3\2\2\2\u008d\u008e\7_\2\2\u008e\6\3\2")
        buf.write("\2\2\u008f\u0090\7p\2\2\u0090\u0091\7k\2\2\u0091\u0092")
        buf.write("\7n\2\2\u0092\b\3\2\2\2\u0093\u0094\7<\2\2\u0094\u0095")
        buf.write("\7?\2\2\u0095\n\3\2\2\2\u0096\u009a\t\2\2\2\u0097\u0099")
        buf.write("\t\3\2\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\f\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u009f\t\4\2\2\u009e\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\16\3\2\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7w\2\2\u00a5\u00ac\7g\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa")
        buf.write("\7u\2\2\u00aa\u00ac\7g\2\2\u00ab\u00a2\3\2\2\2\u00ab\u00a6")
        buf.write("\3\2\2\2\u00ac\20\3\2\2\2\u00ad\u00b3\5\23\n\2\u00ae\u00b4")
        buf.write("\5\25\13\2\u00af\u00b1\5\25\13\2\u00b0\u00af\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\5\27\f")
        buf.write("\2\u00b3\u00ae\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b4\22\3")
        buf.write("\2\2\2\u00b5\u00b7\t\4\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\24\3\2\2\2\u00ba\u00be\7\60\2\2\u00bb\u00bd\t\4\2\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\26\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c3\t\5\2\2\u00c2\u00c4\t\6\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c7\t\4\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\30\3\2")
        buf.write("\2\2\u00ca\u00ce\7$\2\2\u00cb\u00cd\5\33\16\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cf\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d1\u00d2\7$\2\2\u00d2\32\3\2\2\2\u00d3\u00d6\5\35")
        buf.write("\17\2\u00d4\u00d6\5\37\20\2\u00d5\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6\34\3\2\2\2\u00d7\u00d8\n\7\2\2\u00d8")
        buf.write("\36\3\2\2\2\u00d9\u00da\7^\2\2\u00da\u00e7\t\b\2\2\u00db")
        buf.write("\u00dc\7^\2\2\u00dc\u00dd\7$\2\2\u00dd\u00e1\3\2\2\2\u00de")
        buf.write("\u00e0\5\33\16\2\u00df\u00de\3\2\2\2\u00e0\u00e3\3\2\2")
        buf.write("\2\u00e1\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\7^\2\2\u00e5")
        buf.write("\u00e7\7$\2\2\u00e6\u00d9\3\2\2\2\u00e6\u00db\3\2\2\2")
        buf.write("\u00e7 \3\2\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7n\2\2")
        buf.write("\u00ea\u00eb\7c\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed\7u")
        buf.write("\2\2\u00ed\"\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7")
        buf.write("z\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7f\2\2\u00f4\u00f5\7u\2\2\u00f5$\3")
        buf.write("\2\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9")
        buf.write("\7y\2\2\u00f9&\3\2\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7j\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7u\2\2\u00fe(\3")
        buf.write("\2\2\2\u00ff\u0100\7u\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7e\2\2\u0105*\3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a\7c\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b,\3\2\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7v\2\2\u010f.\3\2\2\2\u0110\u0111")
        buf.write("\7x\2\2\u0111\u0112\7q\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\60\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117")
        buf.write("\7n\2\2\u0117\u0118\7q\2\2\u0118\u0119\7c\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\62\3\2\2\2\u011b\u011c\7d\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7q\2\2\u011e\u011f\7n\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7c\2\2\u0121\u0122\7p\2\2\u0122\64")
        buf.write("\3\2\2\2\u0123\u0124\7u\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7i\2\2\u0129\66\3\2\2\2\u012a\u012b\7k\2\2\u012b\u012c")
        buf.write("\7h\2\2\u012c8\3\2\2\2\u012d\u012e\7g\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f\u0130\7u\2\2\u0130\u0131\7g\2\2\u0131:\3")
        buf.write("\2\2\2\u0132\u0133\7v\2\2\u0133\u0134\7j\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135\u0136\7p\2\2\u0136<\3\2\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138\u0139\7q\2\2\u0139\u013a\7t\2\2\u013a>\3")
        buf.write("\2\2\2\u013b\u013c\7v\2\2\u013c\u013d\7q\2\2\u013d@\3")
        buf.write("\2\2\2\u013e\u013f\7f\2\2\u013f\u0140\7q\2\2\u0140\u0141")
        buf.write("\7y\2\2\u0141\u0142\7p\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7q\2\2\u0144B\3\2\2\2\u0145\u0146\7f\2\2\u0146\u0147")
        buf.write("\7q\2\2\u0147D\3\2\2\2\u0148\u0149\7d\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7g\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7m\2\2\u014dF\3\2\2\2\u014e\u014f\7e\2\2\u014f\u0150")
        buf.write("\7q\2\2\u0150\u0151\7p\2\2\u0151\u0152\7v\2\2\u0152\u0153")
        buf.write("\7k\2\2\u0153\u0154\7p\2\2\u0154\u0155\7w\2\2\u0155\u0156")
        buf.write("\7g\2\2\u0156H\3\2\2\2\u0157\u0158\7t\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159\u015a\7v\2\2\u015a\u015b\7w\2\2\u015b\u015c")
        buf.write("\7t\2\2\u015c\u015d\7p\2\2\u015dJ\3\2\2\2\u015e\u015f")
        buf.write("\7*\2\2\u015fL\3\2\2\2\u0160\u0161\7+\2\2\u0161N\3\2\2")
        buf.write("\2\u0162\u0163\7}\2\2\u0163P\3\2\2\2\u0164\u0165\7\177")
        buf.write("\2\2\u0165R\3\2\2\2\u0166\u0167\7=\2\2\u0167T\3\2\2\2")
        buf.write("\u0168\u0169\7<\2\2\u0169V\3\2\2\2\u016a\u016b\7.\2\2")
        buf.write("\u016bX\3\2\2\2\u016c\u016d\7\60\2\2\u016dZ\3\2\2\2\u016e")
        buf.write("\u016f\7?\2\2\u016f\\\3\2\2\2\u0170\u0171\7-\2\2\u0171")
        buf.write("^\3\2\2\2\u0172\u0173\7/\2\2\u0173`\3\2\2\2\u0174\u0175")
        buf.write("\7,\2\2\u0175b\3\2\2\2\u0176\u0177\7\61\2\2\u0177d\3\2")
        buf.write("\2\2\u0178\u0179\7^\2\2\u0179f\3\2\2\2\u017a\u017b\7\'")
        buf.write("\2\2\u017bh\3\2\2\2\u017c\u017d\7#\2\2\u017d\u017e\7?")
        buf.write("\2\2\u017ej\3\2\2\2\u017f\u0180\7?\2\2\u0180\u0181\7?")
        buf.write("\2\2\u0181l\3\2\2\2\u0182\u0183\7>\2\2\u0183n\3\2\2\2")
        buf.write("\u0184\u0185\7@\2\2\u0185p\3\2\2\2\u0186\u0187\7>\2\2")
        buf.write("\u0187\u0188\7?\2\2\u0188r\3\2\2\2\u0189\u018a\7@\2\2")
        buf.write("\u018a\u018b\7?\2\2\u018bt\3\2\2\2\u018c\u018d\7~\2\2")
        buf.write("\u018d\u018e\7~\2\2\u018ev\3\2\2\2\u018f\u0190\7(\2\2")
        buf.write("\u0190\u0191\7(\2\2\u0191x\3\2\2\2\u0192\u0193\7#\2\2")
        buf.write("\u0193z\3\2\2\2\u0194\u0195\7`\2\2\u0195|\3\2\2\2\u0196")
        buf.write("\u019a\7%\2\2\u0197\u0199\13\2\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019c\3\2\2\2\u019a\u019b\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019f")
        buf.write("\t\t\2\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a1\b?\2\2\u01a1~\3\2\2\2\u01a2\u01a3\7\61\2\2\u01a3")
        buf.write("\u01a4\7,\2\2\u01a4\u01a8\3\2\2\2\u01a5\u01a7\13\2\2\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a9\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\7,\2\2\u01ac\u01ad\7\61\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01af\b@\2\2\u01af\u0080\3\2\2\2")
        buf.write("\u01b0\u01b2\t\n\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b6\bA\2\2\u01b6\u0082\3\2\2\2\u01b7")
        buf.write("\u01bb\7$\2\2\u01b8\u01ba\5\33\16\2\u01b9\u01b8\3\2\2")
        buf.write("\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01bf\7^\2\2\u01bf\u01c0\n\13\2\2\u01c0\u01c1\bB\3\2")
        buf.write("\u01c1\u0084\3\2\2\2\u01c2\u01c6\7$\2\2\u01c3\u01c5\5")
        buf.write("\33\16\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c9\u01ca\bC\4\2\u01ca\u0086\3")
        buf.write("\2\2\2\u01cb\u01cc\13\2\2\2\u01cc\u01cd\bD\5\2\u01cd\u0088")
        buf.write("\3\2\2\2\u01ce\u01cf\7\61\2\2\u01cf\u01d0\7,\2\2\u01d0")
        buf.write("\u01d4\3\2\2\2\u01d1\u01d3\13\2\2\2\u01d2\u01d1\3\2\2")
        buf.write("\2\u01d3\u01d6\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d8\7\2\2\3\u01d8\u01d9\bE\6\2\u01d9\u008a\3\2\2\2")
        buf.write("\27\2\u009a\u00a0\u00ab\u00b0\u00b3\u00b8\u00be\u00c3")
        buf.write("\u00c8\u00ce\u00d5\u00e1\u00e6\u019a\u019e\u01a8\u01b3")
        buf.write("\u01bb\u01c6\u01d4\7\b\2\2\3B\2\3C\3\3D\4\3E\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    INTLIT = 6
    BOOLLIT = 7
    FLOATLIT = 8
    STRINGLIT = 9
    CLASS = 10
    EXTEND = 11
    NEW = 12
    SELF = 13
    STATIC = 14
    MUTABLE = 15
    INTTYPE = 16
    VOIDTYPE = 17
    FLOATTYPE = 18
    BOOLTYPE = 19
    STRINGTYPE = 20
    IF = 21
    ELSE = 22
    THEN = 23
    FOR = 24
    TO = 25
    DOWNTO = 26
    DO = 27
    BREAK = 28
    CONT = 29
    RETURN = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    SEMI = 35
    COLON = 36
    COMMA = 37
    DOT = 38
    ASG = 39
    ADD = 40
    SUB = 41
    MUL = 42
    FLOATDIV = 43
    INTDIV = 44
    MOD = 45
    NEQ = 46
    EQ = 47
    LT = 48
    GT = 49
    LEQ = 50
    GEQ = 51
    OR = 52
    AND = 53
    NOT = 54
    CON = 55
    LINECMT = 56
    BLOCKCMT = 57
    WS = 58
    ILLEGAL_ESCAPE = 59
    UNCLOSE_STRING = 60
    ERROR_CHAR = 61
    UNTERMINATED_COMMENT = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'nil'", "':='", "'class'", "'extends'", "'new'", 
            "'this'", "'static'", "'final'", "'int'", "'void'", "'float'", 
            "'boolean'", "'string'", "'if'", "'else'", "'then'", "'for'", 
            "'to'", "'downto'", "'do'", "'break'", "'continue'", "'return'", 
            "'('", "')'", "'{'", "'}'", "';'", "':'", "','", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "BOOLLIT", "FLOATLIT", "STRINGLIT", "CLASS", 
            "EXTEND", "NEW", "SELF", "STATIC", "MUTABLE", "INTTYPE", "VOIDTYPE", 
            "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "IF", "ELSE", "THEN", 
            "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONT", "RETURN", "LB", 
            "RB", "LP", "RP", "SEMI", "COLON", "COMMA", "DOT", "ASG", "ADD", 
            "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", "EQ", "LT", 
            "GT", "LEQ", "GEQ", "OR", "AND", "NOT", "CON", "LINECMT", "BLOCKCMT", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "INTLIT", "BOOLLIT", 
                  "FLOATLIT", "IntegerPart", "DecimalPart", "ExponentPart", 
                  "STRINGLIT", "Char", "SpecialChar", "InnerString", "CLASS", 
                  "EXTEND", "NEW", "SELF", "STATIC", "MUTABLE", "INTTYPE", 
                  "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "IF", 
                  "ELSE", "THEN", "FOR", "TO", "DOWNTO", "DO", "BREAK", 
                  "CONT", "RETURN", "LB", "RB", "LP", "RP", "SEMI", "COLON", 
                  "COMMA", "DOT", "ASG", "ADD", "SUB", "MUL", "FLOATDIV", 
                  "INTDIV", "MOD", "NEQ", "EQ", "LT", "GT", "LEQ", "GEQ", 
                  "OR", "AND", "NOT", "CON", "LINECMT", "BLOCKCMT", "WS", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

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
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UnterminatedComment()
     


