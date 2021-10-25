/*---1911881------------------*/
/*---Vo Hong Phuc-------------*/

grammar BKOOL;

@lexer::header {
from lexererr import *

}

options{
	language=Python3;
}

program  		: classdcls EOF                     ;
classdcls       : classdcl (classdcls|)             ;
classdcl		: CLASS ID (EXTEND ID|) memBlock    ;

memBlock		: LP memList RP
				| LP RP								;
memList			: classMember (memList|)            ;
classMember 	: attributeDeclare
                | methodDeclare			    		;

//Attribute Declaration
//attributes	: attributeDeclare attributes|	;
attributeDeclare: ((STATIC|) (IMMUTABLE|) | IMMUTABLE STATIC) vartype attributeList SEMI ;
vartype			: primtype | arraytype | classtype  ;
primtype		: INTTYPE | VOIDTYPE | FLOATTYPE
                | STRINGTYPE | BOOLTYPE             ;
classtype       : ID                                ;
attributeList	: attri (COMMA attributeList|)      ;
attri			: ID (ASG exp|)                     ;
idList      	: ID (COMMA idList|)                ;
//METHOD DECLR
methodDeclare	: ((STATIC|) vartype|) ID paramList stmBlock;
paramList   	: LB paramDeclare RB
            	| LB RB                   			;
paramDeclare   	: param (SEMI paramDeclare|)        ;
param      	    : vartype idList             		;
//param:vartyep attributeList;

//param được gán assign không??? được thì dùng attri=idlist
stmBlock	    : LP stmList RP
				| LP RP								;

//ARRAY DCLR
arraytype		: (primtype|classtype) '[' size ']'	;
arrayLit		: LP exps RP					;
size            : INTLIT                            ;
//assign problem

//EXPRESSION
explist			: LB exps RB | LB RB				;
exps			: exp COMMA exps
				| exp								;
exp				: exp1 (GT|LT|LEQ|GEQ) exp1|exp1	;		    //relational expression
exp1            : exp2 (EQ|NEQ) exp2| exp2  				;    //relational expression

exp2            : exp2 (AND|OR) exp3|exp3				 ;   //boolean expression
exp3			: exp3 CON exp4	|exp4				    ;//string expression
exp4			: exp4 (MUL|FLOATDIV|INTDIV|MOD) exp5   //arithemic expression
				| exp5								;
exp5			: exp5 (ADD|SUB) exp6|exp6			 ;   //arithemic expression
exp6			: NOT exp7|exp7                     ;
exp7			: (ADD|SUB) exp8					    //sign expression
				| exp8								;
exp8			: exp8 '[' exp ']'                      //index
				| exp9								;
exp9			: methodInvoke | attriAccess | exp10 ;
exp10			: NEW ID explist                        //Object creation
				| operand						    ;
operand			: arrayLit|INTLIT|FLOATLIT|BOOLLIT|STRINGLIT|ID  //operand value
				| SELF | NIL| subexp                       ;
subexp          : LB exp RB                         ;


methodInvoke    : (attriAccess|exp10|ID) DOT ID explist methodRecur;
methodRecur     : DOT ID explist methodRecur |      ;
attriAccess     : (exp10|ID) methodRecur DOT ID attriRecur;
attriRecur      : methodRecur DOT ID attriRecur|    ;


stmList	        : (variables|) (stms|)              ;
variables	    : variable (variables|)             ;
variable	    : (IMMUTABLE|) vartype attributeList SEMI;
//idlist hay attributes

stms		    : stm (stms|)                       ;
stm			    : stmBlock
                | lhs ASGOP exp SEMI
			    | (matchIF|unmatchIF)
			    | FOR scala_var ASGOP exp (TO|DOWNTO) exp DO stm
			    | (BREAK|CONT) SEMI
			    | RETURN exp SEMI
			    | methodCall                ;   //method invoke 5.6
methodCall		: (attriAccess|exp10|ID) DOT ID explist methodRecur SEMI;

matchIF:    IF exp THEN stm ELSE stm SEMI|;
unmatchIF:  IF exp THEN stm
            |IF exp THEN matchIF ELSE unmatchIF;

scala_var       : ID                                ;
lhs             : ID | attriAccess | exp9 '[' exp ']';

CLASS		: 'class'	;
EXTEND		: 'extends'	;
NEW			: 'new'		;
SELF		: 'this'	;
NIL			: 'nil'		;
STATIC		: 'static'	;
IMMUTABLE	: 'final'	;

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
ASG			: '='		;
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
WS 			: [ \t\r\n\f]+ 	            -> skip ; // skip spaces, tabs, newlines


fragment IntegerPart :  [0-9]+			;
fragment DecimalPart : 	'.'[0-9]*		;
fragment ExponentPart:	[Ee][+-]?[0-9]+	;
fragment Char		: ~["\\\r\n]  | EscapeStr;
fragment EscapeStr :  '\\'["bfrnt\\] ;
FLOATLIT	: IntegerPart (DecimalPart | DecimalPart? ExponentPart);
STRINGLIT	: '"'Char*?'"'              ;
INTLIT		: IntegerPart	            ;
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