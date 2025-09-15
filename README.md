# PyMathLib

Methods:
Polynomials:
PolyAddition

Parameters: polynomial1, polynomial2 (they must be lists, with int and float items).
Returns: Returns a polynomial
Description: The function adds 2 polynomials.
PolySubtraction

Parameters: *polynomial1, polynomial2 (They must be lists, with int and float items).
Returns: Returns a polynomial.
Description: The function subtracts 2 polynomials (the order is important!).
PolyMultiplication

Parameters: polynomial1, polynomial2. They can be both lists (with int and float items), or one of them a list and the other an int / float, but they cannot be only two numbers.
Returns: Returns a polynomial.
Description: Multiplicates 2 polynomials, or multiplicates a polynomial with a number.
PolyDivision

Parameters: polynomial1, polynomial2. They can be both lists (with int and float items), or one of them a list and the other an int / float, but they cannot be only two numbers. (Order is important!) (polynomial2 cannot be 0).
Returns: Returns a polynomial.
Description: Divides 2 polynomials, or divides a polynomial with a number.
PolyRoot

Parameters: polynomial. It must be a list, with int and float items.
Returns: Returns an array.
Description: It computes the roots of a given polynomial.
PolyRuffini

Parameters: polynomial, independentTerm. One must be a list and the other one must be an int or float item.
Returns: Returns a tuple with a polynomial (0) and rest (1).
Description: It computes the Ruffini rule.
PolyPow

Parameters: polynomial, n. One must be a list and the other one must be an int or float item.
Returns: Returns a polynomial.
Description: It powers the polynomial to "n".
Equations:
1rst Degree

Parameters:**
Returns:**
Description:**
2nd Degree

Parameters: Polynomial. It must be a list (with only int / float items).
Returns: Returns a tuple with the two results.
Description: It computes the quadratic formula, and returns x1 (+ result) and x2 (- result).
3rt Degree and more

Parameters: Polynomial. It must be a list (with only int / float items)
Returns: It returns an array with all the possible results.
Description: It computes it using ruffini and using custom index roots.
