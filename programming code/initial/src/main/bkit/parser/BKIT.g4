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

declaration :   variable|function       ;
variable    :   TYPE idlist SEMI        ;
idlist      :   ID COMMA idlist
            |   ID                      ;
function    :   TYPE ID paramdcl body   ;
paramdcl    :   LB paramlist RB                 
            |   LB RB                   ;
paramlist   :   params SEMI paramlist
            |   params                  ;
params      :   TYPE idlist             ;
param       :   TYPE ID COMMA           ;





body        :   LCB statements RCB      ;
statements  :   statement statements
            |   statement
            |                           ;

statement   :   assignment | call | returnstate SEMI  ;
assignment  :   ID ASGOP exp            ;
call        :   ID LB vallist RB        ;
returnstate :   RETURN exp              ;
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



ID:         [a-xA-Z]+;

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
TYPE:       'int'|'float';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;