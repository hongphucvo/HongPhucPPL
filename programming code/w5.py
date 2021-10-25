from functools import reduce

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o=[(None,None)]#o={} #o[name]=typ
        o=reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.decl,o)
        self.visit(ctx.exp,o)
        #map(lambda x: self.visit(x,o),ctx.exp)
    def visitVarDecl(self,ctx:VarDecl,o): 
        if type(ctx.typ) is IntType:typ= "int"
        elif type(ctx.typ) is FloatType: typ="float"
        else:typ="bool" 
        return (ctx.name,typ)

    def visitBinOp(self,ctx:BinOp,o):
        e1=self.visit(ctx.e1,o)
        e2=self.visit(ctx.e2,o)
        numtyp=["float","int"]
        if ctx.op in ["+","-","*"]:
            if e1 in numtyp and e2 in numtyp:
                if e1=="float" or e2=="float":
                    return "float"
                return "int"
        elif ctx.op=="/":
            if e1 in numtyp and e2 in numtyp:
                return "float"
        elif ctx.op in ["&&","||"]:
            if e1==e2=="bool":
                return "bool"
        elif ctx.op in [">", "<", "==","!="]:
            if e1==e2:
                return "bool"
        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        val=self.visit(ctx.e,o)
        if ctx.op == "!":
            if val == "bool":
                return "bool"
        elif ctx.op=="-":
            if val in ["int","float"]:
                return val
        raise TypeMismatchInExpression(ctx)
    def visitIntLit(self,ctx:IntLit,o): 
        return "int"
    def visitFloatLit(self,ctx,o): 
        return "float"

    def visitBoolLit(self,ctx,o): 
        return "bool"

    def visitId(self,ctx,o): 
        a=list(filter(lambda x: x[0]==ctx.name, o))
        if len(a)!=0: 
            return a[0][1]
        raise UndeclaredIdentifier(ctx.name)