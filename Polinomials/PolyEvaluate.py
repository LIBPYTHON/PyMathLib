def PolyEvaluate(coeffs, x):
    result = 0
    for a in coeffs:
        result = result * x + a
    return result
