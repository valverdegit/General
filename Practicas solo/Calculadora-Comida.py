ingresosMensuales=float(input("Brindeme su salario mensual"))
gastoComestibles=float(input("Brindeme sus gastos en comestibles"))
def porcentaje():
    porcentageComida=(ingresosMensuales*100)/gastoComestibles
    porcentajeFinal=100-porcentageComida

    return porcentajeFinal
final=porcentaje()
print("El porcentaje restante despues de gastos de comida es\n", final)
#El codigo no esta correcto, tengo que revisar porque