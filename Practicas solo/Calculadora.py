resultado=0
funcion=0
cycle1=True

def suma(num1,num2):
    resultado=num1+num2
    return resultado
def resta(num1,num2):
    resultado=num1-num2
    return resultado
def por(num1,num2):
    resultado=num1*num2
    return resultado
def division(num1,num2):
    resultado=num1/num2
    return resultado

print("Welcome to this program")
while cycle1==True:
    action=str(input("What do you want to do\nADD\nSUBSTRACT\nMULTIPLY\nDIVIDE\n"))
    if action=="ADD" or action=="SUBSTRACT" or action=="MULTIPLY" or action=="DIVIDE":
        cycle1=False
    else:
        print("Write te action the same way is written in the selection part")
        cycle1=True
num1=float(input("First Number\n"))
num2=float(input("Second Number\n"))
if action=="ADD":
    funcion=suma(num1,num2)
    print(resultado)
elif action=="SUBSTRACT":
    funcion=resta(num1,num2)
    print(resultado)
elif action=="MULTIPLY":
    funcion=por(num1,num2)
    print(resultado)
elif action=="DIVIDE" and num2!=0:
    funcion=division(num1,num2)
    print(resultado)
elif action=="DIVIDE" and num2==0:
    print("Second number needs to be diferent from zero")
#Tengo que revisar el codigo porque no funciona todavia