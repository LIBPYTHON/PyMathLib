def EQ2 (Polynomial):
    # Check parameters
    if not isinstance(Polynomial, list):
        if not all(isinstance(e, (int, float)) for e in Polynomial):
            raise TypeError("Unexpected parameter.")
        raise TypeError("Unexpected parameter.")
    if len(Polynomial) != 3:
        raise TypeError("Unexpected parameter.")

    a = Polynomial[2]
    b = Polynomial[1]
    c = Polynomial[0]

    try:
        root: float = sqrt(pow(b, 2) - 4 * a * c)
        x1, x2 = (b * -1 + root) / (2 * a), (b *-1 - root) / (2 * a)
    except:
        return float("NaN")
    return x1, x2
