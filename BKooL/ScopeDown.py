https://drive.google.com/file/d/1rEBV_oAf8slmyTTCK79-HxYqSZvGFxnz/view
1:17

dùng global current



class StaticCheck(BaseVisitor):
	def visitClassDecl(self,ctx,o):
		env={}
		env['current']=ctx.name
		env['global']=o	
		for mem in ctx.mem:
			if type(mem) is FuncDecl:
				self.visit(mem,env)
	def visitFuncDecll(self,ctx,o):
		env={}
		env['current']=o['current']
		env['global']=o['global']
		env['local']={}
		getEnv().visitVarDecl(param,env['local']) for param -> for block
		getEnv().visitVarDecl(var,env['local']) for block.var -> for block
		self.visit block stmt(env)
	def visitAssign(self, ast , o):
        r=self.visit(ast.exp,o) 
        l=self.visit(ast.lhs,o)
        if l=="void":
            raise TypeMismatchInStatement(ast)
        if r!=l:
            if r=="int" and l=="float":
                pass
            #TODO check ông nội
            if r in o["global"]:
                par=o["global"][r]
                while par.get("parent") is not None:
                    if par["parent"]["classType"]==l:
                        return
                    par=o["global"][par["parent"]]
            
            else:
                raise TypeMismatchInStatement(str(ast)) 
        if type(ast.lhs) is Id:
            if o["global"].get(ast.lhs.name):
                raise CannotAssignToConstant(ast)
    def visitId(self, ast , o):
	if ctx.name in o['local']:
		return o['local'][ctx.name]
	if ctx.name in o[global][o[current]]
		return o[global][o[current]][ctx.name]        

        raise Undeclared(Identifier(),ast.name) 
    def visitFieldAccess(self,ctx,o):
	typ-self.visit*ctx.exp,o)
	if typ is ClassType:
		if type.name in o[global]:
			if not ctx.field in o[global][type.name]
				raise Undecl
		else: raise Undecl

	


class GetName(BaseVisitor):
    """Get the name and SIKind in code"""
    def __init__(self):
        self.bl=0

    def visitProgram(self, ast,  o):
        list(map(lambda x: self.visit(x,o),ast.decl))
        return o
    def visitClassDecl(self, ast,  o):
	this=ast.classname.name
        o[this]={}
	if this in o :
            raise Redeclared(Class(),this)
        if(len(ast.memlist)>0): 
            list(map(lambda x: self.visit(x,o[this]),ast.memlist) )
        return o
    
    def visitAttributeDecl(self, ast, o):
        val=self.visit(ast.decl,o)
        return o
    def visitVarDecl(self, ast, o):
        if ast.variable.name in o:
            raise Redeclared(Class(),this)
        else:
            o[ast.variable.name]={}
        return o
        
    def visitConstDecl(self, ast, o):
        if ast.constant.name in o:
            raise Redeclared(Class(),this)
        else:
            o[ast.constant.name]={}
        return o
        
    def visitBlock(self, ast, o):
        o["bl"+str(self.bl)]={
            "mem"  : {}
        }
        for x in ast.decl:
            var=self.visit(x,o["bl"+str(self.bl)]["mem"])
        self.bl+=1
        return "bl"+str(self.bl-1)
    def visitMethodDecl(self, ast, o):
        if ast.name.name in o:
                raise Redeclared(Method(),ast.name.name)
        else:
            o[ast.name.name]={
                "mem"  : {}
            }
    def visitInstance(self, ast , o):
        return 0
    def visitStatic(self, ast, o):
        return 2














class GetName(BaseVisitor):
    def visitProgram(self, ast,  o):
        return reduce (lambda env,x:self.visit(x,env)+env,ast.decl,[])
        # list(map(lambda x: self.visit(x,o),ast.decl))
    def visitClassDecl(self, ast,  o):
        #TODO check parent
        self.classname=ast.classname.name
        return list(map(lambda x: self.visit(x,o),ast.memlist))
    def visitAttributeDecl(self, ast, o):
        # return self.visit(ast.decl,o)
        ctx=ast.decl        
        if type(ctx) is VarDecl:
            return Symbol(ctx.variable.name,MType([],ctx.varType,ast.kind),CName(self.classname))
        return Symbol(ctx.constant.name, MType([],ctx.constType,ast.kind),CName(self.classname))
    
    def visitVarDecl(self, ast, o):
        # return ast.variable.name
        return Symbol(ast.variable.name,MType([],ast.varType,Instance()),Index(ast.varInit))
    def visitConstDecl(self, ast, o):
        return Symbol(ast.constant.name,MType([],ast.constType,Instance()),Index(ast.value))
    def visitBlock(self, ast, o):
        return [map(lambda x: self.visit(x,o),ast.decl)]
    def visitMethodDecl(self, ast, o):
        return Symbol(ast.name.name,MType([map(lambda x: self.visit(x,o),ast.param)],ast.returnType,ast.kind),CName(self.classname))
        # [ast.name.name,[map(lambda x: self.visit(x,newenv),ast.param)]]

