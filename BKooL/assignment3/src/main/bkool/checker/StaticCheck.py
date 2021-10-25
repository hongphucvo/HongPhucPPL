"""
 * @author nhphung
"""
from os import write
from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *
#from main.bkool.utils.AST import Program, VarDecl
from functools import reduce
import enum
T={0:[],1:["Const"],2:["Static"],3:["Static","Const"]}
#to add const: +1
#to add static: +2
#check kind trước cho static
class SI(enum.Enum):
    Instance_Var=0
    Instance_Const=1
    Static_Var=2
    Static_Const=3
class Lit(enum.Enum):
    Int = 0
    Float = 1
    String = 2
    Bool = 3 
class Field:
    def __init__(self, typ, value):
        self.typ=typ
        self.value=value
    def __str__(self):
        return str(self.typ)+str(self.value)
class MType:
    def __init__(self,paramList,rettype):
        self.paramList = paramList
        self.rettype = rettype

class Symbol:
    def __init__(self,mtype,value = None):
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):
    global_envi = {}
    """
    def class tên io chứa các method 
    io:{
        mem:{
            "readInt"   : { "head":MType({"NA":Field("void",None)},"int"),
                    "body":[]},
            "writeInt"  : { "param":{"":"int"},
                            "returnType":VoidType()},
            "writeIntLn": { "param":{"":"int"},
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
    }
    
    }       """
    
    def __init__(self,ast):
        self.ast = ast
        self.o=StaticChecker.global_envi
        self.getName=GetName()
        #self.f = open("dictionary","w")
        #self.f.write("")
    
    def check(self):
        GetFor().visit(self.ast,{})
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast,  o): 
        """Handle type, value, redeclare"""
        #raise Redeclared(Variable(),"Con")
        o=self.getName.visit(ast,o)
        #[map(lambda x: self.visit(x,o),ast.decl)]
        for x in ast.decl:
            self.visit(x,o)
        #self.f.write(str(o))

        #self.f.close()
        #return o
        
        #print( o)
        #return [self.visit(x, o) for x in ast.decl]
        return o
    #def visitFuncDecl(self,ast,  o): 
        #return o
        #return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
        '''
    def visitCallExpr(self, ast,  o): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if o[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype
    '''

    def visitClassDecl(self, ast,  o):
        
        list(map(lambda x: self.visit(x,o),filter(lambda t: type(t) is MethodDecl,ast.memlist)))
        return o
        #pass
        """env={
            "global":o["global"],
            "current":o["current"],
            "local":{}
        }
        return None
        if ast.parentname:
            if not ast.parentname.name in map(lambda x: x.name, o):
                raise Undeclared(Class(),ast.parentname.name)
        return list(map(lambda x: self.visit(x, o),ast.memlist)) 
        """
    """    
    
    """
    def visitMethodDecl(self, ast , o):
        """env={
            "global":o["global"],
            "current":o["current"],
            "local":{}
        }"""
        o={}
        #should local:{"code":self.visit(ast.kind)}
        param=list(map(lambda x: self.getName.visit(x,o),ast.param))#"""env["local"]"""
        #TODO check type param of class
        err=list(filter(lambda x: len(x)>1,param))
        if err:
            raise Redeclared(Parameter(),err[0]["Redeclare"].name) 
        #param được gán trị k ta, có thì 
        #list(map(lambda x:self.visit(x,env["local"]),ast.param))
        self.visit(ast.body,o)
    
    def visitAttributeDecl(self, ast , o):
        return self.visit(ast.decl,o)
    def visitBlock(self, ast , o):
        """env={
            "global":o["global"],
            "current":o["current"],
            "local":{}
        }"""
        var=list(map(lambda x: self.getName.visit(x,o),ast.decl))
        err=list(filter(lambda x: len(x)>1,var))
        if err:
            #if type(err[0])
            raise Redeclared(Variable(),err[0].variable.name) 
        #list(map(lambda x: self.visit(x,o),ast.decl))
        #to get list of 
        #list(map(lambda x: self.visit(x,o),ast.stmt))
        #To handle undeclare ID
        return None
    #TODO we have code in o, we have to assign type and value
    def visitVarDecl(self, ast, o):
        #every variable has these field
        #o of this object is {}
        #To chuc luu tru cho var_const_static_expr
        val=Field(self.visit(ast.varType),self.visit(ast.varInit)if ast.varInit else None)
        if val.typ!=val.value:
            raise TypeMismatchInStatement(ast)
        o[ast.name]["val"]= val
        return o[ast.name]
    def visitConstDecl(self, ast, o):
        val=Field(self.visit(ast.constType),self.visit(ast.value)if ast.value else None)
        if val.value is None:
            raise IllegalConstantExpression(ast)
        #TODO
        # check static expr elif o[val.value
        if val.typ!=val.value:
            raise TypeMismatchInConstant(ast)
        o[ast.name]["val"]= val
        return o[ast.name]
    def visitBinaryOp(self, ast , o):
        r=self.visit(ast.right,o)
        l=self.visit(ast.left,o)
        #TODO: check type of left+right+op
        return "type"
    
    def visitUnaryOp(self, ast , o):
        ex=self.visit(ast.body,o)
        if ast.op in ["!"]:
            if ex=="bool":
                return ex
        return None
    
    def visitCallExpr(self, ast , o):
        obj=self.visit(ast.obj,o)
        med=self.visit(ast.method,o[obj])
        param=list(map(lambda x: self.visit(x,o),ast.param))
        #lấy list expr check với def của method
        err=list(map(filter(lambda x,y: x!=y, (param,o[med]["param"]))))
        if err:
            raise TypeMismatchInExpression(ast)
        return med#type
    
    def visitNewExpr(self, ast , o):
        classname=ast.classname
        param=list(map(lambda x: self.visit(x,o),ast.param))
        err=list(map(filter(lambda x,y: x!=y, (param,o[classname]["mem"]))))
        if err:
            raise TypeMismatchInExpression(ast)
        return classname.name
    
    def visitId(self, ast , o):
        #handle undeclr
        if ast.name not in o:
            o[ast.name]["Undeclare"]=ast.name
            raise Undeclared(Identifier(),ast.name)
        return o[ast.name]
    
    def visitArrayCell(self, ast , o):
        return None
    
    def visitFieldAccess(self, ast , o):
        #remember to check parent
        return None
    def visitIf(self, ast , o):
        return None
    
    def visitFor(self, ast , o):
        env["local"]={"var":ast.name}
        #scalar has type int
        if not (self.visit(ast.exp1)==self.visit(ast.exp2)=="int"):
            raise TypeMismatchInStatement(ast.name+":="+ast.exp1)
    
    def visitContinue(self, ast , o):
        pass
    
    def visitBreak(self, ast , o):
        pass
    
    def visitReturn(self, ast , o):
        val=self.visit(ast.expr,o)
        if val!=env[current]["returntype"]:
            raise TypeMismatchInStatement(ast)
    
    def visitAssign(self, ast , o):
        r=self.visit(ast.exp,o)
        l=self.visit(ast.lhs,o)
        if r!=l:
            #TODO check cha gán con
            raise TypeMismatchInStatement(ast)   
        if o[r.name]["code"]>1:
            #const
            raise CannotAssignToConstant(ast)
         
    def visitCallStmt(self, ast , o):
        obj=self.visit(ast.obj,o)
        med=self.visit(ast.method,o[obj])
        param=list(map(lambda x: self.visit(x,o),ast.param))
        #lấy list expr check với def của method
        err=list(map(filter(lambda x,y: x!=y, (param,o[med]["param"]))))
        if err:
            raise TypeMismatchInStatement(ast)
        
    
    def visitArrayLiteral(self, ast , o):
        value=list(map(lambda x: self.visit(x,value)))
        pure=reduce(lambda acc,ele: acc and (ele==value[0]),value,True)
        if not pure:
            raise IllegalArrayLiteral(ast)
        return value[0]+str(len(value)) 
    
    def visitIntLiteral(self, ast , o):
        return "int"
    
    def visitFloatLiteral(self, ast , o):
        return "float"
    
    def visitBooleanLiteral(self, ast , o):
        return "bool"
    
    def visitStringLiteral(self, ast , o):
        return "string"
    
    def visitNullLiteral(self, ast , o):
        return "null"
    
    def visitSelfLiteral(self, ast , o):
        return "this"
    #TODO: do we need it anymore???
    def visitInstance(self, ast , o):
        return 0
    def visitStatic(self, ast, o):
        return 2
    
    def visitIntType(self, ast , o):
        return "int"
    
    def visitFloatType(self, ast , o):
        return "float"
    
    def visitBoolType(self, ast , o):
        return "bool"
    
    def visitStringType(self, ast , o):
        return "string"
    
    def visitVoidType(self, ast , o):
        return "void"
    
    def visitArrayType(self, ast , o):
        return self.visit(ast.eleType)+str(ast.size)
    
    def visitClassType(self, ast , o):
        return ast.name.name
    







