.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public <init>(LBKoolClass;)V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 7
	bipush 7
	fdiv
	bipush 7
	fdiv
	bipush 7
	fdiv
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>(LBKoolClass;)V
	return
.limit stack 0
.limit locals 0
.end method
