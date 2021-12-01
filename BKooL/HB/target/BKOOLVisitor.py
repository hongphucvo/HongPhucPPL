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


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberlist.
    def visitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#membertail.
    def visitMembertail(self, ctx:BKOOLParser.MembertailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attdecl.
    def visitAttdecl(self, ctx:BKOOLParser.AttdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attdecllist.
    def visitAttdecllist(self, ctx:BKOOLParser.AttdecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paraml.
    def visitParaml(self, ctx:BKOOLParser.ParamlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramtail.
    def visitParamtail(self, ctx:BKOOLParser.ParamtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#alltype.
    def visitAlltype(self, ctx:BKOOLParser.AlltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pctype.
    def visitPctype(self, ctx:BKOOLParser.PctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expl.
    def visitExpl(self, ctx:BKOOLParser.ExplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#explist.
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index.
    def visitIndex(self, ctx:BKOOLParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_access.
    def visitMethod_access(self, ctx:BKOOLParser.Method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#att_access.
    def visitAtt_access(self, ctx:BKOOLParser.Att_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstatement.
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#insidestatement.
    def visitInsidestatement(self, ctx:BKOOLParser.InsidestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decllist.
    def visitDecllist(self, ctx:BKOOLParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decltail.
    def visitDecltail(self, ctx:BKOOLParser.DecltailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statementlist.
    def visitStatementlist(self, ctx:BKOOLParser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statementtail.
    def visitStatementtail(self, ctx:BKOOLParser.StatementtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_stm.
    def visitDecl_stm(self, ctx:BKOOLParser.Decl_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stm.
    def visitAssign_stm(self, ctx:BKOOLParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stm.
    def visitIf_stm(self, ctx:BKOOLParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stm.
    def visitFor_stm(self, ctx:BKOOLParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stm.
    def visitBreak_stm(self, ctx:BKOOLParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stm.
    def visitContinue_stm(self, ctx:BKOOLParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stm.
    def visitReturn_stm(self, ctx:BKOOLParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_stm.
    def visitMethod_stm(self, ctx:BKOOLParser.Method_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylit.
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)



del BKOOLParser