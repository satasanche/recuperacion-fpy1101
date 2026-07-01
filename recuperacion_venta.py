def calcular_descuento(subtotal):
    if subtotal >= 50000:
        return subtotal * 0.10
    else:
        return 0
    
def mostrar_resultado(nombre_producto, subtotal, descuento, total):
    print("----------------------------")
    print("Producto:", nombre_producto)
    print("Subtotal: ", subtotal)
    print("Descuento: ", descuento)
    print("Total a pagar: ", total)
    print("----------------------------")

    

    while print("=== REGISTRO DE VENTA ===")
    
        # 1. Solicitar y validar nombre del producto (no vacío)
        nombre_producto = ""
    while nombre_producto == "":
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto == "":
            print("Error: El nombre no puede estar vacio.")
        
    # 2. Solicitar y validar el precio (mayor a 0 y numérico)
    precio_unitario = 0
    while precio_unitario <= 0:
        try:
            precio_unitario = float(input("Ingrese el precio unitario: "))
            if precio_unitario <= 0:
                print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: Debe ingresar un numero valido.")
            precio_unitario = 0  # Asegura reiniciar la variable ante un error

    # 3. Solicitar y validar la cantidad (mayor a 0 y entera)
    cantidad_comprada = 0
    while cantidad_comprada <= 0:
        try:
            cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
            if cantidad_comprada <= 0:
                print("Error: La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")
            cantidad_comprada = 0  # Asegura reiniciar la variable ante un error

    # Proceso: Calcular subtotal, descuento y total
    subtotal = precio_unitario * cantidad_comprada
    descuento = calcular_descuento(subtotal)
    total_pagar = subtotal - descuento

    # Salida: Mostrar los resultados
    mostrar_resultado(nombre_producto, subtotal, descuento, total_pagar)
    
    # Preguntar si desea repetir
    continuar = input("¿Desea realizar otra venta? (s/n): ")

print("Programa finalizado con exito.")