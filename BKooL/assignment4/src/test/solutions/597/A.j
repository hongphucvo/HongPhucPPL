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
	ldc "gau11"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public main()I
Label0:
.var 0 is x Ljava/lang/String; from Label0 to Label1
	aload_0
	invokestatic io/readStr()Ljava/lang/String;
	ldc "Your name is"
	invokestatic io/writeStr(Ljava/lang/String;)V
	aload_0
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
.limit stack 6
.limit locals 1
.end method

.method public static <clinit>(LA;)V
	return
.limit stack 0
.limit locals 0
.end method
