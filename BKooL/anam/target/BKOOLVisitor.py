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


    # Visit a parse tree produced by BKOOLParser#classList.
    def visitClassList(self, ctx:BKOOLParser.ClassListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBody.
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#membersList.
    def visitMembersList(self, ctx:BKOOLParser.MembersListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributesDecl.
    def visitAttributesDecl(self, ctx:BKOOLParser.AttributesDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramMethod.
    def visitParamMethod(self, ctx:BKOOLParser.ParamMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramDeclList.
    def visitParamDeclList(self, ctx:BKOOLParser.ParamDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramDecl.
    def visitParamDecl(self, ctx:BKOOLParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bodyMethod.
    def visitBodyMethod(self, ctx:BKOOLParser.BodyMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDeclMulList.
    def visitVarDeclMulList(self, ctx:BKOOLParser.VarDeclMulListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecls.
    def visitVarDecls(self, ctx:BKOOLParser.VarDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDeclList.
    def visitVarDeclList(self, ctx:BKOOLParser.VarDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varList.
    def visitVarList(self, ctx:BKOOLParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typeDecl.
    def visitTypeDecl(self, ctx:BKOOLParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listStatement.
    def visitListStatement(self, ctx:BKOOLParser.ListStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statements.
    def visitStatements(self, ctx:BKOOLParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockStmt.
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignStmt.
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#condition.
    def visitCondition(self, ctx:BKOOLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callStmt.
    def visitCallStmt(self, ctx:BKOOLParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expList.
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
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


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpression.
    def visitSubexpression(self, ctx:BKOOLParser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literalList.
    def visitLiteralList(self, ctx:BKOOLParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idList.
    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booleanlit.
    def visitBooleanlit(self, ctx:BKOOLParser.BooleanlitContext):
        return self.visitChildren(ctx)



del BKOOLParser