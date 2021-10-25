from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        o={}
        list(map(lambda x: self.visit(x,o),ctx.decl,o))
        self.visit(ctx.exp,o)
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        o[ctx.name]={}
        list(map(lambda x: self.visit(x,o[ctx.name]),ctx.mem,o))
        
        
        #mem=reduce (lambda acc,ele:acc+[self.visit(ele,acc)],ctx.mem,[[],[]])
        #o+= (ctx.name, ctx.parent, mem)
    def visitVarDecl(self,ctx:VarDecl,o:object):
        
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        #o[ctx.name]=self.visit(ctx.typ,o)
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        o[ctx.name]={}
        #handle inner unc
        #o=reduce(lambda acc,ele:acc+[self.visit(ele,acc)],ctx.body[1],[[],[]])
        #reduce(lambda acc,ele:acc+[self.visit(ele,acc)],ctx.body[2],o)
        #return (ctx.name,[],o)
    
    def visitIntType(self,ctx:IntType,o:object):
        return "int"

    def visitFloatType(self,ctx:FloatType,o:object):
        return "float"
    def visitClassType(self,ctx:ClassType,o:object):
        return ctx.name
    def visitIntLit(self,ctx:IntLit,o:object):
        return "int"
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o[1]:
            raise UndeclaredField(ctx.name)
    
    
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        self.visit(ctx.name,o)
        #reduce (lambda acc,ele: self.visit(ctx.exp,o))
        #self.visit(ctx.field,o)
        


Program(
    [
        ClassDecl(
            "x","",
            [
                FuncDecl(
                    "foo",[],
                    (
                        [
                            VarDecl(
                                "m",ClassType("x"))
                        ],
                        [
                            FieldAccess(Id("m"),"a"),
                            FieldAccess(Id("m"),"b")
                        ]
                    )
                ),
                VarDecl("a",IntType())
            ]
        )
    ]
)
