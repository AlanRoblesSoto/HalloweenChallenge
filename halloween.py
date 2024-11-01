def dulces_max(input, output):
    with open(input, 'r') as f:
        lineas = f.readlines()
        
    T = int(lineas[0].strip())  # Cantidad de casos de prueba
    resultados = []
    index = 1
    for _ in range(T):
        N = int(lineas[index].strip())  # Cantidad de casas
        candies = list(map(int, lineas[index + 1].strip().split()))  # Lista con la cantidad de dulces de las casas
        
        if N == 1:
            resultados.append(candies[0])  # Si solo hay una casa, se agrega la cantidad de dulces de la casa al array con los resultados
        else:
            # Inicializa el array dulces_recolectados
            dulces_recolectados = [0] * N  # Crea un array de N elementos con valores iniciales de 0
            dulces_recolectados[0] = candies[0]
            dulces_recolectados[1] = max(candies[0], candies[1])
            
            # Rellana el array dulces_recolectados
            for i in range(2, N):
                # Para cada casa hay dos opciones, saltarla (dulces_recolectados[i - 1]) o tomar los dulces (dulces_recolectados[i - 2] + candies[i])
                dulces_recolectados[i] = max(dulces_recolectados[i - 1], dulces_recolectados[i - 2] + candies[i])
            
            # El ultimo elemento de dulces recolectados es el maximo numero de dulces que se puede recolectar
            resultados.append(dulces_recolectados[N - 1])
        
        index += 2  # Avanza al siguiente caso de prueba
        
        # Guardar los resultados en el archivo de salida
        with open(output, 'w') as f:
            for result in resultados:
                f.write(str(result) + '\n')


entrada = 'input.txt'
salida = 'output.txt'
dulces_max(entrada, salida)