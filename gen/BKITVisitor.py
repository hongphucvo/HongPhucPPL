# Generated from E:/hongphuc/PPL/programming code/initial/src/main/bkit/parser\BKIT.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declarations.
    def visitDeclarations(self, ctx:BKITParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declaration.
    def visitDeclaration(self, ctx:BKITParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idlist.
    def visitIdlist(self, ctx:BKITParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function.
    def visitFunction(self, ctx:BKITParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramdcl.
    def visitParamdcl(self, ctx:BKITParser.ParamdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramlist.
    def visitParamlist(self, ctx:BKITParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params.
    def visitParams(self, ctx:BKITParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statements.
    def visitStatements(self, ctx:BKITParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment.
    def visitAssignment(self, ctx:BKITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call.
    def visitCall(self, ctx:BKITParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnstate.
    def visitReturnstate(self, ctx:BKITParser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#explist.
    def visitExplist(self, ctx:BKITParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#subexp.
    def visitSubexp(self, ctx:BKITParser.SubexpContext):
        return self.visitChildren(ctx)



del BKITParser