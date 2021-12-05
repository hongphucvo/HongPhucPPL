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
	ldc "hippo20"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public func()I
Label0:
.var 0 is f I from Label0 to Label1
.var 1 is k I from Label0 to Label1
.var 2 is n Ljava/lang/String; from Label0 to Label1
.var 3 is m Ljava/lang/String; from Label0 to Label1
	iload_1
	astore_3
	iconst_3
	ireturn
	goto Label1
Label1:
.limit stack 1
.limit locals 4
.end method

.method public static <clinit>(LA;)V
	return
.limit stack 0
.limit locals 0
.end method
