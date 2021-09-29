
from BKOOLParser import BKOOLParser
from BKOOLVisitor import BKOOLVisitor
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        classdcls=self.visit(ctx.classdcls())
        return Program(classdcls)
    #def visitMemdecl(self,ctx:BKOOLParser.MemdeclContext):
    #    return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkooltype())))
    
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
        #trick: append 1 more index = None instead of fin missing and fill
        #attributeList=list(map(lambda x:x.append(None),attributeList))
        if ctx.IMMUTABLE():
            #add x1 in to declr if there is value,x[1]
            decls=list(map(lambda x:ConstDecl(x[0],vartyp) if len(x)==1 else ConstDecl(x[0],vartyp,x[1]),attributeList))
        else: decls=list(map(lambda x:VarDecl(x[0],vartyp)if len(x)==1 else VarDecl(x[0],vartyp,x[1]),attributeList))     
        #return AttributeDecl(kind,decls[0])
        return list(map(lambda x:AttributeDecl(kind, x),decls))
    def visitAttributeList(self, ctx:BKOOLParser.AttributeListContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.attri())]
        tail=self.visit(ctx.getChild(2))
        return [self.visit(ctx.attri())]+tail
    def visitAttri(self, ctx:BKOOLParser.AttriContext):
        if ctx.exp():
            return [Id(ctx.ID().getText()), self.visit(ctx.exp())]
        return [Id(ctx.ID().getText())]
    
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
                name=Id(ctx.ID().getText()+str('''(<init>)'''))
                returnType= VoidType()
        if ctx.ID().getText()=="main":
            kind=Static()
            name=Id('''main(<init>)''')
        param=self.visit(ctx.paramList())
        body=self.visit(ctx.stmBlock())
        return [MethodDecl(kind,name,param,returnType,body)]
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        if ctx.getChildCount()==3:
            return self.visit(ctx.paramDeclare())
        return[]
    def visitParamDeclare(self, ctx:BKOOLParser.ParamDeclareContext):
        tail=self.visit(ctx.paramDeclare())if ctx.paramDeclare() else []
        return [self.visit(ctx.param())]+tail
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        ids=self.visit(ctx.idList())
        vartype=self.visit(ctx.vartype())
        return [VarDecl(x,vartype,None).toParam()for x in ids]
