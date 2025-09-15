# 📘 PyMathLib

## ⚡ Polynomials

### 🔹 `PolyAddition(polynomial1, polynomial2)`
- **Parameters**:  
  - `polynomial1` *(list[int|float])*  
  - `polynomial2` *(list[int|float])*  
- **Returns**: `list` → Un polinomio resultante.  
- **Description**: Suma dos polinomios.  

### 🔹 `PolySubtraction(polynomial1, polynomial2)`
- **Parameters**:  
  - `polynomial1` *(list[int|float])*  
  - `polynomial2` *(list[int|float])*  
- **Returns**: `list` → Un polinomio resultante.  
- **Description**: Resta dos polinomios (**el orden es importante**).  

### 🔹 `PolyMultiplication(polynomial1, polynomial2)`
- **Parameters**:  
  - `polynomial1` *(list[int|float] | int | float)*  
  - `polynomial2` *(list[int|float] | int | float)*  
- **Restrictions**: No se permiten dos números simples como entrada.  
- **Returns**: `list` → Un polinomio resultante.  
- **Description**: Multiplica dos polinomios, o un polinomio con un escalar.  

### 🔹 `PolyDivision(polynomial1, polynomial2)`
- **Parameters**:  
  - `polynomial1` *(list[int|float] | int | float)*  
  - `polynomial2` *(list[int|float] | int | float)*  
- **Restrictions**: No se permiten dos números simples como entrada. `polynomial2` no puede ser 0.  
- **Returns**: `list` → Un polinomio resultante.  
- **Description**: Divide un polinomio entre otro, o un polinomio entre un escalar.  

### 🔹 `PolyRoot(polynomial)`
- **Parameters**:  
  - `polynomial` *(list[int|float])*  
- **Returns**: `list` → Raíces del polinomio.  
- **Description**: Calcula las raíces de un polinomio dado.  

### 🔹 `PolyRuffini(polynomial, independentTerm)`
- **Parameters**:  
  - `polynomial` *(list[int|float])*  
  - `independentTerm` *(int | float)*  
- **Returns**: `tuple` → `(polynomial, remainder)`  
- **Description**: Aplica la **regla de Ruffini** para dividir un polinomio entre `(x - independentTerm)`.  

### 🔹 `PolyPow(polynomial, n)`
- **Parameters**:  
  - `polynomial` *(list[int|float])*  
  - `n` *(int | float)*  
- **Returns**: `list` → Polinomio elevado a la potencia `n`.  
- **Description**: Eleva un polinomio a la potencia `n`.  

---

## ⚡ Equations

### 🔹 2nd Degree
- **Parameters**:  
  - `polynomial` *(list[int|float])* → Debe tener forma `[a, b, c]`  
- **Returns**: `tuple` → `(x1, x2)`  
- **Description**: Aplica la fórmula cuadrática y devuelve las dos soluciones.  

### 🔹 3rd Degree and more
- **Parameters**:  
  - `polynomial` *(list[int|float])*  
- **Returns**: `list` → Todas las raíces reales/posibles.  
- **Description**: Calcula las raíces de un polinomio de grado ≥ 3 usando **Ruffini** y búsqueda de raíces por aproximación.  

---

## 📌 Ejemplos de uso

```python
# Polinomios representados como listas de coeficientes
# [a, b, c] => ax^2 + bx + c

# Ejemplo: x^2 - 5x + 6 = 0
poly = [1, -5, 6]

# ➤ Raíces cuadráticas
print(PolyRoot(poly))   # [2.0, 3.0]

# ➤ Suma: (x^2 + 2x + 1) + (x^2 - 1)
print(PolyAddition([1, 2, 1], [1, 0, -1]))  # [2, 2, 0]

# ➤ Multiplicación: (x + 1)(x - 1) = x^2 - 1
print(PolyMultiplication([1, 1], [1, -1]))  # [1, 0, -1]

# ➤ División: (x^2 - 1) ÷ (x - 1)
print(PolyDivision([1, 0, -1], [1, -1]))    # [1, 1]
