
class Field:
    def __init__(self, typ, value):
        self.typ=typ
        self.value=value
class MType:
    def __init__(self,paramtype,rettype):
        self.paramtype = paramtype
        self.rettype = rettype

class Symbol:
    def __init__(self,mtype,value = None):
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):
    global_envi = {
    "readInt"   : { "returnType":IntType()},
    "writeInt"  : { "param":{"":IntType()},
                    "returnType":VoidType()},
    "writeIntLn": { "param":{"":IntType()},
                    "returnType":VoidType()},
    "readFloat" : { "returnType": FloatType()},
    "writeFloat": { "param":{"":FloatType()},
                    "returnType":VoidType()},
    "writeFloatLn": { "param":{"":FloatType()},
                    "returnType":VoidType()},
    "readBool"  : { "returnType":BoolType()},
    "writeBool" : { "param":{"":BoolType()},
                    "returnType":VoidType()},
    "writeBoolLn": { "param":{"":BoolType()},
                    "returnType":VoidType()},
    "readStr"   : { "returnType":StringType()},
    "writeStr"  : { "param":{"":StringType()},
                    "returnType":VoidType()},
    "writeStrLn": { "param":{"":StringType()},
                    "returnType":VoidType()}
    }       
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        return c #[self.visit(x,c) for x in ast.decl]

    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitProgram(self, ast, param):
        return None
    
    def visitVarDecl(self, ast, param):
        return None
    
    def visitConstDecl(self, ast, param):
        return None
    
    def visitClassDecl(self, ast, param):
        return None
    
    def visitStatic(self, ast, param):
        return None
    
    def visitInstance(self, ast, param):
        return None
    
    def visitMethodDecl(self, ast, param):
        return None
    
    def visitAttributeDecl(self, ast, param):
        return None
    
    def visitIntType(self, ast, param):
        return None
    
    def visitFloatType(self, ast, param):
        return None
    
    def visitBoolType(self, ast, param):
        return None
    
    def visitStringType(self, ast, param):
        return None
    
    def visitVoidType(self, ast, param):
        return None
    
    def visitArrayType(self, ast, param):
        return None
    
    def visitClassType(self, ast, param):
        return None
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, param):
        return None
    
    def visitNewExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitBlock(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitCallStmt(self, ast, param):
        return None
    
    def visitIntLiteral(self, ast, param):
        return None
    
    def visitFloatLiteral(self, ast, param):
        return None
    
    def visitBooleanLiteral(self, ast, param):
        return None
    
    def visitStringLiteral(self, ast, param):
        return None
    
    def visitNullLiteral(self, ast, param):
        return None
    
    def visitSelfLiteral(self, ast, param):
        return None 

    def visitArrayLiteral(self, ast, param):
        return None 
    
class GetName(BaseVisitor,Utils):
    def visitProgram(self, ast, c, param):
        c={}
        list(map(lambda x: self.visit(x,c),ast.decl))
    def visitClassDecl(self, ast, c, param):
        a=self.visit(ast.classname,c)
        c[ast.classname]={
            "parent": self.visit(ast.parentname,c),
            "mem": {}
        }
        list(map(lambda x: self.visit(x,c[ast.classname]),ast.memList))
    
    def visitVarDecl(self, ast, c, param):
        if ast.variable in c:
            raise Redeclared(ast)
        c[ast.name]={}
        '''c[ast.variable]={
            Field(self.visit(ast.varType), self.visit(ast.varInit))
        }'''
    def visitConstDecl(self, ast,c, param):
        if ast.constant in c:
            raise Redeclared(ast)
        c[ast.constant]={}
    
    def visitMethodDecl(self, ast,c, param):
        if ast.name in c:
            raise Redeclared(ast)
        c[ast.name]={}
        
        '''c[ast.name]={
            "head"  : Symbol(MType(list(map(lambda x: self.visit(x,c),ast.param)), self.visit(ast.returnType,c)),[]),
            "body"  : self.visit(ast.body,c)
        }
    '''
    
    def visitAttributeDecl(self, ast,c, param):
        self.visit(self,ast.decl)