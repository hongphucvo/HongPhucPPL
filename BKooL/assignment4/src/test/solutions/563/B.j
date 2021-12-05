.source B.java
.class public B
.super A

.method public <init>(LB;)V
.var 0 is this LB; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public x()V
Label0:
	iconst_4
	iconst_5
	iadd
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static <clinit>(LB;)V
	return
.limit stack 0
.limit locals 0
.end method
