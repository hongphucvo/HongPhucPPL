class Exp():pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
class UnExp(Exp):
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
class Eval:
    def visit(self,exp):
        if type(exp)is BinExp:
            o1=self.visit(exp.left)
            o2=self.visit(exp.right)
            if exp.op=='+':
                return o1+o2
            elif exp.op=='-':
                return o1-o2
            elif exp.op=='*':
                return o1*o2
            else: return o1/o2
        elif type(exp) is UnExp:
            o1=self.visit(exp.operand)
            if exp.op=='-':
                return -o1
            elif exp.op=='+': return o1
        elif type(exp) is IntLit:
            return exp.value
        elif type(exp) is FloatLit:
            return exp.value
class PrintPrefix:
    def visit(self,exp):
        if type(exp)is BinExp:
            o1=self.visit(exp.left)
            o2=self.visit(exp.right)
            return exp.op +" "+ o1+o2
        elif type(exp) is UnExp:
            o1=self.visit(exp.operand)
            return exp.op+". " +o1
        elif type(exp) is IntLit:
            return str(exp.value)+" "
        elif type(exp) is FloatLit:
            return str(exp.value)+" "
class PrintPostfix:
    def visit(self,exp):
        if type(exp)is BinExp:
            o1=self.visit(exp.left)
            o2=self.visit(exp.right)
            return o1+o2+exp.op
        elif type(exp) is UnExp:
            o1=self.visit(exp.operand)
            return exp.op+o1
        elif type(exp) is IntLit:
            return str(exp.value)+" "
        elif type(exp) is FloatLit:
            return str(exp.value)+" "



x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
