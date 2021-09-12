/*
 Student name: Vo Hong Phuc
 Student Id: 1911881
 */

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  		: classdcls EOF                     ;

mptype			: INTTYPE | VOIDTYPE 				;

body			: funcall SEMI						;

//exp				: funcall | INTLIT 				;

funcall			: ID LB exp? RB 					;
classdcls       : classdcl classdcls| classdcl      ;
classdcl		: CLASS ID memBlock
				| CLASS ID EXTEND ID  memBlock  	;

memBlock		: LP memList RP
				| LP RP								;
memList			: classMember memList
				| classMember						;
classMember 	: attributeDeclare
                | methodDeclare			    		;

//Attribute Declaration
//attributes	: attributeDeclare attributes|	;
attributeDeclare: attribute_type vartype attributeList SEMI ;
attribute_type	: STATIC MUTABLE
				| MUTABLE STATIC
				| STATIC | MUTABLE
				|									;
vartype			: primtype | arraytype | classtype  ;
primtype		: INTTYPE | VOIDTYPE | FLOATTYPE
                | STRINGTYPE | BOOLTYPE             ;
classtype       : ID                                ;
attributeList	: attri COMMA attributeList
				| attri 							;
attri			: ID ASG exp	
				| ID								;

//METHOD DECLR
methodDeclare	: methodType returnType ID paramList stmBlock
				| constructor						;
constructor		: ID paramList stmBlock	            ;
methodType		: STATIC|							;
returnType		: vartype							;
stmBlock	    : LP stmList RP
				| LP RP								;
paramList   	: LB paramDeclare RB
            	| LB RB                   			;
paramDeclare   	: param SEMI paramDeclare
            	| param                  			;
param      	    : vartype idList             		;
idList      	: ID COMMA idList
            	| ID                      			;
//param được gán assign không??? được thì dùng attri=idlist

//ARRAY DCLR
arraytype		: primtype '[' size ']'			    ;
arrayLit		: LP elemList RP					;
elemList		: elem COMMA elemList
				| elem 								;
elem			: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT ;
size            : INTLIT                            ;
//assign problem

//EXPRESSION
explist			: LB exps RB | LB RB				;
exps			: exp COMMA exps
				|exp								;
exp				: exp1 (GT|LT|LEQ|GEQ) exp1			    //relational expression
                | exp1 (EQ|NEQ) exp1				    //relational expression
                | exp1                              ;
exp1            : exp2 (AND|OR) exp1				    //boolean expression
				| exp2 (ADD|SUB) exp1				    //arithemic expression
				| exp2 (MUL|FLOATDIV|INTDIV|MOD) exp1   //arithemic expression
				| exp2 CON exp1 					    //string expression
				| exp2								;
exp2			: NOT exp2
				| (ADD|SUB) exp2					    //sign expression
				| exp3								;
exp3			: exp3 '[' exp ']'                      //index
				| exp4								;
exp4			: methodInvoke | attriAccess | exp5 ;
exp5			: NEW ID explist                        //Object creation
				| operand						    ;
operand			: INTLIT | FLOATLIT |STRINGLIT | BOOLLIT | arrayLit //operand value
				| 'this' | 'nil'
				| ID | subexp                       ;
subexp          : LB exp RB                         ;
methodInvoke    : attriAccess DOT ID explist methodRecur
                | (exp5|ID) DOT ID explist methodRecur;
methodRecur     : DOT ID explist methodRecur |              ;
attriAccess     : (exp5|ID) DOT ID explist methodRecur DOT ID attriRecur
                | (exp5|ID) DOT ID attriRecur;
attriRecur      : DOT ID attriRecur|DOT ID explist methodRecur DOT ID attriRecur|                ;


stmList	        : variables stms
                | variables
		        | stms | 						    ;
variables	    : variable variables
		        | variable                          ;
variable	    : (MUTABLE)? vartype attributeList SEMI ;
//idlist hay attributes

stms		    : stm stms
			    | stm   						    ;
stm			    : lhs ASGOP exp SEMI
			    | IF exp THEN stm
			    | IF exp THEN stm ELSE stm
			    | FOR scala_var ASGOP exp1 (TO|DOWNTO) exp2 DO (stmBlock|stm)
			    | BREAK SEMI
			    | CONT SEMI
			    | RETURN exp SEMI
			    | methodInvoke SEMI                 ;   //method invoke 5.6
scala_var       : ID                                ;
lhs             : ID
                | attriAccess | exp4 '[' exp ']'    ;

CLASS		: 'class'	;
EXTEND		: 'extends'	;
NEW			: 'new'		;
SELF		: 'this'	;

STATIC		: 'static'	;
MUTABLE		: 'final'	;

INTTYPE		: 'int' 	;
VOIDTYPE	: 'void'  	;
FLOATTYPE	: 'float'	;
BOOLTYPE	: 'boolean'	;
STRINGTYPE	: 'string'	;


IF			: 'if'		;
ELSE		: 'else'	;
THEN		: 'then'	;
FOR			: 'for'		;
TO			: 'to'		;
DOWNTO		: 'downto'	;
DO			: 'do'		;
BREAK		: 'break'	;
CONT		: 'continue';
RETURN		: 'return'	;


LB			: '(' 		;
RB			: ')' 		;
LP			: '{'		;
RP			: '}'		;
SEMI		: ';' 		;
COLON		: ':'		;
COMMA		: ','		;
DOT			: '.'		;
ASGOP       : ':='      ;
ASG			: '='		;                   //:=
ADD			: '+'		;
SUB			: '-'		;
MUL			: '*'		;
FLOATDIV	: '/'		;
INTDIV		: '\\'		;
MOD			: '%'		;
NEQ			: '!='		;
EQ			: '=='		;
LT			: '<'		;
GT			: '>'		;
LEQ			: '<='		;
GEQ			: '>='		;
OR			: '||'		;
AND			: '&&'		;
NOT			: '!'		;
CON			: '^'		;


LINECMT		: '#' .*? ('\n'|EOF) 	    -> skip	;
BLOCKCMT	: '/*'.*?'*/'	            -> skip	;
WS 			: [ \t\r\n]+ 	            -> skip ; // skip spaces, tabs, newlines


fragment IntegerPart :  [0-9]+			;
fragment DecimalPart : 	'.'[0-9]*		;
fragment ExponentPart:	[Ee][+-]?[0-9]+	;
fragment Char		: ~["\\\r\n]  | EscapeStr;
fragment EscapeStr :  '\\'["bfrnt\\] ;
FLOATLIT	: IntegerPart (DecimalPart | DecimalPart? ExponentPart);
STRINGLIT	: '"'Char*?'"'              ;
INTLIT		: IntegerPart	                ;
BOOLLIT		: 'true'|'false'            ;
ID			: [a-zA-Z_][a-zA-Z0-9_]* 	;



ILLEGAL_ESCAPE  :	'"' Char* '\\' ~[bfnrt"\\]
                    {raise IllegalEscape(self.text[0:])};
UNCLOSE_STRING  :   '"' Char* ([\n\r]|EOF)
                    {
                    if self.text[-1] in ["\n","\r"] :
                        raise UncloseString(self.text[0:-1])
                    else: raise UncloseString(self.text[0:])};
ERROR_CHAR      :	.
                    {raise ErrorToken(self.text)};