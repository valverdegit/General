try:

    distancia=float(input("Deme su distancia en km hacia la universidad"))
    precio=float(input("Brindeme el precio por kilometro de su region"))
    cantidaddias=int(input("Brindeme la cantidad de dias que visita la universidad"))
except:
    Print("Colo un valor no valido")
cuatrimestre=15
print(cuatrimestre)
def precios():
    resultado=(distancia*precio)*2
    resultado2=resultado*cantidaddias
    resultado3=resultado2*cuatrimestre
    return resultado3
resultadofinal=precios()
print(resultadofinal)
