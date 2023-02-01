class ABC:
    pass


class Visitor:
    pass


class Program:
    pass


class Decl(ABC):
    pass


class VarDecl(Decl):
    pass


class FuncDecl(Decl):
    pass


class Stmt(ABC):
    pass


class Block(Stmt):
    pass


class Assign(Stmt):
    pass


class CallStmt(Stmt):
    pass


class Exp(ABC):
    pass


class BinOp(Exp):  # op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    pass


class UnOp(Exp):  # op:str,e:Exp #op is -,-., !,i2f, floor
    pass


class IntLit(Exp):  # val:int
    pass


class FloatLit(Exp):  # val:float
    pass


class BoolLit(Exp):  # val:bool
    pass


class Id(Exp):  # name:str
    pass


class UndeclaredIdentifier:
    pass


class TypeMismatchInStatement:
    pass


class TypeMismatchInExpression:
    pass


class TypeCannotBeInferred:
    pass


class Redeclared:
    pass


"""============================================================================================================="""


# 01


class MyUtils:
    def inferType(self, exp1, exp2, o):
        # Exp: IntType(), FloatType(), BoolType(), "<str>", None
        # The key is that we want to infer the type of exp2 for exp1
        # Therefore, use type() for cur_type, and getType() for new_typ
        cur_typ = type(exp1)
        new_typ = self._getType(exp2, o)
        # Identifier
        if cur_typ is str:
            if o[exp1] is None:
                # Infer an uninitialized type is an error
                if new_typ is type(None):
                    return False
                # Update the instance of new type
                o[exp1] = self._getIntance(new_typ)
                return True
            cur_typ = type(o[exp1])

        # Expression
        if cur_typ == new_typ:
            return True
        return False

    def compareTypes(self, exp1, exp2, o):
        return self._getType(exp1, o) == self._getType(exp2, o)

    def _getType(self, exp, o):
        typ = type(exp)
        if typ is str:
            typ = type(o[exp])
        return typ

    def _getIntance(self, typ):
        return IntType() if typ is type(IntType()) else \
            FloatType() if typ is type(FloatType()) else \
            BoolType() if typ is type(BoolType()) else \
            None


