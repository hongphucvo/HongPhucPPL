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

.method public x()I
Label0:
.var 0 is a F from Label0 to Label1
	iconst_5
	i2f
	fstore_0
	iconst_5
	ireturn
	goto Label1
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_5
	istore_1
	iconst_2
	istore_1
	iload_1
	bipush 7
	iadd
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
