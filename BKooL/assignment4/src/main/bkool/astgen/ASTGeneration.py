
from AST import *
from BKOOLParser import BKOOLParser
from BKOOLVisitor import BKOOLVisitor


class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        classdcls=self.visit(ctx.classdcls())
        return Program(classdcls)

    def visitClassdcls(self, ctx:BKOOLParser.ClassdclsContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.classdcls())
        return [self.visit(ctx.classdcl())]+tail
    def visitClassdcl(self, ctx:BKOOLParser.ClassdclContext):
        memList=self.visit(ctx.memBlock())
        if ctx.ID(1):
            return ClassDecl(Id(ctx.ID(0).getText()), memList,Id(ctx.ID(1).getText()))
        return ClassDecl(Id(ctx.ID(0).getText()), memList)
    def visitMemBlock(self, ctx:BKOOLParser.MemBlockContext):
        if ctx.memList(): return self.visit(ctx.memList())
        return []
    def visitMemList(self, ctx:BKOOLParser.MemListContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.memList())
        return self.visit(ctx.classMember())+tail
    def visitClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        if ctx.attributeDeclare(): return self.visit(ctx.attributeDeclare())
        return self.visit(ctx.methodDeclare())
    def visitAttributeDeclare(self, ctx:BKOOLParser.AttributeDeclareContext):
        kind=Static() if ctx.STATIC() else Instance()
        vartyp=self.visit(ctx.vartype())
        attributeList=self.visit(ctx.attributeList())
        if ctx.IMMUTABLE():
            decl = list(map(lambda x:ConstDecl(x[0],vartyp,x[1]) if len(x)==2 else ConstDecl(x[0],vartyp,None),attributeList))
        else:
            decl=list(map(lambda x:VarDecl(x[0],vartyp)if len(x)==1 else VarDecl(x[0],vartyp,x[1]),attributeList))
        return list(map(lambda x:AttributeDecl(kind, x),decl))

    def visitAttributeList(self, ctx:BKOOLParser.AttributeListContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.attri())]
        tail=self.visit(ctx.getChild(2))
        return [self.visit(ctx.attri())]+tail
    def visitAttri(self, ctx:BKOOLParser.AttriContext):
        if ctx.exp():
            return [Id(ctx.ID().getText()), self.visit(ctx.exp())]
        return [Id(ctx.ID().getText())]

    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        tail=self.visit(ctx.idList()) if ctx.idList() else []
        return [Id(ctx.ID().getText())]+tail

    def visitMethodDeclare(self, ctx:BKOOLParser.MethodDeclareContext):
        name=Id(ctx.ID().getText())
        if ctx.STATIC():
            kind=Static()
            returnType=self.visit(ctx.vartype())
        else:
            kind=Instance()
            if ctx.vartype():
                returnType=self.visit(ctx.vartype())
            else:
                name=Id(str("<init>"))
                returnType= None
        param=self.visit(ctx.paramList())
        body=self.visit(ctx.stmBlock())
        return [MethodDecl(kind,name,param,returnType,body)]
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        if ctx.getChildCount()==3:
            return self.visit(ctx.paramDeclare())
        return[]
    def visitParamDeclare(self, ctx:BKOOLParser.ParamDeclareContext):
        tail=self.visit(ctx.paramDeclare())if ctx.paramDeclare() else []
        return self.visit(ctx.param())+tail
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        ids=self.visit(ctx.idList())
        vartype=self.visit(ctx.vartype())
        return list(map(lambda x:VarDecl(x,vartype),ids))

    def visitStmBlock(self, ctx:BKOOLParser.StmBlockContext):
        return self.visit(ctx.stmList()) if ctx.getChildCount()==3 else []
    def visitStmList(self, ctx:BKOOLParser.StmListContext):
        var=self.visit(ctx.variables()) if ctx.variables() else []
        stms=self.visit(ctx.stms()) if ctx.stms() else []
        return Block(var,stms)
    def visitVariables(self, ctx:BKOOLParser.VariablesContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.variables())
        return self.visit(ctx.variable())+tail
    def visitVariable(self, ctx:BKOOLParser.VariableContext):
        #TODO kind=Instance()
        vartyp=self.visit(ctx.vartype())
        attributeList=self.visit(ctx.attributeList())
        if ctx.IMMUTABLE():
            return list(map(lambda x:ConstDecl(x[0],vartyp,x[1]) if len(x)==2 else ConstDecl(x[0],vartyp,None) ,attributeList))
        return list(map(lambda x:VarDecl(x[0],vartyp)if len(x)==1 else VarDecl(x[0],vartyp,x[1]),attributeList))

    def visitStms(self,ctx:BKOOLParser.StmsContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.stms())
        return [self.visit(ctx.stm())]+tail
        #trả về list thì [] không thì None

    def visitStm(self,ctx:BKOOLParser.StmContext):
        if ctx.stmBlock():
            return self.visit(ctx.stmBlock())
        elif ctx.lhs():
            return Assign(self.visit(ctx.lhs()),self.visit(ctx.exp(0)))
        ###why exp0
        elif ctx.IF():
            if ctx.ELSE():
                return If(self.visit(ctx.exp(0)),self.visit(ctx.stm(0)),self.visit(ctx.stm(1)))
            return If(self.visit(ctx.exp(0)),self.visit(ctx.stm(0)))
        ###why stm0
        elif ctx.FOR():
            id=self.visit(ctx.scala_var())
            up=bool(ctx.TO())
            return For(id, self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), up, self.visit(ctx.stm(0)))
        elif ctx.BREAK():
            return Break()
        elif ctx.CONT():
            return Continue()
        elif ctx.RETURN():
            return Return(self.visit(ctx.exp(0)))
        elif ctx.DOT():
            return CallStmt(self.visit(ctx.exp9()),Id(ctx.ID().getText()),self.visit(ctx.explist()))
            #self.visit(ctx.methodCall())
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        return self.visit(ctx.exps()) if ctx.exps() else []
    def visitExps(self, ctx:BKOOLParser.ExpsContext):
        tail=self.visit(ctx.exps()) if ctx.exps() else []
        return [self.visit(ctx.exp())]+tail
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp3())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp4())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp5())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp6())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))

    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp6()))
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp8())
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp8()))
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp9())
        return ArrayCell(self.visit(ctx.exp8()),self.visit(ctx.exp()))
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        if ctx.exp10():
            return self.visit(ctx.exp10())
        elif ctx.explist():
            return CallExpr(self.visit(ctx.exp9()),Id(ctx.ID().getText()),self.visit(ctx.explist()))
            #self.visit(ctx.methodInvoke())
        return FieldAccess(self.visit(ctx.exp9()),Id(ctx.ID().getText()))
        #self.visit(ctx.attriAccess())
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.operand())
        return NewExpr(Id(ctx.ID().getText()),self.visit(ctx.explist()))
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        if ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.elem():
            return self.visit(ctx.elem())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        return self.visit(ctx.subexp())

    def visitSubexp(self, ctx:BKOOLParser.SubexpContext):
        return self.visit(ctx.exp())
    def visitScala_var(self, ctx:BKOOLParser.Scala_varContext):
        return Id(ctx.ID().getText())
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.getChildCount()==4:
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))
            #chỗ này nó có nhầm lần exp4 với exp đc k -> nhẩm thì thành exp(1)
        else:
            return self.visit(ctx.exp9())


    def visitVartype(self,ctx:BKOOLParser.VartypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        return self.visit(ctx.classtype())

    def visitPrimtype(self,ctx:BKOOLParser.PrimtypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()
        return VoidType()
    def visitClasstype(self,ctx:BKOOLParser.ClasstypeContext):
        return ClassType(Id(ctx.ID().getText()))
    def visitArraytype(self,ctx:BKOOLParser.ArraytypeContext):
        type=self.visit(ctx.primtype()) if ctx.primtype() else self.visit(ctx.classtype())
        return ArrayType(self.visit(ctx.size()),type)
    def visitSize(self, ctx:BKOOLParser.SizeContext):
        return int(ctx.INTLIT().getText())
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.exps()))
    def visitElemList(self, ctx:BKOOLParser.ElemListContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.elemList())
        return [self.visit(ctx.elem())]+tail
    def visitElem(self, ctx:BKOOLParser.ElemContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(bool(ctx.BOOLLIT().getText()=="true"))
        return StringLiteral(ctx.STRINGLIT().getText())
