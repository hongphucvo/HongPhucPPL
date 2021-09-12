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

program         :   class_declare+ EOF
                ;

class_declare   :   CLASS ID (EXTENDS ID)? LP members_declare* RP
                ;

members_declare :   attributes
                |   methods
                ;
 

attributes	    :   STATIC ? FINAL ? type_Type ID CONST? exp (COMMA ID CONST exp)* SEMICOLON
            	|   FINAL ? STATIC ? type_Type ID CONST? exp (COMMA ID CONST exp)* SEMICOLON
            	;

methods     	:   STATIC ? type_Type ? ID parameter_list block_statement
	            ;

parameter_list  :   LB para_list (SEMICOLON para_list)* RB
                |   LB RB
                ;

para_list       :   type_Type id_list
                ;

id_list         :   ID (COMMA ID)*
                ;

block_statement :   LP attributes* statements* RP
                ;

type_Type       :   primitive_type
                |   array_type
                |   class_type
                ;

primitive_type  :   INT | BOOLEAN | FLOAT | STRING
                ;

array_type      :   (primitive_type | class_type) LSB INTLIT RSB
                ;

class_type      :   ID
                ;

// --------------------- Expressions -------------------- //

exp             :   exp1 (LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ) exp1
                |   exp1
                ;

exp1            :   exp2 (NOT_EQUAL | EQUAL) exp2
                |   exp2
                ;

exp2            :   exp2 AND exp3
                |   exp2 OR exp3
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

exp7            :   ADD exp7
                |   SUB exp7
                |   exp8
                ;

exp8            :   exp9 LSB exp RSB
                |   exp9
                ;

exp9            :   exp9 DOT ID LB exp_list RB
                |   exp9 DOT ID LB RB
                |   exp9 DOT ID
                |   exp10
                ;

exp10           :   NEW ID LB exp_list? RB
                |   exp11
                ;

exp11           :   THIS | NIL | literal | ID
                |   LB exp RB
                ;

exp_list        :   exp (COMMA exp)*
                ;

literal         :   INTLIT | BOOLEANLIT | STRINGLIT | FLOATLIT | arraylit
                ;

// ---------------------- Statements ------------------------//

statements      :   block_statement | assign_stmt | if_stmt | for_stmt | break_stmt | continue_stmt
                |   return_stmt | method_stmt
                ;

assign_stmt     :   lhs ASSIGN exp SEMICOLON
                ;
lhs             :   ID
                |   exp DOT ID
                |   ID DOT ID
                |   exp LSB exp LSB
                ;

if_stmt         :   IF exp THEN statements (ELSE statements)?
                ;

for_stmt        :   FOR ID ASSIGN exp (TO | DOWNTO) exp DO statements
                ;

break_stmt      :   BREAK SEMICOLON
                ;

continue_stmt   :   CONTINUE SEMICOLON
                ;

return_stmt     :   RETURN exp? SEMICOLON
                ;

method_stmt     :   exp DOT ID LB exp_list? RB SEMICOLON
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


// Integer literal
INTLIT                  : [0-9]+;

// Float literal
FLOATLIT                : [0-9]+ (DecimalPart | DecimalPart? ExponentPart)
	                    ;
fragment DecimalPart    : DOT [0-9]*
	                    ;
fragment ExponentPart   : [Ee][+-]?[0-9]+
	                    ;

// Boolean literal
BOOLEANLIT              : TRUE
                        | FALSE
                        ;

// array literal
arraylit                :   LP exp_list RP
                        ;


// String literal
STRINGLIT           :   '"' GET_STR* '"' {
                    self.text = self.text[1:-1]
};

    
UNCLOSED_STRING     : '"' GET_STR* {
                    raise uncloseString(self.text[1:])
};

ILLEGAL_ESCAPE      : '"' GET_STR* ESC_ILLEGAL {
                    raise IllegalEscape(self.text[1:])
};

fragment GET_STR    : ~[\b\f\n\r\t"\\] | ('\\' [bfrnt"\\]);
fragment ESC_ILLEGAL:'\\' ~[bfrnt"\\] | '\\' ;

// Skip tokens
WS                  : [ \t\f\r\n]+                 -> skip; // skip spaces, tabs, newlines
BLOCK_CMT           : '/*' .*? '*/'                -> skip;
LINE_CMT            : '#' .*? ([\n] | EOF)         -> skip;
NEWLINE             : '\n'                         -> skip;

// Identifers
ID	:	[a-zA-Z_][a-zA-Z0-9_]*
    ;

ERROR_CHAR          : .{
                    raise ErrorToken(self.text)
};

