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
    def __init__(self,ast):
        self.ast = ast
        self.o=StaticChecker.global_envi
        self.getName=GetName()
        self.bl=0
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast,  o): 
        GetFor().visit(self.ast,{})
        o={"io": {"mem":
            {
                "readInt":{"param":{},
                            "rType":"int"},
                "writeInt":{"param":{"anArg":{"rType":"int"}},
                            "rType":"void"},
                "writeIntLn":{"param":{"anArg":{"rType":"int"}},
                            "rType":"void"},
                "readBool":{"param":{},
                            "rType":"bool"},
                "writeBool":{"param":{"anArg":{"rType":"bool"}},
                            "rType":"void"},
                "writeBoolLn":{"param":{"anArg":{"rType":"bool"}},
                            "rType":"void"},
                "readFloat":{"param":{},
                            "rType":"float"},
                "writeFloat":{"param":{"anArg":{"rType":"float"}},
                            "rType":"void"},
                "writeFloatLn":{"param":{"anArg":{"rType":"float"}},
                            "rType":"void"},            
                "readStr":{"param":{},
                            "rType":"string"},
                "writeStr":{"param":{"anArg":{"rType":"string"}},
                            "rType":"void"},
                "writeStrLn":{"param":{"anArg":{"rType":"string"}},
                            "rType":"void"}            
                }
            }
        }
        o=self.getName.visit(ast,o)
        env={"global":o}
        
        for x in ast.decl:
            self.visit(x, env)
        return ""
    def visitClassDecl(self, ast,  o):
        env={
            "global":o["global"],
            "current":o["global"][ast.classname.name]
        }
        list(map(lambda x: self.visit(x,env),filter(lambda t: type(t) is AttributeDecl,ast.memlist)))
        #inheritance
        if ast.parentname:
            for x in env["global"][ast.parentname.name]["mem"]:
                if x not in env["current"]["mem"]:
                    env["current"]["mem"].update({x:env["global"][ast.parentname.name]["mem"][x]})
        list(map(lambda x: self.visit(x,env),filter(lambda t: type(t) is MethodDecl,ast.memlist)))
        return o
    def visitMethodDecl(self, ast , o):        
        env={
            "global":o["global"],
            "current":o["current"]["mem"][ast.name.name]
        }
        env["current"]["rType"]=self.visit(ast.returnType,env)
        env["current"]["param"]={}
        env["current"]["bl"+str(self.getName.bl)]={}
        
        for key,value in env["global"].items():
            if env["global"][key]["mem"].get(ast.name.name) is not None:
                env["current"]["parent"] = {"classType":key}
        for x in ast.param:
            par=self.getName.visit(x,env["current"]["param"])
            if len(par)>1:
                raise Redeclared(Parameter(),x.name)
            par.update({"rType":self.visit(x.varType,env)})
            if x.varInit:
                val=self.visit(x.varInit,env)
                if par["rType"] !=val:
                    raise TypeMismatchInStatement(str(ast))
                else: 
                    par.update({"val": val})
        self.visit(ast.body,env)
    
    def visitAttributeDecl(self, ast , o):
        return self.visit(ast.decl,o)
    def visitBlock(self, ast , o):
        
        self.bl+=1
        env={
            "global":o["global"],
            "current":o["current"]
        }
        env["current"]["bl"+str(self.bl-1)]={"mem":{}}
        bl=self.getName.visit(ast,env)
        env["current"]["classType"]=env["current"]["parent"]["classType"]
        env["current"]["parent"]=env["current"]
        env["current"]=env["current"][bl]
        list(map(lambda x: self.visit(x,env),ast.decl))
        list(map(lambda x: self.visit(x,env),ast.stmt)) 
    def visitVarDecl(self, ast, o):
        
        env={
            "global":o["global"],
            "current":o["current"]
        }
        rType=self.visit(ast.varType,o)
        val = self.visit(ast.varInit,env)if ast.varInit else None
        if val and rType!=val:
            raise TypeMismatchInStatement(ast)
        cur=env["current"]["mem"][ast.variable.name]
        cur.update({"rType":rType})
        cur.update({"val": val})
        return env["current"]["mem"][ast.variable.name]
        
    def visitConstDecl(self, ast, o):
        self.statconst=True
        env={
            "global":o["global"],
            "current":o["current"]
        }
        rType=self.visit(ast.constType,o)
        val = self.visit(ast.value,env)if ast.value else None
        #raise IllegalConstantExpression("M"+str(ast))
        if val is None:
            raise IllegalConstantExpression(ast)
        #TODO
        # check static expr elif o[val.value
        if self.statconst==False:
            raise IllegalConstantExpression(ast.value)
        if rType!=val:
            raise TypeMismatchInConstant(ast)
        cur=env["current"]["mem"][ast.constant.name]
        cur.update({"rType":rType})
        cur.update({"val": val})
        return env["current"]["mem"][ast.constant.name]
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
            elif op in ["||","&&"]:
                if r=="bool":
                    return r
        
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast , o):
        ex=self.visit(ast.body,o)
        if ast.op in ["!"]:
            if ex=="bool":
                return ex
        elif ast.op in ["+","-"]:
            if ex in ["float","int"]:
                return ex
        raise TypeMismatchInExpression(ast)
    
        
    def visitCallStmt(self, ast , o):
        obj=self.visit(ast.obj,o)
        #check class type
        if not o["global"][obj]:
            raise Undeclared(Class(),obj)
        med=self.visit(ast.method,o["global"][obj])
        if med != "void":
            raise TypeMismatchInStatement(ast)
        param=o["global"][obj]["mem"][ast.method.name]["param"]
        #raise TypeMismatchInStatement(str(param))
        for idx,x in enumerate(param):
            argType=self.visit(ast.param[idx],o)
            paramType=param[x]["rType"]
            if argType!=paramType:
                if argType=="int" and paramType=="float":
                    pass
                else: 
                    raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast , o):
        obj=self.visit(ast.obj,o)
        if not o["global"][obj]:
            raise Undeclared(Class(),obj)
        med=self.visit(ast.method,o["global"][obj])
        if med=="void":
            raise TypeMismatchInExpression(ast)
        param=o["global"][obj]["mem"][ast.method.name]["param"]
        for idx,x in enumerate(param):
            argType=self.visit(ast.param[idx],o)
            paramType=param[x]["rType"]
            if argType!=paramType:
                if argType=="int" and paramType=="float":
                    pass
                else: 
                    raise TypeMismatchInStatement(ast)

        return med
    
    def visitNewExpr(self, ast , o):
        classname=ast.classname
        param=o["global"][classname]["mem"][ast.method.name]["param"]
        for idx,x in enumerate(param):
            argType=self.visit(ast.param[idx],o)
            paramType=param[x]["rType"]
            if argType!=paramType:
                if argType=="int" and paramType=="float":
                    pass
                else: 
                    raise TypeMismatchInStatement(ast)
        return classname.name
    
    def visitArrayCell(self, ast , o):
        if self.visit(ast.idx,o) != "int":
            raise TypeMismatchInExpression(ast)
        arr=self.visit(ast.arr,o)
        typearr=arr.find("[")
        if typearr==-1:
            raise TypeMismatchInExpression(ast)
        return arr[0:typearr]
    
    def visitFieldAccess(self, ast , o):
        obj=self.visit(ast.obj,o)
        field=o["global"][obj]["mem"]
        
        if field.get(ast.fieldname.name) is not None:
            fieldloc=field[ast.fieldname.name]
            if fieldloc["code"]%2==0:
                self.statconst=False
            if fieldloc["code"]<2:
                return fieldloc["rType"]
        if ast.obj.name:
            if obj==ast.obj.name:
                if field.get(ast.fieldname.name) is not None:
                    fieldloc=field[ast.fieldname.name]
                    if fieldloc["code"]%2==0:
                        self.statconst=False
                    if fieldloc["code"]>1:
                        return fieldloc["rType"]
        raise IllegalMemberAccess(ast)
         
    def visitIf(self, ast , o):
        if(self.visit(ast.expr,o)!="bool"):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,o)
        if ast.elseStmt:
            self.visit(ast.elseStmt,o)
    
    def visitFor(self, ast , o):
        if not (self.visit(ast.expr1,o)==self.visit(ast.expr2,o)=="int"):
            raise TypeMismatchInStatement(str(ast.id.name)+":="+str(ast.expr1))
        o["current"]={"mem":{
            ast.id.name:{"rType":"int","val":"int"} }
        }
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
        #raise TypeMismatchInStatement("M"+str(o))
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
                if o[r]["parent"]==l:
                    pass
            elif r.find("int[")!=-1 and l=="float":
                pass
            else:
                #TODO raise sai r nè
                raise TypeMismatchInStatement(str(ast)) 
        if type(ast.lhs) is Id:
            if o["global"][ast.lhs]["code"]%2==0:
                raise CannotAssignToConstant(ast)
    def visitId(self, ast , o):
        #handle undeclr
        
        env=o["current"]if o.get("current") else o
        if env.get("mem") is not None:
            if env["mem"].get(ast.name) is not None:
                return env["mem"][ast.name]["rType"]
        if ast.name in o["global"]:
            return ast.name
        raise Undeclared(Identifier(),ast.name) 
    
    def visitArrayLiteral(self, ast , o):
        value=list(map(lambda x: self.visit(x,o),ast.value))
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
        #raise IllegalArrayLiteral(str(o))
        
        env=o["current"]if o.get("current") else o
        while env.get("parent") is not None:
            if env["parent"].get("classType") is not None:
                return env["parent"]["classType"]
            env=env["parent"]
        return o["global"]
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
        return self.visit(ast.eleType,o)+"["+str(ast.size)+"]"
    
    def visitClassType(self, ast , o):
        return ast.classname.name
    






















