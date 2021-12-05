.source X.java
.class public X
.super java.lang.Object

.method public <init>(LX;)V
.var 0 is this LX; from Label0 to Label1
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
	ldc "gau12"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>(LX;)V
	return
.limit stack 0
.limit locals 0
.end method
