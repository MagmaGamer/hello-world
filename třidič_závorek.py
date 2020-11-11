def checkuj_zavorky(input,a,b):
	x=0
	y=1
	for char in input:
		if y==0:
			print("wrong ZAVORKY")
			return
		if char==a:
			x+=1
		if char==b:
			x-=1
			if x<=0:
				y=0
	if y!=0:	print("wrong ZAVORKY")
	else:		print("good ZAVORKY")

def trid(input):
	if input[0]=="(":
		a="("
		b=")"
	elif input[0]=="[":
		a="["
		b="]"
	elif input[0]=="<":
		a="<"
		b=">"
	elif input[0]=="{":
		a="{"
		b="}"
	else:
		print("BAAD,  NOT STONKS!")
		print(input[0], "is not ZÁVORKA")
		return
	checkuj_zavorky(input,a,b)
trid(input("Napiš závorky: "))

input()