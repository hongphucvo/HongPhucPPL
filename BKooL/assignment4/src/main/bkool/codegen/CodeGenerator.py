from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import * 
from AST import *

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
                    Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName))
                    ,Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
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
        
    # decl : List[ClassDecl]
        [self.visit(i,c)for i in ast.decl]
        return c#null

    def visitClassDecl(self,ast,c):
    # classname : Id
    # memlist : List[MemDecl]
    # parentname : Id = None # None if there is no parent
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))#check parent
        [self.visit(ele, SubBody(None, self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        # check default
        self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), c, Frame("<init>", VoidType() ))
        self.emit.emitEPILOG()
        return c#null

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None# methodName = "<init>" if isInit else consdecl.name.name
        #57:00 init: tên + return type
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.typ,consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(consdecl.name.name, mtype, not isInit,frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0,StringType()), frame.getStartLabel(), frame.getEndLabel(),frame))
        else:
            local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            glenv = local.sym+glenv
        
        body = consdecl.body



        #get local env
        #TODO





        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # void type k return cũng đc hmihmi 
        # nên là phải bổ sung sự return cho nó nè
        # bắt nó chấm dút cuột tình
        # 
        #     
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitMethodDecl(self, ast, o):
    #     kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # returnType: Type  # None for constructor
    # body: Block
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name,nenv),None)
        #hàm gì đây, s trả đc sym hay v
        #TODO
        cname = sym.value.value    
        ctype = sym.mtype
        in_ = ("", list())
        #lấy param vô stack nè
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        
        







        #TODO check type static chpo kĩ
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))



    
    def visitVarDecl(self,ast,o):
        return None
    
    def visitConstDecl(self,ast,o):
        return None
    
    def visitStatic(self,ast,o):
        return None
    
    def visitInstance(self,ast,o):
        return None
    
    def visitAttributeDecl(self,ast,o):
    #     kind: SIKind #Instance or Static
    # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
    
        return None
    
    def visitIntType(self,ast,o):
        return None
    
    def visitFloatType(self,ast,o):
        return None
    
    def visitBoolType(self,ast,o):
        return None
    
    def visitStringType(self,ast,o):
        return None
    
    def visitVoidType(self,ast,o):
        return None
    
    def visitArrayType(self,ast,o):
    #  size : int
    # eleType:Type
        return None
    
    def visitClassType(self,ast,o):
        # classname:Id
        return None
    
    def visitBinaryOp(self,ast,o):
        return None
    
    def visitUnaryOp(self,ast,o):
        return None
    
    def visitCallExpr(self,ast,o):
        return None
    
    def visitNewExpr(self,ast,o):
        return None
    
    def visitId(self,ast,o):
        return None
    
    def visitArrayCell(self,ast,o):
        return None
    
    def visitFieldAccess(self,ast,o):
        return None
    
    def visitBlock(self,ast,o):
        return None
    
    def visitIf(self,ast,o):
        return None
    
    def visitFor(self,ast,o):
        return None
    
    def visitContinue(self,ast,o):
        return None
    
    def visitBreak(self,ast,o):
        return None
    
    def visitReturn(self,ast,o):
        return None
    
    def visitAssign(self,ast,o):
        return None
    
    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o.frame),IntType()
    def visitBinaryOp(self, ast, o):
        e1c,e1t = self.visit(ast.left,o)
        e2c,e2t = self.visit(ast.right,o)
        return e1c + e2c + self.emit.emitADDOP(ast.op,e1t,o.frame),e1t
    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()

    
    def visitBooleanLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(str(ast.value).lower(), IntType(), o.frame), BoolType()
    
    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    
    def visitNullLiteral(self,ast,o):
        return self.emit.emitPUSHCONST("", NullType(), o.frame)
    
    def visitSelfLiteral(self,ast,o):
        return self.emit.emitREADVAR(0, "this", ClassType(self.className), o.frame)
        
    def visitArrayLiteral(self,ast,o):
        return None 
    
    
class GetName(BaseVisitor):
    """Get the name and SIKind in code"""
    def visitProgram(self, ast,  o):
        list(map(lambda x: self.visit(x,o),ast.decl))
        return o
    def visitClassDecl(self, ast,  o):
        classenv=[]
        #TODO check parent
        return [ast.classname.name,[map(lambda x: self.visit(x,classenv),ast.memlist)]]
    def visitAttributeDecl(self, ast, o):
        return self.visit(ast.decl,o)
    def visitVarDecl(self, ast, o):
        return ast.variable.name
    def visitConstDecl(self, ast, o):
        return ast.constant.name
    def visitBlock(self, ast, o):
        return [map(lambda x: self.visit(x,o),ast.decl)]
    def visitMethodDecl(self, ast, o):
        newenv=[]
        return [ast.name.name,[map(lambda x: self.visit(x,newenv),ast.param)]]
    def visitInstance(self, ast , o):
        return 0
    def visitStatic(self, ast, o):
        return 2
################################################################################
