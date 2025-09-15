def estadistica(datos, modo):
    n = len(datos)
    datos_ordenados = sorted(datos)

    if modo == "media":
        return sum(datos) / n

    elif modo == "mediana":
        mitad = n // 2
        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    elif modo == "moda":
        frecuencias = {x: datos.count(x) for x in datos}
        max_frec = max(frecuencias.values())
        return [k for k, v in frecuencias.items() if v == max_frec]

    elif modo == "varianza":
        media = sum(datos) / n
        return sum((x - media) ** 2 for x in datos) / n

    elif modo == "desv":
        media = sum(datos) / n
        var = sum((x - media) ** 2 for x in datos) / n
        return var ** 0.5

    elif modo == "max":
        return max(datos)

    elif modo == "min":
        return min(datos)

    else:
        return "Modo no reconocido"
