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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\5\7\u00a4\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\7\n\u00ae\n\n\f\n\16\n\u00b1\13\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\7\13\u00b9\n\13\f\13\16\13\u00bc\13\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\6*\u010c\n*\r*\16*\u010d\3+\3+\3+\7+\u0113")
        buf.write("\n+\f+\16+\u0116\13+\5+\u0118\n+\3+\3+\5+\u011c\n+\3+")
        buf.write("\3+\3+\3+\3+\7+\u0123\n+\f+\16+\u0126\13+\3+\3+\5+\u012a")
        buf.write("\n+\3+\5+\u012d\n+\5+\u012f\n+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u013a\n,\3-\3-\7-\u013e\n-\f-\16-\u0141\13-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\39\39\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\7=\u019a\n=\f=\16=\u019d\13=\3>\6>\u01a0")
        buf.write("\n>\r>\16>\u01a1\3>\3>\3?\3?\3?\3@\3@\7@\u01ab\n@\f@\16")
        buf.write("@\u01ae\13@\3@\5@\u01b1\n@\3@\3@\3A\3A\7A\u01b7\nA\fA")
        buf.write("\16A\u01ba\13A\3A\3A\3A\3\u00ba\2B\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\2\17\2\21\2\23\b\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-")
        buf.write("_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>")
        buf.write("\u0081?\3\2\f\5\2\f\f$$^^\t\2$$^^ddhhppttvv\3\2\f\f\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\16\17\"\"\3\3\f\f\2\u01cb\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2")
        buf.write("\2\2\5\u0087\3\2\2\2\7\u008c\3\2\2\2\t\u0094\3\2\2\2\13")
        buf.write("\u009a\3\2\2\2\r\u00a3\3\2\2\2\17\u00a5\3\2\2\2\21\u00a8")
        buf.write("\3\2\2\2\23\u00ab\3\2\2\2\25\u00b4\3\2\2\2\27\u00c2\3")
        buf.write("\2\2\2\31\u00c4\3\2\2\2\33\u00c6\3\2\2\2\35\u00c8\3\2")
        buf.write("\2\2\37\u00ca\3\2\2\2!\u00cc\3\2\2\2#\u00ce\3\2\2\2%\u00d1")
        buf.write("\3\2\2\2\'\u00d4\3\2\2\2)\u00d6\3\2\2\2+\u00d8\3\2\2\2")
        buf.write("-\u00db\3\2\2\2/\u00de\3\2\2\2\61\u00e1\3\2\2\2\63\u00e3")
        buf.write("\3\2\2\2\65\u00e5\3\2\2\2\67\u00e8\3\2\2\29\u00eb\3\2")
        buf.write("\2\2;\u00ed\3\2\2\2=\u00f1\3\2\2\2?\u00f6\3\2\2\2A\u00f8")
        buf.write("\3\2\2\2C\u00fa\3\2\2\2E\u00fc\3\2\2\2G\u00fe\3\2\2\2")
        buf.write("I\u0100\3\2\2\2K\u0102\3\2\2\2M\u0104\3\2\2\2O\u0106\3")
        buf.write("\2\2\2Q\u0108\3\2\2\2S\u010b\3\2\2\2U\u012e\3\2\2\2W\u0139")
        buf.write("\3\2\2\2Y\u013b\3\2\2\2[\u0144\3\2\2\2]\u014b\3\2\2\2")
        buf.write("_\u0151\3\2\2\2a\u0155\3\2\2\2c\u015d\3\2\2\2e\u0160\3")
        buf.write("\2\2\2g\u0165\3\2\2\2i\u016a\3\2\2\2k\u016e\3\2\2\2m\u0171")
        buf.write("\3\2\2\2o\u0178\3\2\2\2q\u017b\3\2\2\2s\u0181\3\2\2\2")
        buf.write("u\u018a\3\2\2\2w\u0190\3\2\2\2y\u0197\3\2\2\2{\u019f\3")
        buf.write("\2\2\2}\u01a5\3\2\2\2\177\u01a8\3\2\2\2\u0081\u01b4\3")
        buf.write("\2\2\2\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086")
        buf.write("\7v\2\2\u0086\4\3\2\2\2\u0087\u0088\7x\2\2\u0088\u0089")
        buf.write("\7q\2\2\u0089\u008a\7k\2\2\u008a\u008b\7f\2\2\u008b\6")
        buf.write("\3\2\2\2\u008c\u008d\7d\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7n\2\2\u0090\u0091\7g\2\2\u0091\u0092")
        buf.write("\7c\2\2\u0092\u0093\7p\2\2\u0093\b\3\2\2\2\u0094\u0095")
        buf.write("\7h\2\2\u0095\u0096\7n\2\2\u0096\u0097\7q\2\2\u0097\u0098")
        buf.write("\7c\2\2\u0098\u0099\7v\2\2\u0099\n\3\2\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7v\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7i\2\2\u00a0\f")
        buf.write("\3\2\2\2\u00a1\u00a4\n\2\2\2\u00a2\u00a4\5\17\b\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\16\3\2\2\2\u00a5")
        buf.write("\u00a6\7^\2\2\u00a6\u00a7\t\3\2\2\u00a7\20\3\2\2\2\u00a8")
        buf.write("\u00a9\7^\2\2\u00a9\u00aa\n\3\2\2\u00aa\22\3\2\2\2\u00ab")
        buf.write("\u00af\7%\2\2\u00ac\u00ae\n\4\2\2\u00ad\u00ac\3\2\2\2")
        buf.write("\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3")
        buf.write("\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3")
        buf.write("\b\n\2\2\u00b3\24\3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b6")
        buf.write("\7,\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9\13\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bd\u00be\7,\2\2\u00be\u00bf\7\61\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\u00c1\b\13\2\2\u00c1\26\3\2\2\2\u00c2\u00c3")
        buf.write("\7-\2\2\u00c3\30\3\2\2\2\u00c4\u00c5\7/\2\2\u00c5\32\3")
        buf.write("\2\2\2\u00c6\u00c7\7,\2\2\u00c7\34\3\2\2\2\u00c8\u00c9")
        buf.write("\7\61\2\2\u00c9\36\3\2\2\2\u00ca\u00cb\7^\2\2\u00cb \3")
        buf.write("\2\2\2\u00cc\u00cd\7\'\2\2\u00cd\"\3\2\2\2\u00ce\u00cf")
        buf.write("\7~\2\2\u00cf\u00d0\7~\2\2\u00d0$\3\2\2\2\u00d1\u00d2")
        buf.write("\7(\2\2\u00d2\u00d3\7(\2\2\u00d3&\3\2\2\2\u00d4\u00d5")
        buf.write("\7#\2\2\u00d5(\3\2\2\2\u00d6\u00d7\7?\2\2\u00d7*\3\2\2")
        buf.write("\2\u00d8\u00d9\7<\2\2\u00d9\u00da\7?\2\2\u00da,\3\2\2")
        buf.write("\2\u00db\u00dc\7#\2\2\u00dc\u00dd\7?\2\2\u00dd.\3\2\2")
        buf.write("\2\u00de\u00df\7?\2\2\u00df\u00e0\7?\2\2\u00e0\60\3\2")
        buf.write("\2\2\u00e1\u00e2\7>\2\2\u00e2\62\3\2\2\2\u00e3\u00e4\7")
        buf.write("@\2\2\u00e4\64\3\2\2\2\u00e5\u00e6\7>\2\2\u00e6\u00e7")
        buf.write("\7?\2\2\u00e7\66\3\2\2\2\u00e8\u00e9\7@\2\2\u00e9\u00ea")
        buf.write("\7?\2\2\u00ea8\3\2\2\2\u00eb\u00ec\7`\2\2\u00ec:\3\2\2")
        buf.write("\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7")
        buf.write("y\2\2\u00f0<\3\2\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7")
        buf.write("j\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7u\2\2\u00f5>\3\2")
        buf.write("\2\2\u00f6\u00f7\7*\2\2\u00f7@\3\2\2\2\u00f8\u00f9\7+")
        buf.write("\2\2\u00f9B\3\2\2\2\u00fa\u00fb\7}\2\2\u00fbD\3\2\2\2")
        buf.write("\u00fc\u00fd\7\177\2\2\u00fdF\3\2\2\2\u00fe\u00ff\7]\2")
        buf.write("\2\u00ffH\3\2\2\2\u0100\u0101\7_\2\2\u0101J\3\2\2\2\u0102")
        buf.write("\u0103\7=\2\2\u0103L\3\2\2\2\u0104\u0105\7<\2\2\u0105")
        buf.write("N\3\2\2\2\u0106\u0107\7.\2\2\u0107P\3\2\2\2\u0108\u0109")
        buf.write("\7\60\2\2\u0109R\3\2\2\2\u010a\u010c\t\5\2\2\u010b\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010eT\3\2\2\2\u010f\u0117\5S*\2\u0110")
        buf.write("\u0114\7\60\2\2\u0111\u0113\t\5\2\2\u0112\u0111\3\2\2")
        buf.write("\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0117")
        buf.write("\u0110\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011b\t\6\2\2\u011a\u011c\t\7\2\2\u011b\u011a\3")
        buf.write("\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\5S*\2\u011e\u012f\3\2\2\2\u011f\u0120\5S*\2\u0120\u0124")
        buf.write("\7\60\2\2\u0121\u0123\t\5\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u012c\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0129\t")
        buf.write("\6\2\2\u0128\u012a\t\7\2\2\u0129\u0128\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\5S*\2\u012c\u0127")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e")
        buf.write("\u010f\3\2\2\2\u012e\u011f\3\2\2\2\u012fV\3\2\2\2\u0130")
        buf.write("\u0131\7v\2\2\u0131\u0132\7t\2\2\u0132\u0133\7w\2\2\u0133")
        buf.write("\u013a\7g\2\2\u0134\u0135\7h\2\2\u0135\u0136\7c\2\2\u0136")
        buf.write("\u0137\7n\2\2\u0137\u0138\7u\2\2\u0138\u013a\7g\2\2\u0139")
        buf.write("\u0130\3\2\2\2\u0139\u0134\3\2\2\2\u013aX\3\2\2\2\u013b")
        buf.write("\u013f\7$\2\2\u013c\u013e\5\r\7\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143")
        buf.write("\7$\2\2\u0143Z\3\2\2\2\u0144\u0145\7t\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146\u0147\7v\2\2\u0147\u0148\7w\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7p\2\2\u014a\\\3\2\2\2\u014b\u014c")
        buf.write("\7e\2\2\u014c\u014d\7n\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7u\2\2\u014f\u0150\7u\2\2\u0150^\3\2\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7k\2\2\u0153\u0154\7n\2\2\u0154`\3")
        buf.write("\2\2\2\u0155\u0156\7g\2\2\u0156\u0157\7z\2\2\u0157\u0158")
        buf.write("\7v\2\2\u0158\u0159\7g\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7f\2\2\u015b\u015c\7u\2\2\u015cb\3\2\2\2\u015d\u015e")
        buf.write("\7k\2\2\u015e\u015f\7h\2\2\u015fd\3\2\2\2\u0160\u0161")
        buf.write("\7v\2\2\u0161\u0162\7j\2\2\u0162\u0163\7g\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164f\3\2\2\2\u0165\u0166\7g\2\2\u0166\u0167")
        buf.write("\7n\2\2\u0167\u0168\7u\2\2\u0168\u0169\7g\2\2\u0169h\3")
        buf.write("\2\2\2\u016a\u016b\7h\2\2\u016b\u016c\7q\2\2\u016c\u016d")
        buf.write("\7t\2\2\u016dj\3\2\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7q\2\2\u0170l\3\2\2\2\u0171\u0172\7f\2\2\u0172\u0173")
        buf.write("\7q\2\2\u0173\u0174\7y\2\2\u0174\u0175\7p\2\2\u0175\u0176")
        buf.write("\7v\2\2\u0176\u0177\7q\2\2\u0177n\3\2\2\2\u0178\u0179")
        buf.write("\7f\2\2\u0179\u017a\7q\2\2\u017ap\3\2\2\2\u017b\u017c")
        buf.write("\7d\2\2\u017c\u017d\7t\2\2\u017d\u017e\7g\2\2\u017e\u017f")
        buf.write("\7c\2\2\u017f\u0180\7m\2\2\u0180r\3\2\2\2\u0181\u0182")
        buf.write("\7e\2\2\u0182\u0183\7q\2\2\u0183\u0184\7p\2\2\u0184\u0185")
        buf.write("\7v\2\2\u0185\u0186\7k\2\2\u0186\u0187\7p\2\2\u0187\u0188")
        buf.write("\7w\2\2\u0188\u0189\7g\2\2\u0189t\3\2\2\2\u018a\u018b")
        buf.write("\7h\2\2\u018b\u018c\7k\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7c\2\2\u018e\u018f\7n\2\2\u018fv\3\2\2\2\u0190\u0191")
        buf.write("\7u\2\2\u0191\u0192\7v\2\2\u0192\u0193\7c\2\2\u0193\u0194")
        buf.write("\7v\2\2\u0194\u0195\7k\2\2\u0195\u0196\7e\2\2\u0196x\3")
        buf.write("\2\2\2\u0197\u019b\t\b\2\2\u0198\u019a\t\t\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019cz\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u01a0\t\n\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a4\b>\2\2\u01a4|\3\2\2\2\u01a5\u01a6\13")
        buf.write("\2\2\2\u01a6\u01a7\b?\3\2\u01a7~\3\2\2\2\u01a8\u01ac\7")
        buf.write("$\2\2\u01a9\u01ab\5\r\7\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1\t\13\2")
        buf.write("\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write("\b@\4\2\u01b3\u0080\3\2\2\2\u01b4\u01b8\7$\2\2\u01b5\u01b7")
        buf.write("\5\r\7\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01bb\u01bc\5\21\t\2\u01bc\u01bd")
        buf.write("\bA\5\2\u01bd\u0082\3\2\2\2\25\2\u00a3\u00af\u00ba\u010d")
        buf.write("\u0114\u0117\u011b\u0124\u0129\u012c\u012e\u0139\u013f")
        buf.write("\u019b\u01a1\u01ac\u01b0\u01b8\6\b\2\2\3?\2\3@\3\3A\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    BOOLTYPE = 3
    FLOATTYPE = 4
    STRINGTYPE = 5
    LINE_CMT = 6
    BLOCK_CMT = 7
    ADD = 8
    SUB = 9
    MUL = 10
    FLOATDIV = 11
    INTDIV = 12
    MOD = 13
    OR = 14
    AND = 15
    NOT = 16
    EQUAL = 17
    ASSIGN = 18
    NOTEQ = 19
    EQ = 20
    LESS = 21
    GREATER = 22
    LESSOREQ = 23
    GREATEROREQ = 24
    CONCAT = 25
    NEW = 26
    THIS = 27
    LB = 28
    RB = 29
    LP = 30
    RP = 31
    LSB = 32
    RSB = 33
    SEMI = 34
    COLON = 35
    COMMA = 36
    DOT = 37
    INTLIT = 38
    FLOATLIT = 39
    BOOLLIT = 40
    STRINGLIT = 41
    RETURN = 42
    CLASS = 43
    NIL = 44
    EXTENDS = 45
    IF = 46
    THEN = 47
    ELSE = 48
    FOR = 49
    TO = 50
    DOWNTO = 51
    DO = 52
    BREAK = 53
    CONTINUE = 54
    FINAL = 55
    STATIC = 56
    ID = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'boolean'", "'float'", "'string'", "'+'", 
            "'-'", "'*'", "'/'", "'\\'", "'%'", "'||'", "'&&'", "'!'", "'='", 
            "':='", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'^'", 
            "'new'", "'this'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "':'", "','", "'.'", "'return'", "'class'", "'nil'", 
            "'extends'", "'if'", "'then'", "'else'", "'for'", "'to'", "'downto'", 
            "'do'", "'break'", "'continue'", "'final'", "'static'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", "STRINGTYPE", 
            "LINE_CMT", "BLOCK_CMT", "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", 
            "MOD", "OR", "AND", "NOT", "EQUAL", "ASSIGN", "NOTEQ", "EQ", 
            "LESS", "GREATER", "LESSOREQ", "GREATEROREQ", "CONCAT", "NEW", 
            "THIS", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COLON", 
            "COMMA", "DOT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "RETURN", "CLASS", "NIL", "EXTENDS", "IF", "THEN", "ELSE", "FOR", 
            "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", "FINAL", "STATIC", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", "STRINGTYPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "LINE_CMT", "BLOCK_CMT", 
                  "ADD", "SUB", "MUL", "FLOATDIV", "INTDIV", "MOD", "OR", 
                  "AND", "NOT", "EQUAL", "ASSIGN", "NOTEQ", "EQ", "LESS", 
                  "GREATER", "LESSOREQ", "GREATEROREQ", "CONCAT", "NEW", 
                  "THIS", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", 
                  "COLON", "COMMA", "DOT", "INTLIT", "FLOATLIT", "BOOLLIT", 
                  "STRINGLIT", "RETURN", "CLASS", "NIL", "EXTENDS", "IF", 
                  "THEN", "ELSE", "FOR", "TO", "DOWNTO", "DO", "BREAK", 
                  "CONTINUE", "FINAL", "STATIC", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		text = str(self.text)
            		if text[-1] == '\n':
            			raise UncloseString(text[0:-1])
            		else:
            			raise UncloseString(text[0:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		text = str(self.text)
            		raise IllegalEscape(text[0:])
            	
     


