while True:
    print("1 Variables")
    print("2 Diccionarios")
    print("3 Juego")
    
    opcion = input("Elije la opción que desee realiza:")
    
    if opcion =="1":
        num1=int(input("Introduzca el primer número:"))
        num2=int(input("Introduzca el segundo número:"))
        
        print("Hay una diferencia de ",num1-num2 )
        if num1-num2 <10:
            print("Números cercanos")
        else:
            print("Números cercanos")
        
        
    elif opcion == "2":
        animales = {"perro": "guau", "gato": "miau", "vaca": "muuu", "oveja": "beee"}
        nombre=input("Introduce un nombre de animal o cree uno nuevo: ")
        
        sonido=animales.get(nombre)
        if sonido is not None:
            print(sonido)
        
        else:
            newanimal=input("introduzca el nuevo animal: ")
            newsound=input ("introduzca el nuevo sonido: ")
            animales[nombre] = newsound
            print("Nuevo animal y sonido añadido ")
      
        
    elif opcion == "3":
        import random
        numero = random.randint(1, 51)
        intentos=0
        while intentos <5:
            intento = int(input("Dime un número entre el 1 y 50: "))
            intentos=intentos +1
            if intento < numero:
                print("Demasiado bajo")
            elif intento > numero:
                print("Demasiado alto")

            elif (numero==intento):
                print("¡Correcto!")
                intentos = 5
        else:
            print("Fin del juego. El número era" )
            print (numero)
            
    else:
        print("Opción no válida")