class StaticCheck(Visitor):

    # decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self, ctx: Program, o):
        o = {}
        [self.visit(decl, o) for decl in ctx.decl]
        [self.visit(stmt, o) for stmt in ctx.stmts]

    # name:str
    def visitVarDecl(self, ctx: VarDecl, o):
        o[ctx.name] = None

    # lhs:Id,rhs:Exp
    def visitAssign(self, ctx: Assign, o):
        rhs = self.visit(ctx.rhs, o)  # exp, Id
        lhs = self.visit(ctx.lhs, o)
        myUtils = MyUtils()
        # Type inference
        myUtils.inferType(lhs, rhs, o)
        myUtils.inferType(rhs, lhs, o)
        # Check error
        if myUtils.compareTypes(lhs, None, o) or myUtils.compareTypes(rhs, None, o):
            raise TypeCannotBeInferred(ctx)
        if not myUtils.compareTypes(lhs, rhs, o):
            raise TypeMismatchInStatement(ctx)  # raise error

    # op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # type inference
        if op in ["+", "-", "*", "/"]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = IntType()
        elif op in ["+.", "-.", "*.", "/."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = FloatType()
        elif op in [">", "="]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = BoolType()
        elif op in [">.", "=."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = BoolType()
        else:
            infer_success = myUtils.inferType(
                e1, BoolType(), o) and myUtils.inferType(e2, BoolType(), o)
            res = BoolType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res
    # op:str,e:Exp #op is -,-., !,i2f, floor

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # Type inference
        if op == "-":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = IntType()
        elif op == "-.":
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = FloatType()
        elif op == "!":
            infer_success = myUtils.inferType(e, BoolType(), o)
            res = BoolType()
        elif op == "i2f":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = FloatType()
        else:
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = IntType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res

    # val:int
    def visitIntLit(self, ctx, o):
        return IntType()

    # val:float
    def visitFloatLit(self, ctx, o):
        return FloatType()

    # val:bool
    def visitBoolLit(self, ctx, o):
        return BoolType()

    # name:str
    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)  # raise error
        return ctx.name


class Type:
    pass


class BoolType(Type):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


"""============================================================================================================="""


# 02


class GetGlobalEnv(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        o = {}
        [self.visit(decl, o) for decl in ctx.decl]
        return o

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise Redeclared(ctx)
        o[ctx.name] = None


class MyUtils:

    """Env manipulation"""

    def lookUp(self, var_name, o):
        [_scope, _] = self._lookUp(var_name, o)
        return True if _scope else False

    def addDecl(self, ctx, var_val, o):
        if len(o['local']):
            scope = o['local'][-1]
        else:
            scope = o['global']
        if ctx.name in scope:
            raise Redeclared(ctx)
        scope[ctx.name] = var_val

    def _lookUp(self, var_name, o):
        if len(o['local']):
            for scope in o['local'][::-1]:
                if var_name in scope:
                    return scope, var_name
        if var_name in o['global']:
            return o['global'], var_name
        return None, None

    """Type manipulation"""

    def inferType(self, exp1, exp2, o):
        # Exp: IntType(), FloatType(), BoolType(), "<str>", None
        # The key is that we want to infer the type of exp2 for exp1
        # Therefore, use type() for cur_type, and getType() for new_typ
        cur_typ = type(exp1)
        new_typ = self._getType(exp2, o)
        # Identifier
        if cur_typ is str:
            # Get scope & name found from env
            [_scope, _name] = self._lookUp(exp1, o)
            if _scope is None:  # Optional
                raise UndeclaredIdentifier(exp1)

            # Now infer the type
            if _scope[_name] is None:
                # Infer an uninitialized type is an error
                if new_typ is type(None):
                    return False
                # Update the instance of new type
                _scope[_name] = self._getIntance(new_typ)
                return True
            cur_typ = type(_scope[_name])

        # Expression
        if cur_typ == new_typ:
            return True
        return False

    def compareTypes(self, exp1, exp2, o):
        return self._getType(exp1, o) == self._getType(exp2, o)

    def _getType(self, exp, o):
        typ = type(exp)
        if typ is str:
            [_scope, _name] = self._lookUp(exp, o)
            if _scope is None:
                raise UndeclaredIdentifier(exp)
            typ = type(_scope[_name])
        return typ

    def _getIntance(self, typ):
        return IntType() if typ is type(IntType()) else \
            FloatType() if typ is type(FloatType()) else \
            BoolType() if typ is type(BoolType()) else \
            None


class StaticCheck(Visitor):

    # decl:List[VarDecl],stmts:List[Stmt]
    def visitProgram(self, ctx: Program, o):
        o = {}
        o['global'] = GetGlobalEnv().visit(ctx, None)
        o['local'] = []
        # [self.visit(decl, o) for decl in ctx.decl]
        [self.visit(stmt, o) for stmt in ctx.stmts]

    # name:str
    def visitVarDecl(self, ctx: VarDecl, o):
        MyUtils().addDecl(ctx, None, o)

    # decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self, ctx: Block, o):
        o['local'].append({})
        [self.visit(decl, o) for decl in ctx.decl]
        [self.visit(stmt, o) for stmt in ctx.stmts]
        o['local'].pop()

    # lhs:Id,rhs:Exp
    def visitAssign(self, ctx: Assign, o):
        rhs = self.visit(ctx.rhs, o)  # exp, Id
        lhs = self.visit(ctx.lhs, o)
        myUtils = MyUtils()
        # Type inference
        myUtils.inferType(lhs, rhs, o)
        myUtils.inferType(rhs, lhs, o)
        # Check error
        if myUtils.compareTypes(lhs, None, o) or myUtils.compareTypes(rhs, None, o):
            raise TypeCannotBeInferred(ctx)
        if not myUtils.compareTypes(lhs, rhs, o):
            raise TypeMismatchInStatement(ctx)  # raise error

    # op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # type inference
        if op in ["+", "-", "*", "/"]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = IntType()
        elif op in ["+.", "-.", "*.", "/."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = FloatType()
        elif op in [">", "="]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = BoolType()
        elif op in [">.", "=."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = BoolType()
        else:
            infer_success = myUtils.inferType(
                e1, BoolType(), o) and myUtils.inferType(e2, BoolType(), o)
            res = BoolType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res
    # op:str,e:Exp #op is -,-., !,i2f, floor

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # Type inference
        if op == "-":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = IntType()
        elif op == "-.":
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = FloatType()
        elif op == "!":
            infer_success = myUtils.inferType(e, BoolType(), o)
            res = BoolType()
        elif op == "i2f":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = FloatType()
        else:
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = IntType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res

    # val:int
    def visitIntLit(self, ctx, o):
        return IntType()

    # val:float
    def visitFloatLit(self, ctx, o):
        return FloatType()

    # val:bool
    def visitBoolLit(self, ctx, o):
        return BoolType()

    # name:str
    def visitId(self, ctx, o):
        if not MyUtils().lookUp(ctx.name, o):
            raise UndeclaredIdentifier(ctx.name)  # raise error
        return ctx.name


class Type:
    pass


class BoolType(Type):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


"""============================================================================================================="""


# 03
# Paramer & Function


class MyUtils:

    """Env manipulation"""

    def lookUp(self, var_name, o):
        # Lookup the whole env, from local to global
        [_scope, _] = self._lookUp(var_name, o)
        return True if _scope else False   


    def _lookUp(self, var_name, o):
        if len(o['local']):
            for scope in o['local'][::-1]:
                if var_name in scope:
                    return scope, var_name
        if var_name in o['global']:
            return o['global'], var_name
        return None, None



    def addDecl(self, ctx, val, o):
        if len(o['local']):
            scope = o['local'][-1]
        else:
            scope = o['global']
        if ctx.name in scope:
            raise Redeclared(ctx)
        scope[ctx.name] = val


    def openScope(self, o):
        o['local'].append({})

    def closeScope(self, o):
        o['local'].pop()

    """Type manipulation"""

    def inferType(self, exp1, exp2, o):
        # Exp: [func_detail, idx], "<str>", IntType(), FloatType(), BoolType(), None
        # The key is that we want to infer the type of exp2 for exp1
        # Therefore, use type() for cur_type, and getType() for new_typ
        cur_typ = type(exp1)
        new_typ = self._getType(exp2, o)
        # Identifier
        if cur_typ is str:
            # Get scope & name found from env
            [_scope, _name] = self._lookUp(exp1, o)
            if _scope is None:  # Optional
                raise UndeclaredIdentifier(exp1)

            # Now infer the type
            if _scope[_name][0] is None:
                # Infer an uninitialized type is an error
                if new_typ is type(None):
                    return False
                # Update the instance of new type
                _scope[_name][0] = self._getIntance(new_typ)
                # Update parameter
                if _scope[_name][1] is not None:
                    _scope[_name][1]["param"][_name] = _scope[_name][0]
                return True
            cur_typ = type(_scope[_name][0])

        # Parameter
        elif cur_typ is list:
            [func_detail, idx] = exp1
            _scope = func_detail["param"]
            _name = func_detail["param_idx"][idx]
            # Now infer the type
            if _scope[_name] is None:
                # Infer an uninitialized type is an error
                if new_typ is type(None):
                    return False
                # Update the instance of new type
                _scope[_name] = self._getIntance(new_typ)
                return True
            cur_typ = type(_scope[_name])

        # Expression
        if cur_typ == new_typ:
            return True
        return False

    def compareTypes(self, exp1, exp2, o):
        return self._getType(exp1, o) == self._getType(exp2, o)

    def _getType(self, exp, o):
        typ = type(exp)
        if typ is str:
            [_scope, _name] = self._lookUp(exp, o)
            if _scope is None:
                raise UndeclaredIdentifier(exp)
            typ = type(_scope[_name][0])
        elif typ is list:
            [func_detail, idx] = exp
            _scope, _name = func_detail["param"], func_detail["param_idx"][idx]
            typ = type(_scope[_name])
        return typ

    def _getIntance(self, typ):
        return IntType() if typ is type(IntType()) else \
            FloatType() if typ is type(FloatType()) else \
            BoolType() if typ is type(BoolType()) else \
            None


class GetGlobalEnv(Visitor):
    def visitProgram(self, ctx: Program, o: object):
        o = {"global": {}, "local": []}
        [self.visit(decl, o) for decl in ctx.decl]
        return o["global"]

    def visitVarDecl(self, ctx: VarDecl, o: object):
        myUtils = MyUtils()
        # Parameter
        if type(o) is list:
            myUtils.addDecl(ctx, [None, o[1]], o[0])
            # update param only in function detail
            o[1]["param"][ctx.name] = None
            o[1]["param_idx"].append(ctx.name)
        # Variable
        else:
            myUtils.addDecl(ctx, [None, None], o)

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise Redeclared(ctx)
        myUtils = MyUtils()
        func_detail = {"return": None, "param": {}, "param_idx": []}
        myUtils.addDecl(ctx, func_detail, o)
        myUtils.openScope(o)
        [self.visit(param, o) for param in ctx.param]
        myUtils.closeScope(o)
        


class StaticCheck(Visitor):

    # decl:List[Decl],stmts:List[Stmt]
    def visitProgram(self, ctx: Program, o):
        o = {}
        o['global'] = GetGlobalEnv().visit(ctx, None)
        o['local'] = []
        for decl in ctx.decl:
            if type(decl) is FuncDecl:
                # Indicates this function is declared in global
                self.visit(decl, [o])
        [self.visit(stmt, o) for stmt in ctx.stmts]

    # name:str
    def visitVarDecl(self, ctx: VarDecl, o: object):
        myUtils = MyUtils()
        # Check whether it's a parameter or variable
        # Parameter
        if type(o) is list:
            myUtils.addDecl(ctx, [None, o[1]], o[0])
            # update param only in function detail
            o[1]["param"][ctx.name] = None
            o[1]["param_idx"].append(ctx.name)
        # Variable
        else:
            myUtils.addDecl(ctx, [None, None], o)

    # name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def visitFuncDecl(self, ctx: FuncDecl, o):
        myUtils = MyUtils()
        env = o
        if type(o) is list:
            [env] = o
            [_scope, _name] = myUtils._lookUp(ctx.name, env)
            func_detail = _scope[_name]
        else:
            func_detail = {"return": None, "param": {}, "param_idx": []}
            MyUtils().addDecl(ctx, func_detail, o)
        myUtils.openScope(env)
        # Param updating
        new_env = [env, func_detail]
        for param in ctx.param:
            self.visit(param, new_env)
        # Local decls
        [self.visit(local, env) for local in ctx.local]
        # Statements
        [self.visit(stmt, env) for stmt in ctx.stmts]
        myUtils.closeScope(env)
        

    # name:str,args:List[Exp]

    def visitCallStmt(self, ctx: CallStmt, o):
        myUtils = MyUtils()
        [_scope, _name] = myUtils._lookUp(ctx.name, o)
        if _scope is None or type(_scope[_name]) is not dict:
            raise UndeclaredIdentifier(ctx.name)

        # Check number of args and params
        func_detail = _scope[_name]
        param_idxs = func_detail["param_idx"]
        args = [self.visit(arg, o) for arg in ctx.args]
        if len(list(param_idxs)) != len(args):
            raise TypeMismatchInStatement(ctx)
        for idx in range(len(param_idxs)):
            param_ele, arg = [func_detail, idx], args[idx]
            # Type inference
            myUtils.inferType(param_ele, arg, o) 
            myUtils.inferType(arg, param_ele, o)
            # Check error
            if not myUtils.compareTypes(param_ele, arg, o):
                raise TypeMismatchInStatement(ctx)
            if myUtils.compareTypes(arg, None, o) or myUtils.compareTypes(param_ele, None, o):
                raise TypeCannotBeInferred(ctx)

    # lhs:Id,rhs:Exp

    def visitAssign(self, ctx: Assign, o):
        rhs = self.visit(ctx.rhs, o)  # exp, Id
        lhs = self.visit(ctx.lhs, o)
        myUtils = MyUtils()
        # Type inference
        myUtils.inferType(lhs, rhs, o)
        myUtils.inferType(rhs, lhs, o)
        # Check error
        if myUtils.compareTypes(lhs, None, o) or myUtils.compareTypes(rhs, None, o):
            raise TypeCannotBeInferred(ctx)
        if not myUtils.compareTypes(lhs, rhs, o):
            raise TypeMismatchInStatement(ctx)  # raise error

    # op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # type inference
        if op in ["+", "-", "*", "/"]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = IntType()
        elif op in ["+.", "-.", "*.", "/."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = FloatType()
        elif op in [">", "="]:
            infer_success = myUtils.inferType(
                e1, IntType(), o) and myUtils.inferType(e2, IntType(), o)
            res = BoolType()
        elif op in [">.", "=."]:
            infer_success = myUtils.inferType(
                e1, FloatType(), o) and myUtils.inferType(e2, FloatType(), o)
            res = BoolType()
        else:
            infer_success = myUtils.inferType(
                e1, BoolType(), o) and myUtils.inferType(e2, BoolType(), o)
            res = BoolType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res
    # op:str,e:Exp #op is -,-., !,i2f, floor

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        op = ctx.op
        myUtils = MyUtils()  # utils
        infer_success, res = False, None

        # Type inference
        if op == "-":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = IntType()
        elif op == "-.":
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = FloatType()
        elif op == "!":
            infer_success = myUtils.inferType(e, BoolType(), o)
            res = BoolType()
        elif op == "i2f":
            infer_success = myUtils.inferType(e, IntType(), o)
            res = FloatType()
        else:
            infer_success = myUtils.inferType(e, FloatType(), o)
            res = IntType()

        # Check error
        if not infer_success:
            raise TypeMismatchInExpression(ctx)  # raise error
        return res

    # val:int
    def visitIntLit(self, ctx, o):
        return IntType()

    # val:float
    def visitFloatLit(self, ctx, o):
        return FloatType()

    # val:bool
    def visitBoolLit(self, ctx, o):
        return BoolType()

    # name:str
    def visitId(self, ctx, o):
        if not MyUtils().lookUp(ctx.name, o):
            raise UndeclaredIdentifier(ctx.name)  # raise error
        return ctx.name


class Type:
    pass


class BoolType(Type):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


