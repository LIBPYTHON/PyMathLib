def addition(polynomial1, polynomial2):    #Definim la funcio
    #Verifiquem parametres llista
    if not isinstance(polynomial1, list) or not isinstance(polynomial2, list):
        raise TypeError("Unexpected parameter.")
    if not polynomial1 and not polynomial2: #listas vacias
        return []
    if not all(isinstance(e, (int, float)) for e in polynomial1) or not all(isinstance(e, (int, float)) for e in polynomial2): #verificamos q sean numeros
        raise TypeError("Unexpected parameter.")
#longitudes listas
    lenPolynomial1 = len(polynomial1)
    lenPolynomial2 = len(polynomial2)
    finalPolynomial = []
    i = 0
    while True: #suma
        try:
            finalPolynomial.append(polynomial1[i] + polynomial2[i])
        except:
            if lenPolynomial1 == lenPolynomial2:
                break
            elif lenPolynomial1 >= i + 1:
                for j in range (i, lenPolynomial1):
                    finalPolynomial.append(polynomial1[j])
            else:
                for j in range (i, lenPolynomial2):
                    finalPolynomial.append(polynomial2[j])
            break
        i += 1
    return finalPolynomial