class GetName(BaseVisitor):
    """Get the name and SIKind in code"""
    def __init__(self):
        self.bl=0

    def visitProgram(self, ast,  o):
        list(map(lambda x: self.visit(x,o),ast.decl))
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
                "parent": par,
                "mem":{}
            }
        else: 
            o[this]={
            "mem":{}
            }
            o[this]["current"]=o[this]
        if(len(ast.memlist)>0): 
            list(map(lambda x: self.visit(x,o[this]["mem"]),ast.memlist) )
        return o
    
    def visitAttributeDecl(self, ast, o):
        val=self.visit(ast.decl,o)
        if len(val)>1:
            raise Redeclared(Attribute(),str(ast.decl.variable.name))
        val["code"]+=self.visit(ast.kind,o)
        return val
    def visitVarDecl(self, ast, o):
        if ast.variable.name in o:
            o[ast.variable.name]["Redeclare"]=ast.variable
        else:
            o[ast.variable.name]={"code":0}
        return o[ast.variable.name]
        
    def visitConstDecl(self, ast, o):
        if ast.constant.name in o:
            raise Redeclared(Constant(),ast.constant.name)
        o[ast.constant.name]={"code":1}
        return o[ast.constant.name]
        
    def visitBlock(self, ast, o):
        o["current"]["bl"+str(self.bl)]={
            "parent": o["current"],
            "rType":o["current"]["rType"],
            "mem"  : {}
        }
        for x in ast.decl:
            var=self.visit(x,o["current"]["bl"+str(self.bl)]["mem"])
            if len(var)>1:
                raise Redeclared(Variable(),var.variable.name) 
        if o["current"].get("param"):
            o["current"]["bl"+str(self.bl)].update(o["current"]["param"])
        if o["current"].get("mem"):
            o["current"]["bl"+str(self.bl)].update(o["current"]["mem"])
        self.bl+=1
        raise Redeclared(Variable(),str(o)) 
        return "bl"+str(self.bl-1)
    def visitMethodDecl(self, ast, o):
        if ast.name.name in o:
            raise Redeclared(Method(),ast.name.name)
        o[ast.name.name]={
            "code":self.visit(ast.kind,o),
            "param"  : {}
        }
        for x in ast.param:
            res=self.visit(x,o[ast.name.name]["param"])
            if len(res)>1: 
                raise Redeclared(Parameter(),res["Redeclare"].name)
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
      