class GetName(BaseVisitor):
    """Get the name and SIKind in code"""
    #def __init__(self):
        
        
        #self.f = open("dictionarybase","w")
        #self.f.write("")

    def visitProgram(self, ast,  o):
        list(map(lambda x: self.visit(x,o),ast.decl))

        #self.f.write(str(o))
        return o
    def visitClassDecl(self, ast,  o):
        this=ast.classname.name
        if this in o :
            raise Redeclared(Class(),this)
        if ast.parentname:    
            par=ast.parentname.name
            if par not in o:
                raise Undeclared(Class(),par)
            o[this]={
                 "parent": par.name ,
                "mem":{}
            }
        else: 
            o[this]={
            "mem":{}
            }
        if(len(ast.memlist)>0): 
            list(map(lambda x: self.visit(x,o[this]["mem"]),ast.memlist) )
        #map(lambda x: ,ast.memlist) 
        
        return o#a=self.visit(ast.classname, o)
    
    def visitAttributeDecl(self, ast, o):
        val=self.visit(ast.decl,o)
        if len(val)>1:
            raise Redeclared(Attribute(),str(ast.decl.variable.name))
        val["code"]+=self.visit(ast.kind,o)
        return val
        #self.visit(ast.decl,)

        
    def visitVarDecl(self, ast, o):
        if ast.variable.name in o:
            o[ast.variable.name]["Redeclare"]=ast.variable
        else:
            o[ast.variable.name]={"code":0}
        return o[ast.variable.name]
        """"const":False,
            #"field":Field(self.visit(ast.varType),None)}
            "field":Field("int",None)}"""
        #none is the assigned value, handle in the 2nd visitor, they will check for type 
        #return o
        '''c[ast.variable]={
            Field(self.visit(ast.varType), self.visit(ast.varInit))
        }'''
    def visitConstDecl(self, ast, o):
        if ast.constant.name in o:
            raise Redeclared(Constant(),ast.constant.name)
        o[ast.constant.name]={"code":1}
        return o[ast.constant.name]
        """o[ast.constant.name]={
            "const":True,
            #"field":Field(self.visit(ast.constType),None)
            }"""
        #return o
    def visitMethodDecl(self, ast, o):
        if ast.name.name in o:
            raise Redeclared(Method(),ast.name.name)
        o[ast.name.name]={"code":self.visit(ast.kind,o)}
        #return o
        
        """o[ast.name.name]={
            "head"  : {},
            "body"  : {}
        }
        for x in ast.param:
            if self.visit(x,o[ast.name.name]["head"])["Redeclare"]: raise Redeclared(Parameter(),x.name.name)
        self.visit(ast.body, o)"""
    def visitInstance(self, ast , o):
        return 0
    def visitStatic(self, ast, o):
        return 2
class GetFor(BaseVisitor):
    def visitProgram(self, ast, o):
        list(map(lambda x: self.visit(x,0),ast.decl))
      
    def visitClassDecl(self, ast, o):
        memlist=list(filter(lambda x: type(x)==MethodDecl,ast.memlist))
        list(map(lambda t:self.visit(t,0),memlist))
        return 0
    def visitMethodDecl(self, ast , o):
        self.visit(ast.body,0)
        return 0
    def visitBlock(self, ast , o):
        list(map(lambda t:self.visit(t,o),ast.stmt))
        return 0
    def visitAssign(self, ast, param):
        return 0
    def visitReturn(self, ast, param):
        return 0
    def visitCallStmt(self, ast, param):
        return 0

    def visitIf(self, ast , o):
        self.visit(ast.thenStmt,o)
        if ast.elseStmt:
            self.visit(ast.elseStmt,o)
        return 0
    
    def visitFor(self, ast , o):
        self.visit(ast.loop,1)
        o=0
        return 0
    
    def visitContinue(self, ast , o):
        if o==0:
            raise MustInLoop(ast)
        return 0
    
    def visitBreak(self, ast , o):
        if o==0:
            raise MustInLoop(ast)
        return 0
      