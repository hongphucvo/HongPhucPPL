/*
    Huynh Nhat Nam
    1810739
*/

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*-----------------------------------------------------------------------*/
/*------------------------------- Parser --------------------------------*/
/*-----------------------------------------------------------------------*/

//syntax

program             :   classList EOF
                    ;

classList           :   classDecl | classDecl classList
                    ;

classDecl           :   CLASS ID EXTENDS ID classBody
                    |   CLASS ID classBody
                    ;

classBody           :   LP membersList RP
                    |   LP RP
                    ;

membersList         :   member 
                    |   member membersList
                    ;

member              :   attributesDecl | methodDecl 
                    ;


// -------------------- Attributes -----------------------//

attributesDecl	    :   ((STATIC|) (FINAL|) | FINAL STATIC) typeDecl varDeclList SEMICOLON
//                    |   STATIC? FINAL? typeDecl varDeclList SEMICOLON
            	    ;


//---------------------- Methods -------------------------//

methodDecl     	:   STATIC ? typeDecl? ID paramMethod bodyMethod
	            ;

paramMethod     :   LB paramDeclList RB 
                |   LB RB 
                ;

paramDeclList   :   paramDecl 
                |   paramDecl SEMICOLON paramDeclList
                ;

paramDecl       :   typeDecl idList 
                ;

bodyMethod      :   blockStmt
                ;

//---------------------- Variable -------------------------//

varDeclMulList  :   varDecls 
                |   varDecls varDeclMulList
                ;

varDecls         :   FINAL? typeDecl varDeclList SEMICOLON
                ;

varDeclList     :   varList 
                |   varList COMMA varDeclList
                ;

varList         :   ID (CONST exp)?
                ;

//---------------------- Type -------------------------//

typeDecl        :   typeDecl LSB INTLIT RSB
                |   INT | FLOAT | BOOLEAN | STRING
                |   VOID
                |   ID
                ;

// ---------------------- Statements ------------------------//

listStatement   :   statements 
                |   statements listStatement
                ;

statements      :   blockStmt | assignStmt | ifStmt | forStmt | breakStmt 
                |   continueStmt | returnStmt | callStmt
                ;

blockStmt       :   LP varDeclMulList listStatement RP 
                |   LP varDeclMulList RP
                |   LP listStatement RP
                |   LP RP
                ;

assignStmt      :   lhs ASSIGN exp SEMICOLON
                ;

lhs             :   ID 
                |   exp9 DOT ID 
                |   exp9 LSB exp RSB
                ;


ifStmt          :   IF exp THEN statements
                |   IF exp THEN statements ELSE statements
                ;

forStmt         :   FOR condition DO statements
                ;

condition       :   ID ASSIGN exp (TO | DOWNTO) exp
                ;

breakStmt       :   BREAK SEMICOLON
                ;

continueStmt    :   CONTINUE SEMICOLON
                ;

returnStmt      :   RETURN exp SEMICOLON
                ;

callStmt        :   exp9 DOT ID LB expList RB SEMICOLON
                |   exp9 DOT ID LB RB SEMICOLON
                ;

// --------------------- Expressions -------------------- //

expList         :   exp COMMA expList
                |   exp 
                ;

exp             :   exp1 (LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ) exp1
                |   exp1
                ;

exp1            :   exp2 (NOT_EQUAL | EQUAL) exp2
                |   exp2
                ;

exp2            :   exp2 (AND | OR) exp3
                |   exp3
                ;

exp3            :   exp3 (ADD | SUB) exp4
                |   exp4
                ;

exp4            :   exp4 (MUL | I_DIV | F_DIV | MOD) exp5
                |   exp5
                ;

exp5            :   exp5 CONCAT exp6
                |   exp6
                ;

exp6            :   NOT exp6
                |   exp7
                ;

exp7            :   (ADD | SUB) exp7
                |   exp8
                ;

exp8            :   exp9 LSB exp RSB
                |   exp9
                ;

