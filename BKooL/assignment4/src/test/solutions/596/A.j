.source A.java
.class public A
.super java.lang.Object

.method public <init>(LA;)V
.var 0 is this LA; from Label0 to Label1
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
	ldc "gau10"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is r F from Label0 to Label1
.var 2 is s F from Label0 to Label1
.var 3 is a [I from Label0 to Label1
.var 4 is b [I from Label0 to Label1
	fconst_2
	fstore_1
	fload_1
	fload_1
	imul
	ldc 3.14
	imul
	i2f
	fstore_2
Label1:
	return
.limit stack 2
.limit locals 5
.end method

.method public static <clinit>(LA;)V
	return
.limit stack 0
.limit locals 0
.end method
