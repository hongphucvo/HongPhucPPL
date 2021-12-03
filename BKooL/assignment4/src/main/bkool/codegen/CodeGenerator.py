from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import * 
from AST import *
from Utils import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

from Emitter import Emitter

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    
                Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                
                Symbol("readBool", MType([], BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                
                Symbol("readStr", MType([], StringType()), CName(self.libName)),
                Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("writeStrLn", MType([StringType()], VoidType()), CName(self.libName)),]


    def gen(self, ast,path):
        #ast: AST
        #dir_: String

        gl = self.init()
        gl=GetName().visit(ast,[])+gl
        gc = CodeGenVisitor(ast, gl,path)
        gc.visit(ast, None)



class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env,path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i,c)for i in ast.decl]
        return c

    def visitClassDecl(self,ast,c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # generate default constructor
        #init handle putfield .field final d=1 .field z=1
        #đưa hết vô params
        #nếu có cons rồi thì đừng genauto nữa :"))
        self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), c, Frame("<init>", VoidType() ))
        ### Tới method bth
        
        # [self.visit(ele, c) for ele in ast.memlist if type(ele) == MethodDecl]
        [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
       


        #clinit handle put static cho .field static y=1, chơi luôn final đi
        
        
        
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.typ,consdecl.param))
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit,frame))
        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame))
            #emit gán giá trị cho non static

        #Check clinit gán giá trị cho static
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0,StringType()), frame.getStartLabel(), frame.getEndLabel(),frame))
        else:
            local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            glenv = local.sym+glenv
        
        #



        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
       
        self.visit(body,SubBody(frame, glenv))
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))
    def visitAttributeDecl(self,ast,o):
    #     kind: SIKind #Instance or Static
    #   decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        field=ast.decl
        if type(ast.kind) is Static:
            if type(field)is VarDecl:
                self.emit.emitSTATICATTRIBUTE(field.name.name,field.varType,False)

                #varInit maybe None
            else:
                self.emit.emitSTATICATTRIBUTE(field.name.name,field.varType,False,field.varInit)





        return None
    def visitVarDecl(self,ast,o):
        
    # variable : Id
    # varType : Type
    # varInit : Expr = None # None if there is no initial
        
        subctxt = o
        frame = subctxt.frame
        mtype = ast.varType
        name = ast.variable.name

        # if frame is None:
        #     # Decl mot bien global
        #     self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, False, ""))
        #     return SubBody(None, [Symbol(name, mtype, CName(self.className))] + subctxt.sym)
        # else:
            # Decl mot bien local hoac param
        print(name)
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, [Symbol(name, mtype, Index(idx))] + subctxt.sym)









































    def visitBlock(self,ast,o):
        
    # decl:List[StoreDecl]
    # stmt:List[Stmt]
    # TODO
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        frame.enterScope(False)
        # generate code for statements
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),ctxt.decl,SubBody(frame,[]))
        nenv = local.sym+nenv
        # [map(lambda x: self.visit(x,SubBody(frame,nenv)),ast.decl)]
        # [map(lambda x: print("HERE"),ast.decl)]
        # print("HERE")# testing
        [map(lambda x: self.visit(x,nenv),ast.stmt)]
        #ast.decl.foreach(x => visit(x, blockContext).asInstanceOf[SimpleSymbol])
        # ast.stmt.map(x => visit(x, blockContext))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()    
        return None
    
    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name,nenv),None)
        cname = sym.value.value    
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
    def visitReturn(self,ast,o):
        
    # expr:Expr
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        typ1=VoidType()
        if ast.expr is not None:
            str1, typ1 = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(frame.returnType) is FloatType:
                str1 += self.emit.emitI2F(frame)
            self.emit.printout(str1)
        self.emit.printout(self.emit.emitRETURN(typ1, frame))        
        #TODO: GOTO or not GOTO
        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))

    def visitBinaryOp(self, ast, o):
        e1c,e1t = self.visit(ast.left,o)
        e2c,e2t = self.visit(ast.right,o)
        return e1c + e2c + self.emit.emitADDOP(ast.op,e1t,o.frame),e1t


    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o.frame),IntType()
    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()
    def visitBooleanLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
    # def visitBooleanLiteral(self,ast,o):
    #     return self.emit.emitPUSHCONST(str(ast.value).lower(), StringType(), o.frame), BoolType()
        # return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()
 
    





  
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"
  
class GetName(BaseVisitor):
    def visitProgram(self, ast,  o):
        return list(map(lambda x: self.visit(x,o),ast.decl))
    def visitClassDecl(self, ast,  o):
        #TODO check parent
        return [ast.classname.name,[map(lambda x: self.visit(x,ast.classname.name),ast.memlist)]]
    def visitAttributeDecl(self, ast, o):
        return self.visit(ast.decl,o)
    def visitVarDecl(self, ast, o):
        # return ast.variable.name
        return Symbol(ast.variable.name,MType([],ast.varType),Index(ast.varInit))
    def visitConstDecl(self, ast, o):
        return Symbol(ast.constant.name,MType([],ast.constType),Index(ast.value))
    def visitBlock(self, ast, o):
        return [map(lambda x: self.visit(x,o),ast.decl)]
    def visitMethodDecl(self, ast, o):
        return Symbol(ast.name.name,MType([map(lambda x: self.visit(x,o),ast.param)],ast.returnType),CName(o))
        # [ast.name.name,[map(lambda x: self.visit(x,newenv),ast.param)]]
