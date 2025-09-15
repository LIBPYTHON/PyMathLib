def basic_statistics(data):
    """
        - mean: La media aritmética.
        - median: La mediana.
        - mode: La moda (si hay más de una, devuelve una lista).
        - variance: La varianza.
        - standard_deviation: La desviación estándar.
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("El parámetro 'data' debe ser una lista de números.")

    # Calcular la media
    mean = sum(data) / len(data)

    # Calcular la mediana
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    # moda
    mode = []
    max_count = 0
    for x in set(data):
        count = data.count(x)
        if count > max_count:
            mode = [x]
            max_count = count
        elif count == max_count:
            mode.append(x)

    # variança
    variance = sum((x - mean)**2 for x in data) / (len(data) - 1)

    # desviacio estandar
    standard_deviation = math.sqrt(variance)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation

