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

from main.bkool.utils.AST import Assign, Stmt
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
    def __init__(self,ast):
        self.ast = ast
        self.o=StaticChecker.global_envi
        self.getName=GetName()
        self.bl=0
        #self.f = open("dictionary","w")
        #self.f.write("")
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast,  o): 
        """Handle type, value, redeclare"""
        #raise Redeclared(Variable(),"Con")
        GetFor().visit(self.ast,{})
        o={"io":{"mem":{}}}
        o["io"]["mem"]={
            "readInt":{
                "param":{},
                "rType":"int"
            }
        }
        o=self.getName.visit(ast,o)
        env={"global":o}
        
        for x in ast.decl:
            self.visit(x, env)
        return o
    #   res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    
    def visitClassDecl(self, ast,  o):
        #TODO
        #raise Undeclared(Class(),str(type(ast)))
        env={
            "global":o["global"],
            "current":o["global"][ast.classname.name]
        }
        list(map(lambda x: self.visit(x,env),filter(lambda t: type(t) is AttributeDecl,ast.memlist)))
        #inheritance
        if ast.parentname:
            env["current"]["mem"].update({map(filter(lambda x: x not in env["current"]["mem"]))})
        list(map(lambda x: self.visit(x,env),filter(lambda t: type(t) is MethodDecl,ast.memlist)))
        return o
    def visitMethodDecl(self, ast , o):
        #should local:{"code":self.visit(ast.kind)}
        #raise Undeclared(Class(), str(o))
        
        env={
            "global":o["global"],
            "current":o["current"]["mem"][ast.name.name]
        }
        env["current"]["rType"]=self.visit(ast.returnType,env)
        env["current"]["param"]={}
        env["current"]["bl"+str(self.getName.bl)]={}
        param=list(map(lambda x: env["current"]["param"].update(self.getName.visit(x,env["current"])),ast.param))#"""env["local"]"""
        #TODO check type param of class
        err=list(filter(lambda x: len(x)>1,param))
        if err:
            raise Redeclared(Parameter(),err[0]["Redeclare"].name) 
        #get value for param
        list(map(lambda x:self.visit(x,env["current"]["param"]),ast.param))
        self.visit(ast.body,env)
    
    def visitAttributeDecl(self, ast , o):
        return self.visit(ast.decl,o)
    def visitBlock(self, ast , o):
        self.bl+=1
        env={
            "global":o["global"],
            "current":o["current"]
        }
        env["current"]["bl"+str(self.bl-1)]["var"]={}
        bl=self.getName.visit(ast,env)
        env["current"]["parent"]=env["current"]
        env["current"]=env["current"][bl]
        
        list(map(lambda x: self.visit(x,env),ast.decl))
        
        list(map(lambda x: self.visit(x,env),ast.stmt))
        """ """   
        
        raise TypeMismatchInStatement("L"+str(env))
        list(map(lambda x: self.visit(x,env),ast.decl))
        #to get list of 
        list(map(lambda x: self.visit(x,env),ast.stmt))
        #To handle undeclare ID
        #return None
    #TODO we have code in o, we have to assign type and value
    def visitVarDecl(self, ast, o):
        #every variable has these field
        #o of this object is {}
        #To chuc luu tru cho var_const_static_expr
        
        env={
            "global":o["global"],
            "current":o["current"]
        }
        #raise Undeclared(Class(), str(o))
        rType=self.visit(ast.varType,o)
        val = self.visit(ast.varInit,env)if ast.varInit else None
        
        if rType!=val:
            raise TypeMismatchInStatement(ast)
        env["current"]["var"][ast.variable.name]["rType"]= rType
        env["current"]["var"][ast.variable.name]["val"]= val
        return env["current"]["var"][ast.variable.name]
        
    def visitConstDecl(self, ast, o):
        env={
            "global":o["global"],
            "current":o["current"]["var"]
        }  
        val=Field(self.visit(ast.constType),self.visit(ast.value)if ast.value else None)
        if val.value is None:
            raise IllegalConstantExpression(ast)
        #TODO
        # check static expr elif o[val.value
        if val.typ!=val.value:
            raise TypeMismatchInConstant(ast)
        env["current"][ast.name]["val"]= val
        return env["current"][ast.name]
    def visitBinaryOp(self, ast , o):
        r=self.visit(ast.right,o)
        l=self.visit(ast.left,o)
        op=ast.op
        core=["+","-","*","/","<","<=",">",">="]
        #TODO: check type of left+right+op
        if op in core:
            #do core
            if r == "float":
                if l == "int":
                    l="float"
            elif l=="float":
                if r=="int":
                    r="float"
        if op in [">","<",">=","<="]:
            if r in ["int","float"]:
                return "bool" 
        if op =="/":
            return "float"
        if r==l:
            if op in ["==","!="]:
                if r in ["int","bool"]:
                    return "bool"
            elif op in ["+","-","*"]  :
                return r
            elif op in ["""\"""","%"]:
                if r=="int":
                    return r
            elif op in["^"]:
                return "string"
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast , o):
        ex=self.visit(ast.body,o)
        if ast.op in ["!"]:
            if ex=="bool":
                return ex
        elif ast.op in ["+","-"]:
            if ex in ["float","int"]:
                return ex
        return None
    
    def visitCallExpr(self, ast , o):
        obj=self.visit(ast.obj,o)
        """if not o["global"][obj]:
            raise TypeMismatchInExpression(ast)"""
        med=self.visit(ast.method,o[obj])
        if med=="void":
            raise TypeMismatchInExpression(ast)
        #param=list(map(lambda x: self.visit(x,o),ast.param))
        #lấy list expr check với def của method
        #err=list(map(filter(lambda x,y: x!=y, (param,o[med]["param"]))))
        #if err:
        #    raise TypeMismatchInExpression(ast)
        list(map(lambda x,y: self.visitAssign((self.visit(x,o),y),o), ast.param,o[med]["param"]))       
    
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
        if self.visit(ast.idx,o) != "int":
            raise TypeMismatchInExpression(ast)
        arr=self.visit(ast.arr,o)
        typearr=arr.find("[")
        if typearr==-1:
            raise TypeMismatchInExpression(ast)
        return arr[0:typearr-1]
    
    def visitFieldAccess(self, ast , o):
        obj=self.visit(ast.obj,o)
        """if not o["global"][obj]:
            raise TypeMismatchInExpression(ast)"""
        #TODO check ID
        field=o[obj]["mem"][ast.fieldname.name]
        if field["code"]>1:
            raise IllegalMemberAccess(ast)
        return field["field"].typ
         
    def visitIf(self, ast , o):
        if(self.visit(ast.expr)!="bool"):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,o)
        if ast.elseStmt:
            self.visit(ast.elseStmt,o)
    
    def visitFor(self, ast , o):
        env=o
        env["local"]={"var":ast.name}
        #scalar has type int
        if not (self.visit(ast.expr1)==self.visit(ast.expr2)=="int"):
            raise TypeMismatchInStatement(ast.name+":="+ast.exp1)
        self.visit(ast.loop)
    def visitContinue(self, ast , o):
        pass
    
    def visitBreak(self, ast , o):
        pass
    
    def visitReturn(self, ast , o):
        r=self.visit(ast.expr,o)
        #TODO trace back the type of current method
        l=o["current"]["rType"]
        if l=="void":
            raise TypeMismatchInStatement(ast)
        if r!=l:
            if r=="int" and l=="float":
                pass
            #TODO check ông nội
            if r in o["global"]:
                if o[r]["parent"]==l:
                    pass
            elif r.find("int[")!=-1 and l=="float":
                pass

            else:
                #TODO raise sai r nè
                raise TypeMismatchInStatement(str(ast)) 
        raise TypeMismatchInStatement("M"+str(o))
    def visitAssign(self, ast , o):
        
        r=self.visit(ast.exp,o) if type(ast) is Stmt else ast[0]
        l=self.visit(ast.lhs,o) if type(ast) is Stmt else ast[1]
        if l=="void":
            raise TypeMismatchInStatement(ast)
        if r!=l:
            if r=="int" and l=="float":
                pass
            #TODO check ông nội
            if r in o["global"]:
                if o[r]["parent"]==l:
                    pass
            elif r.find("int[")!=-1 and l=="float":
                pass

            else:
                #TODO raise sai r nè
                raise TypeMismatchInStatement(str(ast)) 
        #TODO r là type làm s mà có name
        if o[r.name]["code"]>1:
            #const
            raise CannotAssignToConstant(ast)
         
    def visitCallStmt(self, ast , o):
        obj=self.visit(ast.obj,o)
        #check class type
        if not o[obj]:
            raise Undeclared(Class(),obj)
        med=self.visit(ast.method,o[obj])
        if med != "void":
            raise TypeMismatchInStatement(ast)
        #param=list(map(lambda x: self.visit(x,o),ast.param))
        #lấy list expr check với def của method
        list(map(lambda x,y: self.visitAssign((self.visit(x,o),y),o), ast.param,o[med]["param"]))       
    
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
    def __init__(self):
        self.bl=0
        
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
                "parent": par.name,
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
    def visitBlock(self, ast, o):
        o["current"]["bl"+str(self.bl)]={
            "parent": o["current"],
            "rType":o["current"]["rType"],
            "var"  : {}
        }
        #raise TypeMismatchInStatement("HE"+str(o))
        for x in ast.decl:
            var=self.visit(x,o["current"]["bl"+str(self.bl)]["var"])
            if len(var)>1:
                raise Redeclared(Variable(),var.variable.name) 
        self.bl+=1
        return "bl"+str(self.bl-1)
        #return o
    def visitMethodDecl(self, ast, o):
        if ast.name.name in o:
            raise Redeclared(Method(),ast.name.name)
        o[ast.name.name]={"code":self.visit(ast.kind,o)}
        #return o
        
        o[ast.name.name]={
            "param"  : {}
        }
        for x in ast.param:
            res=self.visit(x,o[ast.name.name]["param"])
            if len(res)>1: 
                raise Redeclared(Parameter(),res["Redeclare"].name)
        #self.visit(ast.body, o)
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
      