// My ID: 1912700

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: classdecl+ EOF;  

/*classdecl: CLASS ID (EXTENDS ID)? LP memberlist* RP;

memberlist: attribute | method;*/

classdecl: CLASS ID (EXTENDS ID)? LP memberlist RP;

member: attribute | method;
memberlist: member membertail |;
membertail: member membertail |;

// attribute declaration
/*attribute: STATIC? alltype vardecllist SEMI
		| (FINAL STATIC | FINAL | STATIC FINAL) alltype constdecllist SEMI;

vardecl: ID (EQUAL expr)?;
vardecllist: vardecl (COMMA vardecllist)*;

constdecl: ID EQUAL expr;
constdecllist: constdecl (COMMA constdecllist)*;*/
attribute: STATIC? FINAL? alltype attdecllist SEMI
		| FINAL STATIC alltype attdecllist SEMI;

attdecl: ID (EQUAL expr)?;
attdecllist: attdecl (COMMA attdecllist)*;

// method declaration
method: STATIC? alltype ID LB paraml RB blockstatement 
		| ID LB paraml RB blockstatement;

//paraml: param (SEMI param)* |;
paraml: param paramtail |;
paramtail: SEMI param paramtail |;
param: alltype attdecllist;
//param: alltype ID (COMMA ID)*;
// type
alltype: pctype | arraytype; // ID is class type
pctype: INTTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE | VOIDTYPE | ID;
arraytype: pctype LSB INTLIT RSB;
INTTYPE: 'int' ;
VOIDTYPE: 'void'  ;
BOOLTYPE: 'boolean' ;
FLOATTYPE: 'float' ;
STRINGTYPE: 'string' ;

// character set
fragment STR_CHAR: ~[\n"\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"\\];

// comments
LINE_CMT : '#' ~[\n]* -> skip ;
BLOCK_CMT: '/*' .*? '*/' -> skip ;

// 5. EXPRESSION
// expression list
expl: expr explist | ;
explist: COMMA expr explist | ;

// define expression
expr: expr2 (LESS | GREATER | LESSOREQ | GREATEROREQ) expr2 | expr2;
expr2: expr1 (EQ | NOTEQ) expr1 | expr1;
expr1: <assoc=right> NEW ID LB expl RB
	| expr1 DOT ID (LB expl RB)?
	| expr1 LSB expr RSB
	| <assoc=right> (ADD | SUB) expr1
	| <assoc=right> NOT expr1
	| expr1 CONCAT expr1
	| expr1 (MUL | FLOATDIV | INTDIV | MOD) expr1
	| expr1 (ADD | SUB) expr1
	| expr1 (AND | OR) expr1
	| operand;
operand: literals | THIS | ID | NIL | LB expr RB;
// 5.1 Arithmetic expression
ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
FLOATDIV: '/' ;
INTDIV: '\\' ;
MOD: '%' ;
// 5.2 Boolean expression
OR: '||';
AND: '&&';
NOT: '!';
// 5.3 Relational expression
EQUAL: '=';
ASSIGN: ':=';
NOTEQ: '!=';
EQ: '==';
LESS: '<';
GREATER: '>';
LESSOREQ: '<=';
GREATEROREQ: '>=';
// 5.4 String expression
CONCAT: '^';
// 5.5 Index expression
index: expr LSB expr RSB;
// 5.6 Member access
method_access: expr DOT ID LB expl RB;
att_access: expr DOT ID;
//tail: (DOT ID (LB expl RB)*)*;  
// 5.7 Object creation
NEW: 'new';
// 5.8 This
THIS: 'this';

// 6. STATEMENT
statement: blockstatement | insidestatement;
blockstatement: LP decllist statementlist RP;
insidestatement: assign_stm | if_stm | for_stm | break_stm | continue_stm | return_stm | method_stm;
decllist: decl_stm decltail |;
decltail: decl_stm decltail |;
statementlist: statement statementtail |;
statementtail: statement statementtail |;

// 6.1 Block statement
/*decl_stm: FINAL? (ptype | arraytype) vardecllist SEMI
		| FINAL? ID objectlist SEMI;*/
decl_stm: FINAL? alltype attdecllist SEMI;
// 6.2 Assignment statement
assign_stm: (ID | index | att_access) ASSIGN expr SEMI;
// 6.3 If statement
if_stm: IF expr THEN statement (ELSE statement)?;
// 6.4 For statement
for_stm: FOR ID ASSIGN expr (TO|DOWNTO) expr DO statement;
// 6.5 Break statement
break_stm: BREAK SEMI;
// 6.6 Continue statement
continue_stm: CONTINUE SEMI;
// 6.7 Return statement
return_stm: RETURN expr SEMI;
// 6.8 Method Invocation statement
method_stm: expr DOT ID LB expl RB SEMI;

// seperator
LB: '(' ;
RB: ')' ;

LP: '{';
RP: '}';

LSB: '[';
RSB: ']';

SEMI: ';' ;
COLON: ':';
COMMA: ',';
DOT: '.';

// literal
INTLIT: [0-9]+;
FLOATLIT: INTLIT ('.' [0-9]*)? [eE][+-]?INTLIT
		| INTLIT '.' [0-9]* ([eE][+-]?INTLIT)?;
BOOLLIT: 'true' | 'false';
STRINGLIT: '"' STR_CHAR*'"';
arraylit: LP literals (COMMA literals)* RP;
literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;

// key words
RETURN: 'return';
CLASS: 'class'; //class type
NIL: 'nil'; // value of an uninitialized variable in class type
EXTENDS: 'extends'; // inheritance

// if statement
IF: 'if';
THEN: 'then';
ELSE: 'else';

// loop statement
FOR: 'for';
TO: 'to';
DOWNTO: 'downto';
DO: 'do';
BREAK: 'break';
CONTINUE: 'continue';

// variable declaration
FINAL: 'final';
STATIC: 'static';

// identifier
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// skip spaces, tabs, newlines
WS : [ \t\r\n\f]+ -> skip ; 

//error
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ('\n'| EOF)
	{
		text = str(self.text)
		if text[-1] == '\n':
			raise UncloseString(text[0:-1])
		else:
			raise UncloseString(text[0:])
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		text = str(self.text)
		raise IllegalEscape(text[0:])
	}
	;



