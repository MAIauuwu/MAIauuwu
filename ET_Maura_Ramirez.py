import random
nueva_opcion = -1

trabajadores_nombres=["Juan Perez","Maria Garcia","carlos Lopez","Ana Maria","Pedro Rodriguez","laura Hernandez","Miguel Sanchez","isabel Gomez","francisco Diaz","Elena Fernandez"]
while nueva_opcion != 0:
    print("----------------------------------------\n"
    "------------- Bienvenidos --------------\n"
        "Ingrese una opcion para ingresar a:\n"
        "1.- Asignar sueldos aleartorios\n"
        "2. Clasificar sueldos\n"
        "3. Ver estadísticas.\n"
        "4. Reporte de sueldos.\n"
        "5. Salir del programa\n"
    "---------------------------------------")
    eleccionMenu = int(input())
    match eleccionMenu:
        case 1:
            print("Ha ingresado a asignacion de sueldos aleartorios")
            for trabajadores in trabajadores_nombres:
                nom_valores= sueldo_aleatorio = random.randint(300000,2500000)
            print(F'su sueldo es:', nom_valores)
        case 2: 
                print("Ha ingresado a clasificacion de sueldos")
                for trabajadores in sueldo_aleatorio:
                        clasificacion_sueldomax =sueldo_aleatorio=max({trabajadores_nombres, sueldo_aleatorio})
                        clasificacion_sueldomin =sueldo_aleatorio=min({trabajadores_nombres, sueldo_aleatorio})
        case 3: 
                print("Ha ingresado a estadisticas")            
        case 4: 
            print("Ha ingresado a reporte de sueldos")
            for trabajadores, sueldo_aleatorio in nom_valores.items():
                afp=round(sueldo_aleatorio*0.17)
                fonasa=round(sueldo_aleatorio *0.12)
                liquido=round(sueldo_aleatorio - afp -fonasa, 2)
                print(trabajadores, sueldo_aleatorio)
                print("Su descuento en afp es: ", afp, "Su descuento en fonasa es: ", fonasa, "Su sueldo liquido es: ", liquido)
        case 5:
            print("Se ha finalizado programa...\n"
                "Desarrollado por Maura Ramirez\n"
                "Rut: 21.735.021-2")
            break