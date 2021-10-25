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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\6\66\u0153\n\66\r\66\16\66\u0154\3\67\3\67")
        buf.write("\7\67\u0159\n\67\f\67\16\67\u015c\13\67\38\38\58\u0160")
        buf.write("\n8\38\68\u0163\n8\r8\168\u0164\39\69\u0168\n9\r9\169")
        buf.write("\u0169\39\39\59\u016e\n9\39\59\u0171\n9\3:\3:\3:\5:\u0176")
        buf.write("\n:\3;\3;\3;\3<\3<\7<\u017d\n<\f<\16<\u0180\13<\3<\3<")
        buf.write("\3<\3=\6=\u0186\n=\r=\16=\u0187\3=\3=\3>\3>\3>\3>\7>\u0190")
        buf.write("\n>\f>\16>\u0193\13>\3>\3>\3>\3>\3>\3?\3?\7?\u019c\n?")
        buf.write("\f?\16?\u019f\13?\3?\5?\u01a2\n?\3?\3?\3@\3@\3A\3A\3B")
        buf.write("\3B\5B\u01ac\nB\3B\3B\3B\7B\u01b1\nB\fB\16B\u01b4\13B")
        buf.write("\3C\3C\3D\3D\7D\u01ba\nD\fD\16D\u01bd\13D\3D\3D\3E\3E")
        buf.write("\7E\u01c3\nE\fE\16E\u01c6\13E\3E\3E\3E\3F\3F\3F\6\u017e")
        buf.write("\u0191\u019d\u01c4\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m\2o\2q8s\2u\2w9y:{;}<\177\2\u0081\2\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\3\2\n\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\5\2\f\f$$^^\t\2$$^^ddhhppttvv\5\2\13\f\16\17\"")
        buf.write("\"\3\3\f\f\4\2C\\c|\2\u01d8\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2q\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u008f\3\2\2")
        buf.write("\2\7\u0091\3\2\2\2\t\u0093\3\2\2\2\13\u0095\3\2\2\2\r")
        buf.write("\u0097\3\2\2\2\17\u0099\3\2\2\2\21\u009b\3\2\2\2\23\u009d")
        buf.write("\3\2\2\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a4\3")
        buf.write("\2\2\2\33\u00a6\3\2\2\2\35\u00ae\3\2\2\2\37\u00b4\3\2")
        buf.write("\2\2!\u00ba\3\2\2\2#\u00c3\3\2\2\2%\u00c6\3\2\2\2\'\u00cb")
        buf.write("\3\2\2\2)\u00d3\3\2\2\2+\u00d9\3\2\2\2-\u00dc\3\2\2\2")
        buf.write("/\u00e0\3\2\2\2\61\u00e4\3\2\2\2\63\u00eb\3\2\2\2\65\u00f0")
        buf.write("\3\2\2\2\67\u00f4\3\2\2\29\u00fb\3\2\2\2;\u0100\3\2\2")
        buf.write("\2=\u0106\3\2\2\2?\u010b\3\2\2\2A\u010f\3\2\2\2C\u0114")
        buf.write("\3\2\2\2E\u011a\3\2\2\2G\u0121\3\2\2\2I\u0124\3\2\2\2")
        buf.write("K\u012b\3\2\2\2M\u012d\3\2\2\2O\u012f\3\2\2\2Q\u0131\3")
        buf.write("\2\2\2S\u0133\3\2\2\2U\u0135\3\2\2\2W\u0137\3\2\2\2Y\u0139")
        buf.write("\3\2\2\2[\u013c\3\2\2\2]\u013f\3\2\2\2_\u0142\3\2\2\2")
        buf.write("a\u0145\3\2\2\2c\u0147\3\2\2\2e\u0149\3\2\2\2g\u014c\3")
        buf.write("\2\2\2i\u014f\3\2\2\2k\u0152\3\2\2\2m\u0156\3\2\2\2o\u015d")
        buf.write("\3\2\2\2q\u0167\3\2\2\2s\u0175\3\2\2\2u\u0177\3\2\2\2")
        buf.write("w\u017a\3\2\2\2y\u0185\3\2\2\2{\u018b\3\2\2\2}\u0199\3")
        buf.write("\2\2\2\177\u01a5\3\2\2\2\u0081\u01a7\3\2\2\2\u0083\u01ab")
        buf.write("\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01b7\3\2\2\2\u0089")
        buf.write("\u01c0\3\2\2\2\u008b\u01ca\3\2\2\2\u008d\u008e\7}\2\2")
        buf.write("\u008e\4\3\2\2\2\u008f\u0090\7\177\2\2\u0090\6\3\2\2\2")
        buf.write("\u0091\u0092\7]\2\2\u0092\b\3\2\2\2\u0093\u0094\7_\2\2")
        buf.write("\u0094\n\3\2\2\2\u0095\u0096\7*\2\2\u0096\f\3\2\2\2\u0097")
        buf.write("\u0098\7+\2\2\u0098\16\3\2\2\2\u0099\u009a\7=\2\2\u009a")
        buf.write("\20\3\2\2\2\u009b\u009c\7<\2\2\u009c\22\3\2\2\2\u009d")
        buf.write("\u009e\7.\2\2\u009e\24\3\2\2\2\u009f\u00a0\7\60\2\2\u00a0")
        buf.write("\26\3\2\2\2\u00a1\u00a2\7<\2\2\u00a2\u00a3\7?\2\2\u00a3")
        buf.write("\30\3\2\2\2\u00a4\u00a5\7?\2\2\u00a5\32\3\2\2\2\u00a6")
        buf.write("\u00a7\7d\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7q\2\2\u00a9")
        buf.write("\u00aa\7n\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\34\3\2\2\2\u00ae\u00af\7d\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2")
        buf.write("\u00b3\7m\2\2\u00b3\36\3\2\2\2\u00b4\u00b5\7e\2\2\u00b5")
        buf.write("\u00b6\7n\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7u\2\2\u00b8")
        buf.write("\u00b9\7u\2\2\u00b9 \3\2\2\2\u00ba\u00bb\7e\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\"\3\2\2\2\u00c3\u00c4\7f\2\2\u00c4")
        buf.write("\u00c5\7q\2\2\u00c5$\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("&\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7z\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7f\2\2\u00d1\u00d2\7u\2\2\u00d2(\3\2\2\2\u00d3")
        buf.write("\u00d4\7h\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8*\3\2\2\2\u00d9")
        buf.write("\u00da\7k\2\2\u00da\u00db\7h\2\2\u00db,\3\2\2\2\u00dc")
        buf.write("\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df")
        buf.write(".\3\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7g\2\2\u00e2")
        buf.write("\u00e3\7y\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7u\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7i\2\2\u00ea\62\3\2\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee\7g\2\2\u00ee")
        buf.write("\u00ef\7p\2\2\u00ef\64\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1")
        buf.write("\u00f2\7q\2\2\u00f2\u00f3\7t\2\2\u00f3\66\3\2\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7v\2\2\u00f7")
        buf.write("\u00f8\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7p\2\2\u00fa")
        buf.write("8\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff:\3\2\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103")
        buf.write("\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105<\3\2\2\2\u0106")
        buf.write("\u0107\7x\2\2\u0107\u0108\7q\2\2\u0108\u0109\7k\2\2\u0109")
        buf.write("\u010a\7f\2\2\u010a>\3\2\2\2\u010b\u010c\7p\2\2\u010c")
        buf.write("\u010d\7k\2\2\u010d\u010e\7n\2\2\u010e@\3\2\2\2\u010f")
        buf.write("\u0110\7v\2\2\u0110\u0111\7j\2\2\u0111\u0112\7k\2\2\u0112")
        buf.write("\u0113\7u\2\2\u0113B\3\2\2\2\u0114\u0115\7h\2\2\u0115")
        buf.write("\u0116\7k\2\2\u0116\u0117\7p\2\2\u0117\u0118\7c\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119D\3\2\2\2\u011a\u011b\7u\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011c\u011d\7c\2\2\u011d\u011e\7v\2\2\u011e")
        buf.write("\u011f\7k\2\2\u011f\u0120\7e\2\2\u0120F\3\2\2\2\u0121")
        buf.write("\u0122\7v\2\2\u0122\u0123\7q\2\2\u0123H\3\2\2\2\u0124")
        buf.write("\u0125\7f\2\2\u0125\u0126\7q\2\2\u0126\u0127\7y\2\2\u0127")
        buf.write("\u0128\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7q\2\2\u012a")
        buf.write("J\3\2\2\2\u012b\u012c\7-\2\2\u012cL\3\2\2\2\u012d\u012e")
        buf.write("\7/\2\2\u012eN\3\2\2\2\u012f\u0130\7,\2\2\u0130P\3\2\2")
        buf.write("\2\u0131\u0132\7^\2\2\u0132R\3\2\2\2\u0133\u0134\7\'\2")
        buf.write("\2\u0134T\3\2\2\2\u0135\u0136\7\61\2\2\u0136V\3\2\2\2")
        buf.write("\u0137\u0138\7#\2\2\u0138X\3\2\2\2\u0139\u013a\7(\2\2")
        buf.write("\u013a\u013b\7(\2\2\u013bZ\3\2\2\2\u013c\u013d\7~\2\2")
        buf.write("\u013d\u013e\7~\2\2\u013e\\\3\2\2\2\u013f\u0140\7?\2\2")
        buf.write("\u0140\u0141\7?\2\2\u0141^\3\2\2\2\u0142\u0143\7#\2\2")
        buf.write("\u0143\u0144\7?\2\2\u0144`\3\2\2\2\u0145\u0146\7>\2\2")
        buf.write("\u0146b\3\2\2\2\u0147\u0148\7@\2\2\u0148d\3\2\2\2\u0149")
        buf.write("\u014a\7>\2\2\u014a\u014b\7?\2\2\u014bf\3\2\2\2\u014c")
        buf.write("\u014d\7@\2\2\u014d\u014e\7?\2\2\u014eh\3\2\2\2\u014f")
        buf.write("\u0150\7`\2\2\u0150j\3\2\2\2\u0151\u0153\t\2\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155l\3\2\2\2\u0156\u015a\5\25\13")
        buf.write("\2\u0157\u0159\t\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("n\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015f\t\3\2\2\u015e")
        buf.write("\u0160\t\4\2\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0162\3\2\2\2\u0161\u0163\t\2\2\2\u0162\u0161\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165p\3\2\2\2\u0166\u0168\t\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016a\u0170\3\2\2\2\u016b\u0171\5m\67\2")
        buf.write("\u016c\u016e\5m\67\2\u016d\u016c\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\5o8\2\u0170\u016b")
        buf.write("\3\2\2\2\u0170\u016d\3\2\2\2\u0171r\3\2\2\2\u0172\u0176")
        buf.write("\n\5\2\2\u0173\u0174\7^\2\2\u0174\u0176\t\6\2\2\u0175")
        buf.write("\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0176t\3\2\2\2\u0177")
        buf.write("\u0178\7^\2\2\u0178\u0179\n\6\2\2\u0179v\3\2\2\2\u017a")
        buf.write("\u017e\7$\2\2\u017b\u017d\5s:\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("\u0180\3\2\2\2\u017e\u017f\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017f\u0181\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7")
        buf.write("$\2\2\u0182\u0183\b<\2\2\u0183x\3\2\2\2\u0184\u0186\t")
        buf.write("\7\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018a\b=\3\2\u018az\3\2\2\2\u018b\u018c\7\61\2\2\u018c")
        buf.write("\u018d\7,\2\2\u018d\u0191\3\2\2\2\u018e\u0190\13\2\2\2")
        buf.write("\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0191\u018f\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0194\u0195\7,\2\2\u0195\u0196\7\61\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0198\b>\3\2\u0198|\3\2\2\2\u0199")
        buf.write("\u019d\7%\2\2\u019a\u019c\13\2\2\2\u019b\u019a\3\2\2\2")
        buf.write("\u019c\u019f\3\2\2\2\u019d\u019e\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a2")
        buf.write("\t\b\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a4\b?\3\2\u01a4~\3\2\2\2\u01a5\u01a6\t\2\2\2\u01a6")
        buf.write("\u0080\3\2\2\2\u01a7\u01a8\t\t\2\2\u01a8\u0082\3\2\2\2")
        buf.write("\u01a9\u01ac\5\u0081A\2\u01aa\u01ac\5\u0085C\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01b2\3\2\2\2\u01ad")
        buf.write("\u01b1\5\u0081A\2\u01ae\u01b1\5\177@\2\u01af\u01b1\5\u0085")
        buf.write("C\2\u01b0\u01ad\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u0084\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b6\7a\2\2\u01b6\u0086\3\2\2\2\u01b7\u01bb\7")
        buf.write("$\2\2\u01b8\u01ba\5s:\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\bD\4\2")
        buf.write("\u01bf\u0088\3\2\2\2\u01c0\u01c4\7$\2\2\u01c1\u01c3\5")
        buf.write("s:\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c7\u01c8\5u;\2\u01c8\u01c9\bE\5\2\u01c9")
        buf.write("\u008a\3\2\2\2\u01ca\u01cb\13\2\2\2\u01cb\u01cc\bF\6\2")
        buf.write("\u01cc\u008c\3\2\2\2\25\2\u0154\u015a\u015f\u0164\u0169")
        buf.write("\u016d\u0170\u0175\u017e\u0187\u0191\u019d\u01a1\u01ab")
        buf.write("\u01b0\u01b2\u01bb\u01c4\7\3<\2\b\2\2\3D\3\3E\4\3F\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LP = 1
    RP = 2
    LSB = 3
    RSB = 4
    LB = 5
    RB = 6
    SEMICOLON = 7
    COLON = 8
    COMMA = 9
    DOT = 10
    ASSIGN = 11
    CONST = 12
    BOOLEAN = 13
    BREAK = 14
    CLASS = 15
    CONTINUE = 16
    DO = 17
    ELSE = 18
    EXTENDS = 19
    FLOAT = 20
    IF = 21
    INT = 22
    NEW = 23
    STRING = 24
    THEN = 25
    FOR = 26
    RETURN = 27
    TRUE = 28
    FALSE = 29
    VOID = 30
    NIL = 31
    THIS = 32
    FINAL = 33
    STATIC = 34
    TO = 35
    DOWNTO = 36
    ADD = 37
    SUB = 38
    MUL = 39
    I_DIV = 40
    MOD = 41
    F_DIV = 42
    NOT = 43
    AND = 44
    OR = 45
    EQUAL = 46
    NOT_EQUAL = 47
    LESS_THAN = 48
    GREATER_THAN = 49
    LESS_THAN_EQ = 50
    GREATER_THAN_EQ = 51
    CONCAT = 52
    INTLIT = 53
    FLOATLIT = 54
    STRINGLIT = 55
    WS = 56
    BLOCK_CMT = 57
    LINE_CMT = 58
    ID = 59
    UND = 60
    UNCLOSED_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "':'", "','", 
            "'.'", "':='", "'='", "'boolean'", "'break'", "'class'", "'continue'", 
            "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'^'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMICOLON", "COLON", 
            "COMMA", "DOT", "ASSIGN", "CONST", "BOOLEAN", "BREAK", "CLASS", 
            "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
            "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
            "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", 
            "MUL", "I_DIV", "MOD", "F_DIV", "NOT", "AND", "OR", "EQUAL", 
            "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQ", "GREATER_THAN_EQ", 
            "CONCAT", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "BLOCK_CMT", 
            "LINE_CMT", "ID", "UND", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMICOLON", "COLON", 
                  "COMMA", "DOT", "ASSIGN", "CONST", "BOOLEAN", "BREAK", 
                  "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                  "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                  "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                  "TO", "DOWNTO", "ADD", "SUB", "MUL", "I_DIV", "MOD", "F_DIV", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "LESS_THAN_EQ", "GREATER_THAN_EQ", "CONCAT", 
                  "INTLIT", "DecimalPart", "ExponentPart", "FLOATLIT", "GET_STR", 
                  "ESC_ILLEGAL", "STRINGLIT", "WS", "BLOCK_CMT", "LINE_CMT", 
                  "DIGIT", "LETTER", "ID", "UND", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[58] = self.STRINGLIT_action 
            actions[66] = self.UNCLOSED_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	                self.text=str(self.text)

     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                raise IllegalEscape(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                                raise ErrorToken(self.text)

     


