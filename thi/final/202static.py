class StaticCheck(BaseVisitor):
    def visitProgram(self,ast,o):
        self.visit(ast.exp,o)
    def visitAssoc(self, ast, o):
        if ast.key in o:
            raise DuplicateKey()
        o[ast.key]=self.visit(ast.value,o)
        
    def visitArray(self,ast,o):
        env={}
        [map(lambda x: self.visit(x,o),ast.assocs)]
        if len(env)!=len(ast.assocs):
            raise DuplicateKey(ast)
        return o
    def visitIntLit(self,ast,o):
        return ast.value
