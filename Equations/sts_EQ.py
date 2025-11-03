def resuelve_sistema(A, b):
    """
    Resol un sistema d'equacions lineals del tipus A·x = b
    utilitzant el mètode d'eliminació de Gauss 

    Paràmetres:
    A : llista de llistes (matriu de coeficients)
    b : llista (vector de termes independents)

    Retorna:
    x : llista amb la solució del sistema
    """
    n = len(A)

    # Combinar A i b en una sola matriu augmentada
    for i in range(n):
        A[i].append(b[i])

    # Fase d'eliminació
    for i in range(n):
        # Normalitzar la fila actual (dividir per l'element diagonal)
        divisor = A[i][i]
        if divisor == 0:
            return "Error: no es pot dividir per zero (el sistema pot ser incompatible)."
        for j in range(i, n + 1):
            A[i][j] /= divisor

        # Eliminar les variables de sota de la fila actual
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]

    # Fase de substitució enrere
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x
