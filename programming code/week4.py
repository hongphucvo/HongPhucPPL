lỗi
from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.decl,[])
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        parameter=reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.param,[])
        reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.body,parameter)
        return ctx.name
    def visitIntType(self,ctx:IntType,o:object):pass
        
    def visitFloatType(self,ctx:FloatType,o:object):pass
     
    def visitIntLit(self,ctx:IntLit,o:object):pass



ok 
from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.decl,[])
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        env=[[]]+o
        env[1]+=ctx.name
        reduce(lambda acc,ele: acc+[self.visit(ele,acc)],ctx.param+ctx.body,env[0])
        return ctx.name
    def visitIntType(self,ctx:IntType,o:object):pass
        
    def visitFloatType(self,ctx:FloatType,o:object):pass
     
    def visitIntLit(self,ctx:IntLit,o:object):pass

double [[]]

from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o=[[],[]]
        reduce(lambda acc,ele: acc+[self.visit(ele,[acc,o[1]])],ctx.decl,o[0])
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        return ctx.name
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        env=[[]]+o
        env[1]+=[ctx.name]
        scope=reduce(lambda acc,ele: acc+[self.visit(ele,[acc,env[1]])],ctx.param+ctx.body,env[0])
        return ctx.name
    def visitIntType(self,ctx:IntType,o:object):pass
        
    def visitFloatType(self,ctx:FloatType,o:object):pass
     
    def visitIntLit(self,ctx:IntLit,o:object):pass
    



recur list 
from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o=[[],[]]
        reduce(lambda acc,ele: acc+[self.visit(ele,[acc,o[1]])],ctx.decl,o[0])
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        return ctx.name
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        env=o+[[]]
        env[1]+=[ctx.name]
        scope=reduce(lambda acc,ele: acc+[self.visit(ele,[acc,env[1]])],ctx.param+ctx.body[0],[])
        reduce(lambda acc,ele: acc+[self.visit(ele,[acc,[]])],ctx.body[1],scope+env[0]+env[1])
        return ctx.name
    def visitIntType(self,ctx:IntType,o:object):pass
        
    def visitFloatType(self,ctx:FloatType,o:object):pass
     
    def visitIntLit(self,ctx:IntLit,o:object):pass
    
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o[0]:
            raise UndeclaredIdentifier(ctx.name)
        return ctx.name


[[],[]]

[[b],[]]
o=[[b],[]] env=[[b],[a]]
	param=[m,b,d]
	
	param=[m,b,d,c]
		o(foo)=param+env=[[bmbdc][a]] env=[[bmbdc][a,foo]]
			param=[x]
			param=[xyz]
			exp[xyzbmbdc][a,foo]