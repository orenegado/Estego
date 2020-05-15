#-*-coding: utf-8-*-
print("# cloner by: Renegado #")
op = int(input("[1]-> Ocultar [2]-> Descobrir: "))
if op == 1:
  img = input("IMG> ")
  txt = input("TXT> ")
  try:
  	with open(txt, "r+b") as ftxt:
  	  with open(img, "a+b") as fimg:
  	  	fimg.write(ftxt.read())
  	  	print("Done")
  except IOError:
  	print("Arquivo inexistente!")
elif op == 2:
  img = input("IMG> ")
  try:
  	with open(img, "rb") as fimg:
  	  print(str(fimg.read()))
  	  print("\n================================\nDone")
  except IOError:
  	print("Arquivo inexistente!")
else:
  print("???")