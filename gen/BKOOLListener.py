# Generated from E:/hongphuc/PPL/BKooL/assignment1/src/main/bkool/parser\BKOOL.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete listener for a parse tree produced by BKOOLParser.
class BKOOLListener(ParseTreeListener):

    # Enter a parse tree produced by BKOOLParser#program.
    def enterProgram(self, ctx:BKOOLParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKOOLParser#program.
    def exitProgram(self, ctx:BKOOLParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKOOLParser#mptype.
    def enterMptype(self, ctx:BKOOLParser.MptypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#mptype.
    def exitMptype(self, ctx:BKOOLParser.MptypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#body.
    def enterBody(self, ctx:BKOOLParser.BodyContext):
        pass

    # Exit a parse tree produced by BKOOLParser#body.
    def exitBody(self, ctx:BKOOLParser.BodyContext):
        pass


    # Enter a parse tree produced by BKOOLParser#funcall.
    def enterFuncall(self, ctx:BKOOLParser.FuncallContext):
        pass

    # Exit a parse tree produced by BKOOLParser#funcall.
    def exitFuncall(self, ctx:BKOOLParser.FuncallContext):
        pass


    # Enter a parse tree produced by BKOOLParser#classdcls.
    def enterClassdcls(self, ctx:BKOOLParser.ClassdclsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#classdcls.
    def exitClassdcls(self, ctx:BKOOLParser.ClassdclsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#classdcl.
    def enterClassdcl(self, ctx:BKOOLParser.ClassdclContext):
        pass

    # Exit a parse tree produced by BKOOLParser#classdcl.
    def exitClassdcl(self, ctx:BKOOLParser.ClassdclContext):
        pass


    # Enter a parse tree produced by BKOOLParser#memBlock.
    def enterMemBlock(self, ctx:BKOOLParser.MemBlockContext):
        pass

    # Exit a parse tree produced by BKOOLParser#memBlock.
    def exitMemBlock(self, ctx:BKOOLParser.MemBlockContext):
        pass


    # Enter a parse tree produced by BKOOLParser#memList.
    def enterMemList(self, ctx:BKOOLParser.MemListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#memList.
    def exitMemList(self, ctx:BKOOLParser.MemListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#classMember.
    def enterClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by BKOOLParser#classMember.
    def exitClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attributes.
    def enterAttributes(self, ctx:BKOOLParser.AttributesContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attributes.
    def exitAttributes(self, ctx:BKOOLParser.AttributesContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attributeDeclare.
    def enterAttributeDeclare(self, ctx:BKOOLParser.AttributeDeclareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attributeDeclare.
    def exitAttributeDeclare(self, ctx:BKOOLParser.AttributeDeclareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attribute_type.
    def enterAttribute_type(self, ctx:BKOOLParser.Attribute_typeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attribute_type.
    def exitAttribute_type(self, ctx:BKOOLParser.Attribute_typeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#vartype.
    def enterVartype(self, ctx:BKOOLParser.VartypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#vartype.
    def exitVartype(self, ctx:BKOOLParser.VartypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#primtype.
    def enterPrimtype(self, ctx:BKOOLParser.PrimtypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#primtype.
    def exitPrimtype(self, ctx:BKOOLParser.PrimtypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#classtype.
    def enterClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#classtype.
    def exitClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attributeList.
    def enterAttributeList(self, ctx:BKOOLParser.AttributeListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attributeList.
    def exitAttributeList(self, ctx:BKOOLParser.AttributeListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#attri.
    def enterAttri(self, ctx:BKOOLParser.AttriContext):
        pass

    # Exit a parse tree produced by BKOOLParser#attri.
    def exitAttri(self, ctx:BKOOLParser.AttriContext):
        pass


    # Enter a parse tree produced by BKOOLParser#methodDeclare.
    def enterMethodDeclare(self, ctx:BKOOLParser.MethodDeclareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#methodDeclare.
    def exitMethodDeclare(self, ctx:BKOOLParser.MethodDeclareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#constructor.
    def enterConstructor(self, ctx:BKOOLParser.ConstructorContext):
        pass

    # Exit a parse tree produced by BKOOLParser#constructor.
    def exitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        pass


    # Enter a parse tree produced by BKOOLParser#methodType.
    def enterMethodType(self, ctx:BKOOLParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#methodType.
    def exitMethodType(self, ctx:BKOOLParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#returnType.
    def enterReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#returnType.
    def exitReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#stmBlock.
    def enterStmBlock(self, ctx:BKOOLParser.StmBlockContext):
        pass

    # Exit a parse tree produced by BKOOLParser#stmBlock.
    def exitStmBlock(self, ctx:BKOOLParser.StmBlockContext):
        pass


    # Enter a parse tree produced by BKOOLParser#paramList.
    def enterParamList(self, ctx:BKOOLParser.ParamListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#paramList.
    def exitParamList(self, ctx:BKOOLParser.ParamListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#paramDeclare.
    def enterParamDeclare(self, ctx:BKOOLParser.ParamDeclareContext):
        pass

    # Exit a parse tree produced by BKOOLParser#paramDeclare.
    def exitParamDeclare(self, ctx:BKOOLParser.ParamDeclareContext):
        pass


    # Enter a parse tree produced by BKOOLParser#param.
    def enterParam(self, ctx:BKOOLParser.ParamContext):
        pass

    # Exit a parse tree produced by BKOOLParser#param.
    def exitParam(self, ctx:BKOOLParser.ParamContext):
        pass


    # Enter a parse tree produced by BKOOLParser#idList.
    def enterIdList(self, ctx:BKOOLParser.IdListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#idList.
    def exitIdList(self, ctx:BKOOLParser.IdListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#arraytype.
    def enterArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#arraytype.
    def exitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#arrayLit.
    def enterArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        pass

    # Exit a parse tree produced by BKOOLParser#arrayLit.
    def exitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        pass


    # Enter a parse tree produced by BKOOLParser#elemList.
    def enterElemList(self, ctx:BKOOLParser.ElemListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#elemList.
    def exitElemList(self, ctx:BKOOLParser.ElemListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#elem.
    def enterElem(self, ctx:BKOOLParser.ElemContext):
        pass

    # Exit a parse tree produced by BKOOLParser#elem.
    def exitElem(self, ctx:BKOOLParser.ElemContext):
        pass


    # Enter a parse tree produced by BKOOLParser#size.
    def enterSize(self, ctx:BKOOLParser.SizeContext):
        pass

    # Exit a parse tree produced by BKOOLParser#size.
    def exitSize(self, ctx:BKOOLParser.SizeContext):
        pass


    # Enter a parse tree produced by BKOOLParser#explist.
    def enterExplist(self, ctx:BKOOLParser.ExplistContext):
        pass

    # Exit a parse tree produced by BKOOLParser#explist.
    def exitExplist(self, ctx:BKOOLParser.ExplistContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exps.
    def enterExps(self, ctx:BKOOLParser.ExpsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#exps.
    def exitExps(self, ctx:BKOOLParser.ExpsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp.
    def enterExp(self, ctx:BKOOLParser.ExpContext):
        pass

    # Exit a parse tree produced by BKOOLParser#exp.
    def exitExp(self, ctx:BKOOLParser.ExpContext):
        pass


    # Enter a parse tree produced by BKOOLParser#exp1.
    def enterExp1(self, ctx:BKOOLParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp1.
    def exitExp1(self, ctx:BKOOLParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp2.
    def enterExp2(self, ctx:BKOOLParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp2.
    def exitExp2(self, ctx:BKOOLParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp3.
    def enterExp3(self, ctx:BKOOLParser.Exp3Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp3.
    def exitExp3(self, ctx:BKOOLParser.Exp3Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp4.
    def enterExp4(self, ctx:BKOOLParser.Exp4Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp4.
    def exitExp4(self, ctx:BKOOLParser.Exp4Context):
        pass


    # Enter a parse tree produced by BKOOLParser#exp5.
    def enterExp5(self, ctx:BKOOLParser.Exp5Context):
        pass

    # Exit a parse tree produced by BKOOLParser#exp5.
    def exitExp5(self, ctx:BKOOLParser.Exp5Context):
        pass


    # Enter a parse tree produced by BKOOLParser#operand.
    def enterOperand(self, ctx:BKOOLParser.OperandContext):
        pass

    # Exit a parse tree produced by BKOOLParser#operand.
    def exitOperand(self, ctx:BKOOLParser.OperandContext):
        pass


    # Enter a parse tree produced by BKOOLParser#stmList.
    def enterStmList(self, ctx:BKOOLParser.StmListContext):
        pass

    # Exit a parse tree produced by BKOOLParser#stmList.
    def exitStmList(self, ctx:BKOOLParser.StmListContext):
        pass


    # Enter a parse tree produced by BKOOLParser#variables.
    def enterVariables(self, ctx:BKOOLParser.VariablesContext):
        pass

    # Exit a parse tree produced by BKOOLParser#variables.
    def exitVariables(self, ctx:BKOOLParser.VariablesContext):
        pass


    # Enter a parse tree produced by BKOOLParser#variable.
    def enterVariable(self, ctx:BKOOLParser.VariableContext):
        pass

    # Exit a parse tree produced by BKOOLParser#variable.
    def exitVariable(self, ctx:BKOOLParser.VariableContext):
        pass


    # Enter a parse tree produced by BKOOLParser#stms.
    def enterStms(self, ctx:BKOOLParser.StmsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#stms.
    def exitStms(self, ctx:BKOOLParser.StmsContext):
        pass


    # Enter a parse tree produced by BKOOLParser#stm.
    def enterStm(self, ctx:BKOOLParser.StmContext):
        pass

    # Exit a parse tree produced by BKOOLParser#stm.
    def exitStm(self, ctx:BKOOLParser.StmContext):
        pass


    # Enter a parse tree produced by BKOOLParser#scala_var.
    def enterScala_var(self, ctx:BKOOLParser.Scala_varContext):
        pass

    # Exit a parse tree produced by BKOOLParser#scala_var.
    def exitScala_var(self, ctx:BKOOLParser.Scala_varContext):
        pass


    # Enter a parse tree produced by BKOOLParser#lhs.
    def enterLhs(self, ctx:BKOOLParser.LhsContext):
        pass

    # Exit a parse tree produced by BKOOLParser#lhs.
    def exitLhs(self, ctx:BKOOLParser.LhsContext):
        pass



del BKOOLParser