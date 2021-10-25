from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
#from functools import reduce




class ASTGeneration(BKOOLVisitor):

    #program             :   classList EOF
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.classList()))

    #classList           :   classDecl | classDecl classList
    def visitClassList(self,ctx:BKOOLParser.ClassListContext):
        return [self.visit(ctx.classDecl())] + \
            (self.visit(ctx.classList()) if ctx.classList() else[])
        
    # classDecl           :   CLASS ID EXTENDS ID classBody
    #                     |   CLASS ID classBody
    def visitClassDecl(self,ctx:BKOOLParser.ClassDeclContext):
        return ClassDecl(
            classname = Id(ctx.ID(0).getText()),
            memlist = self.visit(ctx.classBody()),
            parentname = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
            )

    # classBody           :   LP membersList RP
    #                     |   LP RP
    def visitClassBody(self,ctx:BKOOLParser.ClassBodyContext):
        return self.visit(ctx.membersList()) if ctx.membersList() else []

    # membersList         :   member 
    #                 |   member membersList
    #                 ;
    def visitMembersList(self,ctx:BKOOLParser.MembersListContext):
        return self.visit(ctx.member()) + \
            (self.visit(ctx.membersList()) if ctx.membersList() else [])

    #member              :   attributesDecl | methodDecl 
    def visitMember(self,ctx:BKOOLParser.MemberContext):
        return self.visit(ctx.attributesDecl()) if ctx.attributesDecl() else [self.visit(ctx.methodDecl())]
    
    
    ###################################################

    # attributesDecl :   ((STATIC|) (FINAL|) | FINAL STATIC) typeDecl varDeclList SEMICOLON
    def visitAttributesDecl(self,ctx:BKOOLParser.AttributesDeclContext):
        kind=Static() if ctx.STATIC() else Instance()
        vartyp=self.visit(ctx.typeDecl())
        varDL=self.visit(ctx.varDeclList())
        if ctx.FINAL():
            decl = list(map(lambda x:ConstDecl(x[0],vartyp,x[1]) if len(x)==2 else ConstDecl(x[0],vartyp,None),varDL))
        else: 
            decl=list(map(lambda x:VarDecl(x[0],vartyp)if len(x)==1 else VarDecl(x[0],vartyp,x[1]),varDL))     
        return list(map(lambda x:AttributeDecl(kind, x),decl))
        

    # methodDecl     	:   STATIC ? typeDecl? ID paramMethod bodyMethod
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        # return MethodDecl(kind=Static() if ctx.STATIC() else Instance(),
        #                 name = Id(ctx.ID().getText()), 
        #                 param = self.visit(ctx.paramMethod()),
        #                 returnType = self.visit(ctx.typeDecl()),
        #                 body = self.visit(ctx.bodyMethod())
        # )
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramMethod())
        body = self.visit(ctx.bodyMethod())
        if ctx.STATIC():
            kind = Static()
            returnType = self.visit(ctx.typeDecl())
        else:
            kind = Instance()
            if ctx.typeDecl():
                returnType = self.visit(ctx.typeDecl())
            else:
                name = Id(str("<init>"))
                returnType = None
        return MethodDecl(kind, name, param, returnType, body)


    # paramMethod     :   LB paramDeclList RB  |   LB RB 
    def visitParamMethod(self, ctx:BKOOLParser.ParamMethodContext):
        # return self.visit(ctx.paramDeclList()) if ctx.paramDeclList() else []
        if ctx.getChildCount() == 3:
            return self.visit(ctx.paramDeclList())
        return []

    # paramDeclList   :   paramDecl |   paramDecl SEMICOLON paramDeclList
    def visitParamDeclList(self, ctx:BKOOLParser.ParamDeclListContext):#!!!
        return self.visit(ctx.paramDecl()) + \
                (self.visit(ctx.paramDeclList()) if ctx.paramDeclList() else [])


    # paramDecl       :   typeDecl idList
    def visitParamDecl(self, ctx:BKOOLParser.ParamDeclContext):#!!!
        ids = self.visit(ctx.idList())
        vartype = self.visit(ctx.typeDecl())
        return list(map(lambda x: VarDecl(x, vartype), ids))


    # bodyMethod      :   blockStmt
    def visitBodyMethod(self, ctx:BKOOLParser.BodyMethodContext):
        return self.visit(ctx.blockStmt())

    ############################################################

    # varDeclMulList  :   varDecls |   varDecls varDeclMulList
    def visitVarDeclMulList(self, ctx:BKOOLParser.VarDeclMulListContext):
        return [self.visit(ctx.varDecls())] + \
                (self.visit(ctx.varDeclMulList()) if ctx.varDeclMulList() else [])


    # varDecls         :   FINAL? typeDecl varDeclList SEMICOLON
    def visitVarDecls(self, ctx:BKOOLParser.VarDeclsContext):
        vartype = self.visit(ctx.typeDecl())
        varrawlist = self.visit(ctx.varDeclList())
        if ctx.FINAL():  
            return list(map(lambda x: ConstDecl(x[0],vartype,x[1]) \
                            if len(x) == 2 else ConstDecl(x[0],vartype,None), \
                            varrawlist       
                            )
            )
        return list(map(lambda x:VarDecl(x[0],vartype) \
                        if len(x)==1 else VarDecl(x[0],vartype,x[1]), \
                            varrawlist
                        )
        )

    # varDeclList     :   varList |   varList COMMA varDeclList
    def visitVarDeclList(self, ctx:BKOOLParser.VarDeclListContext):
        return [self.visit(ctx.varList())] + \
                (self.visit(ctx.varDeclList()) if ctx.varDeclList() else [])


    # varList         :   ID (CONST exp)?
    def visitVarList(self, ctx:BKOOLParser.VarListContext):#!!!
        #return (Id(ctx.ID().getText()) + self.visit(ctx.exp()) if ctx.exp() else None)
        if ctx.exp():
            return [Id(ctx.ID().getText()), self.visit(ctx.exp())]
        return [Id(ctx.ID().getText())]

    # typeDecl        :   typeDecl LSB INTLIT RSB
                        # |   INT | FLOAT | BOOLEAN | STRING
                        # |   VOID
                        # |   ID
                        # ;
    def visitTypeDecl(self, ctx:BKOOLParser.TypeDeclContext):
        return ArrayType(size = int(ctx.INTLIT().getText()),
                        eleType = self.visit(ctx.typeDecl())
                        ) if ctx.getChildCount() > 1 else \
                            IntType() if ctx.INT() else \
                            FloatType() if ctx.FLOAT() else \
                            BoolType() if ctx.BOOLEAN() else \
                            StringType() if ctx.STRING() else \
                            VoidType() if ctx.VOID() else \
                            ClassType(Id(ctx.ID().getText()))


    # listStatement   :   statements |   statements listStatement
    def visitListStatement(self, ctx:BKOOLParser.ListStatementContext):
        return [self.visit(ctx.statements())] + \
                (self.visit(ctx.listStatement()) if ctx.listStatement() else [])


    # statements      :   blockStmt | assignStmt | ifStmt | forStmt | breakStmt 
    #             |   continueStmt | returnStmt | callStmt
    def visitStatements(self, ctx:BKOOLParser.StatementsContext):
        return self.visit(ctx.getChild(0))


    # blockStmt       :   LP varDeclMulList listStatement RP 
    #             |   LP varDeclMulList RP
    #             |   LP listStatement RP
    #             |   LP RP
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):#!!!
        return Block(decl = self.visit(ctx.varDeclMulList()) if ctx.varDeclMulList() else [],
                    stmt = self.visit(ctx.listStatement()) if ctx.listStatement() else []
        )


    # assignStmt      :   lhs ASSIGN exp SEMICOLON
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return Assign(lhs = self.visit(ctx.lhs()),
                        exp = self.visit(ctx.exp())
        )


    #  lhs             :   ID 
    #                  |   exp9 DOT ID 
    #                  |   exp9 LSB exp RSB
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return ArrayCell(arr = self.visit(ctx.exp9()),
                        idx = self.visit(ctx.exp())
                        ) if ctx.exp() else \
                FieldAccess(obj = self.visit(ctx.exp9()),
                        fieldname = Id(ctx.ID().getText())
                        ) if ctx.getChildCount() > 1 else Id(ctx.ID().getText())


    # ifStmt          :   IF exp THEN statements
    #            |   IF exp THEN statements ELSE statements
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        if ctx.ELSE():
            return If(expr = self.visit(ctx.exp(0)),
                        thenStmt = self.visit(ctx.statements(0)),
                        elseStmt = self.visit(ctx.statements(1))    
            )
        return If(expr = self.visit(ctx.exp(0)), 
                    thenStmt = self.visit(ctx.statements(0))
        )


    # forStmt         :   FOR condition DO statements
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return For(self.visit(ctx.condition()),
                    self.visit(ctx.statements())
        )


    # condition       :   ID ASSIGN exp (TO | DOWNTO) exp
    def visitCondition(self, ctx:BKOOLParser.ConditionContext):
        return [Id(ctx.ID().getText()),
                self.visit(ctx.exp(0)),
                self.visit(ctx.exp(1)),
                True if ctx.TO() else False
        ]

    # breakStmt       :   BREAK SEMICOLON
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        if ctx.BREAK():
            return Break()


    #continueStmt    :   CONTINUE SEMICOLON
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        if ctx.CONTINUE():
            return Continue()



    # returnStmt      :   RETURN exp SEMICOLON
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return Return(self.visit(ctx.exp()))


    # callStmt        :   exp9 DOT ID LB expList RB SEMICOLON
    #           |   exp9 DOT ID LB RB SEMICOLON
    def visitCallStmt(self, ctx:BKOOLParser.CallStmtContext):
        return CallStmt(obj = self.visit(ctx.exp9()),
                        method = Id(ctx.ID().getText()),
                        param = self.visit(ctx.expList()) if ctx.expList() else []
        )

    #######################################################

    # expList         :   exp COMMA expList |   exp 
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        return [self.visit(ctx.exp())] + (self.visit(ctx.expList()) if ctx.expList() else [])


    # exp             :   exp1 (LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ) exp1
    #                 |   exp1
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp1(0)),
        #                 right = self.visit(ctx.exp1(1))
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp1(0))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp1(0)),
                        right = self.visit(ctx.exp1(1))
        )


    # exp1            :   exp2 (NOT_EQUAL | EQUAL) exp2
    #                 |   exp2
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp2(0)),
        #                 right = self.visit(ctx.exp2(1))
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp2(0))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp2(0)),
                        right = self.visit(ctx.exp2(1))
        )


    # exp2            :   exp2 (AND | OR) exp3
    #                 |   exp3
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp2()),
        #                 right = self.visit(ctx.exp3())
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp3())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp2()),
                        right = self.visit(ctx.exp3())
        )


    # exp3            :   exp3 (ADD | SUB) exp4
    #                 |   exp4
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp3()),
        #                 right = self.visit(ctx.exp4())
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp4())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp3()),
                        right = self.visit(ctx.exp4())
        )


    # exp4            :   exp4 (MUL | I_DIV | F_DIV | MOD) exp5
    #                 |   exp5
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp4()),
        #                 right = self.visit(ctx.exp5())
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp5())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp4()),
                        right = self.visit(ctx.exp5())
        )


    # exp5            :   exp5 CONCAT exp6
    #                 |   exp6
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        # return BinaryOp(op = ctx.getChild(1).getText(),
        #                 left = self.visit(ctx.exp5()),
        #                 right = self.visit(ctx.exp6())
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp6())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return BinaryOp(op = ctx.getChild(1).getText(),
                        left = self.visit(ctx.exp5()),
                        right = self.visit(ctx.exp6())
        )


    # exp6            :   NOT exp6
    #                 |   exp7
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        # return UnaryOp(op = ctx.getChild(0).getText(),
        #                 body = self.visit(ctx.exp6()),
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp7())
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        return UnaryOp(op = ctx.getChild(0).getText(),
                        body = self.visit(ctx.exp6())
        )

    # exp7            :   (ADD | SUB) exp7
    #                 |   exp8
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        # return UnaryOp(op = ctx.getChild(0).getText(),
        #                 body = self.visit(ctx.exp7()),
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp8())
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp8())
        return UnaryOp(op = ctx.getChild(0).getText(),
                        body = self.visit(ctx.exp7())
        )


    # exp8            :   exp9 LSB exp RSB
    #                 |   exp9
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        # return ArrayCell(arr = self.visit(ctx.exp9()),
        #                 idx = self.visit(ctx.exp())
        #                 ) if ctx.getChildCount() > 1 else self.visit(ctx.exp9())
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp9())
        return UnaryOp(op = ctx.getChild(0).getText(),
                        body = self.visit(ctx.exp())
        )

    # exp9            :   exp9 DOT ID LB expList RB
                    # |   exp9 DOT ID LB RB
                    # |   exp9 DOT ID
                    # |   exp10
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return CallExpr(obj = self.visit(ctx.exp9()),
                        method = Id(ctx.ID().getText()),
                        param = self.visit(ctx.expList()) if ctx.expList() else []
                        ) if ctx.getChildCount() > 3 else \
                FieldAccess(obj = self.visit(ctx.exp9()),
                        fieldname = Id(ctx.ID().getText())
                        ) if ctx.getChildCount() > 1 else self.visit(ctx.exp10())


    # exp10           :   NEW ID LB expList RB
                    # |   NEW ID LB RB
                    # |   exp11
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return NewExpr(classname = Id(ctx.ID().getText()),
                        param = self.visit(ctx.expList()) if ctx.expList() else []
                        ) if ctx.getChildCount() > 1 else self.visit(ctx.exp11())


    # exp11           :   literal | arrayLit
                    # |   THIS | NIL 
                    # |   ID | subexpression
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return SelfLiteral() if ctx.THIS() else \
                NullLiteral() if ctx.NIL() else \
                Id(ctx.ID().getText()) if ctx.ID() else \
                self.visit(ctx.subexpression()) if ctx.subexpression() else \
                self.visit(ctx.arrayLit()) if ctx.arrayLit() else \
                self.visit(ctx.literal())


    # subexpression   :   LB exp RB 
    def visitSubexpression(self, ctx:BKOOLParser.SubexpressionContext):
        return self.visit(ctx.exp())


    # literalList     :    literal | literal COMMA literalList
    def visitLiteralList(self, ctx:BKOOLParser.LiteralListContext):
        return [self.visit(ctx.literal())] + \
                (self.visit(ctx.literalList()) if ctx.literalList() else [])


    # literal         :    INTLIT | FLOATLIT | booleanlit | STRINGLIT
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return IntLiteral(int(ctx.INTLIT().getText())) if ctx.INTLIT() else \
                FloatLiteral(float(ctx.FLOATLIT().getText())) if ctx.FLOATLIT() else \
                BooleanLiteral(ctx.booleanlit()) if ctx.booleanlit() else \
                StringLiteral(ctx.STRINGLIT().getText())
 

    # idList          :   ID |   ID COMMA idList
    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        return [Id(ctx.ID().getText())] + \
                (self.visit(ctx.idList()) if ctx.idList() else [])


    # arrayLit        :   LP literalList RP
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.literalList()))


    # booleanlit              : TRUE | FALSE
    def visitBooleanlit(self, ctx:BKOOLParser.BooleanlitContext):
        return BooleanLiteral(True if ctx.TRUE() else False)
