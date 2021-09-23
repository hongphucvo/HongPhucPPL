'''Given the grammar of MP as follows:

program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail | ;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID; 

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;'''


#terminal

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visitVardecls(ctx.vardecls())
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl())+self.visitVardecltail(ctx.vardecltail())
                
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount()==2):
            return self.visitVardecl(ctx.vardecl())+self.visitVardecltail(ctx.vardecltail())
        else: return 1
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visitMptype(ctx.mptype())+self.visitIds(ctx.ids())
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1
    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.getChildCount()==1):
            return 1
        else: return 2+ self.visitIds(ctx.ids())


#non terminal
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 1+self.visitVardecls(ctx.vardecls())
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return 1+self.visitVardecl(ctx.vardecl())+self.visitVardecltail(ctx.vardecltail())
                
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount()==2):
            return 1+self.visitVardecl(ctx.vardecl())+self.visitVardecltail(ctx.vardecltail())
        else: return 1
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visitMptype(ctx.mptype())+self.visitIds(ctx.ids())
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return 1
    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.getChildCount()==1):
            return 1
        else: return 1+ self.visitIds(ctx.ids())









class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    #variable:Id
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)
class Id(AST):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)
class ASTGeneration(MPVisitor):

    def visit(self,ctx):
        ctx.accept(self,ctx.getChild())
    def visitProgram(self,ctx:MPParser.ProgramContext):
        

        return str(Program(ctx.getChild()))

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        
        return None

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        return None

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return None

    def visitIds(self,ctx:MPParser.IdsContext):

        return None