######## ids=self.visit(ctx.attributeList()) return [[a],[b,7]]
######## return [VarDecl(x[0],vartype,x[1]).toParam()for x in ids]
    
    
    def visitStmBlock(self, ctx:BKOOLParser.StmBlockContext):
        return self.visit(ctx.stmList()) if ctx.getChildCount()==3 else []
    def visitStmList(self, ctx:BKOOLParser.StmListContext):
        var=self.visit(ctx.variables()) if ctx.variables() else []
        stms=self.visit(ctx.stms()) if ctx.stms() else []
        return Block(var,stms)
    def visitVariables(self, ctx:BKOOLParser.VariablesContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.variables())
        return [self.visit(ctx.variable())]+tail
    def visitVariable(self, ctx:BKOOLParser.VariableContext):
        #kind=Instance()
        vartyp=self.visit(ctx.vartype())
        attributeList=[self.visit(ctx.attributeList())]
        if ctx.IMMUTABLE():
            return list(map(lambda x:ConstDecl(x[0],vartyp,None) if len(x)==1 else ConstDecl(x[0],vartyp,x[1]),attributeList))
        return list(map(lambda x:VarDecl(x[0],vartyp,x[1]) if len(x)==2 else VarDecl(x[0],vartyp), attributeList))
        #return list(map(lambda x:ConstDecl(x[0],vartyp) if len(x)==1 else ConstDecl(x[0],vartyp,x[1]),attributeList))
         
        
    def visitStms(self,ctx:BKOOLParser.StmsContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.stms())
        return [self.visit(ctx.stm())]+tail
        #trả về list thì [] không thì None

    def visitStm(self,ctx:BKOOLParser.StmContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.stmBlock())
        elif ctx.lhs():
            return Assign(self.visit(ctx.lhs()),self.visit(ctx.exp()))
        elif ctx.IF():
            return If(self.visit(ctx.exp()),ctx.stm(0),ctx.stm(1))
        elif ctx.FOR():
            id=self.visit(ctx.scala_var())
            up=bool(ctx.TO())
            return For(id, self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), up, self.visit(ctx.stm()))
        elif ctx.BREAK():
            return Break()
        elif ctx.CONT():
            return Continue()
        elif ctx.RETURN():
            return Return(self.visit(ctx.exp()))
        return self.visit(ctx.methodInvoke())
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
            return self.visit(ctx.exp2())
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp1()))
    
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp3())
        return UnaryOp(ctx.getChild(0).getText(),ctx.exp2())
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp4())
        return ArrayCell(self.visit(ctx.exp3()),self.visit(ctx.exp()))
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.exp5():
            return self.visit(ctx.exp5())
        elif ctx.methodInvoke():
            return self.visit(ctx.methodInvoke())
        return self.visit(ctx.attriAccess())
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.operand())
        return NewExpr(ctx.ID().getText(),self.visit(ctx.explist()))
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        if ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.elem():
            return self.visit(ctx.elem())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        return self.visit(ctx.subexp())
    def visitSubexp(self, ctx:BKOOLParser.SubexpContext):
        return self.visit(ctx.exp())

    def visitMethodInvoke(self,ctx:BKOOLParser.MethodInvokeContext):
        if ctx.attriAccess():
            obj=self.visit(ctx.attriAccess())
        elif ctx.exp5():
            obj=self.visit(ctx.exp5())
        else: obj=Id(ctx.ID(0).getText())
        method=Id(ctx.ID(1).getText())if ctx.ID(1) else Id(ctx.ID(0).getText())
        param=self.visit(ctx.explist())
        tail=self.visit(ctx.methodRecur())
        outer=tail
        call=bool(ctx.getParent().getRuleIndex()!=0)
        if outer == [] and call:
            inner: CallStmt(obj,method,param)
        else: 
            inner=CallExpr(obj,method,param)#kho qua di
        while(outer!=[]):
            if outer[2] == [] and call:
                inner= CallStmt(inner,outer[0],outer[1])
            else: 
                inner=CallExpr(inner,outer[0],outer[1])#kho qua di
            outer=outer[2]
        return inner
    def visitMethodRecur(self,ctx:BKOOLParser.MethodRecurContext):
        if ctx.getChildCount()==0:
            return []
        return [Id(ctx.ID().getText()),self.visit(ctx.explist()),self.visit(ctx.methodRecur())]
    def visitAttriAccess(self, ctx:BKOOLParser.AttriAccessContext):
        obj=self.visit(ctx.exp5()) if ctx.exp5() else Id(ctx.ID(0).getText())
        head_=self.visit(ctx.methodRecur())
        fieldname=Id(ctx.ID(1).getText()) if ctx.ID(1) else Id(ctx.ID(0).getText())
        """if ctx.ID(1):
            fieldname=Id(ctx.ID(1).getText())
            obj=Id(ctx.ID(0).getText())
        else:
            fieldname=Id(ctx.ID(0).getText())
            obj=self.visit(ctx.exp5()) """    
        while(head_!=[]):
            obj=CallExpr(obj,head_[0],head_[1])
            head_=head_[2] if len(head_)==3 else []

        tail_=self.visit(ctx.attriRecur())
        inner=FieldAccess(obj,fieldname)
        outer=tail_[2] if len(tail_)==3 else []
        while(outer!=[]):
            #handle inner into method recur bằng while
            x=outer[0]
            while(x!=[]):
                inner=CallExpr(inner,x[0],x[1])
                x=x[2]
            inner=FieldAccess(inner,outer[1])
            outer=outer[2] if len(outer)==3 else []
        return inner
    def visitAttriRecur(self,ctx:BKOOLParser.AttriRecurContext):
        if ctx.getChildCount()==0:
            return []
        return [self.visit(ctx.methodRecur()),Id(ctx.ID().getText()), self.visit(ctx.attriRecur())]

    def visitScala_var(self, ctx:BKOOLParser.Scala_varContext):
        return Id(ctx.ID().getText())
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.exp4():
            return ArrayCell(self.visit(ctx.exp4()),self.visit(ctx.exp()))
            #chỗ này nó có nhầm lần exp4 với exp đc k -> nhẩm thì thành exp(1)
        else:
            return self.visit(ctx.attriAccess())

    
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
        return IntLiteral(ctx.INTLIT().getInt())
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.elemList()))
    def visitElemList(self, ctx:BKOOLParser.ElemListContext):
        tail=[] if ctx.getChildCount()==1 else self.visit(ctx.elemList())
        return [self.visit(ctx.elem)]+tail
    def visitElem(self, ctx:BKOOLParser.ElemContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        return Id(ctx.ID().getText())
 