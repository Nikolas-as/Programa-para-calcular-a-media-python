Nota1 = int(input("Digite a sua nota do primeiro bimestre""\n"))

while Nota1 > 10:  
    Nota1 = int(input("NOTA INVÁLIDA""\n""Digite a sua nota do primeiro bimestre""\n"))

Nota2 = int(input("Digite a sua nota do segundo bimestre""\n"))

while Nota2 > 10:
    Nota2 = int(input("NOTA INVÁLIDA""\n""Digite a sua nota do segundo bimestre""\n"))

Nota3 = int(input("Digite a sua nota do terceiro bimestre""\n"))

while Nota3 > 10:
    Nota3 = int(input("NOTA INVÁLIDA""\n""Digite a sua nota do terceiro bimestre""\n"))

Nota4 = int(input("Digite a sua nota do quarto bimestre""\n"))

while Nota4 > 10:
    Nota4 = int(input("NOTA INVÁLIDA""\n""Digite a sua nota do quarto bimestre""\n"))

NotaFinal = (Nota1 + Nota2 + Nota3 + Nota4)/4

print("A sua média final é",NotaFinal)

if NotaFinal > 6:
    print("Você passou de ano :)")
if NotaFinal ==6:
    print("Você passou!!!!!! mais foi por pouco :|")
else:
    print("Você repetiu de ano :(")
