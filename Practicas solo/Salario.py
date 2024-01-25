

totalHoras=float(input("Digite las horas\n"))
precioHora=float(input("Digite cuanto le pagan por hora\n"))
cargasSociales=0.105
asociacionSolidarista=0.05
def salario():
    salarioBruto=(totalHoras*precioHora)*4
    return salarioBruto
salarioIntermedio=salario()
def salarioCargas():
    salarioSocial=salarioIntermedio*cargasSociales
    salarioSolidarista=salarioIntermedio*asociacionSolidarista
    salarioFinal=salarioIntermedio-(salarioSocial+salarioSolidarista)
    return salarioFinal
salarioTotal=salarioCargas()
print("Este es su salario\n",salarioTotal)