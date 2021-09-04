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

program  		:STRINGLIT;// classdcls EOF;//VOIDTYPE 'main' LB RB stmBlock EOF ;

mptype			: INTTYPE | VOIDTYPE 				;

body			: funcall SEMI						;

//exp				: funcall | INTLIT 				;

funcall			: ID LB exp? RB 					;
classdcls       : classdcl classdcls| classdcl;
classdcl		: CLASS ID memBlock
				| CLASS ID EXTEND ID  memBlock  	;

memBlock		: LP memList RP
				| LP RP								;
memList			: classMember memList
				| classMember						;
classMember 	: attributeDeclare
                | methodDeclare			    		;



//ATTRIBUTE DCL
attributes		: attributeDeclare attributes
				|									;
attributeDeclare: attribute_type vartype attributeList SEMI;
attribute_type	: STATIC MUTABLE
				| MUTABLE STATIC
				| (STATIC | MUTABLE)
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
constructor		: ID paramDeclare stmBlock	;
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
arraytype			: primtype '[' size ']'			;
arrayLit		: LP elemList RP					;
elemList		: elem COMMA elemList
				| elem 								;
elem			: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT;
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
exp2			: NOT exp3
				| ADD|SUB exp3						    //sign expression
				| exp3								;
exp3			: exp4 '[' exps ']'                     //index
				| exp4								;
exp4			: exp5 DOT ID                           //member access
                | ID DOT ID
                | exp5 DOT ID explist
                | ID DOT ID explist
                | exp5                             ;
	//khong biet lam dot
exp5			: NEW ID explist                        //Object creation
				| operand							;
operand			: INTLIT | FLOATLIT |STRINGLIT | BOOLLIT | arrayLit//operand value
				| 'this' | 'nil'
				| ID                                ;


stmList	        : variables stms
		        | stms							    ;
variables	    : variable SEMI variables
		        | variable SEMI                     ;
variable	    : (MUTABLE)? vartype idList             //SEMI gom lại hay tách riêng
			    |								    ;
//idlist hay attributes
stms		    : stm SEMI stms
			    | stm SEMI						    ;
stm			    : lhs ':=' exp
			    | IF exp THEN stm
			    | IF exp THEN stm SEMI ELSE stm
			    | FOR scala_var ':=' exp1 (TO|DOWNTO) exp2 DO (stmBlock|stm SEMI)
			    | BREAK
			    | CONT
			    | RETURN exp
			    | ID DOT ID explist                 ;   //method invoke 5.6
scala_var       : ID                                ;
lhs             : ID | ID '.' ID
                | exp '.' ID | exp '[' exp ']'      ;



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
INTLIT		: [0-9]+	                ;
BOOLLIT		: 'true'|'false'            ;
FLOATLIT	: IntegerPart (DecimalPart | DecimalPart? ExponentPart);
fragment IntegerPart :  [0-9]+			;
fragment DecimalPart : 	'.'[0-9]*		;
fragment ExponentPart:	[Ee][+-]?[0-9]+	;
STRINGLIT	: '"'Char*?'"'              ;
fragment Char: SpecialChar | SpecialString;
fragment SpecialChar:~["\t\f\r\n\\]        ;
fragment SpecialString:'\\'[bfrnt\\] | '\\"' Char*? '\\"'   ;

LB			: '(' 		;
RB			: ')' 		;
LP			: '{'		;
RP			: '}'		;
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

LINECMT		: '#' .*? '\n' 	            -> skip	;
BLOCKCMT	: '/*'.*?'*/'	            -> skip	;
WS 			: [ \t\r\n]+ 	            -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;