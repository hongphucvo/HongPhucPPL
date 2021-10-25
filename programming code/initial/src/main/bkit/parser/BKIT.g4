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

program  : declarations EOF ;

declarations:   declaration declarations
            |   declaration             ;
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


body        :   LCB statements RCB
            |   LCB RCB                 ;
statements  :   variable statements
            |   statement statements
            |                           ;
statement   :   (assignment | call | returnstate) SEMI  ;


assignment  :   ID ASGOP exp            ;
call        :   ID LB explist RB        
            |   ID LB RB                ;
returnstate :   RETURNKEY exp           ;









VAR         :   'Var';
RETURNKEY   :   'return';
TYPE        :   'int'|'float';
ID          :   [a-xA-Z]+;
INTVAL      :   [+-]?[0-9]+;
FLOATVAL    :   [+-]?[0-9]+'.'[0-9]+;
LB          :   '(';
RB          :   ')';
LCB         :   '{';
RCB         :   '}';
ASGOP       :   '=';
COMMA       :   ',';
ADDOP       :   '+';
SUBOP       :   '-';
MULOP       :   '*';
DIVOP       :   '/';
SEMI        :   ';';
COLON       :   ':';
WS          :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;