# Generated from E:/hongphuc/PPL/programming code/initial/src/main/bkit/parser\BKIT.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#declarations.
    def enterDeclarations(self, ctx:BKITParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by BKITParser#declarations.
    def exitDeclarations(self, ctx:BKITParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by BKITParser#declaration.
    def enterDeclaration(self, ctx:BKITParser.DeclarationContext):
        pass

    # Exit a parse tree produced by BKITParser#declaration.
    def exitDeclaration(self, ctx:BKITParser.DeclarationContext):
        pass


    # Enter a parse tree produced by BKITParser#variable.
    def enterVariable(self, ctx:BKITParser.VariableContext):
        pass

    # Exit a parse tree produced by BKITParser#variable.
    def exitVariable(self, ctx:BKITParser.VariableContext):
        pass


    # Enter a parse tree produced by BKITParser#idlist.
    def enterIdlist(self, ctx:BKITParser.IdlistContext):
        pass

    # Exit a parse tree produced by BKITParser#idlist.
    def exitIdlist(self, ctx:BKITParser.IdlistContext):
        pass


    # Enter a parse tree produced by BKITParser#function.
    def enterFunction(self, ctx:BKITParser.FunctionContext):
        pass

    # Exit a parse tree produced by BKITParser#function.
    def exitFunction(self, ctx:BKITParser.FunctionContext):
        pass


    # Enter a parse tree produced by BKITParser#paramdcl.
    def enterParamdcl(self, ctx:BKITParser.ParamdclContext):
        pass

    # Exit a parse tree produced by BKITParser#paramdcl.
    def exitParamdcl(self, ctx:BKITParser.ParamdclContext):
        pass


    # Enter a parse tree produced by BKITParser#paramlist.
    def enterParamlist(self, ctx:BKITParser.ParamlistContext):
        pass

    # Exit a parse tree produced by BKITParser#paramlist.
    def exitParamlist(self, ctx:BKITParser.ParamlistContext):
        pass


    # Enter a parse tree produced by BKITParser#params.
    def enterParams(self, ctx:BKITParser.ParamsContext):
        pass

    # Exit a parse tree produced by BKITParser#params.
    def exitParams(self, ctx:BKITParser.ParamsContext):
        pass


    # Enter a parse tree produced by BKITParser#body.
    def enterBody(self, ctx:BKITParser.BodyContext):
        pass

    # Exit a parse tree produced by BKITParser#body.
    def exitBody(self, ctx:BKITParser.BodyContext):
        pass


    # Enter a parse tree produced by BKITParser#statements.
    def enterStatements(self, ctx:BKITParser.StatementsContext):
        pass

    # Exit a parse tree produced by BKITParser#statements.
    def exitStatements(self, ctx:BKITParser.StatementsContext):
        pass


    # Enter a parse tree produced by BKITParser#statement.
    def enterStatement(self, ctx:BKITParser.StatementContext):
        pass

    # Exit a parse tree produced by BKITParser#statement.
    def exitStatement(self, ctx:BKITParser.StatementContext):
        pass


    # Enter a parse tree produced by BKITParser#assignment.
    def enterAssignment(self, ctx:BKITParser.AssignmentContext):
        pass

    # Exit a parse tree produced by BKITParser#assignment.
    def exitAssignment(self, ctx:BKITParser.AssignmentContext):
        pass


    # Enter a parse tree produced by BKITParser#call.
    def enterCall(self, ctx:BKITParser.CallContext):
        pass

    # Exit a parse tree produced by BKITParser#call.
    def exitCall(self, ctx:BKITParser.CallContext):
        pass


    # Enter a parse tree produced by BKITParser#returnstate.
    def enterReturnstate(self, ctx:BKITParser.ReturnstateContext):
        pass

    # Exit a parse tree produced by BKITParser#returnstate.
    def exitReturnstate(self, ctx:BKITParser.ReturnstateContext):
        pass


    # Enter a parse tree produced by BKITParser#explist.
    def enterExplist(self, ctx:BKITParser.ExplistContext):
        pass

    # Exit a parse tree produced by BKITParser#explist.
    def exitExplist(self, ctx:BKITParser.ExplistContext):
        pass


    # Enter a parse tree produced by BKITParser#exp.
    def enterExp(self, ctx:BKITParser.ExpContext):
        pass

    # Exit a parse tree produced by BKITParser#exp.
    def exitExp(self, ctx:BKITParser.ExpContext):
        pass


    # Enter a parse tree produced by BKITParser#exp1.
    def enterExp1(self, ctx:BKITParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKITParser#exp1.
    def exitExp1(self, ctx:BKITParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKITParser#exp2.
    def enterExp2(self, ctx:BKITParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#exp2.
    def exitExp2(self, ctx:BKITParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#operand.
    def enterOperand(self, ctx:BKITParser.OperandContext):
        pass

    # Exit a parse tree produced by BKITParser#operand.
    def exitOperand(self, ctx:BKITParser.OperandContext):
        pass


    # Enter a parse tree produced by BKITParser#subexp.
    def enterSubexp(self, ctx:BKITParser.SubexpContext):
        pass

    # Exit a parse tree produced by BKITParser#subexp.
    def exitSubexp(self, ctx:BKITParser.SubexpContext):
        pass



del BKITParser