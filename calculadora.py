numero_uno = float(input("agrege un numero"))
numero_dos = float(input("agrege otro numero"))
operacion_requerida = input("seleccione que operacion requiere")


if operacion_requerida == "suma":
    print("usted selecciono suma")
    resultado_final = numero_uno + numero_dos
    print(type(resultado_final))
    print(resultado_final)
    print(round(resultado_final))
    print(abs(resultado_final))
   

elif operacion_requerida == "resta":
    print ("usted selecciono resta")
    resultado_final = numero_uno - numero_dos
    print(type(resultado_final))
    print(resultado_final)
    print(round(resultado_final))
    print(abs(resultado_final))

elif operacion_requerida == "multiplicacion":
    print ("usted selecciono multiplicacion")
    resultado_final = numero_uno * numero_dos
    print(type(resultado_final))
    print(resultado_final)
    print(round(resultado_final))
    print(abs(resultado_final))


elif operacion_requerida == "division":
    print ("usted selecciono division")
    resultado_final = numero_uno/ numero_dos
    print(type(resultado_final))
    print(resultado_final)
    print(round(resultado_final))
    print(abs(resultado_final))



