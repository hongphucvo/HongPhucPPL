grammar BKIT;

@lexer::header {
from lexererr import *
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

options{
	language=Python3;
}

program  : declaration EOF ;

ID:         [a-xA-Z]+;
INT:        'int';
FLOAT:      'float';
INTVAL:     [+-][0-9]+;
FLOATVAL:   [+-]'.'[0-9]+;
LB:         '(';
RB:         ')';
LCB:        '{';
RCB:        '}';
ASGOP:      '=';
COMMA:      ',';
ADDOP:      '+';
SUBOP:      '-';
MULOP:      '*';
DIVOP:      '/';
SEMI:       ';';
COLON:      ':';
VAR:        'Var';
RETURN:     'return';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

declaration :   variable|function       ;
variable    :   type idlist SEMI        ;
type        :   (INT|FLOAT)               ; 
idlist      :   ID COMMA idlist
            |   ID                      ;
function    :   type ID LB varlist RB LCB body RCB;
varlist     :   type idlist varlist               
            |   variable                        
            |                           ;
body        :   statements              ;
statements  :   statement statements
            |   statement
            |                           ;

statement   :   assignment | call | return SEMI  ;
assignment  :   ID ASGOP exp            ;
call        :   ID LB vallist RB        ;
return      :   RETURN exp              ;
exp         :   exp1 ADDOP exp|exp1     
            |   exp1                    ;
exp1        :   exp2 SUBOP exp1
            |   exp2                    ;
exp2        :   exp2 (MULOP|DIVOP) operand
            |   operand                 ;
vallist     :   values 
            |                           ;
values      :   val COMMA values
            |   val                     ;
val         :   ID | INTVAL | FLOATVAL  ;
operand     :   val | call | subexp     ;
subexp      :   LB exp RB               ;



ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;