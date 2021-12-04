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
        self.emit.printout(self.emit.emitPROLOG(self.className, ast.parentname.name if(ast.parentname) else "java.lang.Object"))
        # map(lambda x: print(x),self.env)
        
        # print(self.env[0])
        #field decl
        [map(lambda x: self.visit(x,c) ,filter(lambda x: type(x) is AttributeDecl,ast.memlist))]
        
        
        #init handle putfield .field final d=1 .field z=1
        #đưa hết vô params
        #nếu có cons rồi thì đừng genauto nữa :"))
        mem=list(filter(lambda x: x.value.value==ast.classname.name,self.env))
        # self.lookup(ast.classname.name,self.env,lambda x: x.value.value)
        # print
        init=self.lookup("<init>",mem,lambda x: x.name)
        if not init:
        # if "<init>" not in mem:
            self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), self.env, Frame("<init>", VoidType() ))
        ### Tới method bth
        
        # [self.visit(ele, c) for ele in ast.memlist if type(ele) == MethodDecl]
        # [map(lambda x:self.visit(x,SubBody(None, self.env)),[filter(lambda mem: type(mem)is MethodDecl, ast.memlist)])]
       
        [self.visit(ele, SubBody(Frame(ele.name, ele.returnType), self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
      
        self.genCLINITMETHOD(MethodDecl(Instance(),Id("<clinit>"), list(), None,Block([],[])), c, Frame("<clinit>", VoidType() ))
        #TODO clinit handle put static cho .field static y=1, chơi luôn final đi
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #included default init and init
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        # methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.typ,consdecl.param))
        mtype = MType(intype, returnType)
        isStatic=True if isMain else \
            False if isInit else type(consdecl.kind) is Static
        self.emit.printout(self.emit.emitMETHOD(consdecl.name.name, mtype, isStatic,frame))
        frame.enterScope(True)

        glenv = o
        # print(glenv)

        # map(lambda x: print(str(x)),glenv)
        # Generate code for parameter declarations
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0,StringType()), frame.getStartLabel(), frame.getEndLabel(),frame,False))
        else:
            if isInit:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame,False))
            # index = frame.getNewIndex()
            # emitter.printout(emitter.emitVAR(x.index, x.name, x.dataType.get, frame.getStartLabel(), frame.getEndLabel(), frame))
            # Đoạn cmt nằm trong visit vardecl
            # local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            
        # reduce (lambda env,x:self.visit(x,SubBody(frame,env))+env,consdecl.param,glenv)
        local = list(map(lambda x: self.visit(x,SubBody(frame,glenv)),consdecl.param))
        glenv=local+glenv
            # map(lambda x: print(str(x)),glenv)
            # glenv = local+glenv
        
        #



        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
        # // call super's constructor
        # emitter.printout(emitter.emitREADVAR(0, "this", ClassType(className), frame))
        # //: call super's constructor: <methodType>???
        # emitter.printout(emitter.emitINVOKESPECIAL(superClass + "/<init>", if (superClass == "java/lang/Object") MethodType(List(), VoidType) else methodType, frame))
        # emitter.printout("\n")
        #first in init

            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            # emitter.printout(emitter.emitFieldInitialization(className, init, clinit = false, frame = frame))
    
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.decl))
        local = list(map(lambda x: self.visit(x,SubBody(frame,glenv)),body.decl))
        glenv=local+glenv
        
        # reduce (lambda env,x:[self.visit(x,SubBody(frame,env))]+env,body.decl,glenv)
        # for x in glenv:
        #     print(x)
        #     print("JKASDJKAS")
        # print("hmihmi")
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    def genCLINITMETHOD(self, consdecl, o, frame):
        #included default init and init
        isInit = True
        isMain = False
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True,frame))
        frame.enterScope(True)
        
        
        #field init value for static
        # self.emit.printout(self.emit.emitFieldInitialization(self.className, true, frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    # def genDEFAULTINITMETHOD(self, consdecl, o, frame):
    #     #included default init and init
    #     isInit = True
    #     self.emit.printout(self.emit.emitMETHOD("<init>", MType([ClassType(self.className)], VoidType()), False,frame))
    #     frame.enterScope(True)
    #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame))
        
        
        
    #     #TODO emit gán giá trị cho non static

    #     self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

    #     # Generate code for statements
    #     if isInit:
    #         self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
    #         self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
       
    #     self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
    #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
    #     self.emit.printout(self.emit.emitENDMETHOD(frame))
    #     frame.exitScope()
    
    def visitMethodDecl(self, ast, o):
        # frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, o.frame)
        # return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))
      
    # def visitAttributeDecl(self,ast,o):
    #     kind: SIKind #Instance or Static
    #   decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        # field=ast.decl
        # # if type(ast.kind) is Static:
        # if type(field)is VarDecl:
        #     self.emit.emitATTRIBUTE(field.name.name,field.varType,False)

    #     return None
    def visitVarDecl(self,ast,o):
        #TODO: value init
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
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame,False))
        return Symbol(name, mtype, Index(idx))

        # return SubBody(frame, [Symbol(name, mtype, Index(idx))] + subctxt.sym)

    #     return None

    def visitConstDecl(self,ast,o):
          #TODO: chưa handle 
          #TODO: value in code
    # constant : Id
    # constType : Type
    # value : Expr
        
        subctxt = o
        frame = subctxt.frame
        mtype = ast.constType
        name = ast.constant.name
        val=ast.value

        # if frame is None:
        #     # Decl mot bien global
        #     self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, False, ""))
        #     return SubBody(None, [Symbol(name, mtype, CName(self.className))] + subctxt.sym)
        # else:
            # Decl mot bien local hoac param
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitCONST(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, [Symbol(name, mtype, Index(idx))] + subctxt.sym)
    def visitFieldAccess(self,ast,o):
        #TODO 
        pass

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
        # val caller = visit(ast.parent, AccessContext(context, isLhs = false, isFirstAccess = true)).asInstanceOf[DataObject]
        # emitter.printout(caller.code)

        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
    
    def visitFor(self,ast,o):
    # id:Id
    # expr1:Expr
    # expr2:Expr
    # up: bool #True => increase; False => decrease
    # loop:Stmt  
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        label1 = frame.getNewLabel()

        frame.enterLoop()
        accessT = Access(frame, nenv, True, True)
        accessF = Access(frame, nenv, False, True)
        # Gan gia tri expr1 cho id
        expr1, _ = self.visit(ast.expr1, accessF)
        id1, _ = self.visit(ast.id, accessT)

        #TODO: Assign expr to 1 and 2



        self.emit.printout(expr1)
        self.emit.printout(id1)
        # In ra label 1
        self.emit.printout(self.emit.emitLABEL(label1, frame))

        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()

        id1, _ = self.visit(ast.id, accessF)
        self.emit.printout(id1)
        expr2, _ = self.visit(ast.expr2, accessF)
        self.emit.printout(expr2)
        if ast.up is True:
            self.emit.printout(self.emit.emitIFICMPGT(labelBreak, frame))
        else:
            self.emit.printout(self.emit.emitIFICMPLT(labelBreak, frame))

        self.visit(ast.loop,o)
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))

        if ast.up: 
        # i + 1 dat len stack
            expr, _ = self.visit(BinaryOp( '+', ast.id, IntLiteral(1)), accessF)
        else:
            expr, _ = self.visit(BinaryOp('-', ast.id, IntLiteral(1)), accessF)
            
        # Gan gia tri tren stack vao Id
        id2, _ = self.visit(ast.id, accessT)
        self.emit.printout(expr)
        self.emit.printout(id2)
        
        # quay lai label1
        self.emit.printout(self.emit.emitGOTO(label1, frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()
    
        return None
    
    def visitContinue(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
    
    def visitBreak(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
    
    
    def visitIf(self,ast,o):
    #     expr:Expr
    # thenStmt:Stmt
    # elseStmt:Stmt = None # None if there is no else branch
        e1c,e1t=self.visit(ast.expr,Access(o.frame,o.sym,False))
        self.emit.printout(e1c)
        falseLable=o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLable,o.frame))
        self.visit(ast.tstmt,o)
        
        if not ast.estmt:
            self.emit.printout(self.emit.emitLABEL(falseLable,o.frame))
        else:
            endelse=o.frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(endelse,o.frame))
            self.emit.printout(self.emit.emitLABEL(falseLable,o.frame))
            self.visit(ast.estmt,o)
            self.emit.printout(self.emit.emitLABEL(endelse,o.frame))
  
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

    
    def visitAssign(self,ast,o):
    # lhs:Expr
    # exp:Expr
    
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # if type(ast.lhs) is ArrayCell:
        #     # gan mot gia tri cho mot index expression.
        #     lc, lt = self.visit(ast.lhs, Access(frame, nenv, True, True))
        #     self.emit.printout(lc)
        #     rc, rt = self.visit(ast.exp, Access(frame, nenv, False, True))
        #     self.emit.printout(rc)
        #     if type(lt) != type(rt):
        #         self.emit.printout(self.emit.emitI2F(frame))
        #     self.emit.printout(self.emit.emitASTORE(lt, frame))          
        # else:
            # gan mot gia tri cho mot bien
        rc, rt = self.visit(ast.exp, Access(frame, nenv, False, True))
        lc, lt = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if type(rt) is IntType and type(lt) is FloatType:
            rc += self.emit.emitI2F(frame)
        print(rc+lc)
        self.emit.printout(rc + lc)

        # return None
    

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        leftVal,leftType = self.visit(ast.left,o)
        rightVal,rightType = self.visit(ast.right,o)
    #      op:str
    # left:Expr
    # right:Expr
        eqOp=[ "==" , "!=" ]
        shortOP=['&&','||']
        corrList=['+',' -', '*' ,'/' ,'<' ,'<=' ,'>', '>=']
        corrType=[IntType(),FloatType()]
        if ast.op in corrList:
            if leftType!=rightType:
                if leftType is FloatType:
                    rightVal +=self.emit.emitI2F(frame)
                    rightType=FloatType
                else:
                    leftVal += self.emit.emitI2F(frame)
                    leftType=FloatType
            if leftType is FloatType or rightType is FloatType or ast.op=='/' :
                rType=FloatType
            else:
                rType = IntType
            if ast.op in ['+','-']:
                return leftVal + rightVal+ self.emit.emitADDOP(ast.op, rType, frame), rType
            elif ast.op in ['*','/']:
                return leftVal + rightVal+ self.emit.emitMULOP(ast.op, rType, frame), rType
            # elif ast.op=='/':
            #     return leftVal + rightVal+ self.emit.emitMULOP(ast.op, rType, frame), rType
            elif ast.op in ['<' ,'<=' ,'>', '>=']:
                if type(rType) is FloatType:
                    return self.emit.emitRELOP(ast.op, leftVal, rightVal, frame), BoolType()
                return self.emit.emitREOP(ast.op, leftVal, rightVal, frame), BoolType()
        elif ast.op in eqOp:
            if type(leftType) is FloatType:
                return self.emit.emitRELOP(ast.op, leftVal, rightVal, frame), BoolType()
            return self.emit.emitREOP(ast.op, leftVal, rightVal, frame), BoolType()
        elif ast.op in shortOP:
            if ast.op=='&&':
                labelFalse = frame.getNewLabel()
                labelTrue = frame.getNewLabel()
                leftVal+=self.emit.emitIFFALSE(labelFalse,frame)
                rightVal+=self.emit.emitIFFALSE(labelFalse,frame)
                con=self.emit.emitPUSHICONST("true", frame)+self.emit.emitGOTO(labelTrue,frame) + self.emit.emitLABEL(labelFalse,frame)
                brk=self.emit.emitPUSHICONST("false", frame)+self.emit.emitLABEL(labelTrue,frame)
                return leftVal+rightVal+con+brk,BoolType()
            else:
                labelFalse = frame.getNewLabel()
                labelTrue = frame.getNewLabel()
                leftVal+=self.emit.emitIFTRUE(labelFalse,frame)
                rightVal+=self.emit.emitIFTRUE(labelFalse,frame)
                con=self.emit.emitPUSHICONST("false", frame)+self.emit.emitGOTO(labelFalse,frame) + self.emit.emitLABEL(labelTrue,frame)
                brk=self.emit.emitPUSHICONST("true", frame)+self.emit.emitLABEL(labelFalse,frame)
                return leftVal+rightVal+con+brk,BoolType()
            
        else:
            #TODO
            if ast.op == '''\\''':             
                return leftVal + rightVal + self.emit.emitMOD(frame), IntType()
            elif ast.op == '%':
                return leftVal + rightVal + self.emit.emitMOD(frame), IntType()
            #TODO
            elif ast.op=='^':
                return leftVal + rightVal
        # e1c,e1t = self.visit(ast.left,o)
        # e2c,e2t = self.visit(ast.right,o)
        # return e1c + e2c + self.emit.emitADDOP(ast.op,e1t,o.frame),e1t
    def visitUnaryOp(self,ast,o):
    #     op:str
    # body:Expr
        frame = o.frame
        nenv = o.sym

        body, typ = self.visit(ast.body, Access(frame, nenv, False, True))
        if ast.op.lower() == 'not' and type(typ) is BoolType:
            return body + self.emit.emitNOT(IntType(), frame), BoolType()
        elif ast.op == '-' and type(typ) is IntType:
            return body + self.emit.emitNEGOP(IntType(), frame), IntType()
        elif ast.op == '-' and type(typ) is FloatType:
            return body + self.emit.emitNEGOP(FloatType(), frame), FloatType()

    def visitId(self,ast,o):
    # name:str
        # index=(type(sym.value) == Index)
        # if o.isLeft:
        #     if type(sym.value) is Index:
        #         code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame)
        #     else:
        #         code = self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
        # else:
        #     if type(sym.value) is Index:
        #         code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
        #     else:
        #         code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame)
        # # return code, sym.mtype
        # for x in o.sym:
        #     print(x)
        sym = self.lookup(ast.name, o.sym, lambda x: x.name)
        # sym=next(filter(lambda x: x.name==ast.name, o.sym), False)
        typ = sym.mtype

        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitWRITEVAR(sym.name, typ, sym.value.value, o.frame), typ
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitREADVAR(sym.name, typ, sym.value.value, o.frame), typ
       
    

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
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    





  
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
            return Symbol(ctx.variable.name,MType([],ctx.varType),CName(o))
        return Symbol(ctx.constant.name, MType([],ctx.constType),CName(o))
    
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
