class Exp:
    def eval():
    def printPrefix():

class BinExp(Exp):
    operand1=0
    operator="+"
    operand2=0
    def __init__(self, operand1, operator, operand2):
        self.operand1=operand1
        self.operator=operator
        self.operand2=operand2
    def val(self):
        if(self.operator=="+"):
            return self.operand1 + self.operand2
        elif(self.operator=="-"):
            return self.operand1-self.operand2
        elif(self.operator=="/"):
            return self.operand1/self.operand2
        else:
            return self.operand1*self.operand2
    def printPrefix():
        return operand1+" "+operator+" "+operand2
class UnExp(Exp):
    operator="+"
    operand=0
    def __init__(self, operator, operand):
        self.operator=operator
        self.operand=operand
    def val(self):
        if(self.operator=="+"):
            return self.operand
        else: return -self.operand

class IntLit(Exp):
    number=0
    def __init__(self, value):
        self.number=value   
    def val(self):
        return int(self.number)

class FloatLit(Exp):
    number=0.0
    def __init__(self,value):
        self.number=value
    def val(self):
        return float(self.number)

x = Exp(3 + 4 * 2.0);