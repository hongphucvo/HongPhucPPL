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

exp				: funcall | INTLIT 					;

funcall			: ID LB exp? RB 					;

classdcl		: CLASS ID LP memlist RP
				| CLASS ID EXTEND ID LP memlist RP	;

memlist			: mems 
				|									;
mems			: mem mems
				| mem								;
mem 			: attribute|method					;

attribute		: attribute_type vartype attrilist SEMI;
attribute_type	: STATIC MUTABLE
				| MUTABLE STATIC
				| (STATIC | MUTABLE)
				|									;
vartype			: primtype | array | CLASSTYPE ;
primtype		:INTTYPE|VOIDTYPE|FLOATTYPE|STRINGTYPE|BOOLTYPE;
array			: primtype LSB INTLIT RSB			;
attrilist		: attri COMMA attrilist
				| attri 							;
attri			: ID ASG exp	
				| ID								;

method			: method_type return_type ID paramdcl block	
				| constructor						;
constructor		: ID paramdcl block					; 
method_type		: STATIC|							;
return_type		:;// section4							;
block			:;// section6							;
paramdcl    	: LB paramlist RB                 
            	| LB RB                   		;
paramlist   	: params SEMI paramlist
            	| params                  		;
params      	: vartype idlist             		;
idlist      	: ID COMMA idlist
            	| ID                      		;
//param được gán assign không??? được thì dùng attri=idlist

cmt				: blockcmt | linecmt				;
linecmt			: '#' cmttext '\n'					;
blockcmt		: '/*' cmttext '*/'					;
cmttext			: .*								;


/*
memstatic	: STATIC memmutable
			| memmutable			;		;
memmutable	: FINAL mem3			
			| mem3					;
mem3		:						;

*/










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

ID			: [a-zA-Z|_][a-zA-Z0-9|_]* ;
INTLIT		: [0-9]+	;
FLOATLIT	: [+-]?		;
BOOLLIT		: 'true'|'false';
STRINGLIT	: '"'.*'"'	;
ARRLIT		: LP (INTLIT+|FLOATLIT+|BOOLLIT+|STRINGLIT+) RB;

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
INEQ		: '!='		;
EQ			: '=='		;
LT			: '<'		;
GT			: '>'		;
LEQ			: '<='		;
GEQ			: '>='		;
OR			: '||'		;
AND			: '&'		;
NOT			: '!'		;
CON			: '^'		;
WS 			: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;