exp9            :   exp9 DOT ID LB expList RB
                |   exp9 DOT ID LB RB
                |   exp9 DOT ID
                |   exp10
                ;

exp10           :   NEW ID LB expList RB
                |   NEW ID LB RB
                |   exp11
                ;


exp11           :   literal | arrayLit
                |   THIS | NIL 
                |   ID | subexpression
                ;

subexpression   :   LB exp RB 
                ;



/*-----------------------------------------------------------------------*/
/*------------------------------- Lexer ---------------------------------*/
/*-----------------------------------------------------------------------*/

// Separators
LP          : '{';
RP          : '}';
LSB         : '[';
RSB         : ']';
LB          : '(';
RB          : ')';
SEMICOLON   : ';';
COLON       : ':';
COMMA       : ',';
DOT         : '.';

//	LEXER
ASSIGN			: ':=';
CONST			: '=';

// Keywords
BOOLEAN		: 'boolean';
BREAK 		: 'break';
CLASS		: 'class';
CONTINUE	: 'continue';
DO 			: 'do';
ELSE		: 'else';
EXTENDS		: 'extends';
FLOAT 		: 'float';
IF			: 'if';
INT         : 'int';
NEW 		: 'new';
STRING 		: 'string';
THEN		: 'then';
FOR 		: 'for';
RETURN		: 'return';
TRUE		: 'true';
FALSE		: 'false';
VOID 		: 'void';
NIL 		: 'nil';
THIS 		: 'this';
FINAL 		: 'final';
STATIC 		: 'static';
TO 			: 'to';
DOWNTO 		: 'downto';

//SHAPE       : 'Shape';

// Operators
ADD                 : '+' ;
SUB                 : '-' ;
MUL                 : '*' ;
I_DIV               : '\\' ;
MOD  		        : '%' ;
F_DIV               : '/' ;

NOT                 : '!' ;
AND                 : '&&' ;
OR   	            : '||' ;

EQUAL               : '==' ;
NOT_EQUAL           : '!=' ;
LESS_THAN           : '<' ;
GREATER_THAN        : '>' ;
LESS_THAN_EQ        : '<=' ;
GREATER_THAN_EQ     : '>=' ;
CONCAT 				: '^' ;


// Literal
literalList     :    literal | literal COMMA literalList
                ;
literal         :    INTLIT | FLOATLIT | booleanlit | STRINGLIT
                ;

// idList 
idList          :   ID
                |   ID COMMA idList
                ;

// Integer literal
INTLIT          :   [0-9]+;

arrayLit        :   LP expList RP
                ;


// Float literal
fragment DecimalPart    : DOT [0-9]*
	                    ;
fragment ExponentPart   : [Ee][+-]?[0-9]+
	                    ;
FLOATLIT                : [0-9]+ (DecimalPart | DecimalPart? ExponentPart)
	                    ;

// Boolean literal
booleanlit              : TRUE | FALSE
                        ;

// String literal
fragment GET_STR    : ~["\n\\] | '\\' [bfrnt"\\];
fragment ESC_ILLEGAL:'\\' ~[bfrnt"\\] ;

STRINGLIT           :   '"' GET_STR*? '"'{
	                self.text=str(self.text)
};
// Skip tokens
WS                  : [ \t\f\r\n]+                 -> skip; // skip spaces, tabs, newlines
BLOCK_CMT           : '/*' .*? '*/'                -> skip;
LINE_CMT            : '#' .*? ([\n] | EOF)         -> skip;

// Identifers
fragment DIGIT      :   [0-9];
fragment LETTER     :   [a-zA-Z];
ID                  :   (LETTER | UND) (LETTER | DIGIT | UND)*;
UND                 :   '_';

UNCLOSED_STRING     : '"' GET_STR* {
                    raise UncloseString(self.text)
};

ILLEGAL_ESCAPE      : '"' GET_STR*? ESC_ILLEGAL {
                    raise IllegalEscape(self.text)
};

ERROR_CHAR          : .{
                    raise ErrorToken(self.text)
};

