from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

class ASTGeneration(BKOOLVisitor):

    #program: classdecl+ EOF; 
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    #classdecl: CLASS ID (EXTENDS ID)? LP memberlist RP;
    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):
        if len(ctx.ID()) == 1:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberlist()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberlist()),Id(ctx.ID(1).getText()))
    
    #memberlist: member membertail |;
    def visitMemberlist(self,ctx:BKOOLParser.MemberlistContext):
        if ctx.getChildCount():
            return self.visit(ctx.member()) + self.visit(ctx.membertail())
        else:
            return []
    
    #membertail: member membertail |;
    def visitMembertail(self,ctx:BKOOLParser.MembertailContext):
        if ctx.getChildCount():
            return self.visit(ctx.member()) + self.visit(ctx.membertail())
        else:
            return []

    #member: attribute | method;
    def visitMember(self,ctx:BKOOLParser.MemberContext):
        return self.visit(ctx.attribute()) if ctx.attribute() else self.visit(ctx.method())

    #attribute: STATIC? FINAL? alltype attdecllist SEMI
	#	| FINAL STATIC alltype attdecllist SEMI;
    def visitAttribute(self,ctx:BKOOLParser.AttributeContext):
        list = []
        for x in self.visit(ctx.attdecllist()):
            if type(x) is tuple:
                if (ctx.STATIC() and ctx.FINAL()):
                    list.append(AttributeDecl(Static(), ConstDecl(x[0], self.visit(ctx.alltype()), x[1])))
                elif ctx.FINAL():
                    list.append(AttributeDecl(Instance(), ConstDecl(x[0], self.visit(ctx.alltype()), x[1])))
                elif ctx.STATIC():
                    list.append(AttributeDecl(Static(), VarDecl(x[0], self.visit(ctx.alltype()), x[1])))
                else:
                    list.append(AttributeDecl(Instance(), VarDecl(x[0], self.visit(ctx.alltype()), x[1])))
            else:
                if (ctx.STATIC() and ctx.FINAL()):
                    list.append(AttributeDecl(Static(), ConstDecl(x, self.visit(ctx.alltype()), None)))
                elif ctx.FINAL():
                    list.append(AttributeDecl(Instance(), ConstDecl(x, self.visit(ctx.alltype()), None)))
                elif ctx.STATIC():
                    list.append(AttributeDecl(Static(), VarDecl(x, self.visit(ctx.alltype()))))
                else:
                    list.append(AttributeDecl(Instance(), VarDecl(x, self.visit(ctx.alltype()))))
        return list

    #alltype: alltype: pctype | arraytype;; 
    def visitAlltype(self,ctx:BKOOLParser.AlltypeContext):
        return self.visit(ctx.pctype()) if ctx.pctype() else self.visit(ctx.arraytype())

    #pctype: INTTYPE | BOOLTYPE | FLOATTYPE | STRINGTYPE | VOIDTYPE | ID;
    def visitPctype(self,ctx:BKOOLParser.PctypeContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        else: 
            return VoidType()

    #arraytype: pctype LSB INTLIT RSB;
    def visitArraytype(self,ctx:BKOOLParser.ArraytypeContext):
        return ArrayType(int(ctx.INTLIT().getText()), self.visit(ctx.pctype()))
    
    #attdecl: ID (EQUAL expr)?;
    def visitAttdecl(self,ctx:BKOOLParser.AttdeclContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return (Id(ctx.ID().getText()), self.visit(ctx.expr()))

    #attdecllist: attdecl (COMMA attdecllist)*;
    def visitAttdecllist(self,ctx:BKOOLParser.AttdecllistContext):
        return reduce(lambda a,b: a + b, [self.visit(x) for x in ctx.attdecllist()], [self.visit(ctx.attdecl())])

    #method: STATIC? alltype ID LB paraml RB blockstatement 
	#	| ID LB paraml RB blockstatement;
    def visitMethod(self,ctx:BKOOLParser.MethodContext):
        if ctx.STATIC():
            return [MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.paraml()), 
            self.visit(ctx.alltype()), self.visit(ctx.blockstatement()))]
        elif ctx.alltype():
            return [MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.paraml()), self.visit(ctx.alltype()), self.visit(ctx.blockstatement()))]
        else:
            return [MethodDecl(Instance(), Id("<init>"), self.visit(ctx.paraml()), None, self.visit(ctx.blockstatement()))]

    #paraml: param paramtail |;
    def visitParaml(self,ctx:BKOOLParser.ParamlContext):
        if ctx.getChildCount():
            return self.visit(ctx.param()) + self.visit(ctx.paramtail())
        else:
            return []

    #paramtail: SEMI param paramtail |;
    def visitParamtail(self,ctx:BKOOLParser.ParamtailContext):
        if ctx.getChildCount():
            return self.visit(ctx.param()) + self.visit(ctx.paramtail())
        else:
            return []

    #param: alltype attdecllist;
    def visitParam(self,ctx:BKOOLParser.ParamContext):
        return [VarDecl(x, self.visit(ctx.alltype())) for x in self.visit(ctx.attdecllist())]

    #expl: expr explist | ;
    def visitExpl(self, ctx:BKOOLParser.ExplContext):
        if ctx.getChildCount():
            return [self.visit(ctx.expr())] + self.visit(ctx.explist())
        else:
            return []

    #explist: COMMA expr explist | ;
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        if ctx.getChildCount():
            return [self.visit(ctx.expr())] + self.visit(ctx.explist())
        else:
            return []

    #expr: expr2 (LESS | GREATER | LESSOREQ | GREATEROREQ) expr2 | expr2;
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))

    #expr2: expr1 (EQ | NOTEQ) expr1 | expr1;
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))

    '''
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
    '''
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        if ctx.NEW():
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.expl()))
        elif ctx.DOT() and ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.expr1(0)), Id(ctx.ID().getText()))
        elif ctx.DOT():
            return CallExpr(self.visit(ctx.expr1(0)), Id(ctx.ID().getText()), self.visit(ctx.expl()))
        elif ctx.LSB():
            return ArrayCell(self.visit(ctx.expr1(0)), self.visit(ctx.expr()))
        elif ctx.NOT() or (ctx.getChildCount() == 2 and (ctx.ADD() or ctx.SUB())):
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr1(0)))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        
    #operand: literals | THIS | ID | NIL | LB expr RB;
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.NIL():
            return NullLiteral()
        else:
            return self.visit(ctx.expr())

    #index: expr LSB expr RSB;
    def visitIndex(self, ctx:BKOOLParser.IndexContext):
        return ArrayCell(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    #method_access: expr DOT ID LB expl RB;
    def visitMethod_access(self, ctx:BKOOLParser.Method_accessContext):
        return CallExpr(self.visit(ctx.expr()), Id(ctx.ID().getText()), self.visit(ctx.expl()))

    #att_access: expr DOT ID;
    def visitAtt_access(self, ctx:BKOOLParser.Att_accessContext):
        return FieldAccess(self.visit(ctx.expr()), Id(ctx.ID().getText()))

    #statement: blockstatement | insidestatement;
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visit(ctx.blockstatement()) if ctx.blockstatement() else self.visit(ctx.insidestatement())

    #blockstatement: LP decllist statementlist RP;
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return Block(self.visit(ctx.decllist()), self.visit(ctx.statementlist()))

    #insidestatement: assign_stm | if_stm | for_stm | break_stm | continue_stm | return_stm | method_stm;
    def visitInsidestatement(self, ctx:BKOOLParser.InsidestatementContext):
        if ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        elif ctx.if_stm():
            return self.visit(ctx.if_stm())
        elif ctx.for_stm():
            return self.visit(ctx.for_stm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        elif ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        elif ctx.return_stm():
            return self.visit(ctx.return_stm())
        else:
            return self.visit(ctx.method_stm())

    #decllist: decl_stm decltail |;
    def visitDecllist(self, ctx:BKOOLParser.DecllistContext):
        if ctx.getChildCount():
            return self.visit(ctx.decl_stm()) + self.visit(ctx.decltail())
        else:
            return []

    #decltail: decl_stm decltail |;
    def visitDecltail(self, ctx:BKOOLParser.DecltailContext):
        if ctx.getChildCount():
            return self.visit(ctx.decl_stm()) + self.visit(ctx.decltail())
        else:
            return []

    #statementlist: statement statementtail |;
    def visitStatementlist(self, ctx:BKOOLParser.StatementlistContext):
        if ctx.getChildCount():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementtail())
        else:
            return []

    #statementtail: statement statementtail |;
    def visitStatementtail(self, ctx:BKOOLParser.StatementtailContext):
        if ctx.getChildCount():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementtail())
        else:
            return []

    #decl_stm: FINAL? alltype attdecllist SEMI;
    def visitDecl_stm(self, ctx:BKOOLParser.Decl_stmContext):
        list = []
        for x in self.visit(ctx.attdecllist()):
            if type(x) is tuple:
                if ctx.FINAL():
                    list.append(ConstDecl(x[0], self.visit(ctx.alltype()), x[1]))
                else:
                    list.append(VarDecl(x[0], self.visit(ctx.alltype()), x[1]))
            else:
                if ctx.FINAL():
                    list.append(ConstDecl(x, self.visit(ctx.alltype()), None))
                else:
                    list.append(VarDecl(x, self.visit(ctx.alltype())))
        return list

    #assign_stm: (ID | index | att_access) ASSIGN expr SEMI;
    def visitAssign_stm(self, ctx:BKOOLParser.Assign_stmContext):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.expr()))
        elif ctx.index():
            return Assign(self.visit(ctx.index()), self.visit(ctx.expr()))
        else:
            return Assign(self.visit(ctx.att_access()), self.visit(ctx.expr()))

    #if_stm: IF expr THEN statement (ELSE statement)?;
    def visitIf_stm(self, ctx:BKOOLParser.If_stmContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)) if ctx.ELSE() else None)
    
    # for_stm: FOR ID ASSIGN expr (TO|DOWNTO) expr DO statement;
    def visitFor_stm(self, ctx:BKOOLParser.For_stmContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), True if ctx.TO() else False, self.visit(ctx.statement()))

    #break_stm: BREAK SEMI;
    def visitBreak_stm(self, ctx:BKOOLParser.Break_stmContext):
        return Break()

    #continue_stm: CONTINUE SEMI;
    def visitContinue_stm(self, ctx:BKOOLParser.Continue_stmContext):
        return Continue()
        
    #return_stm: RETURN expr SEMI;
    def visitReturn_stm(self, ctx:BKOOLParser.Return_stmContext):
        return Return(self.visit(ctx.expr()))

    #method_stm: expr DOT ID LB expl RB SEMI;
    def visitMethod_stm(self, ctx:BKOOLParser.Method_stmContext):
        return CallStmt(self.visit(ctx.expr()), Id(ctx.ID().getText()), self.visit(ctx.expl()))

    #arraylit: LP literals (COMMA literals)* RP;
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return ArrayLiteral(self.visit(x) for x in ctx.literals())
    
    #literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT() and ctx.BOOLLIT().getText() == 'true':
            return BooleanLiteral(True)
        elif ctx.BOOLLIT() and ctx.BOOLLIT().getText() == 'false':
            return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())

