# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdcls.
    def visitClassdcls(self, ctx:BKOOLParser.ClassdclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdcl.
    def visitClassdcl(self, ctx:BKOOLParser.ClassdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memBlock.
    def visitMemBlock(self, ctx:BKOOLParser.MemBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memList.
    def visitMemList(self, ctx:BKOOLParser.MemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classMember.
    def visitClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeDeclare.
    def visitAttributeDeclare(self, ctx:BKOOLParser.AttributeDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vartype.
    def visitVartype(self, ctx:BKOOLParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primtype.
    def visitPrimtype(self, ctx:BKOOLParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classtype.
    def visitClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeList.
    def visitAttributeList(self, ctx:BKOOLParser.AttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attri.
    def visitAttri(self, ctx:BKOOLParser.AttriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDeclare.
    def visitMethodDeclare(self, ctx:BKOOLParser.MethodDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramDeclare.
    def visitParamDeclare(self, ctx:BKOOLParser.ParamDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idList.
    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmBlock.
    def visitStmBlock(self, ctx:BKOOLParser.StmBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elemList.
    def visitElemList(self, ctx:BKOOLParser.ElemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elem.
    def visitElem(self, ctx:BKOOLParser.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#size.
    def visitSize(self, ctx:BKOOLParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#explist.
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exps.
    def visitExps(self, ctx:BKOOLParser.ExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexp.
    def visitSubexp(self, ctx:BKOOLParser.SubexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodInvoke.
    def visitMethodInvoke(self, ctx:BKOOLParser.MethodInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodRecur.
    def visitMethodRecur(self, ctx:BKOOLParser.MethodRecurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attriAccess.
    def visitAttriAccess(self, ctx:BKOOLParser.AttriAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attriRecur.
    def visitAttriRecur(self, ctx:BKOOLParser.AttriRecurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmList.
    def visitStmList(self, ctx:BKOOLParser.StmListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variables.
    def visitVariables(self, ctx:BKOOLParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable.
    def visitVariable(self, ctx:BKOOLParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stms.
    def visitStms(self, ctx:BKOOLParser.StmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stm.
    def visitStm(self, ctx:BKOOLParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodCall.
    def visitMethodCall(self, ctx:BKOOLParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scala_var.
    def visitScala_var(self, ctx:BKOOLParser.Scala_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)



del BKOOLParser