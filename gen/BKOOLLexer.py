# Generated from E:/hongphuc/PPL/BKooL/assignment1/src/main/bkool/parser\BKOOL.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01a2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\7\33")
        buf.write("\u0107\n\33\f\33\16\33\u010a\13\33\3\34\6\34\u010d\n\34")
        buf.write("\r\34\16\34\u010e\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u011a\n\35\3\36\3\36\3\36\3\36\3\36\7\36")
        buf.write("\u0121\n\36\f\36\16\36\u0124\13\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u012b\n\37\3\37\5\37\u012e\n\37\3 \6 \u0131")
        buf.write("\n \r \16 \u0132\3!\3!\7!\u0137\n!\f!\16!\u013a\13!\3")
        buf.write("\"\3\"\5\"\u013e\n\"\3\"\6\"\u0141\n\"\r\"\16\"\u0142")
        buf.write("\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+")
        buf.write("\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<")
        buf.write("\3<\7<\u017f\n<\f<\16<\u0182\13<\3<\3<\3<\3<\3=\3=\3=")
        buf.write("\3=\7=\u018c\n=\f=\16=\u018f\13=\3=\3=\3=\3=\3=\3>\6>")
        buf.write("\u0197\n>\r>\16>\u0198\3>\3>\3?\3?\3@\3@\3A\3A\4\u0180")
        buf.write("\u018d\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?\2A\2C\2")
        buf.write("E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m")
        buf.write("\65o\66q\67s8u9w:y;{<}=\177>\u0081?\3\2\t\6\2C\\aac|~")
        buf.write("~\7\2\62;C\\aac|~~\3\2\62;\4\2$$``\4\2GGgg\4\2--//\5\2")
        buf.write("\n\f\16\17\"\"\2\u01ad\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2")
        buf.write("\2\2\5\u0085\3\2\2\2\7\u0087\3\2\2\2\t\u008b\3\2\2\2\13")
        buf.write("\u008e\3\2\2\2\r\u0094\3\2\2\2\17\u009c\3\2\2\2\21\u00a0")
        buf.write("\3\2\2\2\23\u00a5\3\2\2\2\25\u00ac\3\2\2\2\27\u00b2\3")
        buf.write("\2\2\2\31\u00b6\3\2\2\2\33\u00bb\3\2\2\2\35\u00c1\3\2")
        buf.write("\2\2\37\u00c9\3\2\2\2!\u00d0\3\2\2\2#\u00d3\3\2\2\2%\u00d8")
        buf.write("\3\2\2\2\'\u00dd\3\2\2\2)\u00e1\3\2\2\2+\u00e4\3\2\2\2")
        buf.write("-\u00eb\3\2\2\2/\u00ee\3\2\2\2\61\u00f4\3\2\2\2\63\u00fd")
        buf.write("\3\2\2\2\65\u0104\3\2\2\2\67\u010c\3\2\2\29\u0119\3\2")
        buf.write("\2\2;\u011b\3\2\2\2=\u0127\3\2\2\2?\u0130\3\2\2\2A\u0134")
        buf.write("\3\2\2\2C\u013b\3\2\2\2E\u0144\3\2\2\2G\u0146\3\2\2\2")
        buf.write("I\u0148\3\2\2\2K\u014a\3\2\2\2M\u014c\3\2\2\2O\u014e\3")
        buf.write("\2\2\2Q\u0150\3\2\2\2S\u0152\3\2\2\2U\u0154\3\2\2\2W\u0156")
        buf.write("\3\2\2\2Y\u0158\3\2\2\2[\u015a\3\2\2\2]\u015c\3\2\2\2")
        buf.write("_\u015e\3\2\2\2a\u0160\3\2\2\2c\u0162\3\2\2\2e\u0165\3")
        buf.write("\2\2\2g\u0168\3\2\2\2i\u016a\3\2\2\2k\u016c\3\2\2\2m\u016f")
        buf.write("\3\2\2\2o\u0172\3\2\2\2q\u0175\3\2\2\2s\u0178\3\2\2\2")
        buf.write("u\u017a\3\2\2\2w\u017c\3\2\2\2y\u0187\3\2\2\2{\u0196\3")
        buf.write("\2\2\2}\u019c\3\2\2\2\177\u019e\3\2\2\2\u0081\u01a0\3")
        buf.write("\2\2\2\u0083\u0084\7]\2\2\u0084\4\3\2\2\2\u0085\u0086")
        buf.write("\7_\2\2\u0086\6\3\2\2\2\u0087\u0088\7p\2\2\u0088\u0089")
        buf.write("\7k\2\2\u0089\u008a\7n\2\2\u008a\b\3\2\2\2\u008b\u008c")
        buf.write("\7<\2\2\u008c\u008d\7?\2\2\u008d\n\3\2\2\2\u008e\u008f")
        buf.write("\7e\2\2\u008f\u0090\7n\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7u\2\2\u0092\u0093\7u\2\2\u0093\f\3\2\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7z\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7p\2\2\u0099\u009a\7f\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\16\3\2\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u009f\7y\2\2\u009f\20\3\2\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7j\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7u\2\2\u00a4\22\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7e\2\2\u00ab\24\3\2\2\2\u00ac\u00ad")
        buf.write("\7h\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7n\2\2\u00b1\26\3\2\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\30")
        buf.write("\3\2\2\2\u00b6\u00b7\7x\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9")
        buf.write("\7k\2\2\u00b9\u00ba\7f\2\2\u00ba\32\3\2\2\2\u00bb\u00bc")
        buf.write("\7h\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7v\2\2\u00c0\34\3\2\2\2\u00c1\u00c2")
        buf.write("\7d\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb")
        buf.write("\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7i\2\2\u00cf \3\2\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7h\2\2\u00d2\"\3\2\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7$\3\2\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7j\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7p\2\2\u00dc&\3")
        buf.write("\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0(\3\2\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3*\3\2\2\2\u00e4\u00e5\7f\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7y\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7q\2\2\u00ea,\3\2\2\2\u00eb\u00ec")
        buf.write("\7f\2\2\u00ec\u00ed\7q\2\2\u00ed.\3\2\2\2\u00ee\u00ef")
        buf.write("\7d\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7m\2\2\u00f3\60\3\2\2\2\u00f4\u00f5")
        buf.write("\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc\62\3\2\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7t\2\2\u0102\u0103\7p\2\2\u0103\64")
        buf.write("\3\2\2\2\u0104\u0108\t\2\2\2\u0105\u0107\t\3\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\66\3\2\2\2\u010a\u0108\3\2")
        buf.write("\2\2\u010b\u010d\t\4\2\2\u010c\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("8\3\2\2\2\u0110\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112")
        buf.write("\u0113\7w\2\2\u0113\u011a\7g\2\2\u0114\u0115\7h\2\2\u0115")
        buf.write("\u0116\7c\2\2\u0116\u0117\7n\2\2\u0117\u0118\7u\2\2\u0118")
        buf.write("\u011a\7g\2\2\u0119\u0110\3\2\2\2\u0119\u0114\3\2\2\2")
        buf.write("\u011a:\3\2\2\2\u011b\u0122\7$\2\2\u011c\u0121\t\5\2\2")
        buf.write("\u011d\u0121\3\2\2\2\u011e\u011f\7\61\2\2\u011f\u0121")
        buf.write("\7$\2\2\u0120\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3")
        buf.write("\2\2\2\u0125\u0126\7$\2\2\u0126<\3\2\2\2\u0127\u012d\5")
        buf.write("? \2\u0128\u012e\5A!\2\u0129\u012b\5A!\2\u012a\u0129\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e")
        buf.write("\5C\"\2\u012d\u0128\3\2\2\2\u012d\u012a\3\2\2\2\u012e")
        buf.write(">\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133@\3\2\2\2\u0134\u0138\7\60\2\2\u0135\u0137\t\4\2")
        buf.write("\2\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139B\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013d\t\6\2\2\u013c\u013e\t\7\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2")
        buf.write("\u013f\u0141\t\4\2\2\u0140\u013f\3\2\2\2\u0141\u0142\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143D")
        buf.write("\3\2\2\2\u0144\u0145\7*\2\2\u0145F\3\2\2\2\u0146\u0147")
        buf.write("\7+\2\2\u0147H\3\2\2\2\u0148\u0149\7}\2\2\u0149J\3\2\2")
        buf.write("\2\u014a\u014b\7\177\2\2\u014bL\3\2\2\2\u014c\u014d\7")
        buf.write("=\2\2\u014dN\3\2\2\2\u014e\u014f\7<\2\2\u014fP\3\2\2\2")
        buf.write("\u0150\u0151\7.\2\2\u0151R\3\2\2\2\u0152\u0153\7\60\2")
        buf.write("\2\u0153T\3\2\2\2\u0154\u0155\7?\2\2\u0155V\3\2\2\2\u0156")
        buf.write("\u0157\7-\2\2\u0157X\3\2\2\2\u0158\u0159\7/\2\2\u0159")
        buf.write("Z\3\2\2\2\u015a\u015b\7,\2\2\u015b\\\3\2\2\2\u015c\u015d")
        buf.write("\7\61\2\2\u015d^\3\2\2\2\u015e\u015f\7^\2\2\u015f`\3\2")
        buf.write("\2\2\u0160\u0161\7\'\2\2\u0161b\3\2\2\2\u0162\u0163\7")
        buf.write("#\2\2\u0163\u0164\7?\2\2\u0164d\3\2\2\2\u0165\u0166\7")
        buf.write("?\2\2\u0166\u0167\7?\2\2\u0167f\3\2\2\2\u0168\u0169\7")
        buf.write(">\2\2\u0169h\3\2\2\2\u016a\u016b\7@\2\2\u016bj\3\2\2\2")
        buf.write("\u016c\u016d\7>\2\2\u016d\u016e\7?\2\2\u016el\3\2\2\2")
        buf.write("\u016f\u0170\7@\2\2\u0170\u0171\7?\2\2\u0171n\3\2\2\2")
        buf.write("\u0172\u0173\7~\2\2\u0173\u0174\7~\2\2\u0174p\3\2\2\2")
        buf.write("\u0175\u0176\7(\2\2\u0176\u0177\7(\2\2\u0177r\3\2\2\2")
        buf.write("\u0178\u0179\7#\2\2\u0179t\3\2\2\2\u017a\u017b\7`\2\2")
        buf.write("\u017bv\3\2\2\2\u017c\u0180\7%\2\2\u017d\u017f\13\2\2")
        buf.write("\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0183\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0183\u0184\7\f\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0186\b<\2\2\u0186x\3\2\2\2\u0187\u0188\7\61\2")
        buf.write("\2\u0188\u0189\7,\2\2\u0189\u018d\3\2\2\2\u018a\u018c")
        buf.write("\13\2\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0190\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u0190\u0191\7,\2\2\u0191\u0192\7")
        buf.write("\61\2\2\u0192\u0193\3\2\2\2\u0193\u0194\b=\2\2\u0194z")
        buf.write("\3\2\2\2\u0195\u0197\t\b\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019b\b>\2\2\u019b|\3\2\2\2")
        buf.write("\u019c\u019d\13\2\2\2\u019d~\3\2\2\2\u019e\u019f\13\2")
        buf.write("\2\2\u019f\u0080\3\2\2\2\u01a0\u01a1\13\2\2\2\u01a1\u0082")
        buf.write("\3\2\2\2\21\2\u0108\u010e\u0119\u0120\u0122\u012a\u012d")
        buf.write("\u0132\u0138\u013d\u0142\u0180\u018d\u0198\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    CLASS = 5
    EXTEND = 6
    NEW = 7
    SELF = 8
    STATIC = 9
    MUTABLE = 10
    INTTYPE = 11
    VOIDTYPE = 12
    FLOATTYPE = 13
    BOOLTYPE = 14
    STRINGTYPE = 15
    IF = 16
    ELSE = 17
    THEN = 18
    FOR = 19
    TO = 20
    DOWNTO = 21
    DO = 22
    BREAK = 23
    CONT = 24
    RETURN = 25
    ID = 26
    INTLIT = 27
    BOOLLIT = 28
    STRINGLIT = 29
    FLOATLIT = 30
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
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

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
            "CLASS", "EXTEND", "NEW", "SELF", "STATIC", "MUTABLE", "INTTYPE", 
            "VOIDTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "IF", "ELSE", 
            "THEN", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONT", "RETURN", 
            "ID", "INTLIT", "BOOLLIT", "STRINGLIT", "FLOATLIT", "LB", "RB", 
            "LP", "RP", "SEMI", "COLON", "COMMA", "DOT", "ASG", "ADD", "SUB", 
            "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", "EQ", "LT", "GT", 
            "LEQ", "GEQ", "OR", "AND", "NOT", "CON", "LINECMT", "BLOCKCMT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "CLASS", "EXTEND", "NEW", 
                  "SELF", "STATIC", "MUTABLE", "INTTYPE", "VOIDTYPE", "FLOATTYPE", 
                  "BOOLTYPE", "STRINGTYPE", "IF", "ELSE", "THEN", "FOR", 
                  "TO", "DOWNTO", "DO", "BREAK", "CONT", "RETURN", "ID", 
                  "INTLIT", "BOOLLIT", "STRINGLIT", "FLOATLIT", "IntegerPart", 
                  "DecimalPart", "ExponentPart", "LB", "RB", "LP", "RP", 
                  "SEMI", "COLON", "COMMA", "DOT", "ASG", "ADD", "SUB", 
                  "MUL", "FLOATDIV", "INTDIV", "MOD", "NEQ", "EQ", "LT", 
                  "GT", "LEQ", "GEQ", "OR", "AND", "NOT", "CON", "LINECMT", 
                  "BLOCKCMT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


