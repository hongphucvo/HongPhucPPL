grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

@lexer::members {
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
}

program  		: mptype 'main' LB RB LP body? RP EOF ;

mptype			: INTTYPE | VOIDTYPE 				;

body			: funcall SEMI						;

//exp				: funcall | INTLIT 					;

funcall			: ID LB exp? RB 					;

classdcl		: CLASS ID memlist
				| CLASS ID EXTEND ID  memlist 	;

memlist			: LP mems RP
				| LP RP									;
mems			: mem mems
				| mem								;
mem 			: attribute|method					;



//ATTRIBUTE DCL
attributes		: attribute attributes
				|									;
attribute		: attribute_type vartype attrilist SEMI;
attribute_type	: STATIC MUTABLE
				| MUTABLE STATIC
				| (STATIC | MUTABLE)
				|									;
vartype			: primtype | array | ;//CLASSTYPE ;
primtype		: INTTYPE|VOIDTYPE|FLOATTYPE|STRINGTYPE|BOOLTYPE;

attrilist		: attri COMMA attrilist
				| attri 							;
attri			: ID ASG exp	
				| ID								;


//METHOD DECLR
method			: method_type return_type ID paramdcl block
				| constructor						;
constructor		: ID paramdcl block					; 
method_type		: STATIC|							;
return_type		: vartype							;
block			: LP statements RP
				| LP RP								;
paramdcl    	: LB paramlist RB                 
            	| LB RB                   			;
paramlist   	: params SEMI paramlist
            	| params                  			;
params      	: vartype idlist             		;
idlist      	: ID COMMA idlist
            	| ID                      			;
//param được gán assign không??? được thì dùng attri=idlist




//ARRAY DCLR
array			: primtype LSB INTLIT RSB			;
arraylit		: LP elemlist RP					;
elemlist		: elem COMMA elemlist
				| elem 								;
elem			: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT+;
//assign problem





//EXPRESSION
explist			: exps|								;
exps			: exp COMMA exps
				|exp								;
exp				: exp1 (GT|LT|LEQ|GEQ) exp1			//relational expression
				| exp1								;
exp1			: exp2 (EQ|NEQ) exp2					//relational expression			
				| exp2 (AND|OR) exp2				//boolean expression
				| exp2								;
exp2			: exp3 (ADD|SUB) exp2				//arithemic expression
				| exp3 (MUL|FLOATDIV|INTDIV|MOD) exp2//arithemic expression
				| exp3 CON exp2						//string expression
				| exp3								;
exp3			: NOT exp4
				| ADD|SUB exp4						//sign expression
				| exp4								;
exp4			: exp5 LSB exps RSB
				| exp5								;
exp5			:exp6 DOT ID
                 			| ID DOT ID
                 			| exp6 DOT ID LB explist RB
                 			| ID DOT ID LB explist RB
                 			| exp6                          ;
	//khong biet lam dot
exp6			: NEW ID LB exps RB
				| operand							;
operand			: INTLIT | FLOATLIT |STRINGLIT | BOOLLIT
				| 'this' | 'nil'
				| ID                                ;


//6. statement
statements	: variables stms
			| stms							;
variables	: variable SEMI variables
		    | variable SEMI                         ;
variable	: (MUTABLE)? vartype idlist                 //SEMI
			|									;			
//idlist hay attributes
stms		: stm SEMI stms
			| stm 								;
stm			: lhs ':=' exp
			| IF exp THEN stms					
			| IF exp THEN stms ELSE stms 			
			| FOR scala_var ':=' exp1 (TO|DOWNTO) exp2 DO stms
			| BREAK
			| CONT
			| RETURN exp
			| ;//method invoke 5.6
scala_var: ID;
lhs         : ID | ID LSB exp RSB               ;



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

ID			: [a-zA-Z|_][a-zA-Z0-9|_]* 	;
INTLIT		: [0-9]+	;
BOOLLIT		: 'true'|'false';
STRINGLIT	: '"'.*'"'	;
//ARRLIT		: LP (INTLIT+|FLOATLIT+|BOOLLIT+|STRINGLIT+) RB;
FLOATLIT	:	IntegerPart (DecimalPart | DecimalPart? ExponentPart);
fragment IntegerPart :  [0-9]+			;
fragment DecimalPart : 	'.'[0-9]*		;
fragment ExponentPart:	[Ee][+-]?[0-9]+	;

LB			: '(' 		;
RB			: ')' 		;
LP			: '{'		;
RP			: '}'		;
LSB			: '['		;
RSB			: ']'		;
SEMI		: ';' 		;
COLON		: ':'		;
COMMA		: ','		;
DOT			: '.'		;

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






LINECMT		: '#' .*? '\n' 	        -> skip	;
BLOCKCMT	: '/*' (~['*/'EOF])* '*/'	-> skip	;//eof????

WS 			: [ \t\r\n]+ 	-> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;