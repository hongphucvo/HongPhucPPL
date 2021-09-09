class Exp:
    def eval():pass
    def printPrefix():pass

class BinExp(Exp):
    def __init__(self, operand1, operator, operand2):
        self.operand1=operand1
        self.operator=operator
        self.operand2=operand2
    def eval(self):
        if(self.operator=="+"):
            return self.operand1.eval() + self.operand2.eval()
        elif(self.operator=="-"):
            return self.operand1.eval()-self.operand2.eval()
        elif(self.operator=="/"):
            return self.operand1.eval()/self.operand2.eval()
        else:
            return self.operand1.eval()*self.operand2.eval()
    def printPrefix(self):
        return(self.operator+" "+self.operand1.printPrefix()+self.operand2.printPrefix())
class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator=operator
        self.operand=operand
    def eval(self):
        if(self.operator=="+"):
            return self.operand.eval()
        else: return -self.operand.eval()
    def printPrefix(self):
        return self.operator+". "+self.operand.printPrefix()
class IntLit(Exp):
    def __init__(self, value):
        self.number=value   
    def eval(self):
        return int(self.number)
    def printPrefix(self):
        return str(self.number)+" "
class FloatLit(Exp):
    def __init__(self,value):
        self.number=value
    def eval(self):
        return float(self.number)
    def printPrefix(self):
        return str(self.number)+" "
x1 = IntLit(1)
x1.printPrefix()
x2 = FloatLit(2.0)
x2.printPrefix()
x4 = UnExp("-",x1)
x4.printPrefix()
x3 = BinExp(x1,"+",x1)
print(x3.printPrefix())
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
