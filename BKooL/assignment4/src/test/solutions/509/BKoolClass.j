.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public <init>()V
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
.var 1 is x F from Label0 to Label1
	ldc 1.3
	fstore_1
	fload_1
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
