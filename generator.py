import random

def generar_problema_avanzado(tipo, resultado):
    """
    Genera un problema de tipo polinomio, ecuación o estadística
    cuyo resultado final sea el número indicado.
    
    Parámetros:
        tipo (str): 'polinomio', 'ecuacion' o 'estadistica'
        resultado (float/int): valor numérico deseado como solución.
    
    Retorna:
        problema (str): enunciado del problema
        solucion (str): explicación o resolución del problema
    """
    
    if tipo == "polinomio":
        # Crear un polinomio que al evaluarse en x = 1, por ejemplo, dé el resultado
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = resultado - (a + b)
        problema = (
            f"Considera el polinomio P(x) = {a}x² + {b}x + {c}. "
            f"Calcula P(1)."
        )
        solucion = f"P(1) = {a}(1)² + {b}(1) + {c} = {resultado}"
    
    elif tipo == "ecuacion":
        # Crear una ecuación lineal o cuadrática que tenga como solución el resultado
        opcion = random.choice(["lineal", "cuadratica"])
        
        if opcion == "lineal":
            m = random.randint(1, 10)
            b = -m * resultado
            problema = f"Resuelve la ecuación: {m}x + {b} = 0"
            solucion = f"x = -({b}) / {m} = {resultado}"
        
        else:  # cuadrática
            a = 1
            b = -2 * resultado
            c = resultado ** 2
            problema = f"Resuelve la ecuación cuadrática: x² {b:+}x {c:+} = 0"
            solucion = f"Las soluciones son x = {resultado} (doble raíz)."
    
    elif tipo == "estadistica":
        # Crear un conjunto de datos cuya media sea el resultado
        n = random.randint(3, 6)
        datos = [random.randint(resultado - 3, resultado + 3) for _ in range(n - 1)]
        ultimo = (resultado * n) - sum(datos)
        datos.append(ultimo)
        problema = f"Calcula la media de los siguientes datos: {datos}"
        solucion = f"Media = (suma de los datos) / {n} = {sum(datos)}/{n} = {resultado}"
    
    else:
        problema = "Tipo de problema no reconocido. Usa 'polinomio', 'ecuacion' o 'estadistica'."
        solucion = "-"
    
    return problema, solucion


