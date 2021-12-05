.source BKoolClass.java
.class public BKoolClass
.super X

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

.method public x(I)I
.var 0 is e I from Label0 to Label1
Label0:
.var 1 is temp LA; from Label0 to Label1
	iconst_5
	aload_1
	putfield BKoolClass/k I
	iconst_3
	ireturn
	goto Label1
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpgt Label4
	iconst_0
	invokestatic io/writeBool(Z)V
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
